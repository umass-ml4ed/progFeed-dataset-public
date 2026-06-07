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
from feedback_generation import (
    get_student_email,
    student_consented,
    generate_ai_feedback
)
# https://docs.python.org/3/library/unittest.html
# https://gradescope-utils.readthedocs.io/en/latest/source/gradescope_utils.autograder_utils.html
# https://docs.python.org/3/library/re.html
# https://stackoverflow.com/questions/15340582/python-extract-pattern-matches
# https://docs.python.org/3/library/subprocess.html#subprocess.Popen
# https://stackoverflow.com/questions/4289331/how-to-extract-numbers-from-a-string-in-python
# https://pynative.com/python-random-randrange/
# https://stackoverflow.com/questions/3131217/error-handling-when-importing-modules


def debug_print(*args, **kwargs):
    print(*args, file=sys.__stdout__, **kwargs)

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
for mod in ['triangle_class']:
  try:
    m = import_module(mod)
  except:
    pass
  else:
    mod_lookup[mod] = m
print_on()

their = mod_lookup['triangle_class'] if 'triangle_class' in mod_lookup else None

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
  @weight(7)
  def test_is_edge_sorted(self):
      """is_edge_sorted() test"""
      mod, fun = "triangle_class", "is_edge_sorted"
      print(f"*** Testing {fun}() ***\n")
      self.require_function(mod, fun)

      passed = 0

      # 🔒 10 fixed, strong cases (cover edge order, equal edges, descending order)
      test_cases = [
          ((1, 2, 3), True),          # strictly increasing
          ((3, 2, 1), False),         # strictly decreasing
          ((5, 5, 5), True),          # all equal
          ((2, 2, 3), True),          # non-decreasing with equality
          ((2, 3, 3), True),          # non-decreasing with equality
          ((7, 7, 6), False),         # equality then decreasing
          ((10, 20, 30), True),       # large increasing
          ((30, 20, 10), False),      # large decreasing
          ((100, 100, 101), True),    # edge case large numbers
          ((50, 49, 50), False),      # middle smaller than first
      ]

      for i, ((a, b, c), expected) in enumerate(test_cases, start=1):
          result = their.is_edge_sorted(a, b, c)

          if result == expected:
              print(f"✅ Test case {i} passed")
              passed += 1
          else:
              print(f"❌ Test case {i} failed")
              debug_print(f"Debugging info for {fun}")
              debug_print(f"    Input: ({a}, {b}, {c})")
              debug_print(f"    Expected: {expected}, but got: {result}")
              

      if passed != len(test_cases):
          student_email = get_student_email()
          if student_email and student_consented(student_email):
              feedback = generate_ai_feedback(
                  problem_description_file="is_edge_sorted_desc.txt",
                  file_name="triangle_class.py",
                  function_name="is_edge_sorted",
                  openaiprompt="openaiprompt.txt"
              )
              print("\n\n\n🤖🤖🤖 AI Feedback for you 🤖🤖🤖:\n", feedback)
              print('\n\n\n')

      # ✅ Final assertion
      self.assertTrue(passed == len(test_cases), f"❌ Only {passed}/{len(test_cases)} test cases passed.")

      print("✅ is_edge_sorted seems good")
      print()



  def classify_by_angles(self, a, b, c):
    if a+b <= c:
      return 'invalid'
    elif a*a + b*b == c*c:
      return 'right'
    elif a*a + b*b > c*c:
      return 'obtuse'
    else:
      return 'acute'

  def classify_by_edges(self, a, b, c):
    if a+b <= c:
      return 'invalid'
    elif a==b and b==c:
      return 'equilateral'
    elif a==b or b==c or c==a:
      return 'isosceles'
    else:
      return 'scalene'

  @number(2)
  @weight(7)
  def test_classify_by_edges(self):
      """classify_by_edges() test"""
      mod, fun = "triangle_class", "classify_by_edges"
      print(f"*** Testing {fun}() ***\n")
      self.require_function(mod, fun)

      passed = 0

      # 🔒 10 fixed, strong cases (equilateral, isosceles, scalene, invalid)
      test_cases = [
          ((3, 3, 3), "equilateral"),      # all equal
          ((5, 5, 8), "isosceles"),        # isosceles (two equal sides)
          ((7, 7, 10), "isosceles"),       # isosceles (different equal sides)
          ((6, 8, 10), "scalene"),         # classic Pythagorean triple
          ((2, 3, 4), "scalene"),          # small scalene
          ((1, 2, 3), "invalid"),          # fails triangle inequality
          ((10, 20, 30), "invalid"),       # larger invalid case
          ((100, 100, 150), "isosceles"),  # big isosceles
          ((50, 60, 70), "scalene"),       # mid-size scalene
          ((200, 200, 200), "equilateral") # large equilateral
      ]

      for i, ((a, b, c), expected) in enumerate(test_cases, start=1):
          result = their.classify_by_edges(a, b, c).lower()
          if result == expected:
              print(f"✅ Test case {i} passed")
              passed += 1
          else:
              print(f"❌ Test case {i} failed")
              debug_print(f"Debugging info for {fun}")
              debug_print(f"    Input: ({a}, {b}, {c})")
              debug_print(f"    Expected: {expected}, but got: {result}")

      if passed != len(test_cases):
          student_email = get_student_email()
          if student_email and student_consented(student_email):
              feedback = generate_ai_feedback(
                  problem_description_file="classify_by_edges_desc.txt",
                  file_name="triangle_class.py",
                  function_name="classify_by_edges",
                  openaiprompt="openaiprompt.txt"
              )
              print("\n\n\n🤖🤖🤖 AI Feedback for you 🤖🤖🤖:\n", feedback)
              print('\n\n\n')

      # ✅ Final assertion
      self.assertTrue(passed == len(test_cases), f"❌ Only {passed}/{len(test_cases)} test cases passed.")

      print("✅ classify_by_edges seems good")
      print()
  
  @number(3)
  @weight(1)
  def test_classify_by_angles(self):
      """classify_by_angles() test"""
      mod, fun = "triangle_class", "classify_by_angles"
      print(f"*** Testing {fun}() ***\n")
      self.require_function(mod, fun)

      passed = 0

      # 🔒 10 fixed, strong cases (acute, right, obtuse, invalid)
      test_cases = [
          ((3, 4, 5), "right"),        # classic right triangle
          ((5, 12, 13), "right"),      # another Pythagorean triple
          ((7, 24, 25), "right"),      # large right triangle
          ((3, 3, 4), "acute"),        # acute triangle
          ((8, 15, 17), "right"),      # right triangle
          ((10, 10, 15), "obtuse"),    # obtuse isosceles
          ((6, 8, 10), "right"),       # scaled 3-4-5
          ((2, 3, 4), "obtuse"),       # small obtuse
          ((1, 2, 3), "invalid"),      # invalid triangle
          ((50, 60, 70), "acute"),     # larger acute
      ]

      for i, ((a, b, c), expected) in enumerate(test_cases, start=1):
          result = their.classify_by_angles(a, b, c).lower()
          if result == expected:
              print(f"✅ Test case {i} passed")
              passed += 1
          else:
              print(f"❌ Test case {i} failed")
              debug_print(f"Debugging info for {fun}")
              debug_print(f"    Input: ({a}, {b}, {c})")
              debug_print(f"    Expected: {expected}, but got: {result}")

      if passed != len(test_cases):
          student_email = get_student_email()
          if student_email and student_consented(student_email):
              feedback = generate_ai_feedback(
                  problem_description_file="classify_by_angles_desc.txt",
                  file_name="triangle_class.py",
                  function_name="classify_by_angles",
                  openaiprompt="openaiprompt.txt"
              )
              print("\n\n\n🤖🤖🤖 AI Feedback for you 🤖🤖🤖:\n", feedback)
              print("\n\n\n")

      # ✅ Final assertion
      self.assertTrue(passed == len(test_cases), f"❌ Only {passed}/{len(test_cases)} test cases passed.")

      print("✅ classify_by_angles seems good")
      print()


