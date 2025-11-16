#!/usr/bin/python3
def remove_char_at(str, n):
    """Return a copy of the string without the character at index n"""
    if n < 0 or n >= len(str):
        return str  # indeks səhvdirsə orijinal stringi qaytar
    return str[:n] + str[n+1:]

# Nümunə istifadə
print(remove_char_at("Chicago", 3))  # Çap: Chiago
