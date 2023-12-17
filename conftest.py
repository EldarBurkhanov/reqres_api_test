import pytest

# PATH = C:\Users\eldar.burkhanov\PycharmProjects\reqres_autotesting\test_api_reqres\allure_result

"""Hook for add custom marks"""
def pytest_configure(config):
    config.addinivalue_line("markers", "delete_method: mark a test as a DELETE method test")
    config.addinivalue_line("markers", "get_method: mark a test as a GET method test")
    config.addinivalue_line("markers", "post_method: mark a test as a POST method test")
    config.addinivalue_line("markers", "put_method: mark a test as a PUT method test")
    config.addinivalue_line("markers", "patch_method: mark a test as a PATCH method test")

@pytest.fixture
def post_data():
    data = {
    "name": "morpheus",
    "job": "leader"
    }
    return data


@pytest.fixture
def put_patch_data():
    data = {
    "name": "morpheus",
    "job": "zion resident"
    }
    return data


@pytest.fixture
def post_reg_data():
    data = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
    }
    return data


@pytest.fixture
def post_reg_invalid_data():
    data = {
    "email": "sydney@fife"
    }
    return data


@pytest.fixture
def post_login_data():
    data = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
    }
    return data


@pytest.fixture
def post_login_invalid_data():
    data = {
    "email": "peter@klaven"
    }
    return data

