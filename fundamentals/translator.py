def translator(phrase):
    translation = ""
    phrase = phrase.lower()
    for letter in phrase:
        if letter in "aeiou":
            translation += "g"
        else:
            translation += letter
    return translation

print(translator())  # Output: Hgllg Wgrld