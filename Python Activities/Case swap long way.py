# swapping uppercase characters to lowercase and vice versa

while True:
    text=input('insert text ')
    new_text=''
    for character in text:
        if character.islower():
            new_text += character.upper()
        else:
            new_text += character.lower()
    print(new_text)