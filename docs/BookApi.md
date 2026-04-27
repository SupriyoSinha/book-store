# openapi_client.BookApi

All URIs are relative to *https://bookstore.swagger.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addbook**](BookApi.md#addbook) | **POST** /book | Add a new book to the store
[**deletebook**](BookApi.md#deletebook) | **DELETE** /book/{bookId} | Deletes a book
[**findbooks_by_status**](BookApi.md#findbooks_by_status) | **GET** /book/findByStatus | Finds books by status
[**findbooks_by_tags**](BookApi.md#findbooks_by_tags) | **GET** /book/findByTags | Finds books by tags
[**getbook_by_id**](BookApi.md#getbook_by_id) | **GET** /book/{bookId} | Find book by ID
[**updatebook**](BookApi.md#updatebook) | **PUT** /book | Update an existing book
[**updatebook_with_form**](BookApi.md#updatebook_with_form) | **POST** /book/{bookId} | Updates a book in the store with form data


# **addbook**
> addbook(body)

Add a new book to the store

### Example

* OAuth Authentication (bookstore_auth):

```python
import openapi_client
from openapi_client.models.book import Book
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://bookstore.swagger.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://bookstore.swagger.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.BookApi(api_client)
    body = openapi_client.Book() # Book | book object that needs to be added to the store

    try:
        # Add a new book to the store
        api_instance.addbook(body)
    except Exception as e:
        print("Exception when calling BookApi->addbook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Book**](Book.md)| book object that needs to be added to the store | 

### Return type

void (empty response body)

### Authorization

[bookstore_auth](../README.md#bookstore_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**405** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletebook**
> deletebook(book_id, api_key=api_key)

Deletes a book

### Example

* OAuth Authentication (bookstore_auth):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://bookstore.swagger.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://bookstore.swagger.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.BookApi(api_client)
    book_id = 56 # int | book id to delete
    api_key = 'api_key_example' # str |  (optional)

    try:
        # Deletes a book
        api_instance.deletebook(book_id, api_key=api_key)
    except Exception as e:
        print("Exception when calling BookApi->deletebook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **book_id** | **int**| book id to delete | 
 **api_key** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bookstore_auth](../README.md#bookstore_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Invalid ID supplied |  -  |
**404** | book not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **findbooks_by_status**
> List[Book] findbooks_by_status(status)

Finds books by status

Multiple status values can be provided with comma separated strings

### Example

* OAuth Authentication (bookstore_auth):

```python
import openapi_client
from openapi_client.models.book import Book
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://bookstore.swagger.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://bookstore.swagger.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.BookApi(api_client)
    status = ['status_example'] # List[str] | Status values that need to be considered for filter

    try:
        # Finds books by status
        api_response = api_instance.findbooks_by_status(status)
        print("The response of BookApi->findbooks_by_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BookApi->findbooks_by_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | [**List[str]**](str.md)| Status values that need to be considered for filter | 

### Return type

[**List[Book]**](Book.md)

### Authorization

[bookstore_auth](../README.md#bookstore_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid status value |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **findbooks_by_tags**
> List[Book] findbooks_by_tags(tags)

Finds books by tags

Multiple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing.

### Example

* OAuth Authentication (bookstore_auth):

```python
import openapi_client
from openapi_client.models.book import Book
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://bookstore.swagger.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://bookstore.swagger.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.BookApi(api_client)
    tags = ['tags_example'] # List[str] | Tags to filter by

    try:
        # Finds books by tags
        api_response = api_instance.findbooks_by_tags(tags)
        print("The response of BookApi->findbooks_by_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BookApi->findbooks_by_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tags** | [**List[str]**](str.md)| Tags to filter by | 

### Return type

[**List[Book]**](Book.md)

### Authorization

[bookstore_auth](../README.md#bookstore_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid tag value |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getbook_by_id**
> Book getbook_by_id(book_id)

Find book by ID

Returns a single book

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.book import Book
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://bookstore.swagger.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://bookstore.swagger.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.BookApi(api_client)
    book_id = 56 # int | ID of book to return

    try:
        # Find book by ID
        api_response = api_instance.getbook_by_id(book_id)
        print("The response of BookApi->getbook_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BookApi->getbook_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **book_id** | **int**| ID of book to return | 

### Return type

[**Book**](Book.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid ID supplied |  -  |
**404** | book not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updatebook**
> updatebook(body)

Update an existing book

### Example

* OAuth Authentication (bookstore_auth):

```python
import openapi_client
from openapi_client.models.book import Book
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://bookstore.swagger.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://bookstore.swagger.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.BookApi(api_client)
    body = openapi_client.Book() # Book | book object that needs to be added to the store

    try:
        # Update an existing book
        api_instance.updatebook(body)
    except Exception as e:
        print("Exception when calling BookApi->updatebook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Book**](Book.md)| book object that needs to be added to the store | 

### Return type

void (empty response body)

### Authorization

[bookstore_auth](../README.md#bookstore_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Invalid ID supplied |  -  |
**404** | book not found |  -  |
**405** | Validation exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updatebook_with_form**
> updatebook_with_form(book_id, name=name, status=status)

Updates a book in the store with form data

### Example

* OAuth Authentication (bookstore_auth):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://bookstore.swagger.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://bookstore.swagger.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.BookApi(api_client)
    book_id = 56 # int | ID of book that needs to be updated
    name = 'name_example' # str | Updated name of the book (optional)
    status = 'status_example' # str | Updated status of the book (optional)

    try:
        # Updates a book in the store with form data
        api_instance.updatebook_with_form(book_id, name=name, status=status)
    except Exception as e:
        print("Exception when calling BookApi->updatebook_with_form: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **book_id** | **int**| ID of book that needs to be updated | 
 **name** | **str**| Updated name of the book | [optional] 
 **status** | **str**| Updated status of the book | [optional] 

### Return type

void (empty response body)

### Authorization

[bookstore_auth](../README.md#bookstore_auth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**405** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

