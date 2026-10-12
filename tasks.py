# Задачи пары: раунд 2 — fizzbuzz, раунд 3 — is_prime.

# Вместо ... впишите своё имя, вместо raise NotImplementedError — решение.
# Проверить, что файл запускается без ошибок: python3 tasks.py



def fizzbuzz(n):
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return f'{n}'
    """что0то"""
    """Вернуть "FizzBuzz", если n делится на 3 и на 5, "Fizz" — только на 3,
    "Buzz" — только на 5, иначе само число строкой.

    Примеры:
        fizzbuzz(9) -> "Fizz"
        fizzbuzz(10) -> "Buzz"
        fizzbuzz(15) -> "FizzBuzz"
        fizzbuzz(7) -> "7"
    """
    # Реализовал(а): ...
    raise NotImplementedError


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
    """Вернуть True, если n — простое число (больше 1 и делится только на 1 и на себя).

    Примеры:
        is_prime(13) -> True
        is_prime(9) -> False
        is_prime(1) -> False
    """
    # Реализовал(а): ...
    raise NotImplementedError

print(fizzbuzz(9))
print(fizzbuzz(15))
print(fizzbuzz(5))
print(fizzbuzz(7))
print(is_prime(1))
print(is_prime(9))
print(is_prime(13))