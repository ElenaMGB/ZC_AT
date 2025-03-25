def is_palindrome(text):
    # Подготовка строки: убираем пробелы и знаки, приводим к нижнему регистру
    clean_text = ''.join(char.lower() for char in text if char.isalnum())

    # Проверка: сравниваем строку с её перевёрнутой версией
    return clean_text == clean_text[::-1]


# Вызов функции и вывод результата
result = is_palindrome("А роза упала на лапу Азора")
if result:
    print("Результат:", "строка является палиндромом")
else:
    print("Результат:", "не палиндром")
