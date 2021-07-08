

import pytest
import logging as logger
from wooapitest.src.utilities.requestsUtility import RequestUtility
from wooapitest.src.dao.products_dao import ProductsDAO
from wooapitest.src.helpers.products_helper import ProductsHelper

@pytest.mark.products
@pytest.mark.tcid24
def test_get_all_products():
    req_helper = RequestUtility()
    rs_api = req_helper.get(endpoint='products')

    assert rs_api, f"Get all products endpoint returned nothing."

@pytest.mark.tcid25
def test_get_product_by_id():

    # get a product (test data) from db
    rand_product = ProductsDAO().get_random_product_from_db(qty=1)
    rand_product_id = rand_product[0]['ID']
    db_name = rand_product[0]['post_title']

    # make the call
    product_helper = ProductsHelper()
    rs_api = product_helper.get_product_by_id(rand_product_id)
    api_name = rs_api['name']

    # verify the response
    assert db_name == api_name, f"Get product by id returned wrong product. Id: {rand_product_id}" \
                                f"Db name: {db_name}, Api name: {api_name}"