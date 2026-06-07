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
  # @weight(5)
  # def test_count_words(self):
  #   """count_words test"""
  #   print("*** Testing count_words ***\n")
  #   self.require_function(their, "count_words")

  #   # test single word repeated
  #   for i in range(5):
  #     words = tuple(['hello']*i)
  #     ref_ret = {} if i==0 else {'hello':i}
  #     their_ret = their.count_words(words)
  #     self.assertEqual(their_ret, ref_ret, f"❌ count_words({words}) should return {ref_ret}, yours is {their_ret}")

  #   # test 10 words sampled with random probability
  #   pool = ('hello', 'world', 'hello-world', 'hello world', 'count', 'words', 'tests', 'test', 'python', 'number')
  #   sample = []
  #   for w in pool:
  #     sample += [w]*random.randint(1, 10)
  #   words = tuple(random.choices(sample, k=5000))

  #   # build reference solution
  #   d = {}
  #   for word in words:
  #     if word in d:
  #       d[word] += 1
  #     else:
  #       d[word] = 1

  #   their_ret = their.count_words(words)
  #   ref_ret = d
  #   self.assertEqual(their_ret, ref_ret, f"❌ count_words(words) should return {ref_ret}, yours is {their_ret}")

  #   print("✅ count_words passed all tests")
  #   print()
  @number(1)
  @weight(5)
  def test_count_words(self):
      """count_words() test"""
      mod, fun = "dictionaries", "count_words"
      self.require_file(f"{mod}.py")
      print(f"*** Testing {fun}() ***\n")
      self.require_function(their, fun)

      passed = 0

      # 🔒 10 fixed, strong test cases (empty input, repeats, mixed words)
      test_cases = [
          ((), {}),  # empty tuple
          (("hello",), {"hello": 1}),
          (("hello", "hello"), {"hello": 2}),
          (("hi", "hi", "hi"), {"hi": 3}),
          (("a", "b", "a", "b", "a"), {"a": 3, "b": 2}),
          (("apple", "banana", "apple", "cherry", "banana", "apple"), {"apple": 3, "banana": 2, "cherry": 1}),
          (("one", "two", "three", "two", "three", "three"), {"one": 1, "two": 2, "three": 3}),
          (("repeat", "once", "repeat", "repeat", "once"), {"repeat": 3, "once": 2}),
          (("case", "Case", "CASE", "case"), {"case": 2, "Case": 1, "CASE": 1}),  # case-sensitive
          (("x", "y", "z", "x", "y", "x", "z", "z", "z"), {"x": 3, "y": 2, "z": 4}),
      ]

      for i, (inputs, expected) in enumerate(test_cases, start=1):
          try:
              result = their.count_words(inputs)
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
                  problem_description_file="count_words_desc.txt",
                  file_name="dictionaries.py",
                  function_name="count_words",
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

  
  # @number(2)
  # @weight(5)
  # def test_average_prices(self):
  #   """average_prices test"""
  #   print("*** Testing average_prices ***\n")
  #   self.require_function(their, "average_prices")

  #   # test single commodity price
  #   prices = []
  #   total = 0
  #   for i in range(11):
  #     # to avoid floating point issues, we will compare total price instead
  #     ref_ret = {} if i==0 else {'milk':round(total, 2)}
  #     their_ret = their.average_prices(tuple(prices))
  #     for k in their_ret:
  #       their_ret[k] = round(their_ret[k]*i, 2)
  #     self.assertEqual(their_ret, ref_ret, f"❌ average_prices({prices}) should return {ref_ret}, yours is {their_ret}")
  #     price = self.rand_price(4, 6)
  #     total += price
  #     prices.append(('milk', price))

  #   # test 8 random commodity prices
  #   items = (('pencil', 0.5, 1.0), ('chicken', 3, 6), ('pasta', 1, 2), ('lobster', 20, 30), ('eggs', 2, 4), ('milk', 4, 8), ('ipad', 299, 399), ('imac', 899, 1099))
  #   prices = []
  #   for i in range(1000):
  #     s = random.choice(items)
  #     price = self.rand_price(s[1], s[2])
  #     prices.append((s[0], price))

  #   # build reference solution --> total price per item instead of average
  #   dict = {}
  #   count = {}
  #   for item in prices:
  #     if item[0] in dict:
  #       dict[item[0]] += item[1]
  #       count[item[0]]+= 1
  #     else:
  #       dict[item[0]] = item[1]
  #       count[item[0]] = 1

  #   ref_ret = dict
  #   ref_ret_avg = dict.copy()
  #   for key in ref_ret_avg:
  #     ref_ret_avg[key] /= count[key]

  #   for key in ref_ret:
  #     ref_ret[key] = round(ref_ret[key], 2) # compute total price rounded to 2 decimal points

  #   their_ret = their.average_prices(prices)
  #   their_ret_avg = their_ret.copy()
  #   for k in their_ret:
  #     their_ret[k] = round(their_ret[k]*count[k], 2)  # compute total price rounded to 2 decimal points
  #   self.assertEqual(their_ret, ref_ret, f"❌ average_prices(prices) should return {ref_ret_avg}, yours is {their_ret_avg}")

  #   print("✅ average_prices passed all tests")
  #   print()
  
  @number(2)
  @weight(5)
  def test_average_prices(self):
      """average_prices() test"""
      mod, fun = "dictionaries", "average_prices"
      print(f"*** Testing {fun}() ***\n")
      self.require_file(f"{mod}.py")
      self.require_function(their, fun)

      passed = 0

      # 🔒 10 fixed, strong test cases (single and multiple items, varying quantities)
      test_cases = [
          # empty list
          ([], {}),

          # single item, single price
          ([('milk', 4.0)], {'milk': 4.0}),

          # single item, multiple prices
          ([('milk', 4.0), ('milk', 6.0)], {'milk': 5.0}),

          # two items, no overlap
          ([('milk', 4.0), ('eggs', 2.0)], {'milk': 4.0, 'eggs': 2.0}),

          # two items, multiple prices
          ([('milk', 4.0), ('milk', 6.0), ('eggs', 2.0), ('eggs', 4.0)],
           {'milk': 5.0, 'eggs': 3.0}),

          # three items, multiple prices
          ([('milk', 4.0), ('milk', 6.0), ('eggs', 2.0), ('eggs', 4.0), ('bread', 3.0)],
           {'milk': 5.0, 'eggs': 3.0, 'bread': 3.0}),

          # repeated same price
          ([('milk', 5.0), ('milk', 5.0), ('milk', 5.0)], {'milk': 5.0}),

          # single high value item
          ([('lobster', 25.5)], {'lobster': 25.5}),

          # two items, mixed prices
          ([('milk', 4.0), ('milk', 6.0), ('bread', 2.5), ('bread', 3.5)],
           {'milk': 5.0, 'bread': 3.0}),

          # three items, overlapping quantities
          ([('milk', 4.0), ('milk', 6.0), ('eggs', 2.0), ('eggs', 4.0), ('bread', 2.0), ('bread', 4.0)],
           {'milk': 5.0, 'eggs': 3.0, 'bread': 3.0}),
      ]

      for i, (inputs, expected) in enumerate(test_cases, start=1):
          try:
              result = their.average_prices(inputs)
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
                  problem_description_file="average_prices_desc.txt",
                  file_name="dictionaries.py",
                  function_name="average_prices",
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

  # @number(3)
  # @weight(5)
  # def test_count_bigrams(self):
  #   """count_bigrams test"""
  #   print("*** Testing count_bigrams ***\n")
  #   self.require_function(their, "count_bigrams")

  #   # test single word repeated
  #   for i in range(10):
  #     words = tuple(['hello']*i)
  #     ref_ret = {} if i<2 else {('hello', 'hello'):i-1}
  #     their_ret = their.count_bigrams(words)
  #     self.assertEqual(their_ret, ref_ret, f"❌ count_bigrams({words}) should return {ref_ret}, yours is {their_ret}")

  #   # test random letter bigrams
  #   words = tuple(random.choices(string.ascii_lowercase, k=5000))

  #   # build reference solution
  #   dict = {}
  #   for i in range(len(words)-1):
  #     key = (words[i], words[i+1])
  #     if key in dict:
  #       dict[key] += 1
  #     else:
  #       dict[key] = 1
    
  #   their_ret = their.count_bigrams(words)
  #   ref_ret = dict
  #   self.assertEqual(len(their_ret), len(ref_ret), f"❌ count_bigrams(words) should have {len(ref_ret)} entries, yours has {len(their_ret)}")
  #   self.assertEqual(their_ret, ref_ret, f"❌ count_bigrams(words) should return {ref_ret}, yours is {their_ret}")

  #   print("✅ count_bigrams passed all tests")
  #   print()

  # def rand_price(self, low, high):
  #   return round(random.triangular(low, high),2)


  @number(3)
  @weight(5)
  def test_count_bigrams(self):
      """count_bigrams() test"""
      mod, fun = "dictionaries", "count_bigrams"
      print(f"*** Testing {fun}() ***\n")
      self.require_file(f"{mod}.py")
      self.require_function(their, fun)

      passed = 0

      # 🔒 10 fixed, strong test cases (single word repeats, multiple words, edge cases)
      test_cases = [
          # empty tuple
          ((), {}),

          # single word
          (("hello",), {}),

          # two same words
          (("hello", "hello"), {("hello", "hello"): 1}),

          # three same words
          (("hello", "hello", "hello"), {("hello", "hello"): 2}),

          # two different words
          (("hi", "there"), {("hi", "there"): 1}),

          # three different words
          (("a", "b", "c"), {("a", "b"): 1, ("b", "c"): 1}),

          # mix repeats
          (("cat", "dog", "cat", "dog"), {("cat", "dog"): 2, ("dog", "cat"): 1}),

          # four words, some repeats
          (("a", "b", "a", "b", "a"), {("a", "b"): 2, ("b", "a"): 2}),

          # case-sensitive
          (("Hello", "hello", "HELLO", "Hello"), {("Hello", "hello"): 1, ("hello", "HELLO"): 1, ("HELLO", "Hello"): 1}),

          # longer sequence
          (("x", "y", "z", "x", "y", "z"), {("x", "y"): 2, ("y", "z"): 2, ("z", "x"): 1}),
      ]

      for i, (inputs, expected) in enumerate(test_cases, start=1):
          try:
             result = their.count_bigrams(inputs)
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
                  problem_description_file="count_bigrams_desc.txt",
                  file_name="dictionaries.py",
                  function_name="count_bigrams",
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
