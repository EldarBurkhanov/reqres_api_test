from post_user_model_validator import RegisterSuccesful, RegisterOrLoginUnsuccesful, LoginSuccesful
import requests
import pytest

URL = "https://reqres.in"


@pytest.mark.post_method
def test_register_succesful(post_reg_data):
    """ This case tests user registration"""
    data = requests.post(URL + "/api/register", post_reg_data) # Using same Link Optimize in the future

    assert data.status_code == 200

    assert RegisterSuccesful(**data.json())

@pytest.mark.post_method
def test_register_unsuccesful(post_reg_invalid_data):

    data = requests.post(URL + "/api/register", post_reg_invalid_data)

    assert data.status_code == 400

    assert RegisterOrLoginUnsuccesful(**data.json())

@pytest.mark.post_method
def test_login_succesful(post_login_data):

    data = requests.post(URL + "/api/login", post_login_data)

    assert data.status_code == 200

    assert LoginSuccesful(**data.json())

@pytest.mark.post_method
def test_login_unsuccesful(post_login_invalid_data):

    data = requests.post(URL + "/api/login", post_login_invalid_data)

    assert data.status_code == 400

    assert RegisterOrLoginUnsuccesful(**data.json())

# Add test with only password without email