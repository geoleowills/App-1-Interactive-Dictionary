import json

data = json.load(open("data.json", "r"))


def translate(w):
    if w in data:
        return data[w]
    else:
        return "The word doesn't exist. Please double check it."


word = input("Enter Word: ").lower()

print(translate(word))
