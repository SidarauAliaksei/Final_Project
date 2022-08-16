import allure
from pets_store_requests import *


@allure.feature('Testing the PetStore via REST API')
class TestRestApiPetStore:
    @allure.story('Add and delete pet from store')
    def test_api_add_and_delete_pet_from_store(self):
        with allure.step('POST REQUEST | Adding new pet by id 2'):
            post_add_new_pet_with_id_and_name(2, 'cat')
        with allure.step('GET REQUEST | Searching pet by ID'):
            get_pet_search_by_id(2)
        with allure.step('DELETE REQUEST | Removing pet by ID'):
            delete_pet_by_id(2)
        with allure.step('GET REQUEST | Searching pet by id after delete'):
            get_pet_search_by_id_after_delete(2)

    @allure.story('Add user and change his first name')
    def test_api_add_user_and_change_his_first_name(self):
        with allure.step('POST REQUEST | Creating user'):
            post_create_user(1, "nswp", "alex", "sidorov", "111@bk.ru", "123", "111")
        with allure.step('GET REQUEST | Getting user data'):
            get_user_information_by_username("nswp")
        with allure.step('PUT REQUEST | Changing user first name'):
            put_change_user_data_by_username("nswp", "aliaksei", 1, "sidorov", "111@bk.ru", "123", "111")
        with allure.step('GET REQUEST | Getting user data after changed'):
            get_user_data_after_change("nswp")
