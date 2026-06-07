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

def debug_print(*args, **kwargs):
    print(*args, file=sys.__stdout__, **kwargs)

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
  mod = import_module("leap_year")
except:
  pass
else:
  their = mod


their2 = None
try:
  mod2 = import_module("positive_numbers")
except:
  pass
else:
  their2 = mod2

print_on()


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
  @weight(5)
  def test_is_leap_year(self):
      """is_leap_year() test"""
      mod, fun = "leap_year", "is_leap_year"
      print(f"*** Testing {fun}() ***\n")
      self.require_file("leap_year.py")
      self.require_function(their, fun)

      passed = 0

      # 🔒 10 fixed, strong cases
      test_cases = [
          (1600, True),   # divisible by 400 → leap
          (2000, True),   # divisible by 400 → leap
          (1700, False),  # divisible by 100 but not 400 → not leap
          (1800, False),  # divisible by 100 but not 400 → not leap
          (2004, True),   # divisible by 4 but not 100 → leap
          (1996, True),   # divisible by 4 but not 100 → leap
          (2019, False),  # not divisible by 4 → not leap
          (2021, False),  # not divisible by 4 → not leap
          (2400, True),   # divisible by 400 → leap
          (2100, False),  # divisible by 100 but not 400 → not leap
      ]

      for i, (year, expected) in enumerate(test_cases, start=1):
          result = their.is_leap_year(year)
          if result == expected:
              print(f"✅ Test case {i} passed")
              passed += 1
          else:
              print(f"❌ Test case {i} failed")
              debug_print(f"    Input: {year}")
              debug_print(f"    Expected: {expected}, but got: {result}")

      
      # ✅ Final assertion
      self.assertTrue(passed == len(test_cases), f"❌ Only {passed}/{len(test_cases)} test cases passed.")

      print("✅ is_leap_year seems good")
      print()

  @number(2)
  @weight(5)
  def test_list_leap_years(self):
      """list_leap_years() test"""
      mod, fun = "leap_year", "list_leap_years"
      print(f"*** Testing {fun}() ***\n")
      self.require_file("leap_year.py")
      self.require_function(their, fun)

      passed = 0

      # 🔒 10 fixed, strong cases (cover small, large ranges, no leap years, single year, etc.)
      test_cases = [
          ((2000, 2020), [2000, 2004, 2008, 2012, 2016, 2020]),    # range with several leap years
          ((1900, 1904), [1904]),                                  # 1900 not leap, 1904 yes
          ((1897, 1903), []),                                  # no leap years
          ((1600, 1600), [1600]),                                  # single year, leap
          ((1700, 1700), []),                                      # single year, not leap
          ((1996, 2000), [1996, 2000]),                            # multiple leap years
          ((2001, 2004), [2004]),                                  # only last year leap
          ((2017, 2021), [2020]),                                  # only one leap year in range
          ((2400, 2400), [2400]),                                  # divisible by 400
          ((2100, 2104), [2104]),                                  # 2100 not leap, 2104 yes
      ]

      for i, ((start, end), expected) in enumerate(test_cases, start=1):
          result = their.list_leap_years(start, end)
          if result == expected:
              print(f"✅ Test case {i} passed")
              passed += 1
          else:
              print(f"❌ Test case {i} failed")
              debug_print(f"    Input: ({start}, {end})")
              debug_print(f"    Expected: {expected}, but got: {result}")

      # ✅ Final assertion
      self.assertTrue(passed == len(test_cases), f"❌ Only {passed}/{len(test_cases)} test cases passed.")

      print("✅ list_leap_years seems good")
      print()

  @number(3)
  @weight(5)
  def test_filter_positive(self):
      """filter_positive() test"""
      mod, fun = "positive_numbers", "filter_positive"
      print(f"*** Testing {fun}() ***\n")
      self.require_file("positive_numbers.py")
      self.require_function(their2, fun)

      passed = 0

      # 🔒 10 fixed, strong cases (positive, negative, zeros, mix)
      test_cases = [
          ([1, 2, 3], [1, 2, 3]),                     # all positive
          ([0, -1, -5], []),                          # all non-positive
          ([-5, 0, 10, 20], [10, 20]),                # mixed
          ([100, -100, 50], [100, 50]),               # positive and negative
          ([0, 0, 0], []),                            # all zeros
          ([-1, -2, -3], []),                         # all negative
          ([1, -1, 1, -1, 1], [1, 1, 1]),             # alternating
          ([7], [7]),                                 # single positive
          ([-7], []),                                 # single negative
          ([5, 0, -5, 10, -10, 0, 15], [5, 10, 15])  # larger mixed
      ]

      for i, (lst, expected) in enumerate(test_cases, start=1):
          result = their2.filter_positive(lst)
          if result == expected:
              print(f"✅ Test case {i} passed")
              passed += 1
          else:
              print(f"❌ Test case {i} failed")
              debug_print(f"    Input: {lst}")
              debug_print(f"    Expected: {expected}, but got: {result}")

      # ✅ Final assertion
      self.assertTrue(passed == len(test_cases), f"❌ Only {passed}/{len(test_cases)} test cases passed.")

      print("✅ filter_positive seems good")
      print()
