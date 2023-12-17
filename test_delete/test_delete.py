import pytest
import requests


URL = "https://reqres.in"


@pytest.mark.delete_method
def test_delete():
    """ This case tests the Delete request  """
    data = requests.delete(URL + "/api/users/2")

    assert data.status_code == 204

    # Add empty validation

    # Add deleting unexciting Argument (will fail)