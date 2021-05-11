

import pytest
import logging as logger
from wooapitest.src.utilities.requestsUtility import RequestUtility

@pytest.mark.tcid30
def test_get_all_customers():
    req_helper = RequestUtility()
    rs_api = req_helper.get('customers')
    logger.debug(f'Response of list all: {rs_api}')

    # Assert the response is not empty
    assert rs_api, f"Response of list all customers is empty."