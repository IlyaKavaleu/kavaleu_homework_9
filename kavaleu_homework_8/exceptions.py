class Exception():
    """Класс-родитель Exception"""

class ValidationError():
    """this class inherits from Exception and describes data validation errors"""
    """
    Этот пустой класс просто с условиями задания. 
    Создаём модуль exceptions, в нем класс ValidationError, который наследуется от Exception. Никакие методы, 
    свойства переопределять не нужно, необходимо только описать в docstring, что это класс ошибки валидации данных.
    """
class AuthorizationError():
    """
    Создаем ошибку AuthorizationError для авторизации
    """

class RegistrationError():
    """
    Создаем ошибку RegistrationError для регистрации
    """