

import pytest
import logging as logger
from wooapitest.src.utilities.requestsUtility import RequestUtility

@pytest.mark.products
@pytest.mark.tcid24
def test_get_all_products():
    req_helper = RequestUtility()
    rs_api = req_helper.get(endpoint='products')

    assert rs_api, f"Get all products endpoint returned nothing."
