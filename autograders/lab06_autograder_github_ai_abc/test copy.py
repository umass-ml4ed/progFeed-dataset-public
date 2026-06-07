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
from feedback_generation import get_student_email, student_consented, generate_ai_feedback, student_experiment_type


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
  mod = import_module("nested_loops")
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
  # def test_get_names(self):
  #   """get_names test"""
  #   print("*** Testing get_names ***\n")
  #   self.require_function(their, "get_names")

  #   # test one or both lists empty
  #   their_ret = their.get_names([], [])
  #   self.assertEqual(their_ret, [], f"❌ get_names([], []) should return [], yours is {their_ret}")

  #   first_names = ['aaa', 'bbb']
  #   last_names = ['ccc', 'ddd']
  #   their_ret = their.get_names([], last_names)
  #   self.assertEqual(their_ret, [], f"❌ get_names([], {last_names}) should return [], yours is {their_ret}")

  #   their_ret = their.get_names(first_names, [])
  #   self.assertEqual(their_ret, [], f"❌ get_names({first_names}, []) should return [], yours is {their_ret}")

  #   # test random lists
  #   for i in range(self.trials):
  #     first_names = []
  #     last_names = []
  #     for n in range(random.randint(1, 10)):
  #       first_names.append(''.join(random.choices(string.ascii_letters, k=random.randint(3, 9))))  # generate strings of random lengths (between [3, 9])

  #     for n in range(random.randint(1, 10)):
  #       last_names.append(''.join(random.choices(string.ascii_letters, k=random.randint(3, 9))))  # generate strings of random lengths (between [3, 9])
      
  #     ref_ret = [i+' '+j for i in first_names for j in last_names]
  #     their_ret = their.get_names(first_names, last_names)
  #     self.assertEqual(their_ret, ref_ret, f"❌ get_names({first_names}, {last_names}) does not match expected output")


  #   print("✅ get_names passed all tests")
  #   print()
  @number(1)
  @weight(8)
  def test_get_names(self):
      """get_names() test"""
      mod, fun = "get_names", "get_names"
      print(f"*** Testing {fun}() ***\n")
      self.require_function(their, "get_names")

      passed = 0

      # 🔒 10 fixed, strong test cases (covering small, large, and mixed-length name lists)
      test_cases = [
          (["Alice"], ["Smith"], ["Alice Smith"]),
          (["Bob", "Carol"], ["Jones"], ["Bob Jones", "Carol Jones"]),
          (["John"], ["Doe", "Lee"], ["John Doe", "John Lee"]),
          (
              ["Ann", "Ben"],
              ["Clark", "Davis"],
              ["Ann Clark", "Ann Davis", "Ben Clark", "Ben Davis"]
          ),
          (
              ["X", "Y", "Z"],
              ["A", "B"],
              ["X A", "X B", "Y A", "Y B", "Z A", "Z B"]
          ),
          (
              ["Tom", "Jerry"],
              ["Mickey", "Donald", "Goofy"],
              ["Tom Mickey", "Tom Donald", "Tom Goofy", "Jerry Mickey", "Jerry Donald", "Jerry Goofy"]
          ),
          (
              ["Liam", "Noah", "Oliver"],
              ["Adams"],
              ["Liam Adams", "Noah Adams", "Oliver Adams"]
          ),
          (
              ["Eva", "Mia"],
              ["Brown", "Clarkson"],
              ["Eva Brown", "Eva Clarkson", "Mia Brown", "Mia Clarkson"]
          ),
          (
              ["Leo", "Nina"],
              ["Ray", "Sky", "Ash"],
              ["Leo Ray", "Leo Sky", "Leo Ash", "Nina Ray", "Nina Sky", "Nina Ash"]
          ),
          (
              ["Hasnain", "Neena"],
              ["Thota", "Lan"],
              ["Hasnain Thota", "Hasnain Lan", "Neena Thota", "Neena Lan"]
          )
      ]

      for i, (first_names, last_names, expected) in enumerate(test_cases, start=1):
          result = their.get_names(first_names, last_names)
          if result == expected:
              print(f"✅ Test case {i} passed")
              passed += 1
          else:
              print(f"❌ Test case {i} failed")
              debug_print(f"    Input: first_names={first_names}, last_names={last_names}")
              debug_print(f"    Expected: {expected}, but got: {result}")

      # 🧠 Generate AI feedback if not all cases passed
      if passed != len(test_cases):
          student_email = get_student_email()
          if student_email and student_consented(student_email):
              hinttype = student_experiment_type(student_email)
              feedback = generate_ai_feedback(
                  problem_description_file="get_names_desc.txt",
                  file_name="nested_loops.py",
                  function_name="get_names",
                  openaiprompt="openaiprompt.txt",
                  hinttype=hinttype
              )
              print("\n\n\n🤖🤖🤖 AI Feedback for you 🤖🤖🤖:\n", feedback)
              print("\n\n\n")

      # ✅ Final assertion
      self.assertTrue(passed == len(test_cases),
                      f"❌ Only {passed}/{len(test_cases)} test cases passed.")

      print("✅ get_names seems good")
      print()



  @number(2)
  @weight(7)
  def test_average_scores(self):
    """average_scores test"""
    print("*** Testing average_scores ***\n")
    self.require_function(their, "average_scores")

    # test single commodity price
    scores = []
    total = 0
    for i in range(1000):
        all_scores = []
        answers = []
        num_students = random.randint(3, 9)
        for j in range(num_students):
            scores = []
            total = 0
            for k in range(random.randint(4, 6)):
                score = random.randint(0, 10)*10
                lateness = random.randint(0, 4)
                scores.append(tuple([score, lateness]))
                if lateness == 0:
                    total += score
                elif  lateness == 1:
                    total += score * 0.9
                elif lateness == 2:
                    total += score * 0.75
                elif lateness == 3:
                    total += score * 0.5
                
            all_scores.append(scores)
            answers.append(round(total / len(scores), 2))
      
        their_ret = their.average_scores(all_scores)
        their_ret_reformatted = [round(avg, 2) for avg in their_ret]
        self.assertEqual(their_ret_reformatted, answers, f"❌ average_scores({all_scores}) should return a list {answers}, yours is {their_ret_reformatted}")

    print("✅ average_scores passed all tests")
    print()


