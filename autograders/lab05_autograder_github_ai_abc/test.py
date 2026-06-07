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

from feedback_generation import get_student_email, student_consented, generate_ai_feedback, student_experiment_type

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
  mod = import_module("is_prime")
except:
  pass
else:
  their = mod


their2 = None
try:
  mod2 = import_module("for_count")
except:
  pass
else:
  their2 = mod2

their3 = None
try:
  mod3 = import_module("zigzag")
except:
  pass
else:
  their3 = mod3

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
  def test_is_prime(self):
      """is_prime() test"""
      mod, fun = "is_prime", "is_prime"
      print(f"*** Testing {fun}() ***\n")
      self.require_function(their, "is_prime")
      # self.require_function(mod, fun)

      passed = 0

      # 🔒 10 fixed, strong test cases (small primes, composites, edge cases, large primes)
      test_cases = [
          (2, True),                   # smallest prime
          (3, True),                   # small prime
          (4, False),                  # smallest composite > 2
          (5, True),                   # prime after 4
          (25, False),                 # square of 5
          (97, True),                  # large two-digit prime
          (100, False),                # round number, not prime
          (7919, True),                # large known prime
          (305175781, True),           # large known prime
          (7919*331777, False)         #large composite
      ]

      for i, (n, expected) in enumerate(test_cases, start=1):
          result = their.is_prime(n)
          if result == expected:
              print(f"✅ Test case {i} passed")
              passed += 1
          else:
              print(f"❌ Test case {i} failed")
              debug_print(f"    Input: {n}")
              debug_print(f"    Expected: {expected}, but got: {result}")

      # 🧠 Generate AI feedback if not all cases passed
      if passed != len(test_cases):
          student_email = get_student_email()
          if student_email and student_consented(student_email):
              hinttype = student_experiment_type(student_email)
              feedback = generate_ai_feedback(
                  problem_description_file="is_prime_desc.txt",
                  file_name="is_prime.py",
                  function_name="is_prime",
                  openaiprompt="openaiprompt.txt",
                  hinttype=hinttype
              )
              print("\n\n\n🤖🤖🤖 AI Feedback for you 🤖🤖🤖:\n", feedback)
              print("\n\n\n")

      # ✅ Final assertion
      self.assertTrue(passed == len(test_cases), f"❌ Only {passed}/{len(test_cases)} test cases passed.")

      print("✅ is_prime seems good")
      print()

  
  @number(2)
  @weight(5)
  def test_count_strings(self):
    """count_strings test"""
    their = their2
    print("*** Testing count_strings ***\n")
    self.require_file("for_count.py")
    self.require_function(their, "count_strings")
    passed = 0

    test_cases = [
        # (strings, n, expected)
        ([], 0, 0),
        ([], 5, 0),
        (['a'], 0, 1),
        (['a'], 1, 1),
        (['a'], 2, 0),
        (['ab', 'c', 'def', 'ghij'], 2, 3),
        (['ab', 'c', 'def', 'ghij'], 4, 1),
        (['', 'a', 'bb', 'ccc'], 1, 3),
        (['xyz', 'pqrs', 't', ''], 3, 2),
        (['a'*i for i in range(10)], 5, 5),
    ]

    for i, (strings, n, expected) in enumerate(test_cases, start=1):
      result = their.count_strings(strings, n)
      if result == expected:
          print(f"✅ Test case {i} passed")
          passed += 1
      else:
          print(f"❌ Test case {i} failed")
          debug_print(f"    Input: {n}")
          debug_print(f"    Expected: {expected}, but got: {result}")

    # 🧠 Generate AI feedback if not all cases passed 
    if passed != len(test_cases):
        student_email = get_student_email()
        if student_email and student_consented(student_email):
            hinttype = student_experiment_type(student_email)
            feedback = generate_ai_feedback(
                problem_description_file="count_strings_desc.txt",
                file_name="for_count.py",
                function_name="count_strings",
                openaiprompt="openaiprompt.txt",
                hinttype=hinttype
            )
            print("\n\n\n🤖🤖🤖 AI Feedback for you 🤖🤖🤖:\n", feedback)
            print("\n\n\n")

    # ✅ Final assertion
    self.assertTrue(passed == len(test_cases), f"❌ Only {passed}/{len(test_cases)} test cases passed.")

    print("✅ count_strings seems good")
    print()

  @number(3)
  @weight(5)
  def test_is_zigzag(self):
      """is_zigzag test"""
      their = their3
      print("*** Testing is_zigzag ***\n")
      self.require_file("zigzag.py")
      self.require_function(their, "is_zigzag")

      passed = 0

      test_cases = [
          # (nums, expected)
          ([], True),                   # Empty list
          ([5], True),                  # Single element
          ([1, 2], True),               # Two elements
          ([1, 3, 2], True),            # Classic zigzag: up then down
          ([3, 1, 4, 4, 5], False),     # Breaks pattern (1<4>2<5 not consistent)
          ([1, 3, 2, 4, 3], True),      # Alternating pattern
          ([10, 5, 10, 5, 10], True),   # Down-up-down-up pattern
          ([1, 2, 3, 4], False),        # Strictly increasing → not zigzag
          ([4, 3, 2, 1], False),        # Strictly decreasing → not zigzag
          ([1, 4, 2, 6, 3, 7], True),   # Longer valid zigzag
      ]

      for i, (n, expected) in enumerate(test_cases, start=1):
          result = their.is_zigzag(n)
          if result == expected:
              print(f"✅ Test case {i} passed")
              passed += 1
          else:
              print(f"❌ Test case {i} failed")
              debug_print(f"    Input: {n}")
              debug_print(f"    Expected: {expected}, but got: {result}")

      # 🧠 Generate AI feedback if not all cases passed
      if passed != len(test_cases):
          student_email = get_student_email()
          if student_email and student_consented(student_email):
              hinttype = student_experiment_type(student_email)
              feedback = generate_ai_feedback(
                  problem_description_file="is_zigzag_desc.txt",
                  file_name="zigzag.py",
                  function_name="is_zigzag",
                  openaiprompt="openaiprompt.txt",
                  hinttype=hinttype
              )
              print("\n\n\n🤖🤖🤖 AI Feedback for you 🤖🤖🤖:\n", feedback)
              print("\n\n\n")

      # ✅ Final assertion
      self.assertTrue(passed == len(test_cases), f"❌ Only {passed}/{len(test_cases)} test cases passed.")

      print("✅ is_zigzag seems good")
      print()

