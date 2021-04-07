import pytest

# tag the whole module
pytest = [pytest.mark.e2e, pytest.mark.slow]


class TestCheckout(object):

    def test_checkout_as_guest(self):
        print("Checkout as guest")
        print("Class: 1111111")

    def test_checkout_with_existing_user(self):
        print("Checkout with existing user")
        print("Class: 2222222")
