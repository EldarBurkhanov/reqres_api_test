from get_user_model_validator import User, Support, SingleUser, ListUsers
import requests
import pytest
import allure

@pytest.mark.get_method
@allure.title("Test GET method for Single User")
@allure.description("This test sends a GET request to retrieve data for a single user.")
@allure.tag("NewUI", "Essentials", "GetMethod", "SingleUser")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_single_user(get_url):
    with allure.step("Send GET request to retrieve data for user with ID 2"):
        data = requests.get(get_url + "/api/users/2")

    with allure.step("Verify the response status code is 200"):
        assert data.status_code == 200

    with allure.step("Validate the response data against the SingleUser model"):
        assert SingleUser(**data.json())

@pytest.mark.get_method
@allure.title("Test GET method for List Users")
@allure.description("This test sends a GET request to retrieve data for a list of users (page 2).")
@allure.tag("NewUI", "Essentials", "GetMethod", "ListUsers")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_list_users(get_url):
    with allure.step("Send GET request to retrieve data for the list of users (page 2)"):
        data = requests.get(get_url + "/api/users?page=2")

    with allure.step("Verify the response status code is 200"):
        assert data.status_code == 200

    with allure.step("Validate the response data against the ListUsers model"):
        assert ListUsers(**data.json())

@pytest.mark.get_method
@allure.title("Test GET method for User Not Found")
@allure.description("This test sends a GET request to retrieve data for a non-existent user (ID 23). Expects 404 response.")
@allure.tag("NewUI", "Essentials", "GetMethod", "UserNotFound")
@allure.severity(allure.severity_level.NORMAL)
def test_get_user_not_found(get_url):
    with allure.step("Send GET request to retrieve data for non-existent user with ID 23"):
        data = requests.get(get_url + "/api/users/23")

    with allure.step("Verify the response status code is 404"):
        assert data.status_code == 404

    with allure.step("Verify the response data is empty"):
        assert not bool(data)

@pytest.mark.get_method
@allure.title("Test GET method for List Users with Delayed Response")
@allure.description("This test sends a GET request to retrieve data for a list of users with a delayed response (3 seconds).")
@allure.tag("NewUI", "Essentials", "GetMethod", "ListUsers", "DelayedResponse")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_list_users_delayed_resonce(get_url):
    with allure.step("Send GET request to retrieve data for the list of users with delayed response (3 seconds)"):
        data = requests.get(get_url + "/api/users?delay=3")

    with allure.step("Verify the response status code is 200"):
        assert data.status_code == 200

    with allure.step("Validate the response data against the ListUsers model"):
        assert ListUsers(**data.json())
