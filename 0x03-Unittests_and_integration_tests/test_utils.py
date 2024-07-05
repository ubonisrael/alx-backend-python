#!/usr/bin/env python3
"""Contains the TestAccessNestedMap class"""
from parameterized import parameterized  # type: ignore
from utils import access_nested_map, get_json, memoize
from typing import Mapping, Sequence, Dict, Union
from unittest.mock import Mock, patch
import unittest


class TestAccessNestedMap(unittest.TestCase):
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


class TestGetJson(unittest.TestCase):
    """Tests for the get_json function"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    def test_get_json(self, test_url, test_payload):
        """tests the get_json functions output"""
        attr = {'json.return_value': test_payload}
        with patch('requests.get', return_value=Mock(**attr)) as req:
            self.assertEqual(get_json(test_url), test_payload)
            req.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Tests for the utils.memoize method"""
    def test_memoize(self):
        """tests the utils.memoize method"""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=lambda: 42) as f:
            obj = TestClass()
            self.assertEqual(obj.a_property(), 42)
            self.assertEqual(obj.a_property(), 42)
            f.assert_called_once()
