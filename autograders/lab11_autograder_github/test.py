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
from itertools import permutations

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
import sys

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
  mod = import_module("recursion")
except:
  pass
else:
  their = mod
print_on()

def funky(x):
  if x==0 or x==1:
    return 1
  if x%2==0:
    return 2*funky(x//2)
  return 1+2*funky(x+1)

def max_recursive(lst):
    if len(lst) == 0:
        return 0  # or raise an exception
    else:
        sub_max = max_recursive(lst[1:])
        return lst[0] if lst[0] > sub_max else sub_max


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

  def require_recursion(self, func, *args, **kwargs):
    old_limit = sys.getrecursionlimit()
    # print(f"Current recursion limit: {old_limit}")
    sys.setrecursionlimit(30)   # very shallow limit

    try:
        func(*args, **kwargs)
        self.assertTrue(False,f'❌ the function {func.__name__}() is not recursive')
        return False
    except RecursionError:
        print(f"✅ the function {func.__name__}() is recursive")
        return True    
    finally:
        sys.setrecursionlimit(old_limit)

    return False


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
  def test_funky(self):
    """funky test"""
    print("*** Testing funky ***\n")
    self.require_function(their, "funky")
    self.require_recursion(their.funky, 1000000)

    # test base case
    their_ret = their.funky(0)
    ref_ret = 1
    self.assertEqual(their_ret, ref_ret, f"❌ funky(0) should return {ref_ret}, yours is {their_ret}")

    their_ret = their.funky(1)
    ref_ret = 1
    self.assertEqual(their_ret, ref_ret, f"❌ funky(1) should return {ref_ret}, yours is {their_ret}")


    for n in range(-500, 501, 10):
        their_ret = their.funky(n)
        ref_ret = funky(n)
        self.assertEqual(their_ret, ref_ret, f"❌ funky({n}) should return {ref_ret}, yours is {their_ret}")

    print("✅ funky passed all tests")
    print()


  @number(2)
  @weight(5)
  def test_max_recursive(self):
      """max_recursive test"""
      print("*** Testing max_recursive ***\n")
      self.require_function(their, "max_recursive")
      self.require_recursion(their.max_recursive, [1]*1000)

      # --- base case tests ---
      lst = [5]
      their_ret = their.max_recursive(lst)
      ref_ret = max_recursive(lst)
      self.assertEqual(their_ret, ref_ret,
                      f"❌ max_recursive({lst}) should return {ref_ret}, yours is {their_ret}")

      lst = [1.5]
      their_ret = their.max_recursive(lst)
      ref_ret = max_recursive(lst)
      self.assertEqual(their_ret, ref_ret,
                      f"❌ max_recursive({lst}) should return {ref_ret}, yours is {their_ret}")

      # --- small lists ---
      test_lists = [
          [1, 2],
          [2, 1],
          [10, 5, 7],
          [3.2, 3.1, 3.3],
          [100, 99, 98, 150],
          [5, 5, 5, 5],
          [0.1, 0.9, 0.3, 0.2]
      ]

      for lst in test_lists:
          their_ret = their.max_recursive(lst)
          ref_ret = max_recursive(lst)
          self.assertEqual(their_ret, ref_ret,
                          f"❌ max_recursive({lst}) should return {ref_ret}, yours is {their_ret}")

      # --- large randomized tests ---
      import random
      random.seed(0)

      for _ in range(200):
          size = random.randint(1, 50)
          lst = [random.uniform(0.1, 1000.0) for _ in range(size)]
          their_ret = their.max_recursive(lst)
          ref_ret = max_recursive(lst)
          self.assertEqual(their_ret, ref_ret,
                          f"❌ max_recursive({lst[:10]}...) incorrect result")

      print("✅ max_recursive passed all tests")
      print()
  
  @number(3)
  @weight(5)
  def test_sum_lists_recursive(self):
      """sum_lists_recursive test"""
      print("*** Testing sum_lists_recursive ***\n")
      self.require_function(their, "sum_lists_recursive")
      self.require_recursion(their.sum_lists_recursive, [1]*1000, [1]*1000)

      # reference implementation
      def ref_sum_lists_recursive(a, b):
          if not a and not b:
              return 0
          return a[0] + b[0] + ref_sum_lists_recursive(a[1:], b[1:])

      # --- base cases ---
      lst1, lst2 = [], []
      their_ret = their.sum_lists_recursive(lst1, lst2)
      ref_ret = ref_sum_lists_recursive(lst1, lst2)
      self.assertEqual(their_ret, ref_ret,
                      f"❌ sum_lists_recursive({lst1}, {lst2}) should return {ref_ret}, yours is {their_ret}")

      lst1, lst2 = [5], [7]
      their_ret = their.sum_lists_recursive(lst1, lst2)
      ref_ret = ref_sum_lists_recursive(lst1, lst2)
      self.assertEqual(their_ret, ref_ret,
                      f"❌ sum_lists_recursive({lst1}, {lst2}) should return {ref_ret}, yours is {their_ret}")

      # --- small fixed tests ---
      tests = [
          ([1, 2], [3, 4]),
          ([10, 20, 30], [1, 2, 3]),
          ([0, 0, 0], [0, 0, 0]),
          ([5, 5, 5], [5, 5, 5]),
          ([100], [200]),
          ([2, 4, 6, 8], [1, 3, 5, 7]),
      ]

      for lst1, lst2 in tests:
          their_ret = their.sum_lists_recursive(lst1, lst2)
          ref_ret = ref_sum_lists_recursive(lst1, lst2)
          self.assertEqual(their_ret, ref_ret,
                          f"❌ sum_lists_recursive({lst1}, {lst2}) should return {ref_ret}, yours is {their_ret}")

      # --- randomized tests ---
      import random
      random.seed(0)

      for _ in range(200):
          size = random.randint(0, 30)
          lst1 = [random.randint(0, 1000) for _ in range(size)]
          lst2 = [random.randint(0, 1000) for _ in range(size)]
          their_ret = their.sum_lists_recursive(lst1, lst2)
          ref_ret = ref_sum_lists_recursive(lst1, lst2)
          self.assertEqual(their_ret, ref_ret,
                          f"❌ sum_lists_recursive({lst1[:5]}..., {lst2[:5]}...) incorrect result")

      print("✅ sum_lists_recursive passed all tests")
      print()


  @number(4)
  @weight(0)
  def test_permutations(self):
    """permutations test"""
    print("*** Testing permutations ***\n")
    self.require_function(their, "permutations")
    # self.require_recursion(their.permutations, [1,2,3,4,5,6,7,8,9,10])

    # test base case
    lis = [110]
    their_ret = their.permutations(lis)
    ref_ret = [[110]]
    self.assertEqual(isinstance(their_ret[0], list), True, f"❌ permutations({lis}) should return a list of lists {ref_ret}, yours is {their_ret}")
    self.assertEqual(their_ret, ref_ret, f"❌ permutations({lis}) should return {ref_ret}, yours is {their_ret}")

    # utility function to convert list of lists to set of tuples for easy comparison
    l2s = lambda lis : {tuple(e) for e in lis}
    # test 2-element case
    lis = ['A', 1]
    their_ret = their.permutations(lis)
    ref_ret = [['A',1], [1,'A']]
    self.assertEqual(l2s(their_ret), l2s(ref_ret), f"❌ permutations({lis}) should return {ref_ret}, yours is {their_ret}")

    # test n-element case
    nfac = 2
    for n in range(3, 10):
        lis = [k if random.random()>0.5 else chr(64+k) for k in range(1, n+1)]
        their_ret = their.permutations(lis)
        nfac *= n
        self.assertEqual(nfac, len(their_ret), f"❌ calling your permutations with a {n}-element list should return a list whose length is {nfac}, yours is {len(their_ret)}")
        ref_ret = [e for e in permutations(lis)]
        self.assertEqual(l2s(their_ret), l2s(ref_ret), f"❌ calling your permutations with a {n}-element list did not return the correct result")

    print("✅ permutations passed all tests")
    print()



