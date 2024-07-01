#!/usr/bin/env python3
"""Contains the TestAccessNestedMap class"""
import unittests


class TestAcessNestedMap(unittests.TestCase):
	"""Tests for the AccessNestedMap Function"""

        @parameterized.expand([
                {"a": 1}, ("a",),
                {"a": {"b": 2}}, ("a",),
                {"a": {"b": 2}}, ("a", "b")
                ])
        def test_access_nested_map(self, nested_map, path):
                self.assertEqual()
