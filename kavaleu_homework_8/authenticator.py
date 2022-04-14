from datetime import datetime
import os.path
from exceptions import AuthorizationError, RegistrationError


class Authenticator:
    """
    Класс Authenticator
    """

    def __init__(self):
        """
        Конструктор класса, который инициализирует атрибуты класса.
        В нем создаются переменные экземпляра класса self.login: str | None, self._password | None, self.last_success_login_at: datetime
        | None, self.errors_count: int. По умолчанию у этих переменных должно быть None значение.
        У переменной errors_count значение 0. Вызываем метод _is_auth_file_exist. Если файл существует, вызвать метод _read_auth_file.
        """
        self.login: str | None = None
        self._password: str | None = None
        self.last_success_login_at: datetime | None = None
        self.errors_count: int = 0

        if self._is_auth_file_exist():   #вызываем метод _is_auth_file_exist
            self._read_auth_file()       #если файл существует, вызвать метод _read_auth_file.

        else:
            print("Registration")

    def _is_auth_file_exist(self) -> bool:
        """
        Проверяем наличие файла auth.txt рядом в той папке. Не принимаем аргументов, возвращает bool значение.
        True - файл авторизации существует. False - не существует.
        """
        return os.path.isfile("auth.txt")

    def _read_auth_file(self) -> None:
        """
        Чтение данных из файла auth.txt.
        Данные из файла записываем в переменные объекта класса созданные ранее (self.login, self._password,
        self.last_success_login_at, self.errors_count ).
        Ничего не возвращаем. В файле должно быть 4 строк.
        """
        print("Authorization")
        with open("auth.txt", "r") as file:
            self.login = file.readline().strip()
            self._password = file.readline().strip()
            self.last_success_login_at = file.readline().strip()
            self.errors_count = int(file.readline().strip())

    def authorize(self, login, password) -> None:
        """
        Проверка логина и пароля. Принимает аргументы строки логина и пароля.
        Сравнивает логин и пароль из аргументов с логином и паролем из файла.
        Если логин и пароль неверные, вызывает исключение AuthorizationError (нужно создать этот класс в соответствующем месте)
        и увеличиваем счетчик проваленных попыток-ошибок и перезаписываем в файле - вызывает метод _update_auth_file.
        Если self.login имеет None значение, вызвать ошибку AuthorizationError.
        """
        if login:

            if login != self.login or password != self._password:
                self.errors_count += 1
                self._update_auth_file()
                raise AuthorizationError("Неверные данные!")

            else:
                self._update_auth_file()

        else:
            raise AuthorizationError("Enter login")

    def registrate(self, login, password) -> None:
        """
        Регистрация пользователя. Принимает аргументы строки логина и пароля. Делает проверку, что файла рядом auth.txt нет.
        Если он есть, вызывает исключение RegistrationError (нужно создать этот класс в соответствующем месте).
        Создает файл auth.txt и сохраняет туда логин, пароль, datetime.utcnow().isoformat(), количество проваленных
        попыток (ошибки) при попытке регистрации (Вызывает метод _update_auth_file).
        Если self.login имеет НЕ None значение, вызываем ошибку RegistrationError.
        """

        if self.login:
            self.errors_count += 1
            raise RegistrationError("Ошибка регистрации")

        if login:
            self.login = login
            self._password = password
            self._update_auth_file()

        else:
            self.errors_count += 1
            self._update_auth_file()
            raise RegistrationError("Введите логин")

    def _update_auth_file(self) -> None:
        """
        Перезапись файла auth.txt. Не принимает аргументов, не возвращает ничего.
        Метод должен перезаписать количество попыток авторизации и время авторизации, что лежат в переменных экземпляра.
        """
        with open("auth.txt", "w") as f:
            f.write(f"{self.login}\n")
            f.write(f"{self._password}\n")
            self.last_success_login_at = datetime.utcnow().isoformat(" ")
            f.writelines(self.last_success_login_at)
            f.write(f"\n{self.errors_count}")