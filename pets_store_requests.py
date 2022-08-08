import requests


def post_add_new_pet_with_id_2():
    pet_data = {"id": 2, "category": {"id": 0, "name": "test_pets"},
            "name": "test_dog", "photoUrls": ["string"],
            "tags": [{"id": 0, "name": "string"}],
            "status": "available"}
    response = requests.post(url='https://petstore.swagger.io/v2/pet', json=pet_data)


def get_pet_search_by_id_2():
    response = requests.get(url='https://petstore.swagger.io/v2/pet/2').json()
    if response['id'] == 2 and response['name'] == 'test_dog' and response['status'] == 'available':
        return True
    else:
        return False


def delete_pet_with_id_2():
    response = requests.delete(url='https://petstore.swagger.io/v2/pet/2')


def get_pet_search_by_id_2_after_delete():
    response = requests.get(url='https://petstore.swagger.io/v2/pet/2').json()
    if response['message'] == 'Pet not found':
        return True
    else:
        return False


def post_create_user():
    global data
    data = {
        "id": 1,
        "username": "nswp",
        "firstName": "alex",
        "lastName": "sidarau",
        "email": "alex@gmail.com",
        "password": "1111",
        "phone": "77777",
        "userStatus": 0
    }
    response = requests.post(url='https://petstore.swagger.io/v2/user', json=data)


def get_user_data():
    response = requests.get(url='https://petstore.swagger.io/v2/user/nswp').json()
    assert data == response, "Error: Data doesn't match!"


def put_change_user_first_name():
    global changed_data
    changed_data = {
        "id": 1,
        "username": "nswp",
        "firstName": "aliaksei",
        "lastName": "sidarau",
        "email": "alex@gmail.com",
        "password": "1111",
        "phone": "77777",
        "userStatus": 0
    }
    response = requests.put(url='https://petstore.swagger.io/v2/user/nswp', json=changed_data)


def get_user_data_after_change():
    response = requests.get(url='https://petstore.swagger.io/v2/user/nswp').json()
    assert changed_data == response, "Error: Data doesn't match!"
