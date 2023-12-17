from get_resource_model_validator import Resource, Support, SingleResource, ListResourcees
import requests
import pytest
import allure

@pytest.mark.get_method
@allure.title("Test GET method for Single Resource")
@allure.description("This test sends a GET request to retrieve data for a single resource.")
@allure.tag("NewUI", "Essentials", "GetMethod", "SingleResource")
@allure.severity(allure.severity_level.CRITICAL)
def test_single_resurce(get_url):
    with allure.step("Send GET request to retrieve data for resource with ID 2"):
        data = requests.get(get_url + "/api/unknown/2")

    with allure.step("Verify the response status code is 200"):
        assert data.status_code == 200

    with allure.step("Validate the response data against the SingleResource model"):
        assert SingleResource(**data.json())

@pytest.mark.get_method
@allure.title("Test GET method for List Resources")
@allure.description("This test sends a GET request to retrieve data for a list of resources.")
@allure.tag("NewUI", "Essentials", "GetMethod", "ListResources")
@allure.severity(allure.severity_level.CRITICAL)
def test_list_resurces(get_url):
    with allure.step("Send GET request to retrieve data for the list of resources"):
        data = requests.get(get_url + "/api/unknown")

    with allure.step("Verify the response status code is 200"):
        assert data.status_code == 200

    with allure.step("Validate the response data against the ListResources model"):
        assert ListResourcees(**data.json())

@pytest.mark.get_method
@allure.title("Test GET method for Unknown Resource")
@allure.description("This test sends a GET request to retrieve data for an unknown resource (ID 23). Expects 404 response.")
@allure.tag("NewUI", "Essentials", "GetMethod", "UnknownResource")
@allure.severity(allure.severity_level.NORMAL)
def test_get_resource_not_found(get_url):
    with allure.step("Send GET request to retrieve data for unknown resource with ID 23"):
        data = requests.get(get_url + "/api/unknown/23")

    with allure.step("Verify the response status code is 404"):
        assert data.status_code == 404

    with allure.step("Verify the response data is empty"):
        assert not bool(data)
