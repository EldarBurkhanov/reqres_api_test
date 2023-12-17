import pytest
import requests
import allure


@allure.title("Test Authentication")
# @allure.description("This test attempts to log into the website using a login and a password. Fails if any error happens.\n\nNote that this test does not test 2-Factor Authentication.")
# @allure.tag("NewUI", "Essentials", "Authentication")
# @allure.severity(allure.severity_level.CRITICAL)
# @allure.label("owner", "John Doe")
# @allure.link("https://dev.example.com/", name="Website")
# @allure.issue("AUTH-123")
# @allure.testcase("TMS-456")
# @allure.parent_suite("Tests for web interface")
# @allure.suite("Tests for essential features")
# @allure.sub_suite("Tests for authentication")
# ALURE PATTERNS
def test_api_acess(get_url):
    with allure.step("Trying to get responce from main server"):
        data = requests.get(get_url)
        assert data.status_code == 200


