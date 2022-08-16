import requests


def post_add_new_pet_with_id_and_name(id_pet: int, pet_name: str):
    pet_data = {"id": f"{id_pet}", "category": {"id": 0, "name": "test_pets"},
                "name": f"{pet_name}", "photoUrls": ["string"],
                "tags": [{"id": 0, "name": "string"}],
                "status": "available"}
    response = requests.post(url='https://petstore.swagger.io/v2/pet', json=pet_data)
    assert response.status_code == 200, \
        f"Error! New pet with id={id_pet} and pet name={pet_name} doesn't added to the store!," \
        f" Actual status code {response.status_code} with error {response.json()}"


def get_pet_search_by_id(id_pet: int):
    response = requests.get(url=f'https://petstore.swagger.io/v2/pet/{id_pet}')
    assert response.status_code == 200, \
        f"Error! Pet with id={id_pet} not found to the store!," \
        f" Actual status code {response.status_code} with error {response.json()}"
    if response.json()['id'] == id_pet and response.json()['status'] == 'available':
        return True
    else:
        return False


def delete_pet_by_id(id_pet: int):
    response = requests.delete(url=f'https://petstore.swagger.io/v2/pet/{id_pet}')
    assert response.status_code == 200, \
        f"Error! The pet may not have been deleted, check request," \
        f"Actual status code {response.status_code} with error {response.json()}"


def get_pet_search_by_id_after_delete(id_pet: int):
    response = requests.get(url=f'https://petstore.swagger.io/v2/pet/{id_pet}')
    assert response.status_code == 404, \
        f"Error! Pet with id={id_pet} found, check if it deleted," \
        f"Actual status code {response.status_code} with error {response.json()}"
    if response.json()['message'] == 'Pet not found':
        return True
    else:
        return False


def post_create_user(id_user: int, username: str, firstname: str,
                     lastname: str, email: str, password: str, phone: str):
    global user_data
    user_data = {
        "id": f"{id_user}",
        "username": f"{username}",
        "firstName": f"{firstname}",
        "lastName": f"{lastname}",
        "email": f"{email}",
        "password": f"{password}",
        "phone": f"{phone}",
        "userStatus": 0
    }
    response = requests.post(url='https://petstore.swagger.io/v2/user', json=user_data)
    assert response.status_code == 200, \
        f"Error! New user with {user_data} not added to the store!," \
        f"Actual status code {response.status_code} with error {response.json()}"


def get_user_information_by_username(username: str):
    response = requests.get(url=f'https://petstore.swagger.io/v2/user/{username}')
    assert response.status_code == 200, \
        f"Error! User with username={username} not found," \
        f"Actual status code {response.status_code} with error {response.json()}"
    assert user_data['firstName'] == response.json()['firstName'], "Error: Data doesn't match!"


def put_change_user_data_by_username(username: str, modified_firstname: str,
                                     id_user, lastname: str, email: str, password: str, phone: str):
    global changed_data

    changed_data = {
        "id": f"{id_user}",
        "username": f"{username}",
        "firstName": f"{modified_firstname}",
        "lastName": f"{lastname}",
        "email": f"{email}",
        "password": f"{password}",
        "phone": f"{phone}",
        "userStatus": 0
    }
    response = requests.put(url=f'https://petstore.swagger.io/v2/user/{username}', json=changed_data)
    assert response.status_code == 200, \
        f"Error! User data doesn't been changed," \
        f"Actual status code {response.status_code} with error {response.json()}"


def get_user_data_after_change(username: str):
    response = requests.get(url=f'https://petstore.swagger.io/v2/user/{username}')
    assert response.status_code == 200, \
        f"Error! User with username={username} not found," \
        f"Actual status code {response.status_code} with error {response.json()}"
    assert changed_data['firstName'] == response.json()['firstName'], "Error: Data doesn't match!"
