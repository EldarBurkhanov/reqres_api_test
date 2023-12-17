from put_user_model_validator import UpdateUser
import requests
import pytest
import allure

API_PUT_PATCH = "/api/users/2"

@pytest.mark.put_method
@allure.title("Test User Update via PUT Request")
@allure.description("This test sends a PUT request to update user data.")
@allure.tag("NewUI", "Essentials", "PutMethod", "UserUpdate")
@allure.severity(allure.severity_level.NORMAL)
def test_put_update(put_patch_data, get_url):
    with allure.step(f"Send PUT request to update user: {put_patch_data}"):
        data = requests.put(get_url + API_PUT_PATCH, json=put_patch_data)

    with allure.step("Verify the response status code is 200"):
        assert data.status_code == 200

    with allure.step("Validate the response data against the UpdateUser model"):
        assert UpdateUser(**data.json())

@pytest.mark.patch_method
@allure.title("Test User Update via PATCH Request")
@allure.description("This test sends a PATCH request to update user data.")
@allure.tag("NewUI", "Essentials", "PatchMethod", "UserUpdate")
@allure.severity(allure.severity_level.NORMAL)
def test_patch_update(put_patch_data, get_url):
    with allure.step(f"Send PATCH request to update user: {put_patch_data}"):
        data = requests.patch(get_url + API_PUT_PATCH, json=put_patch_data)

    with allure.step("Verify the response status code is 200"):
        assert data.status_code == 200

    with allure.step("Validate the response data against the UpdateUser model"):
        assert UpdateUser(**data.json())

