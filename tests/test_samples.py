import unittest
import pytest

from approvaltests.approvals import verify, verify_all

from approvaltests.reporters.python_native_reporter import PythonNativeReporter
from approvaltests import Options, verify_as_json
from approvaltests.reporters.generic_diff_reporter_factory import GenericDiffReporterFactory
from approvaltests import set_default_reporter


def is_alive(matrix, x=1, y=1):
    if x == 1 and y == 1:
        living_neighbours = sum(matrix[0]) + sum(matrix[1]) + sum(matrix[2]) - matrix[1][1]

        if living_neighbours == 1 or living_neighbours == 0 or living_neighbours > 3:
            return False
        else:
            return True
    else:
        i_min = max(i - 1, 0)
        j_min = max(j - 1, 0)
        i_max = min(i + 1, n)
        j_max = max(j + 1, n)
        pass


class SampleTests(unittest.TestCase):
    def setUp(self):
        set_default_reporter(None)

    def test_living_center_and_no_alive_neighbour_then_dies(self):
        matrix = [[0, 0, 0],
                  [0, 1, 0],
                  [0, 0, 0]]
        self.assertEqual(is_alive(matrix), False)

    def test_living_center_and_1_alive_neighbour_then_dies(self):
        matrix = [[0, 0, 0],
                  [0, 1, 0],
                  [0, 0, 1]]
        self.assertEqual(is_alive(matrix), False)

    def test_if_living_and_neighbours_are_2_then_lives(self):
        matrix = [[0, 0, 0],
                  [1, 1, 0],
                  [0, 1, 0]]
        self.assertEqual(is_alive(matrix), True)

    def test_if_living_and_neighbours_are_3_then_lives(self):
        matrix = [[0, 0, 0],
                  [1, 1, 0],
                  [0, 1, 1]]
        self.assertEqual(is_alive(matrix), True)

    def test_living_center_and_4_alive_neighbours_then_dies(self):
        matrix = [[0, 1, 0],
                  [1, 1, 1],
                  [0, 1, 0]]
        self.assertEqual(is_alive(matrix), False)

    def test_dead_center_and_3_alive_neighbours_then_is_born(self):
        matrix = [[0, 0, 0],
                  [1, 0, 0],
                  [0, 1, 1]]
        self.assertEqual(is_alive(matrix), True)

    def test_dead_center_and_1_alive_neighbours_then_is_not_born(self):
        matrix = [[0, 0, 0],
                  [1, 0, 0],
                  [0, 0, 0]]
        self.assertEqual(is_alive(matrix), False)

    def test_dead_center_and_0_alive_neighbours_then_is_not_born(self):
        matrix = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]
        self.assertEqual(is_alive(matrix), False)

    def test_if_living_in_0_and_0_and_neighbours_are_3_then_lives(self):
        matrix = [[1, 1, 0],
                  [1, 1, 0],
                  [0, 1, 0]]
        self.assertEqual(is_alive(matrix, 0, 0), True)

    def test_straight_unittest(self):
        self.assertEqual(5, 5)

    def test_with_approvals(self):
        sample = "Welcome To Approvals"
        verify(sample)

    def test_with_approvals_from_project_code(self):
        from project.sample_function import this_is_the_function
        verify(this_is_the_function())

    def test_with_json(self):
        sample = {"firstName": "jayne",
                  "lastName": "cobb",
                  "isMale": True,
                  "age": 38}
        verify_as_json(sample)

    def test_list(self):
        sample = ["welcome", "to", "approvals"]
        verify_all("words", sample)

    def test_with_specific_reporter(self):
        sample = "Welcome To Approvals"
        verify(sample, options=Options().with_reporter(PythonNativeReporter()))


def test_pytest():
    assert True
