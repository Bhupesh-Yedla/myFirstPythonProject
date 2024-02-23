import pytest
import requests
from assertpy import assert_that


class TestUsersAPI:
    baseurl = "https://reqres.in"

    @pytest.fixture(autouse=True)
    def setup(self):
        print("\nSetup before tests")


    def test_get_all_users(self):
        r = requests.get(f"{self.baseurl}/api/users?page=2")
        assert_that(r.status_code).is_equal_to(200)
        assert_that(r.json()).is_instance_of(dict)
        print(r.status_code)
        print(r.content)


    def test_get_single_user(self):
        user_id = 2
        r = requests.get(f"{self.baseurl}/api/users/{user_id}")
        assert_that(r.status_code).is_equal_to(200)
        assert_that(r.json()).contains_key("data")
        print(r.status_code)
        print(r.content)


    def test_add_user(self):
        url = f"{self.baseurl}/api/users"
        request_body = {"name": "morpheus", "job": "leader"}
        r = requests.post(url, request_body)
        print(r.status_code)
        print(r.content)
        assert_that(r.status_code).is_equal_to(201)
        assert_that(r.json()).contains_key("id")
        assert_that(r.json()).contains_key("job").contains_value("leader")

    @pytest.mark.parametrize("id, first_name",[(2,"IT"),(3,"Restaurant Manager")])
    def test_update_user_job(self,id, first_name):
        url = f"{self.baseurl}/api/users/{id}"
        request_body = { "first_name": first_name}
        r = requests.put(url, request_body)
        print(r.status_code)
        print(r.content)
        assert_that(r.status_code).is_equal_to(200)
        assert_that(r.json()).contains_key("first_name").contains_value(first_name)


    def test_delete_user(self):
        url = f"{self.baseurl}/api/users/2"

        r = requests.delete(url)
        print(r.status_code)
        print(r.content)
        assert_that(r.status_code).is_equal_to(204)


    def test_patch_request(self):
        url = f"{self.baseurl}/api/users/2"
        request_body = {"name": "morpheus updated"}
        r = requests.patch(url, request_body)
        print(r.status_code)
        print(r.content)
        assert_that(r.status_code).is_equal_to(200)


    def test_login_user_with_missing_fields(self):
        url = f"{self.baseurl}/api/register"
        request_body = {"email": "sydney@fife"}
        r = requests.post(url, request_body)
        print(r.status_code)
        print(r.content)
        assert_that(r.status_code).is_equal_to(400)

    def test_get_non_existent_user(self):
        url = f"{self.baseurl}/api/unknown/23"
        r = requests.get(url)
        print(r.status_code)
        print(r.text)
        assert_that(r.status_code).is_equal_to(404)
        r.raise_for_status()

    def test_get_user_invalid_id(self):
        url = f"{self.baseurl}/api/unknown/abc"
        r = requests.get(url)
        assert_that(r.status_code).is_equal_to(404)
        print(r.status_code)
        print(r.text)
        # r.raise_for_status()


    def test_get_user_invalid_endpoint(self):
        url = f"{self.baseurl}/api"
        r = requests.get(url)
        print(r.status_code)
        print(r.content)
        assert_that(r.status_code).is_equal_to(404)
        r.raise_for_status()