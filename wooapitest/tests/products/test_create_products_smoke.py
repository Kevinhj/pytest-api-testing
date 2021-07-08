from wooapitest.src.utilities.genericUtilities import generate_random_string
from wooapitest.src.helpers.products_helper import ProductsHelper
from wooapitest.src.dao.products_dao import ProductsDAO
import pytest

@pytest.mark.products
@pytest.mark.tcid26
def test_create_one_simple_product():

    # generate some data
    payload = dict()
    payload['name'] = generate_random_string(20)
    payload['type'] = 'simple'
    payload['regular_price'] = '10.99'

    # make the call
    product_rs = ProductsHelper().call_create_product(payload)

    # verify the response is not empty
    assert product_rs, f"Create product api response is empty. Payload: {payload}"
    assert product_rs['name'] == payload['name'], f"Create product api call response has" \
            f"unexpected name. Expected: {payload['name']}, Actual: {product_rs['name']}"

    # verify the product exist in db
    product_id = product_rs['id']
    db_product = ProductsDAO().get_product_by_id(product_id)

    assert payload['name'] == db_product[0]['post_title'], f"Create product, title in db does not match" \
            f"title in api. DB: {db_product['post_title']}, API: {payload['name']}"
