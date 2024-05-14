#!/usr/bin/env python3
"""0. Parameterize a unit test"""
import unittest
from unittest import mock
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
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, access_map, path):
        """Tests that an assertion is raised"""
        with self.assertRaises(KeyError):
            utils.access_nested_map(access_map, path)

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @mock.patch("utils.requests.get")
    def test_get_json(self, url, payload, get):
        """Test get_json function"""
        json_mock = mock.Mock()
        json_mock.json.return_value = payload
        get.return_value = json_mock

        res = utils.get_json(url)

        get.assert_called_once_with(url)
        self.assertEqual(res, payload)
