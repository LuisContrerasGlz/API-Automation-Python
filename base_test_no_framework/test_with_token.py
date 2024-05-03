 # Importing the requests library for HTTP communication

import requests


# Function to create an authentication token
def create_token():
    # URL for the authentication endpoint
    url = "https://restful-booker.herokuapp.com/auth"
    
    # Set headers for the HTTP request
    headers = {"Content-Type": "application/json"}
    
    # Payload for the request containing login credentials
    json_payload = {
        "username": "admin",
        "password": "password123"
    }
    
    # Make a POST request to obtain an authentication token
    response = requests.post(url=url, headers=headers, json=json_payload)
    
    # Extract the token from the JSON response

    # Parse JSON data
    data = response.json()  
    # Get the token value
    token = data["token"]  
    
    print("Authentication token:", token)  
    
    return token  # Return the generated token


# Function to create a booking
def create_booking():
    print("Creating a new booking...")  
    
    # URL for the booking endpoint
    URL = "https://restful-booker.herokuapp.com/booking"
    
    # Set headers and payload for the booking request
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "firstname": "Luis",
        "lastname": "Contreras",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    
    # Send a POST request to create a new booking
    response = requests.post(url=URL, headers=headers, json=json_payload)
    
    # Verify the response status code to ensure the booking was created
    assert response.status_code == 200, "Booking creation"
    
    # Extract the booking ID from the response
    data = response.json()  
    # Retrieve booking ID
    booking_id = data["bookingid"]  
    
    # Return the created booking ID
    return booking_id  


# Function to test an HTTP PUT request to update an existing booking
def test_put_request():
    # Base URL and endpoint for booking
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/"
    
    # Create a new booking and get its ID
    booking_id = create_booking()
    
    # Construct the full PUT URL using the booking ID
    PUT_URL = base_url + base_path + str(booking_id)
    
    # Get an authentication token and set it as a cookie in the headers
    cookie = "token=" + create_token()
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }
    
    # Define the payload for updating the booking
    json_payload = {
        "firstname": "Luis",
        "lastname": "Contreras",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    
    # Send a PUT request to update the booking
    response = requests.put(url=PUT_URL, headers=headers, json=json_payload)
    
    # Verify that the status code indicates success
    assert response.status_code == 200, "update the booking"
    
    # Check that the updated booking has the expected first name
    data = response.json()  
    assert data["firstname"] == "Luis", "updated first name"


# Function to test the deletion of a booking
def test_delete():
    # Handle exceptions that might occur during booking deletion
    try:
        # Base URL for booking
        URL = "https://restful-booker.herokuapp.com/booking/"
        
        # Create a new booking and get its ID
        booking_id = create_booking()
        
        # Construct the full DELETE URL using the booking ID
        DELETE_URL = URL + str(booking_id)
        
        # Get an authentication token and set it in the headers
        cookie_value = "token=" + create_token()
        headers = {
            "Content-Type": "application/json",
            "Cookie": cookie_value
        }
        
        # Send a DELETE request to remove the booking
        response = requests.delete(url=DELETE_URL, headers=headers)
        
        # Ensure the status code indicates success (201 for delete in this API)
        assert response.status_code == 201, "delete the booking"
    
    except Exception as e:
        # Handle exceptions and print the error message
        print("Error during booking deletion:", e)  
