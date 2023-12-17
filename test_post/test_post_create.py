from post_user_model_validator import CreateUser
import requests
import pytest
import allure

@pytest.mark.post_method
@allure.title("Test POST method for Create User")
@allure.description("This test sends a POST request to create a new user.")
@allure.tag("NewUI", "Essentials", "PostMethod", "CreateUser")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("post_data", [
    {"name": "John", "job": "Engineer"},
    {"name": "Alice", "job": "Designer"},

])
def test_create_user(post_data, get_url):
    with allure.step(f"Send POST request to create a new user with data: {post_data}"):
        data = requests.post(get_url + "/api/users", json=post_data)

    with allure.step("Verify the response status code is 201"):
        assert data.status_code == 201

    with allure.step("Validate the response data against the CreateUser model"):
        assert CreateUser(**data.json())

        # Add check for chaning new body