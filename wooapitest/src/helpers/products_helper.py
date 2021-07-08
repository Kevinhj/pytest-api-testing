from wooapitest.src.utilities.requestsUtility import RequestUtility


class ProductsHelper(object):

    def __init__(self):
        self.requests_utility = RequestUtility()

    # **kwargs is used to pass several params
    def get_product_by_id(self, product_id):

        return self.requests_utility.get(f"products/{product_id}")

    def call_create_product(self, payload):
        return self.requests_utility.post('products', payload=payload, expected_status_code=201)