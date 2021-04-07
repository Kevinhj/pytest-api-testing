import pytest
import pdb


# the set up, the scope mean that setup is for the module
@pytest.fixture(scope='module')
def my_setup():
    print("")
    print(">>>> MY SETUP <<<<")

    return {'id': 20, 'name': 'Kevin'}


# tag single tests
@pytest.mark.smoke
def test_login_page_valid_user(my_setup):
    print("Login with valid user")
    print("function: aaaaa")
    print("Name: {}".format(my_setup.get('name')))
    # pdb.set_trace() # this is a breakpoint


@pytest.mark.regression
def test_login_page_wrong_password():
    print("Login with wrong password")
    print("Function: bbbbb")
    # assert 1==2, "One is not two"
