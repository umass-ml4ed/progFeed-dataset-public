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
from feedback_generation import (
    generate_ai_feedback,
    student_consented,
    student_experiment_type,
    get_student_email,)

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
  if sys.stdout == sys.__stdout__:
    sys.stdout = open(os.devnull, 'w')

def print_on():
  if sys.stdout != sys.__stdout__:
    sys.stdout.close()
    sys.stdout = sys.__stdout__

print_off()
their = None
try:
  mod = import_module("files")
except:
  pass
else:
  their = mod
print_on()

def write_grades_to_file(grades, fname='grades.txt'):
  with open(fname, 'w') as f:
    for i in range(len(grades)):
      f.write(str(grades[i]))
      if i!=len(grades)-1:
        f.write('\n')

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
  # @weight(5)
  # def test_count_words(self):
  #     """count_words() test"""
  #     mod, fun = "dictionaries", "count_words"
  #     self.require_file(f"{mod}.py")
  #     print(f"*** Testing {fun}() ***\n")
  #     self.require_function(their, fun)

  #     passed = 0

  #     # 🔒 10 fixed, strong test cases (empty input, repeats, mixed words)
  #     test_cases = [
  #         ((), {}),  # empty tuple
  #         (("hello",), {"hello": 1}),
  #         (("hello", "hello"), {"hello": 2}),
  #         (("hi", "hi", "hi"), {"hi": 3}),
  #         (("a", "b", "a", "b", "a"), {"a": 3, "b": 2}),
  #         (("apple", "banana", "apple", "cherry", "banana", "apple"), {"apple": 3, "banana": 2, "cherry": 1}),
  #         (("one", "two", "three", "two", "three", "three"), {"one": 1, "two": 2, "three": 3}),
  #         (("repeat", "once", "repeat", "repeat", "once"), {"repeat": 3, "once": 2}),
  #         (("case", "Case", "CASE", "case"), {"case": 2, "Case": 1, "CASE": 1}),  # case-sensitive
  #         (("x", "y", "z", "x", "y", "x", "z", "z", "z"), {"x": 3, "y": 2, "z": 4}),
  #     ]

  #     for i, (inputs, expected) in enumerate(test_cases, start=1):
  #         try:
  #             result = their.count_words(inputs)
  #         except:
  #             result = "EXCEPTION"

  #         if result == expected:
  #             print(f"✅ Test case {i} passed")
  #             passed += 1
  #         else:
  #             print(f"❌ Test case {i} failed")
  #             debug_print(f"    Input: {inputs}")
  #             debug_print(f"    Expected: {expected}")
  #             debug_print(f"    Got: {result}")

  #     # 🧠 AI feedback generation
  #     if passed != len(test_cases):
  #         student_email = get_student_email()
  #         if student_email and student_consented(student_email):
  #             hinttype = student_experiment_type(student_email)
  #             feedback = generate_ai_feedback(
  #                 problem_description_file="count_words_desc.txt",
  #                 file_name="dictionaries.py",
  #                 function_name="count_words",
  #                 openaiprompt="openaiprompt.txt",
  #                 hinttype=hinttype
  #             )
  #             print("\n\n\n🤖🤖🤖 AI Feedback for you 🤖🤖🤖:\n", feedback)
  #             print("\n\n\n")

  #     # ✅ Final assertion
  #     self.assertTrue(passed == len(test_cases),
  #                     f"❌ Only {passed}/{len(test_cases)} test cases passed.")

  #     print(f"✅ {fun} seems good")
  #     print()

  
  @number(1)
  @weight(8)
  def test_print_stars_to_file(self):
      """print_stars_to_file() test"""
      mod, fun = "files", "print_stars_to_file"
      self.require_file(f"{mod}.py")
      print(f"*** Testing {fun}() ***\n")
      self.require_function(their, fun)

      passed = 0

      # 🔒 10 fixed, strong test cases
      test_cases = [
          (1, "*\n"),
          (2, " *\n***\n"),
          (3, "  *\n ***\n*****\n"),
          (4, "   *\n  ***\n *****\n*******\n"),
          (5, "    *\n   ***\n  *****\n *******\n*********\n"),
          (6, "     *\n    ***\n   *****\n  *******\n *********\n***********\n"),
          (7, "      *\n     ***\n    *****\n   *******\n  *********\n ***********\n*************\n"),
          (8, "       *\n      ***\n     *****\n    *******\n   *********\n  ***********\n *************\n***************\n"),
          (9, "        *\n       ***\n      *****\n     *******\n    *********\n   ***********\n  *************\n ***************\n*****************\n"),
          (10, "         *\n        ***\n       *****\n      *******\n     *********\n    ***********\n   *************\n  ***************\n *****************\n*******************\n"),
      ]

      for i, (inputs, expected) in enumerate(test_cases, start=1):
          try:
              fname = 'stars_'+str(inputs)+'.txt'
              if os.path.exists(fname):
                  os.remove(fname)  # delete existing file
              their.print_stars_to_file(inputs)
              if os.path.exists(fname):
                  with open(fname, 'r') as f:
                      result = f.read()
                      if result[-1]=='\n':
                          result = result[:-1]
                      if expected[-1]=='\n':
                          expected = expected[:-1]
                  os.remove(fname)  # clean up after test
              else:
                  result = "FILE_NOT_FOUND"
          except:
              result = "EXCEPTION"

          if result == expected:
              print(f"✅ Test case {i} passed")
              passed += 1
          else:
              print(f"❌ Test case {i} failed")
              debug_print(f"    Input: {inputs}")
              debug_print(f"    Expected: {expected}")
              debug_print(f"    Got: {result}")

      # 🧠 AI feedback generation
      if passed != len(test_cases):
          student_email = get_student_email()
          if student_email and student_consented(student_email):
              hinttype = student_experiment_type(student_email)
              feedback = generate_ai_feedback(
                  problem_description_file="print_stars_to_file_desc.txt",
                  file_name="files.py",
                  function_name="print_stars_to_file",
                  openaiprompt="openaiprompt.txt",
                  hinttype=hinttype
              )
              print("\n\n\n🤖🤖🤖 AI Feedback for you 🤖🤖🤖:\n", feedback)
              print("\n\n\n")

      # ✅ Final assertion
      self.assertTrue(passed == len(test_cases),
                      f"❌ Only {passed}/{len(test_cases)} test cases passed.")

      print(f"✅ {fun} seems good")
      print()
  
  
  @number(2)
  @weight(7)
  def test_calc_avg_from_file(self):
      """calc_avg_from_file() test"""
      mod, fun = "files", "calc_avg_from_file"
      self.require_file(f"{mod}.py")
      print(f"*** Testing {fun}() ***\n")
      self.require_function(their, fun)

      passed = 0

      # 🔒 10 fixed, strong test cases
      test_cases = [
          ([1.0], 1.0),
          ([2.0, 4.0], 3.0),
          ([3.0, 6.0, 9.0], 6.0),
          ([10.0, 20.0, 30.0, 40.0], 25.0),
          ([5.0, 15.0, 25.0, 35.0, 45.0], 25.0),
          ([7.5, 12.5, 17.5], 12.5),
          ([100.0, 200.0, 300.0, 400.0, 500.0], 300.0),
          ([0.0, 10.0, 20.0, 30.0], 15.0),
          ([1.5, 2.5, 3.5, 4.5, 5.5], 3.5),
          ([50.0, 60.0, 70.0, 80.0, 90.0, 100.0], 75.0),
      ]

      for i, (inputs, expected) in enumerate(test_cases, start=1):
          try:
              write_grades_to_file(inputs)
              result = their.calc_avg_from_file()
          except:
              result = "EXCEPTION"

          if isinstance(result, float) and abs(result - expected) < 0.01:
              print(f"✅ Test case {i} passed")
              passed += 1
          else:
              print(f"❌ Test case {i} failed")
              debug_print(f"    Input: {inputs}")
              debug_print(f"    Expected: {expected}")
              debug_print(f"    Got: {result}")

      # 🧠 AI feedback generation
      if passed != len(test_cases):
          student_email = get_student_email()
          if student_email and student_consented(student_email):
              hinttype = student_experiment_type(student_email)
              feedback = generate_ai_feedback(
                  problem_description_file="calc_avg_from_file_desc.txt",
                  file_name="files.py",
                  function_name="calc_avg_from_file",
                  openaiprompt="openaiprompt.txt",
                  hinttype=hinttype
              )
              print("\n\n\n🤖🤖🤖 AI Feedback for you 🤖🤖🤖:\n", feedback)
              print("\n\n\n")

      # ✅ Final assertion
      self.assertTrue(passed == len(test_cases),
                      f"❌ Only {passed}/{len(test_cases)} test cases passed.")

      print(f"✅ {fun} seems good")
      print()
  
  
