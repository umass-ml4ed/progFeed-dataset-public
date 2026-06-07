"""
Tests
"""
from difflib import SequenceMatcher, unified_diff
import random
import string
import re
import os
import subprocess

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
  @weight(1)
  def test_echo(self):
    """echo.py test"""
    print("*** Testing echo.py ***\n")
    echo_exec = self.set_up_file("echo.py")
    self.require_author("echo.py")

    phrases = ["Hello, World!", "ECHOOOOOOOO!!!"]
    phrases += [''.join(random.choice(string.ascii_letters) for i in range(25)) for j in range(self.trials-2)]
    for s in phrases:
      lines = self.run_and_get_out(echo_exec, f"{s}\n")
      self.maxDiff = 0
      self.assertTrue(len(lines) ==1,
        f"❌ There should be exactly 1 line of *output* (ignoring the one line of input) generated for echo.py")

      self.assertTrue(lines[0] == s, f"❌ The echo was not correct.")
    print("✅ Echos heard clearly")
    print()

  @number(2)
  @weight(7)
  def test_ana(self):
    """ana.py test"""
    print("*** Testing ana.py ***\n")
    ana_exec = self.set_up_file("ana.py")
    self.require_author("ana.py")

    for i in range(self.trials):
      s = ''.join(random.choice(string.ascii_letters) for _ in range(10))
      n = random.randint(1, 10)
      lines = self.run_and_get_out(ana_exec, f"{s}\n{n}\n")
      self.maxDiff = 0
      self.assertTrue(len(lines) == 1,
        f"❌ There should be exactly 1 line of *output* (ignoring the two lines of input) generated for ana.py")

      r = f"{s * n}{n}{s * n}"
      # self.assertEqual(lines[0], r, f"❌ output for inputs \"{s}\" and \"{n}\" was \"{lines[0]}\", expected {r}")
      self.assertTrue(lines[0] == r, f"❌ output is not correct")

    print("✅ String repetition and concatenation seem correct")
    print()

  @number(3)
  @weight(7)
  def test_divide_apples(self):
      """divide_apples.py test"""
      print("*** Testing divide_apples.py ***\n")
      apples_exec = self.set_up_file("divide_apples.py")
      self.require_author("divide_apples.py")

      for _ in range(self.trials):
          total_apples = random.randint(0, 200)
          baskets = random.randint(1, 20)

          inputs = f"{total_apples}\n{baskets}\n"
          lines = self.run_and_get_out(apples_exec, inputs)

          nums = self.get_last_nums(lines, 4, int, f"{total_apples}, {baskets}")
          self.maxDiff = 0
          self.assertTrue(nums[0] == total_apples,
              f"❌ Total apples is not correct")

          self.assertTrue(nums[1] == baskets,
              f"❌ Total baskets is not correct")

          apples_per_basket = total_apples // baskets
          self.assertTrue(nums[2] == apples_per_basket,
              f"❌ Apples per basket is not correct")

          leftover_apples = total_apples % baskets
          self.assertTrue(nums[3] == leftover_apples,
              f"❌ Leftover apples is not correct")

      print("✅ Apple distribution calculations are correct")
      print()



