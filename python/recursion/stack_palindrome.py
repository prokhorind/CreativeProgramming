def is_palindrome(s):
    stack = []

    for char in s:
        stack.append(char)

    for char in s:
        top_char = stack.pop()
        if char != top_char:
            return False

    return True


word = "radar"
if is_palindrome(word):
    print(f"'{word}' є паліндромом")
else:
    print(f"'{word}' не є паліндромом")