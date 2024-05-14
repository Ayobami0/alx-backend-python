#!/usr/bin/env python3
"""4. Parameterize and patch as decorators"""
import unittest
from unittest import mock
from parameterized import parameterized

import client


class TestGithubOrgClient(unittest.TestCase):
    "Test cases for client module"
    @parameterized.expand([
        ('google'),
        ('abc'),
    ])
    @mock.patch('client.get_json')
    def test_org(self, org, get_json_mock):
        """Test different orgs"""
        new_mock = mock.Mock(return_value=org)
        get_json_mock.return_value = new_mock

        _client = client.GithubOrgClient(org)
        self.assertEqual(_client.org(), org)

        get_json_mock.assert_called_once_with(_client.ORG_URL.format(org=org))
