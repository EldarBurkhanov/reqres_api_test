from put_user_model_validator import UpdateUser
import requests
import pytest

URL = "https://reqres.in"

@pytest.mark.put_method
def test_put_update(put_patch_data):

    data = requests.put(URL + "/api/users/2", put_patch_data) # Same Strings

    assert data.status_code == 200

    assert UpdateUser(**data.json())

@pytest.mark.patch_method
def test_patch_update(put_patch_data):

    data = requests.patch(URL + "/api/users/2", put_patch_data) # Add parametrize

    assert data.status_code == 200

    assert UpdateUser(**data.json())

