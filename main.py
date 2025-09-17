# Разработай систему управления учетными записями пользователей для небольшой компании. Компания разделяет сотрудников на обычных работников и администраторов. У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа. Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень доступа и могут добавлять или удалять пользователя из системы.

#Требования:

#1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе: ID, имя и уровень доступа ('user' для обычных сотрудников).

#2.Класс Admin: Этот класс должен наследоваться от класса User. Добавь дополнительный атрибут уровня доступа, специфичный для администраторов ('admin'). Класс должен также содержать методы add_user и remove_user, которые позволяют добавлять и удалять пользователей из списка (представь, что это просто список экземпляров User).

#3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации снаружи. Предоставь доступ к необходимым атрибутам через методы (например, get и set методы).

class User():
    def __init__(self, user_id, name):
        self.__user_id = user_id # приватный атрибут
        self.__name = name # приватный атрибут
        self.__access_level = 'user' # приватный атрибут
    
    # Методы для получения данных (getters)    
    def get_user_id(self):
        return self.__user_id
    
    def get_name(self):
        return self.__name
    
    def get_access_level(self):
        return self.__access_level
    
    # Методы для изменения данных (setters)
    def set_name(self, new_name):
        self.__name = new_name
        print(f"Имя пользователя {self.__user_id} изменено на: {self.__name}")
        
    def info(self):
        return f"ID: {self.__user_id}, Имя: {self.__name}, Уровень доступа: {self.__access_level}"
    
class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._User__access_level = 'admin' # приватный атрибут, вместо создания нового атрибута, изменяем унаследованный
        self.__users_list = [] # приватный атрибут для хранения пользователей
     
     # Метод для добавления пользователя   
    def add_user(self, user):
        self.__users_list.append(user)
    
    # Метод для удаления пользователя по ID    
    def remove_user(self, user_id):
        for user in self.__users_list:
            if user.get_user_id() == user_id:
                self.__users_list.remove(user)
                print(f"Пользователь с ID {user_id} успешно удален")
                return True
        print(f"Пользователь с ID {user_id} не найден.")
        return False
    
    # Метод для отображения всех пользователей
    def show_all_users(self):
        for user in self.__users_list:
            print(f"  {user.info()}")
    
    # Метод для получения количества пользователей
    def get_users_list(self):
        return len(self.__users_list)
    
# Демонстрация работы системы

# Создаем администратора
admin = Admin(1, "Админ")
print(f"Создан администратор: {admin.info()}")

# Создаем обычных пользователей
user1 = User(2, "Иванов Иван")
user2 = User(3, "Петров Петр")
user3 = User(4, "Антон Антонов")
print(f"Создан пользователь: {user1.info()}")
print(f"Создан пользователь: {user2.info()}")
print(f"Создан пользователь: {user3.info()}")
    
# Администратор добавляет пользователей
admin.add_user(user1)
admin.add_user(user2)
admin.add_user(user3)

# Показываем всех пользователей
print("Список всех пользователей:")
admin.show_all_users()

 # Администратор удаляет пользователя
admin.remove_user(3)
print("Список всех пользователей:")
admin.show_all_users()     
    
# Попытка удалить несуществующего пользователя
print("Попытка удалить несуществующего пользователя:")
admin.remove_user(5) 

# Изменение имени пользователя
user1.set_name("Иванов Иван Иванович")
admin.show_all_users()    
  