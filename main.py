class User:
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._access_level = 'user'

    # Геттеры и сеттеры
    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_access_level(self):
        return self._access_level


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'admin'
        self._user_list = []  # Список для хранения пользователей

    # Метод для добавления пользователя
    def add_user(self, user):
        self._user_list.append(user)
        print(f'User {user.get_name()} added.')

    # Метод для удаления пользователя по ID
    def remove_user(self, user_id):
        for user in self._user_list:
            if user.get_user_id() == user_id:
                self._user_list.remove(user)
                print(f'User {user.get_name()} removed.')
                return
        print('User not found.')


# Пример использования
admin = Admin(1, 'Admin User')
user1 = User(2, 'John Doe')
user2 = User(3, 'Jane Doe')

admin.add_user(user1)
admin.add_user(user2)

admin.remove_user(2)  # Удалить пользователя John Doe

print(f"Remaining users: {[user.get_name() for user in admin._user_list]}")


