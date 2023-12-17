from post_user_model_validator import RegisterSuccesful, RegisterOrLoginUnsuccesful, LoginSuccesful
import requests
import pytest
import allure

API_REG = "/api/register"
API_LOG = "/api/login"


@pytest.mark.post_method
@allure.title("Test Successful User Registration")
@allure.description("This test sends a POST request to register a new user with valid data.")
@allure.tag("NewUI", "Essentials", "PostMethod", "UserRegistration")
@allure.severity(allure.severity_level.CRITICAL)
def test_register_succesful(post_reg_data, get_url):
    with allure.step(f"Send POST request to register a new user with data: {post_reg_data}"):
        data = requests.post(get_url + API_REG, json=post_reg_data)

    with allure.step("Verify the response status code is 200"):
        assert data.status_code == 200

    with allure.step("Validate the response data against the RegisterSuccesful model"):
        assert RegisterSuccesful(**data.json())

@pytest.mark.post_method
@allure.title("Test Unsuccessful User Registration with Invalid Data")
@allure.description("This test sends a POST request to register a new user with invalid data.")
@allure.tag("NewUI", "Essentials", "PostMethod", "UserRegistration")
@allure.severity(allure.severity_level.NORMAL)
def test_register_unsuccesful(post_reg_invalid_data, get_url):
    with allure.step(f"Send POST request to register a new user with invalid data: {post_reg_invalid_data}"):
        data = requests.post(get_url + API_REG, json=post_reg_invalid_data)

    with allure.step("Verify the response status code is 400"):
        assert data.status_code == 400

    with allure.step("Validate the response data against the RegisterOrLoginUnsuccesful model"):
        assert RegisterOrLoginUnsuccesful(**data.json())

@pytest.mark.post_method
@allure.title("Test Successful User Login")
@allure.description("This test sends a POST request to log in with valid user credentials.")
@allure.tag("NewUI", "Essentials", "PostMethod", "UserLogin")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_succesful(post_login_data, get_url):
    with allure.step(f"Send POST request to log in with data: {post_login_data}"):
        data = requests.post(get_url + API_LOG, json=post_login_data)

    with allure.step("Verify the response status code is 200"):
        assert data.status_code == 200

    with allure.step("Validate the response data against the LoginSuccesful model"):
        assert LoginSuccesful(**data.json())

@pytest.mark.post_method
@allure.title("Test Unsuccessful User Login")
@allure.description("This test sends a POST request to log in with invalid user credentials.")
@allure.tag("NewUI", "Essentials", "PostMethod", "UserLogin")
@allure.severity(allure.severity_level.NORMAL)
def test_login_unsuccesful(post_login_invalid_data, get_url):
    with allure.step(f"Send POST request to log in with invalid data: {post_login_invalid_data}"):
        data = requests.post(get_url + API_LOG, json=post_login_invalid_data)

    with allure.step("Verify the response status code is 400"):
        assert data.status_code == 400

    with allure.step("Validate the response data against the RegisterOrLoginUnsuccesful model"):
        assert RegisterOrLoginUnsuccesful(**data.json())

@pytest.mark.post_method
@allure.title("Test Unsuccessful User Login with Incorrect Password")
@allure.description("This test sends a POST request to log in with invalid password.")
@allure.tag("NewUI", "Essentials", "PostMethod", "UserLogin")
@allure.severity(allure.severity_level.NORMAL)
def test_login_unsuccesful_only_password(post_login_invalid_data_only_pass, get_url):
    with allure.step(f"Send POST request to log in with invalid password: {post_login_invalid_data_only_pass}"):
        data = requests.post(get_url + API_LOG, json=post_login_invalid_data_only_pass)

    with allure.step("Verify the response status code is 400"):
        assert data.status_code == 400

    with allure.step("Validate the response data against the RegisterOrLoginUnsuccesful model"):
        assert RegisterOrLoginUnsuccesful(**data.json())


@pytest.mark.post_method
@allure.title("Test Unsuccessful User Registration with Incorrect Password")
@allure.description("This test sends a POST request to register with an invalid password.")
@allure.tag("NewUI", "Essentials", "PostMethod", "UserRegistration")
@allure.severity(allure.severity_level.NORMAL)
def test_register_unsuccesful_only_password(post_login_invalid_data_only_pass, get_url):
    with allure.step(f"Send POST request to register with invalid password: {post_login_invalid_data_only_pass}"):
        data = requests.post(get_url + API_REG, json=post_login_invalid_data_only_pass)

    with allure.step("Verify the response status code is 402"):
        assert data.status_code == 402

    with allure.step("Validate the response data against the RegisterOrLoginUnsuccesful model"):
        assert RegisterOrLoginUnsuccesful(**data.json())

