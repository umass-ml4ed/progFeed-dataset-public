"""
Tests
"""
import string
import random
import re
import os
import sys
from importlib import import_module

import unittest
from gradescope_utils.autograder_utils.decorators import number, weight
from gradescope_utils.autograder_utils.files import check_submitted_files
from feedback_generation import get_student_email, student_consented, generate_ai_feedback

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
for mod in ['to_do_list']:
  try:
    m = import_module(mod)
  except:
    pass
  else:
    mod_lookup[mod] = m
print_on()

their = mod_lookup['to_do_list'] if 'to_do_list' in mod_lookup else None

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
  @weight(5)
  def test_add_task(self):
      """add_task() test"""
      mod, fun = "to_do_list", "add_task"
      print(f"*** Testing {fun}() ***\n")
      self.require_function(mod, fun)
      
      list_ref = []
      list_their = []
      passed = 0

      # 🔒 10 fixed, strong cases
      test_tasks = [
          "Homework",                     # simple word
          "Buy groceries",                # with space
          "1234567890",                   # numeric string
          "task_with_underscores",        # underscores
          "MixedCASEtask",                # mixed case
          "!@#$%^&*()",                   # special characters
          "   leading spaces",            # leading whitespace
          "trailing spaces   ",           # trailing whitespace
          "a"*50,                         # long string (50 chars)
          "Do homework; then rest"        # punctuation & multiple words
      ]

      for i, task in enumerate(test_tasks, start=1):
          list_ref.append(task)
          ack_ref = f"Task successfully added. {len(list_ref)} tasks remaining."

          ack_their = their.add_task(list_their, task)

          if ack_ref == ack_their and list_ref == list_their:
              print(f"✅ Test case {i} passed")
              passed += 1
          else:
              print(f"❌ Test case {i} failed")


      if passed != len(test_tasks):
          student_email = get_student_email()
          if student_email and student_consented(student_email):
              feedback = generate_ai_feedback(problem_description_file="add_task_desc.txt", file_name="to_do_list.py", function_name="add_task", openaiprompt="openaiprompt.txt")
              print("\n🤖 AI Feedback for you:\n", feedback)

      # ✅ Use assertTrue instead of assertEqual
      self.assertTrue(list_ref == list_their, "❌ The list after adding tasks does not match reference")
      self.assertTrue(ack_ref == ack_their, "❌ Return string does not match.")

      print("✅ add_task seems good")
      print()


  @number(2)
  @weight(5)
  def test_delete_task(self):
      """delete_task() test"""
      mod, fun = "to_do_list", "delete_task"
      print(f"*** Testing {fun}() ***\n")
      self.require_function(mod, fun)
      
      # 🔒 Fixed initial list
      test_tasks = [
          "Homework",
          "Buy groceries",
          "1234567890",
          "task_with_underscores",
          "MixedCASEtask",
          "!@#$%^&*()",
          "   leading spaces",
          "trailing spaces   ",
          "a"*50,
          "Do homework; then rest"
      ]

      list_ref = test_tasks.copy()
      list_their = test_tasks.copy()
      passed = 0

      # Delete tasks in a fixed order
      delete_order = test_tasks.copy()

      for i, task in enumerate(delete_order, start=1):
          list_ref.remove(task)
          ack_ref = f"Task successfully deleted. {len(list_ref)} tasks remaining."

          ack_their = their.delete_task(list_their, task)

          if ack_ref == ack_their and list_ref == list_their:
              print(f"✅ Test case {i} passed")
              passed += 1
          else:
              print(f"❌ Test case {i} failed")

      if passed != len(delete_order):
          student_email = get_student_email()
          if student_email and student_consented(student_email):
              feedback = generate_ai_feedback(
                  problem_description_file="delete_task_desc.txt",
                  file_name="to_do_list.py",
                  function_name="delete_task",
                  openaiprompt="openaiprompt.txt"
              )
              print("\n🤖 AI Feedback for you:\n", feedback)

      self.assertTrue(list_ref == list_their, "❌ The list after deletions does not match reference")
      self.assertTrue(ack_ref == ack_their, "❌ Return string does not match.")

      print("✅ delete_task seems good")
      print()


  @number(3)
  @weight(5)
  def test_move_task(self):
      """move_task() test"""
      mod, fun = "to_do_list", "move_task"
      print(f"*** Testing {fun}() ***\n")
      self.require_function(mod, fun)
      
      # 🔒 Fixed initial list
      test_tasks = [
          "Homework",
          "Buy groceries",
          "1234567890",
          "task_with_underscores",
          "MixedCASEtask",
          "!@#$%^&*()",
          "   leading spaces",
          "trailing spaces   ",
          "a"*50,
          "Do homework; then rest"
      ]

      list_ref = test_tasks.copy()
      list_their = test_tasks.copy()
      passed = 0

      # Predefined move operations: (from_index, to_index)
      moves = [
          (0, 5),
          (2, 0),
          (4, 9),
          (7, 3),
          (1, 1),
          (0, 9),
          (5, 2),
          (3, 7),
          (8, 4),
          (2, 6)
      ]

      for i, (index_from, index_to) in enumerate(moves, start=1):
          task = list_ref.pop(index_from)
          list_ref.insert(index_to, task)
          ack_ref = f"Task '{task}' successfully moved to index {index_to}"

          ack_their = their.move_task(list_their, index_from, index_to)

          if ack_ref == ack_their and list_ref == list_their:
              print(f"✅ Test case {i} passed")
              passed += 1
          else:
              # print(ack_ref, ack_their)
              print(f"❌ Test case {i} failed")

      if passed != len(moves):
          student_email = get_student_email()
          if student_email and student_consented(student_email):
              feedback = generate_ai_feedback(
                  problem_description_file="move_task_desc.txt",
                  file_name="to_do_list.py",
                  function_name="move_task",
                  openaiprompt="openaiprompt.txt"
              )
              print("\n🤖 AI Feedback for you:\n", feedback)

      self.assertTrue(list_ref == list_their, "❌ The list after moves does not match reference")
      self.assertTrue(ack_ref == ack_their, "❌ Return string does not match.")

      print("✅ move_task seems good")
      print()
