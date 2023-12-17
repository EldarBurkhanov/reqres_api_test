from post_user_model_validator import CreateUser
import requests
import pytest

URL = "https://reqres.in"

@pytest.mark.post_method
def test_create_user(post_data): # Add parametrize for different data
    """This case tests user creating """
    data = requests.post(URL + "/api/users", post_data)

    assert data.status_code == 201

    assert CreateUser(**data.json())

