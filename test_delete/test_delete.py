import pytest
import requests
import allure

@pytest.mark.delete_method
@allure.title("Test DELETE method")
@allure.description("This test sends a DELETE request to delete a user. Fails if any error happens.")
@allure.tag("NewUI", "Essentials", "DeleteMethod")
@allure.severity(allure.severity_level.CRITICAL)
def test_delete(get_url):
    with allure.step("Send DELETE request to delete user with ID 2"):
        data = requests.delete(get_url + "/api/users/2")

    with allure.step("Verify the response status code is 204"):
        assert data.status_code == 204


@pytest.mark.xfail(reason="This tool is not realized")
@allure.title("Test DELETE method with non-existing element")
@allure.description("This test sends a DELETE request to delete a non-existing user. Expects 404 response.")
@allure.tag("NewUI", "Essentials", "DeleteMethod", "NonExistingElement")
@allure.severity(allure.severity_level.NORMAL)
def test_delete_not_existing_elem(get_url):
    with allure.step("Send DELETE request to delete non-existing user with ID 255"):
        data = requests.delete(get_url + "/api/users/255")

    with allure.step("Verify the response status code is 404"):
        assert data.status_code == 404
