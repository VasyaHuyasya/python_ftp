def check_credentials(filename, username, password):
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Удаляем пробелы и разбиваем строку на логин и пароль
                stored_username, stored_password = line.strip().split(':')
                
                # Сравниваем с введенными логином и паролем
                if stored_username == username and stored_password == password:
                    return True
    except FileNotFoundError:
        print("Файл не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

    return False

# Пример использования
if __name__ == "__main__":
    username_input = input("Введите логин: ")
    password_input = input("Введите пароль: ")
    
    if check_credentials('credentials.txt', username_input, password_input):
        print("Успешный вход!")
    else:
        print("Неверный логин или пароль.")
