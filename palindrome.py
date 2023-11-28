def palindrome(word):
    cleaned_word = ''.join(filter(str.isalpha, word.lower()))
    return cleaned_word == cleaned_word[::-1]

text = ["Kajak", "Potop", "Wino", "Radar", "Ogórek"]

for word in text:
    result = palindrome(word)
    print(f"Czy '{word}' jest palindromem? {result}")
