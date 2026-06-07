import sys
import unittest
from gradescope_utils.autograder_utils.json_test_runner import JSONTestRunner

if __name__ == '__main__':
    results = '/autograder/results/results.json'
    if len(sys.argv) > 1:
        results = 'results.json'

    suite = unittest.defaultTestLoader.discover('.')
    with open(results, 'w') as f:
        JSONTestRunner(visibility='visible', stdout_visibility='visible', stream=f).run(suite)
