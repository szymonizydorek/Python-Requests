import requests

print("Importing Requests ... ")

def fetch_data(url):
    '''Fetch data from given URL'''
    response = requests.get(url)
    print(f"Request succeedded with status code: {response.status_code} ")
    return response.json()

def print_print(data):
    '''Printing the fetched data'''
    print("Here is JSON retrived:")
    print(data)

def view_menu():
    '''Display and select option'''
    menu = """
    Menu Options:
    1. View all JSON data
    2. View specific key from JSON file
    3. Exit
    """
    print(menu)

def read_choice():
    '''Read user choice'''
    choice = input("Please enter which option you select 1/2/3: ")
    return choice

def handling_choice(choice, data):
    '''Handle user's chocies'''
    if choice == '1':
        print(data)
    elif choice == '2':
        key = input("Which element you want to view: ")
        print(f"Data for '{key}' : {data[0][key]}")
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")
        
if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/posts'
    data = fetch_data(url)
    
    while True:
        view_menu()  # Call display_menu to show the options
        user_choice = read_choice()  # Call get_user_choice to get the user's input
        handling_choice(user_choice, data)  # Call handle_choice to process the user's choice   