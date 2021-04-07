import pytest

# tag single tests
@pytest.mark.smoke
def test_login_page_valid_user():
    print("Login with valid user")
    print("function: aaaaa")

@pytest.mark.regression
def test_login_page_wrong_password():
    print("Login with wrong password")
    print("Function: bbbbb")
    #assert 1==2, "One is not two"