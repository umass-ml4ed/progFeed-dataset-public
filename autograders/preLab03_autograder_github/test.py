"""
Tests
"""
import string
import random
import re
import os
import sys
import math
from importlib import import_module

import unittest
from gradescope_utils.autograder_utils.decorators import number, weight
from gradescope_utils.autograder_utils.files import check_submitted_files

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
for mod in ['list_class']:
  try:
    m = import_module(mod)
  except:
    pass
  else:
    mod_lookup[mod] = m
print_on()

their = mod_lookup['list_class'] if 'list_class' in mod_lookup else None

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
  @weight(10)
  def test_combine_lists(self):
      """combine_lists() test"""
      mod, fun = "list_class", "combine_lists"
      print(f"*** Testing {fun}() ***\n")
      self.require_function(mod, fun)

      passed = 0

      # 🔒 10 fixed, strong cases
      test_cases = [
          # (a, b, expected_result)
          ([1, 2, 3], [4, 5, 6, 7], [4, 1, 3, 7]),
          ([1, 2, 3, 4, 5], [4, 5, 6, 7], [4, 1, 2, 4, 5, 7]),
          ([10], [1, 2, 3], [1, 3]),                      # single element in a
          ([5, 6, 7], [9, 8], [9, 5, 7, 8]),                  # b with 2 elements
          ([0, 1, 2, 3, 4], [100, 200, 300], [100, 0, 1, 3, 4, 300]),
          ([9, 8, 7], [1, 2, 3, 4, 5], [1, 9, 7, 5]),
          ([42], [99], [99, 99]),                         # a = 1 element, b = 1 element
          ([11, 22, 33, 44, 55], [77, 88], [77, 11, 22, 44, 55, 88]),
          ([7, 14, 21], [2, 4, 6, 8], [2, 7, 21, 8]),
          ([100, 200, 300, 400, 500], [0, 9], [0, 100, 200, 400, 500, 9]),
      ]

      for i, (a, b, expected) in enumerate(test_cases, start=1):
          result = their.combine_lists(a.copy(), b.copy())

          if result == expected:
              print(f"✅ Test case {i} passed")
              passed += 1
          else:
              print(f"❌ Test case {i} failed")

      # ✅ Final assertion
      self.assertTrue(passed == len(test_cases), f"❌ Only {passed}/{len(test_cases)} test cases passed.")

      print("✅ combine_lists seems good")
      print()
  
  @number(2)
  @weight(10)
  def test_classify_by_length(self):
      """classify_by_length() test"""
      mod, fun = "list_class", "classify_by_length"
      print(f"*** Testing {fun}() ***\n")
      self.require_function(mod, fun)

      passed = 0

      # 🔒 fixed test cases: (input list, expected result)
      test_cases = [
          ([], "empty"),                     # empty list
          ([1], "odd_length"),               # single element
          ([1, 2], "even_length"),           # two elements
          ([1, 2, 3], "odd_length"),         # three elements
          ([1, 2, 2, 3], "even_length"),     # four elements
          ([0, 0, 0, 0, 0], "odd_length"),   # five elements
          ([9, 8, 7, 6], "even_length"),     # four elements
          ([42], "odd_length"),              # single element again
          ([10, 20, 30, 40, 50, 60], "even_length"), # six elements
          ([100, 200, 300], "odd_length")    # three elements
      ]

      for i, (lst, expected) in enumerate(test_cases, start=1):
          result = their.classify_by_length(lst.copy())

          if result == expected:
              print(f"✅ Test case {i} passed")
              passed += 1
          else:
              print(f"❌ Test case {i} failed")  

      # ✅ Final assertion
      self.assertTrue(passed == len(test_cases), f"❌ Only {passed}/{len(test_cases)} test cases passed.")

      print("✅ classify_by_length seems good")
      print()




