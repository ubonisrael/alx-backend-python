#!/usr/bin/env python3
"""Contains the TestAccessNestedMap class"""
from parameterized import parameterized
import unittest


access_nested_map = __import__('utils').access_nested_map


class TestAcessNestedMap(unittest.TestCase):
    """Tests for the AccessNestedMap Function"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map, path, expected):
        """tests the output of the access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
