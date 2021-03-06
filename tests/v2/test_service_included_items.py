# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.user import User
from datadog_api_client.v2.model.user_attributes import UserAttributes
from datadog_api_client.v2.model.user_response_relationships import UserResponseRelationships
from datadog_api_client.v2.model.users_type import UsersType
globals()['User'] = User
globals()['UserAttributes'] = UserAttributes
globals()['UserResponseRelationships'] = UserResponseRelationships
globals()['UsersType'] = UsersType
from datadog_api_client.v2.model.service_included_items import ServiceIncludedItems


class TestServiceIncludedItems(unittest.TestCase):
    """ServiceIncludedItems unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testServiceIncludedItems(self):
        """Test ServiceIncludedItems"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ServiceIncludedItems()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
