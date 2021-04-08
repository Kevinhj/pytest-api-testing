import pytest
import logging as logger
from wooapitest.src.utilities.genericUtilities import generate_random_email_and_password
from wooapitest.src.helpers.customers_helper import CustomerHelper

@pytest.mark.tcid29
def test_create_customer_only_email_password():
    logger.info("TEST: Ceate new customer with email and password only")

    rand_info = generate_random_email_and_password()
    logger.info(rand_info)

    email = rand_info['email']
    password = rand_info['password']

    # create the payload
    payload = {'email': email, 'password': password}

    # make the call
    cust_obj = CustomerHelper()
    cust_api_info = cust_obj.create_customer(email=email, password=password)

    # verify status code of the call

    # verify email in the response

    # verify customer is created in database
