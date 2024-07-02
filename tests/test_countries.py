# tests/test_countries.py

""" Implement the Country and City Management Endpoints """

import requests
import pytest

API_URL = "http://localhost:5000"
country_code = "UY"


def test_get_countries():
    """
    Test to retrieve all countries
    Sends a GET request to /countries and checks that the response status is 200
    and the returned data is a list.
    """
    response = requests.get(f"{API_URL}/countries")
    assert (
        response.status_code == 200
    ), f"Expected status code 200 but got {response.status_code}. Response: {response.text}"
    assert isinstance(
        response.json(), list
    ), f"Expected response to be a list but got {type(response.json())}"


def test_get_cities_in_country():
    """
    Test to retrieve cities in a specific country
    Sends a GET request to /countries/{country_code}/cities and checks that the response status is 200
    and the returned data is a list.
    """
    response = requests.get(f"{API_URL}/countries/{country_code}/cities")
    assert (
        response.status_code == 200
    ), f"Expected status code 200 but got {response.status_code}. Response: {response.text}"
    assert isinstance(
        response.json(), list
    ), f"Expected response to be a list but got {type(response.json())}"


if __name__ == "__main__":
    pytest.main()


from tests import test_functions

API_URL = "http://localhost:5000"
country_code = "UY"


def test_get_countries():
    """
    Test to retrieve all countries
    Sends a GET request to /countries and checks that the response status is 200
    and the returned data is a list.
    """
    response = requests.get(f"{API_URL}/countries")
    assert (
        response.status_code == 200
    ), f"Expected status code 200 but got {response.status_code}. Response: {response.text}"
    assert isinstance(
        response.json(), list
    ), f"Expected response to be a list but got {type(response.json())}"


def test_get_cities_in_country():
    """
    Test to retrieve cities in a specific country
    Sends a GET request to /countries/{country_code}/cities and checks that the response status is 200
    and the returned data is a list.
    """
    response = requests.get(f"{API_URL}/countries/{country_code}/cities")
    assert (
        response.status_code == 200
    ), f"Expected status code 200 but got {response.status_code}. Response: {response.text}"
    assert isinstance(
        response.json(), list
    ), f"Expected response to be a list but got {type(response.json())}"
