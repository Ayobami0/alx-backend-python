#!/usr/bin/env python3
"""0. Parameterize a unit test"""
import unittest
from parameterized import parameterized

import utils


class TestAccessNestedMap(unittest.TestCase):
    """Tests the AccessNestedMap
        """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, access_map, path, expected):
        """Tests the nested map"""
        self.assertEqual(utils.access_nested_map(access_map, path), expected)

    @parameterized.expand([
        ({"a": 1}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, access_map, path):
        """Tests that an assertion is raised"""
        with self.assertRaises(KeyError):
            utils.access_nested_map(access_map, path)
