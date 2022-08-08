import allure
from pets_store_requests import *


@allure.feature('Testing the PetStore via REST API')
class TestRestApiPetStore:
    @allure.story('Add and delete pet from store')
    def test_api_add_and_delete_pet_from_store(self):
        with allure.step('POST REQUEST | Adding new pet with id 2'):
            post_add_new_pet_with_id_2()
        with allure.step('GET REQUEST | Searching pet with id 2'):
            get_pet_search_by_id_2()
        with allure.step('DELETE REQUEST | Removing pet with ID 2'):
            delete_pet_with_id_2()
        with allure.step('GET REQUEST | Searching pet with id 2 after delete'):
            get_pet_search_by_id_2_after_delete()

    @allure.story('Add user and change his first name')
    def test_api_add_user_and_change_his_first_name(self):
        with allure.step('POST REQUEST | Creating user'):
            post_create_user()
        with allure.step('GET REQUEST | Getting user data'):
            get_user_data()
        with allure.step('PUT REQUEST | Changing user first name'):
            put_change_user_first_name()
        with allure.step('GET REQUEST | Getting user data after changed'):
            get_user_data_after_change()
