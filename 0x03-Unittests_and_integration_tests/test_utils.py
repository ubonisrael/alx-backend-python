#!/usr/bin/env python3
"""Contains the TestAccessNestedMap class"""
from parameterized import parameterized  # type: ignore
from utils import access_nested_map
from typing import Mapping, Sequence, Dict, Union
import unittest


class TestAcessNestedMap(unittest.TestCase):
    """Tests for the AccessNestedMap Function"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence,
                               expected: Union[Dict, int]) -> None:
        """tests the output of the access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
        ])
    def test_access_nested_map_exception(self,
                                         nested_map: Mapping, path: Sequence,
                                         expected) -> None:
        """tests invalid output for the access_nested_map function"""
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)
