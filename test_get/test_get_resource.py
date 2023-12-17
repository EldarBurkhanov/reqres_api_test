from get_resource_model_validator import Resource, Support, SingleResource, ListResourcees
import requests
import pytest

URL = "https://reqres.in"

@pytest.mark.get_method
def test_single_resurce():
    """ Send a request to get single resource data """

    data = requests.get(URL + "/api/unknown/2")

    assert data.status_code == 200

    assert SingleResource(**data.json())

@pytest.mark.get_method
def test_list_resurces():
    """ Send a request to get List resources data """
    data = requests.get(URL + "/api/unknown")

    assert data.status_code == 200

    assert ListResourcees(**data.json())

@pytest.mark.get_method
def test_get_resource_not_found():
    """ Send a request to get Unknown Resource data """
    data = requests.get(URL + "/api/unknown/23")

    assert data.status_code == 404

    assert bool(data) == False

# Add some test for skip
