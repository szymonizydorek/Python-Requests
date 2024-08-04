# Requests Library Testing Project


## What is Python Request library?

The requests library in Python is a powerful and user-friendly library for making HTTP requests. It abstracts the complexities of making requests behind a simple API, making it easy to send HTTP requests and handle responses. It supports various HTTP methods, allowing you to interact with web services effectively.

## Table of Contents

<!-- Request features-LIST:START -->

- Supports all HTTP methods: Including GET, POST, PUT, DELETE, PATCH, etc.
- Error handling: Provides straightforward error handling for failed requests.
- Automatic content decoding: Handles various response content types, including JSON.
- Support for cookies and headers: You can easily set headers and manage cookies.
  
<!-- Request features-LIST:END -->


## Features

- Easy-to-use interface for making HTTP requests
- Examples of GET, POST, PUT, and DELETE requests
- Error handling and response validation
- Comprehensive test cases to ensure functionality

## Most common Methods in Requests

1. **GET Request**: Fetches data from a specified resource.
   ```
   response = requests.get('https://api.example.com/data')   
   ``` 
2. **POST Request**: Sends data to a server to create or update a resource.
   ```
   payload = {'key': 'value'}
   response = requests.post('https://api.example.com/data', json=payload)
   ```
3. **PUT Request**: Updates a resource with new data.
   ```
   payload = {'key': 'updated_value'}
   response = requests.put('https://api.example.com/data', json=payload)
   ```












