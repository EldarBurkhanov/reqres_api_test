from get_user_model_validator import User, Support, SingleUser, ListUsers
import requests
import pytest

URL = "https://reqres.in" # Find solution add automaticli this link to every test MB via Fixture


@pytest.mark.get_method
def test_get_single_user():
    """ Send a request to get single user data """
    data = requests.get(URL + "/api/users/2")

    assert data.status_code == 200

    assert SingleUser(**data.json())

@pytest.mark.get_method
def test_get_list_users():
    """ Send a request to get List users data """
    data = requests.get(URL + "/api/users?page=2") # Add params

    assert data.status_code == 200

    assert ListUsers(**data.json())

@pytest.mark.get_method
def test_get_user_not_found():
    """ Send a request to get Unknown user data """
    data = requests.get(URL + "/api/users/23")

    assert data.status_code == 404

    assert bool(data) == False


@pytest.mark.get_method
def test_get_list_users_delayed_resonce():
    """ Send a request to get List users data """
    data = requests.get(URL + "/api/users?delay=3") # Add params

    assert data.status_code == 200

    assert ListUsers(**data.json())

# Add some test for skip


