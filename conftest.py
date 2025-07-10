import pytest
from methods.user_methods import UserMethods as UM


@pytest.fixture
def fxtr_create_and_remove_user():
    new_user_status_code, new_user_json, new_user_creds = UM.user_register_new_one()
    new_user_access_token = new_user_json["accessToken"]
    yield new_user_status_code, new_user_json, new_user_access_token, new_user_creds
    UM.user_delete_profile(new_user_access_token)
