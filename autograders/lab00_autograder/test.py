"""
Tests
"""
from difflib import SequenceMatcher, unified_diff
import re
import os

import unittest
from gradescope_utils.autograder_utils.decorators import tags, number, weight
from gradescope_utils.autograder_utils.files import check_submitted_files

class TestProject(unittest.TestCase):
  def require_file(self, fname):
    missing_files = check_submitted_files([fname], base='.')
    self.assertEqual(len(missing_files), 0, f"Missing {fname}! ❌\nPerhaps the file is not named correctly, it needs to match {fname} exactly \nOr perhaps there is some critical error stopping the file from being read...")

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

  @number(1.0)
  @weight(5)
  def test_hello_exists(self):
    """hello.py exists"""
    self.meta_test_file_exists("hello.py")

  @number(1.1)
  @weight(5)
  def test_hello_author(self):
    """hello.py author"""
    self.meta_test_file_author("hello.py")

  @number(1.2)
  @weight(5)
  def test_hello(self):
    """hello.py test"""
    print("*** Testing hello.py ***\n")
    self.require_file("hello.py")

    os.system("rm -f output.txt")
    os.system("python3 hello.py > output.txt")

    with open("output.txt") as fd:
      line = fd.read()

    #self.assertTrue(re.match(r"(HELLO|(H|h)ello),? (WORLD|(W|w)orld).*", line),
    #  "Output does not seem to be \"Hello, World!\" ❌")
    line = str(line)
    line = line[:-1] if line[-1] =='\n' else line
    self.assertEqual(line,"Hello, World!", f"Output does not seem to be \"Hello, World!\", instead it is \"{line}\"\nYou can use the above text to identify what characters are different,\n\t what needs to be added, and what needs to be removed to make the program produce correct output.")

    print("✅ World successfully greeted, nicely done")
    print()
