import json
from difflib import get_close_matches
import time

data = json.load(open("data.json", "r"))


def translate(w):
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input(
            f"Did you mean to enter {get_close_matches(w, data.keys())[0]} instead? Enter Y if yes and N if no:")
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."


while True:
    print("Enter .q to quit.")
    time.sleep(0.2)
    word = input("Enter Word: ").lower()

    output = translate(word)

    if word == ".q":
        break
    elif type(output) == list:
        print("**********")
        count = 0
        for item in output:
            count += 1
            print(f"{count}. {item}")
        print("**********")
    else:
        print("**********")
        print(f"1. {output}")
        print("**********")
