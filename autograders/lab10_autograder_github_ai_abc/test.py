"""
Tests
"""
from difflib import SequenceMatcher, unified_diff
import random
import string
import re
import os
import sys
import subprocess
from importlib import import_module
from itertools import permutations

import unittest
from gradescope_utils.autograder_utils.decorators import tags, number, weight
from gradescope_utils.autograder_utils.files import check_submitted_files

import cull_input

# https://docs.python.org/3/library/unittest.html
# https://gradescope-utils.readthedocs.io/en/latest/source/gradescope_utils.autograder_utils.html
# https://docs.python.org/3/library/re.html
# https://stackoverflow.com/questions/15340582/python-extract-pattern-matches
# https://docs.python.org/3/library/subprocess.html#subprocess.Popen
# https://stackoverflow.com/questions/4289331/how-to-extract-numbers-from-a-string-in-python
# https://pynative.com/python-random-randrange/

def print_off():
  if sys.stdout == sys.stdout:
    sys.stdout = open(os.devnull, 'w')

def print_on():
  if sys.stdout != sys.__stdout__:
    sys.stdout.close()
    sys.stdout = sys.__stdout__

print_off()
their = None
try:
  mod = import_module("thermostat")
except:
  print(f"❌ Error importing thermostat.py: either the file is not named correctly or it has a syntax error")
else:
  their = mod
print_on()

def random_time():
    m = random.randint(0, 23)
    s = random.randint(0, 59)
    return str(m//10)+str(m%10)+':'+str(s//10)+str(s%10)

def random_temp():
    return round(random.triangular(55, 85), 2)

class TestExpressionHW(unittest.TestCase):
  trials = 50

  def nth(self, i):
    if i // 10 % 10 == 1: return "th"
    match i % 10:
      case 1: return "st"
      case 2: return "nd"
      case 3: return "rd"
      case _: return "th"

  def require_file(self, fname):
    missing_files = check_submitted_files([fname], base='.')
    self.assertEqual(len(missing_files), 0, f"❌ Missing {fname}!")

  def require_author(self, fname):
    self.require_file(fname)
    with open(fname) as fd:
      lines = fd.read().splitlines()

    self.assertTrue(len(lines) >= 3,
      f"❌ {fname} doesn't have enough lines to possibly have Author, Email, and Spire ID")

    author = lines[0]
    email = lines[1]
    spire_id = lines[2]

    self.assertTrue(re.match(r"\uFEFF?\s*#*\s*(AUTHORS?|(A|a)uthors?).*", author),
      "❌ You did not include an Author comment on line 1 or it wasn't formatted correctly")
    print("✅ Author information was included")

    self.assertTrue(re.match(r"\s*#*\s*(EMAILS?|(E|e)mails?).*", email),
      "❌ You did not include an Email comment on line 2 or it wasn't formatted correctly")
    print("✅ Email information was included")

    self.assertTrue(re.match(r"\s*#*\s*(SPIRE|(S|s)pire)\s*(ID(S|s)?|ids?).*", spire_id),
      "❌ You did not include a Spire ID comment on line 3 or it wasn't formatted correctly")
    print("✅ Spire ID information was included")
    print()

  def require_function(self, mod, fun):
    self.assertTrue(hasattr(mod, fun), f"❌ Missing {fun}()")

  def set_up_file(self, fname, nfname="un_ast.py"):
    self.require_file(fname)
    os.system("rm -f {nfname}")
    cull_input.cull_input_text(fname, nfname)
    return nfname

  def run_and_get_out(self, fname, stdin):
    child = subprocess.Popen(['python3', fname], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, encoding='utf-8')
    out,_ = child.communicate(stdin)
    child.wait()
    return out.splitlines()

  def get_last_nums(self, lines, num_lines, cast, inp):
    self.assertGreaterEqual(len(lines), num_lines, f"❌ Running with input(s): {inp}:\nThere should be at least {num_lines} lines of *output* (ignoring the line(s) of input) generated.\nOnly see {len(lines)} lines")
    nums = [re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", l) for l in lines]
    last_nums = [cast(l[-1]) if l else None for l in nums[-num_lines:]]
    self.assertNotIn(None, last_nums, f"❌ Running with input(s): {inp}:\nCould not find numbers for last {num_lines} lines\nFound the following last numbers per line: {last_nums}")
    return last_nums

  def meta_test_file_exists(self, fname):
    print(f"*** Looking for {fname} ***\n")
    self.require_file(fname)
    print(f"✅ {fname} found")
    print()

  def meta_test_file_author(self, fname):
    print(f"*** Looking for {fname}'s author info ***\n")
    self.require_author(fname)
    print(f"✅ {fname} author information found")
    print()

  @number(1)
  @weight(2)
  def test_constructor(self):
    """Thermostat constructor test"""
    print("*** Testing Thermostat constructor ***\n")

    # test default parameter value
    try:
        their_ret = their.Thermostat()
    except:
        self.assertEqual(True, False, f"❌ Thermostate() resulted in an error")

    # test non-default parameter value
    try:
        their_ret = their.Thermostat(110)
    except:
        self.assertEqual(True, False, f"❌ Thermostate(110) resulted in an error")


    print("✅ Thermostat constructor passed all tests")
    print()

  @number(2)
  @weight(2)
  def test_add_schedule(self):
    """add_schedule test"""
    print("*** Testing add_schedule ***\n")

    # check if function exists
    self.assertEqual(hasattr(their.Thermostat, 'add_schedule'), True, f"❌ Your Thermostat class does not have an add_schedule function")

    t = their.Thermostat()
    try:
        t.add_schedule('00:00', 50)
        t.add_schedule('08:30', 60)
        t.add_schedule('12:45', 70)
        t.add_schedule('23:59', 80)
    except:
        self.assertEqual(True, False, f"❌ Error encountered while calling add_schedule function")

    print("✅ add_schedule passed all tests")
    print()

  @number(3)
  @weight(5)
  def test_cast_to_string(self):
    """__str__ test"""
    print("*** Testing __str__ ***\n")

    # check if function exists
    self.assertEqual(hasattr(their.Thermostat, '__str__'), True, f"❌ Your Thermostat class does not have a __str__ function")

    t = their.Thermostat()
    their_ret = str(t)
    ref_ret = 'Default temperature: 68 degrees'
    self.assertEqual(their_ret, ref_ret, f"❌ Expected return is {ref_ret}, yours is {their_ret}. Check if you may have a trailing newline or if your constructor has a default parameter value")

    t = their.Thermostat(110)
    their_ret = str(t)
    ref_ret = 'Default temperature: 110 degrees'
    self.assertEqual(their_ret, ref_ret, f"❌ Expected return is {ref_ret}, yours is {their_ret}. Check if you may have a trailing newline or if your constructor has a default parameter value")

    # check unique times
    t = their.Thermostat(75)
    d = {}
    for i in range(500):
        tm = random_time()
        tp = random_temp()
        t.add_schedule(tm, tp)
        d[tm] = tp

    their_ret = str(t)

    ref_ret = f'Default temperature: 75 degrees\n'
    for s in sorted(d):
      ref_ret += f'{s} {d[s]} degrees\n'
    ref_ret = ref_ret[:-1]
    self.assertEqual(their_ret[-1]!='\n', True, f"❌ The returned string by your __str__ function has a trailing newline")
    self.assertEqual(their_ret, ref_ret, f"❌ The returned string by your __str__ function does not match the expected. This could be due to either your __str__ function or adding_schedules implemented incorrectly")

    # check overwrite times
    t = their.Thermostat()
    d = {}
    tm_pool = [random_time() for i in range(10)]
    for i in range(500):
       tm = random.choice(tm_pool)
       tp = random_temp()
       t.add_schedule(tm, tp)
       d[tm] = tp

    their_ret = str(t)
    ref_ret = f'Default temperature: 68 degrees\n'
    for s in sorted(d):
      ref_ret += f'{s} {d[s]} degrees\n'
    ref_ret = ref_ret[:-1]
    self.assertEqual(their_ret[-1]!='\n', True, f"❌ The returned string by your __str__ function has a trailing newline")
    self.assertEqual(their_ret, ref_ret, f"❌ The returned string by your __str__ function does not match the expected. This could be due to either your __str__ function or adding_schedules implemented incorrectly")

    print("✅ add_schedule passed all tests")
    print()


  @number(4)
  @weight(6)
  def test_get_target_temperature(self):
    """get_target_temperature test"""
    print("*** Testing get_target_temperature ***\n")

    # check if function exists
    self.assertEqual(hasattr(their.Thermostat, 'get_target_temperature'), True, f"❌ Your Thermostat class does not have a get_target_temperature function")

    # check get default temperature
    t = their.Thermostat()
    ref_ret = 68
    for i in range(20):
      tm = random_time()
      their_ret = t.get_target_temperature(tm)
      self.assertEqual(their_ret, ref_ret, f"❌ t.get_target_temperature({tm}) should return {ref_ret}, yours is {their_ret}")

    # check get non-default temperature
    ref_ret = 72.34
    t = their.Thermostat(ref_ret)
    for i in range(20):
      tm = random_time()
      their_ret = t.get_target_temperature(tm)
      self.assertEqual(their_ret, ref_ret, f"❌ t.get_target_temperature({tm}) should return {ref_ret}, yours is {their_ret}")

    # check one schedule at 00:00
    t = their.Thermostat(58)
    ref_ret = 78.66
    t.add_schedule('00:00', ref_ret)
    for i in range(20):
      tm = random_time()
      their_ret = t.get_target_temperature(tm)
      self.assertEqual(their_ret, ref_ret, f"❌ t.get_target_temperature({tm}) should return {ref_ret}, yours is {their_ret}")

    # check one schedule at 23:59
    ref_ret = 82.33
    schedule_tp = 66
    t = their.Thermostat(ref_ret)
    t.add_schedule('23:59', schedule_tp)
    for i in range(20):
      tm = random_time()
      if tm=='23:59':
         continue
      their_ret = t.get_target_temperature(tm)
      self.assertEqual(their_ret, ref_ret, f"❌ t.get_target_temperature({tm}) should return {ref_ret}, yours is {their_ret}")

    tm = '23:59'
    their_ret = t.get_target_temperature(tm)
    ref_ret = schedule_tp
    self.assertEqual(their_ret, ref_ret, f"❌ t.get_target_temperature({tm}) should return {ref_ret}, yours is {their_ret}")

    # check unique times
    default_tp = 52.6
    t = their.Thermostat(default_tp)
    d = {}
    for i in range(10):
        tm = random_time()
        tp = random_temp()
        t.add_schedule(tm, tp)
        d[tm] = tp

    for i in range(1000):
       tm = random_time()
       their_ret = t.get_target_temperature(tm)
       smaller = [tt for tt in d if tt<=tm]
       ref_ret = default_tp if len(smaller)==0 else d[max(smaller)]
       self.assertEqual(their_ret, ref_ret, f"❌ t.get_target_temperature({tm}) should return {ref_ret}, yours is {their_ret}")

    print("✅ get_target_temperature passed all tests")
    print()
