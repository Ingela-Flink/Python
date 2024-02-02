
def ja():
    Nej = input()
    number = 1
    for letter in Nej:
        if number > 10:
            print("BÖG Jävel (AMin gillar barn)")
        else:
            print(letter, str(number))
        number += 1


ja()