# API Request - HTTP Request

# Import necessary modules for API testing and reporting
import allure
import pytest
import requests

# Test case to verify successful creation of a booking

@allure.title("Create Booking CRUD")
@allure.description("TC#1 - Verify create Booking")
@pytest.mark.crud

def test_create_booking_positive():
    # Request
    # URL
    # Method
    # Headers
    # Payload / Data / Body
    # Auth

    # API base URL and endpoint for booking creation
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"

    # Full URL for the API endpoint
    URL = base_url + base_path

    # Define request headers and payload for the booking request
    headers = {"Content-Type": "application/json"}
    payload = {
        "firstname": "Amit",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    # Send a POST request to create a new booking
    response = requests.post(url=URL, headers=headers, json=payload)
    
    # Response Body  Verification,
    # Headers
    # Status Code
    # JSON Schema Validation
    # Time Response
    
    # Expect a successful response
    assert response.status_code == 200
    # Parse the JSON response
    print(response.headers)
    response_json = response.json()

    # Extract and verify booking information from the response
    booking_id = response_json["bookingid"]
    assert booking_id is not None
    assert booking_id > 0
    assert type(booking_id) == int

    # Verify specific details in the booking response
    firstname = response_json["booking"]["firstname"]
    checkin = response_json["booking"]["bookingdates"]["checkin"]
    assert firstname == "Amit"
    assert checkin == "2018-01-01"
    

# Test case to verify that booking creation fails with invalid (empty) data    
@allure.title("Create Booking CRUD")
@allure.description("TC#2 - Verify Booking is not created with {} data ")
@pytest.mark.crud

def test_create_booking_negative():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path

    # Define headers and an empty payload for the request
    headers = {"Content-Type": "application/json"}
    json_payload = {}

    # Send a POST request with an empty payload
    response = requests.post(url=URL, headers=headers, json=json_payload)

    # Output the type of certain variables (debugging assistance)
    print(type(URL))
    print(type(headers))
    print(type(json_payload))
    
    # Assertions, verify that the response status code indicates a failure, expect an error response due to empty data
    assert response.status_code == 500
