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
from unittest import result
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
  mod = import_module("dictionaries")
except:
  pass
else:
  their = mod
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

  # @number(1)
  # @weight(8)
  # def test_pyramid(self):
  #     """pyramid() test"""
  #     mod, fun = "loops_and_dictionaries", "pyramid"
  #     self.require_file(f"{mod}.py")
  #     print(f"*** Testing {fun}() ***\n")
  #     self.require_function(their, fun)

  #     passed = 0

  #     # 🔒 10 fixed test cases (n from 1 to 10)
  #     test_cases = [
  #         (1, "1\n"),
  #         (2, "2 1\n1\n"),
  #         (3, "3 2 1\n2 1\n1\n"),
  #         (4, "4 3 2 1\n3 2 1\n2 1\n1\n"),
  #         (5, "5 4 3 2 1\n4 3 2 1\n3 2 1\n2 1\n1\n"),
  #         (6, "6 5 4 3 2 1\n5 4 3 2 1\n4 3 2 1\n3 2 1\n2 1\n1\n"),
  #         (7, "7 6 5 4 3 2 1\n6 5 4 3 2 1\n5 4 3 2 1\n4 3 2 1\n3 2 1\n2 1\n1\n"),
  #         (8, "8 7 6 5 4 3 2 1\n7 6 5 4 3 2 1\n6 5 4 3 2 1\n5 4 3 2 1\n4 3 2 1\n3 2 1\n2 1\n1\n"),
  #         (9, "9 8 7 6 5 4 3 2 1\n8 7 6 5 4 3 2 1\n7 6 5 4 3 2 1\n6 5 4 3 2 1\n5 4 3 2 1\n4 3 2 1\n3 2 1\n2 1\n1\n"),
  #         (10, "10 9 8 7 6 5 4 3 2 1\n9 8 7 6 5 4 3 2 1\n8 7 6 5 4 3 2 1\n7 6 5 4 3 2 1\n6 5 4 3 2 1\n5 4 3 2 1\n4 3 2 1\n3 2 1\n2 1\n1\n"),
  #     ]

  #     for i, (inputs, expected) in enumerate(test_cases, start=1):
  #         their_ret = their.pyramid(inputs)

  #         if their_ret == expected:
  #             print(f"✅ Test case {i} passed")
  #             passed += 1
  #         else:
  #             print(f"❌ Test case {i} failed")
  #             debug_print(f"    Input: {inputs}")
  #             debug_print(f"    Expected: {repr(expected)}")
  #             debug_print(f"    Got: {repr(result)}")


  #     # ✅ Final assertion
  #     self.assertTrue(passed == len(test_cases),
  #                     f"❌ Only {passed}/{len(test_cases)} test cases passed.")

  #     print(f"✅ {fun} seems good")
  #     print()
  
  # @number(2)
  # @weight(7)
  # def test_merge_dicts(self):
  #     """merge_dicts() test"""
  #     mod, fun = "loops_and_dictionaries", "merge_dicts"
  #     print(f"*** Testing {fun}() ***\n")
  #     self.require_function(their, fun)

  #     passed = 0

  #     # 🔒 10 fixed, strong test cases (covering overlaps, empty dicts, and various value types)
  #     test_cases = [
  #         # 1. Both empty
  #         (({}, {}), {}),

  #         # 2. First empty
  #         (({}, {'a': 1, 'b': 2}), {'a': 1, 'b': 2}),

  #         # 3. Second empty
  #         (({'x': 9}, {}), {'x': 9}),

  #         # 4. No overlapping keys
  #         (({'a': 1, 'b': 2}, {'c': 3, 'd': 4}), {'a': 1, 'b': 2, 'c': 3, 'd': 4}),

  #         # 5. Single overlapping key
  #         (({'a': 5, 'b': 1}, {'a': 3, 'c': 2}), {'a': 8, 'b': 1, 'c': 2}),

  #         # 6. Multiple overlapping keys
  #         (({'x': 10, 'y': 5, 'z': 3}, {'y': 2, 'z': 7, 'w': 1}),
  #          {'x': 10, 'y': 7, 'z': 10, 'w': 1}),

  #         # 7. Larger numeric values
  #         (({'p': 100, 'q': 200}, {'q': 300, 'r': 400}),
  #          {'p': 100, 'q': 500, 'r': 400}),

  #         # 8. Single-element overlap, zero values
  #         (({'a': 0, 'b': 5}, {'a': 0, 'c': 10}), {'a': 0, 'b': 5, 'c': 10}),

  #         # 9. Negative values
  #         (({'a': -3, 'b': 4}, {'a': 5, 'b': -2, 'c': 7}),
  #          {'a': 2, 'b': 2, 'c': 7}),

  #         # 10. Large dictionary
  #         (({'a': 1, 'b': 2, 'c': 3, 'd': 4},
  #           {'b': 10, 'c': 20, 'd': 30, 'e': 40}),
  #          {'a': 1, 'b': 12, 'c': 23, 'd': 34, 'e': 40}),
  #     ]

  #     for i, (inputs, expected) in enumerate(test_cases, start=1):
  #         if isinstance(inputs, tuple):
  #             result = their.merge_dicts(*inputs)
  #         else:
  #             result = their.merge_dicts(inputs)

  #         if result == expected:
  #             print(f"✅ Test case {i} passed")
  #             passed += 1
  #         else:
  #             print(f"❌ Test case {i} failed")
  #             debug_print(f"    Input: {inputs}")
  #             debug_print(f"    Expected: {expected}")
  #             debug_print(f"    Got: {result}")


  #     # ✅ Final assertion
  #     self.assertTrue(passed == len(test_cases),
  #                     f"❌ Only {passed}/{len(test_cases)} test cases passed.")

  #     print(f"✅ {fun} seems good")
  #     print()
  @number(1)
  @weight(8)
  def test_most_frequent_element(self):
      """most_frequent_element test"""
      mod, fun = "dictionaries", "most_frequent_element"
      print(f"*** Testing {fun}() ***\n")
      self.require_file(f'{mod}.py')
      self.require_function(their, fun)

      passed = 0

      # 🔒 10 fixed, well-chosen test cases
      test_cases = [
          # empty list
          ([], [None]),

          # single element
          ([7], [7]),

          # all unique elements
          (["a", "b", "c"], ["a", "b", "c"]),  # any valid return; we'll accept one of them manually

          # repeated single number
          ([1, 1, 1, 1], [1]),

          # mix of numbers
          ([1, 2, 2, 3, 3, 3], [3]),

          # mix of strings
          (["apple", "banana", "apple", "pear", "banana", "apple"], ["apple"]),

          # tie between numbers
          ([5, 6, 5, 6], [5, 6]),  # any of 5 or 6 acceptable; we'll accept one manually

          # mix of numbers and strings
          (["x", 1, "x", 2, "x", 2, 2, 2], [2]),

          # large uniform list
          (["test"] * 100, ["test"]),

          # mixed case sensitivity
          (["Hello", "hello", "HELLO", "hello", "HELLO", "HELLO"], ["HELLO"]),
      ]

      for i, (inputs, expected) in enumerate(test_cases, start=1):
          result = their.most_frequent_element(inputs)

          valid_answers = expected

          if result in valid_answers:
              print(f"✅ Test case {i} passed")
              passed += 1
          else:
              print(f"❌ Test case {i} failed")
              debug_print(f"    Input: {inputs}")
              debug_print(f"    Expected one of: {valid_answers}")
              debug_print(f"    Got: {result}")

      self.assertTrue(passed == len(test_cases),
                      f"❌ Only {passed}/{len(test_cases)} test cases passed.")

      print(f"✅ {fun} seems good")
      print()
  
  @number(5)
  @weight(7)
  def test_greet_user(self):
      """greet_user() test"""
      mod, fun = "dictionaries", "greet_user"
      print(f"*** Testing {fun}() ***\n")
      self.require_file(f'{mod}.py')
      self.require_function(their, fun)

      passed = 0

      # 🧩 Common users dictionary
      users = {
          "u1": {"name": "Alice", "language": "en", "age": 25},
          "u2": {"name": "Bobby", "language": "en", "age": 12},
          "u3": {"name": "Carlos", "language": "es", "age": 30},
          "u4": {"name": "Diego", "language": "es", "age": 10},
          "u5": {"name": "Élise", "language": "fr", "age": 22},
          "u6": {"name": "François", "language": "fr", "age": 8},
          "u7": {"name": "Grace", "age": 20},           # missing language
          "u8": {"name": "Hana", "language": "es"},     # missing age
          "u9": {"name": "Ivy", "language": "fr"},      # missing age + will test with default_age override
          "u10": {"name": "Jake", "language": "en", "age": 16},
          "u12": {"name": "Kris"},                      # missing both language & age
      }

      # 🔒 11 fixed test cases (covering language, age, defaults, and missing users)
      test_cases = [
          ((users, "u1"), "Hello, Alice!"),                     # English adult
          ((users, "u2"), "Hey there, Bobby!"),                 # English child
          ((users, "u3"), "Hola, Carlos!"),                     # Spanish adult
          ((users, "u4"), "¡Hola, pequeño/a Diego!"),           # Spanish child
          ((users, "u5"), "Bonjour, Élise!"),                   # French adult
          ((users, "u7"), "Hello, Grace!"),                     # Missing language → default en
          ((users, "u8"), "Hola, Hana!"),                       # Missing age → default 18 adult
          ((users, "u9", "fr", 10), "Salut, Ivy!"),             # Missing age + override default_ages
          ((users, "u12"), "Hello, Kris!"),                     # Missing both language & age → defaults
          ((users, "u11"), "User not found."),                  # Missing user
      ]

      for i, (inputs, expected) in enumerate(test_cases, start=1):
          result = their.greet_user(*inputs)
          if result == expected:
              print(f"✅ Test case {i} passed")
              passed += 1
          else:
              print(f"❌ Test case {i} failed")
              debug_print(f"    Input: {inputs}")
              debug_print(f"    Expected: {expected}")
              debug_print(f"    Got: {result}")


      # ✅ Final assertion
      self.assertTrue(passed == len(test_cases),
                      f"❌ Only {passed}/{len(test_cases)} test cases passed.")

      print(f"✅ {fun} seems good")
      print()


