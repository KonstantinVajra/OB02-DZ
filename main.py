class User:
    def __init__(self, user_id: int, name: str, access_level: str = 'user'):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = access_level

    # Getters
    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    # Setters
    def set_name(self, name: str):
        self.__name = name

    def set_access_level(self, access_level: str):
        self.__access_level = access_level

    def __repr__(self):
        return f"User(ID: {self.__user_id}, Name: {self.__name}, Access Level: {self.__access_level})"


class Admin(User):
    def __init__(self, user_id: int, name: str, admin_level: str = 'admin'):
        super().__init__(user_id, name, access_level=admin_level)
        self.__admin_level = admin_level

    def add_user(self, user_list: list, user: User):
        user_list.append(user)
        print(f"User {user.get_name()} (ID: {user.get_user_id()}) added.")

    def remove_user(self, user_list: list, user_id: int):
        for user in user_list:
            if user.get_user_id() == user_id:
                user_list.remove(user)
                print(f"User {user.get_name()} (ID: {user_id}) removed.")
                break
        else:
            print(f"User with ID {user_id} not found.")


## Создаем пустой список пользователей
user_list = []

# Создаем обычного пользователя
user1 = User(user_id=1, name="Alice")

# Создаем администратора
admin1 = Admin(user_id=2, name="Bob")

# Добавляем пользователей
admin1.add_user(user_list, user1)
print(user_list)  # Выведет список пользователей

# Удаляем пользователя
admin1.remove_user(user_list, 1)
print(user_list)  # Выведет обновленный список пользователей