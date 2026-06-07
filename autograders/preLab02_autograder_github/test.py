"""
Tests
"""
from difflib import SequenceMatcher, unified_diff
import random
import string
import re
import os
import subprocess
import sys
from importlib import import_module

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
# https://stackoverflow.com/questions/3131217/error-handling-when-importing-modules

def print_off():
  if sys.stdout == sys.stdout:
    sys.stdout = open(os.devnull, 'w')

def print_on():
  if sys.stdout != sys.__stdout__:
    sys.stdout.close()
    sys.stdout = sys.__stdout__

def find_mod(mod_lookup):
  return

print_off()
mod_lookup = {}
for mod in ['ab_with_func']:
  try:
    m = import_module(mod)
  except:
    pass
  else:
    mod_lookup[mod] = m
print_on()

their = mod_lookup['ab_with_func'] if 'ab_with_func' in mod_lookup else None

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
    self.assertEqual(len(missing_files), 0, f"Missing {fname}! ❌")

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
    self.assertGreaterEqual(len(lines), num_lines, f"❌ There should be at least {num_lines} lines of *output* (ignoring the line(s) of input) generated.\nOnly see {len(lines)} lines")
    nums = [re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", l) for l in lines]
    last_nums = [cast(l[-1]) if l else None for l in nums[-num_lines:]]
    self.assertNotIn(None, last_nums, f"❌ Could not find numbers for last {num_lines} lines\nFound the following last numbers per line: {last_nums}")
    return last_nums

  def require_function(self, mod, fun):
    self.assertIn(mod, mod_lookup,
      f"❌ Missing {mod}.py.\nThis could also happen if the file would crash when run.\nThis could happen if there is a call to input() (since the autograder doesn't send information that way anymore).")
    self.assertTrue(hasattr(mod_lookup[mod], fun), f"❌ Missing {fun}()")

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
  @weight(5)
  def test_ab(self):
    """ab.py test"""
    print("*** Testing ab.py ***\n")
    ab_exec = self.set_up_file("ab.py")
    self.require_author("ab.py")
    a = [1, 3, 4, 99, 2, 5, 6, 7, 8, 97]
    b = [2, 4, 6, 8, 10, 12, 14, 16, 8, 32]
    passed = 0
    for i in range(len(a)):
      lines = self.run_and_get_out(ab_exec, f"{a[i]}\n{b[i]}\n")

      self.assertTrue(len(lines) == 1,
        f"❌ There should be exactly 1 line of *output* (ignoring the two lines of input) generated for ab.py")

      r = f"{str(a[i])*b[i]}{str(b[i])*a[i]}"
      if r == lines[0]:
        print(f"✅ Test case {i+1} passed")
        passed += 1
      else:
        print(f"❌ Test case {i+1} failed")

    self.assertTrue(passed == len(a), f"❌ output is not correct. Passed {passed} out of {len(a)} test cases")
    print("✅ String repetition and concatenation seem correct")
    print()

  @number(2)
  @weight(5)
  def test_list(self):
    """list.py test"""
    print("*** Testing list.py ***\n")
    list_exec = self.set_up_file("list.py")
    self.require_author("list.py")
    a = ['apple',   'banana',   'cherry',     'date',       'fig',        'daikon',      'kiwi',     'mango',   'xigua', 'nectarine']
    b = ['orange',  'papaya',   'quince',     'raspberry',  'strawberry', 'tangerine',  'ugli',     'watermelon', 'xigua', 'zucchini']
    c = ['yellow',  'zucchini', 'artichoke',  'broccoli',   'carrot',     'daikon',     'eggplant', 'garlic', 'xigua', 'yam']
    d = ['apple',   'papaya',   'artichoke',  'date',       'fig',        'daikon',     'ugli',     'mango', 'xigua', 'zucchini']
    passed = 0
    for i in range(len(a)):
        inp = f"{a[i]}\n{b[i]}\n{c[i]}\n{d[i]}\n"
        lines = self.run_and_get_out(list_exec, inp)
        self.assertTrue(len(lines) == 5,
            f"❌ There should be exactly 5 lines of *output* (ignoring the four lines of input) generated for list.py")
        r = ""
        list_ref = []
        list_ref.append(a[i])
        r = r + str(list_ref)
        list_ref.append(b[i])
        r = r + str(list_ref)
        list_ref.insert(0, c[i])
        r = r + str(list_ref)
        list_ref.remove(d[i])
        r = r + str(list_ref)
        r = r + str(len(list_ref))

        if r == ''.join(lines):
          print(f"✅ Test case {i+1} passed")
          passed += 1
        else:
          print(f"❌ Test case {i+1} failed")

    self.assertTrue(passed == len(a), f"❌ output is not correct. Passed {passed} out of {len(a)} test cases")

    print("✅ List operations seem correct")
    print()

  @number(3)
  @weight(5)
  def test_ab_with_func(self):
    """ab_func() test"""
    mod, fun = "ab_with_func", "ab_func"
    print(f"*** Testing {fun}() ***\n")
    self.require_author("ab_with_func.py")
    self.require_function(mod, fun)
    a = [1, 3, 4, 99, 2, 5, 6, 7, 8, 97]
    b = [2, 4, 6, 8, 10, 12, 14, 16, 8, 32]
    passed = 0  
    for i in range(len(a)):
      ack_ref = f"{str(a[i])*b[i]}{str(b[i])*a[i]}"
      ack_their = their.ab_func(a[i], b[i])
      if ack_ref == ack_their:
        print(f"✅ Test case {i+1} passed")
        passed += 1
      else:
        print(f"❌ Test case {i+1} failed")

    self.assertTrue(passed == len(a), f"❌ output is not correct. Passed {passed} out of {len(a)} test cases")
    print("✅ String repetition, concatenation and return seem correct inside the function")
    print()

