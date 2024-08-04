import requests

print("Importing requests...")

def view_menu():
    '''Display menu and select option'''
    menu = """
    Menu options: 
    1. Getting JSON data from the Server
    2. Posting JSON data to the Server
    3. Exit
    """
    print(menu)
    choice = input("Please enter which option you select 1/2/3: ")
    return choice
    
def handling_choice(choice, data):
    if choice == '1':
        response = requests.get(url_get, headers=headers, params=querystring)
        print("Response from the server: ")
        print(response.text)

    elif choice == '2':
        # Use JSON for payload
        payload = {"data": "Hello DevNet"}
        response = requests.post(url_post, json=payload, headers=headers)   
        print("Response from the server: ")
        print(response.text)
        
    elif choice == '3':
        print("Goodbye")
        return False     
    
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")

    return True  # Continue the loop

if __name__ == "__main__":
    # Defining the URLs
    url_get = "https://postman-echo.com/get"
    url_post = "https://postman-echo.com/post"

    querystring = {"test": "123"}

    # Define headers
    headers = {}

    # Initialize data variable (can be modified as needed)
    data = {}  # Initialize data as an empty dictionary
    
    while True:
        user_choice = view_menu()  # Call view_menu to show the options
        if not handling_choice(user_choice, data):
            break
