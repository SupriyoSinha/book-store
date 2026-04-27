import os

import openapi_client
from openapi_client import Book
from openapi_client.rest import ApiException
from pprint import pprint
def test_me_out():
# Defining the host is optional and defaults to https://bookstore.swagger.io/v2
# See configuration.py for a list of all supported configuration parameters.
    configuration = openapi_client.Configuration(
        host = "https://bookstore.swagger.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

    #configuration.access_token = "os.environ[ACCESS_TOKEN]"

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_books():
    response = client.get("/api/v1/books")
    assert response.status_code == 200
# Enter a context with an instance of the API client
    with openapi_client.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = openapi_client.BookApi(api_client)
        json ='{ "id" : 123 ,"name" : "Charlie", "status" : "available","photoUrls":[] }'

    # create an instance of Book from a JSON string
        book_instance = Book.from_json(json)
    # print the JSON string representation of the object
    print(Book.to_json(book_instance))

    # Book | book object that needs to be added to the store

    try:
        # Add a new book to the store
        api_instance.addbook(book_instance)
    except ApiException as e:
        print("Exception when calling BookApi->addbook: %s\n" % e)