"""

2. В `main` функции (в файле `main.py`) создаем объект класса `Authenticator`.
3. Проверяем, что у объекта класса `Authenticator` есть логин (не None значение). Если его нет, сказать пользователю,
    что он проходит регистрацию. Если логин есть, сказать, что нужно для авторизации вести логин и пароль.
4. В бесконечном цикле запрашиваем у пользователя логи и пароль. Нужно либо зарегистрировать пользователя, либо
    авторизовать в зависимости от предыдущей проверки в пункте выше. Обрабатывать ошибки, вызываемые методами класса
    `Authenticator`.
5. Удаляем весь код с подсказкой паспорта, ввода имени и возраста. Класс валидатора, модуль валидатора и ошибку
    валидации удаляем (но не забываем, что это должно быть все в гит истории, потому что к этому вернемся).
6. Приветствуем пользователя: пишем логин, время последней успешной авторизации
   (формат `день.месяц.год час:минута:секунда`) и сколько раз пытались войти в приложение с ошибкой авторизации.
7. Запускаем игру в отгадайку рандомного числа.
"""
from authenticator import Authenticator
from random import randint
from exceptions import RegistrationError, AuthorizationError
from datetime import datetime

__author__ = "Ilya Kavaleu"



def guess_number_game() -> None:
    """
    Фунцкия guess_number_game - игра, угадай число от 1 до 5, генерируте случайное число и просит юзера его угадать,
    процесс продолжается пока пользователь его не угадает, в конце выводит количество попыток
    В переменной count = 0 начинаем отсчет с 0 о количестве попыток,
    Метод randint - возращает случайное целочисленное число в пределах между двумя аргументами(1 и 5 в нашем случае)

    Запускаем цикл While: приветствие, применение функции очищения на случай неправильности ввода нашего числа(например буквы),
    следующая попытка и досчет +1,

    Операция continue позволяет пропустить часть цикла в случае возникновения какаго-нибудь фактора и приступить к следующей
    итерации цикла, то есть если что-то пошло не так возращаемся в начало цикла.
    Далее обычная проверка если наше число == загаданному числу программой, мы победили, break - игра окончена, если
    наше число > 5, то в связи с условиями от 1 до 5, выводит соответсвующее сообщение, если наше число != 5, то возвращаемся в
    начало цикла, также идет счет +1 на каждую попытку.
    """
    count = 0

    game_number =  randint(1, 5)

    while True:
        guess = input("Hello! Guess the number from 1 to 5: ")
        try:
            guess = int((guess))
        except ValueError:
            print("You have entered symbols, you need to enter numbers")
            count += 1
            continue

        if guess == game_number:
            print("You guesses!")
            break
        if guess > 5:
            print("Your number should less or equals 5!")
        elif guess != game_number:
            print(f"No guessed")
        count += 1

def dekorator(func):
    def wrapper():
        while True:
            if func():
                break
    return wrapper

@dekorator
def main() -> None:
    """
    Основная функция, в которой создается объект класса Authenticator.
    В бесконечном цикле просит пользователя ввести логин и пароль и далее обрабатываем функции
    """
    odj = Authenticator()


    login = input("Enter login: ")
    password = input("Enter password: ")

    if odj.login:

        try:
            odj.authorize(login, password)
            times = datetime.fromisoformat(odj.last_success_login_at).strftime("%d.%m.%Y %H:%M:%S")
            print(f"Привет: {odj.login[0].upper() + odj.login[1:]} "
                  f"Авторизация прошла успешно в: {times}\n"
                  f"С {odj.errors_count} попытки.")    #obj = Authenticator !!!

            guess_number_game()

        except AuthorizationError as error:
            return False
    else:

        try:
            odj.registrate(login, password)
        except RegistrationError as error:
            return False



if __name__ == '__main__':
    main()