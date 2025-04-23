import re

def is_palindrome(text):
    """Проверяет, является ли строка палиндромом (без учета регистра, знаков пунктуации и пробелов)."""
    processed_text = re.sub(r'[^a-zA-Zа-яА-ЯёЁ]', '', text).lower()
    return processed_text == processed_text[::-1]

assert is_palindrome("А роза упала на лапу Азора") == True
assert is_palindrome("Лёша на полке клопа нашёл") == True
assert is_palindrome("Madam, I'm Adam") == True
assert is_palindrome("Race fast, safe car") == True
assert is_palindrome("hello") == False
assert is_palindrome("12321") == True
assert is_palindrome("") == True
assert is_palindrome("A man, a plan, a canal: Panama") == True
