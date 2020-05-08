import json
from difflib import get_close_matches
import time

data = json.load(open("data.json", "r"))


def translate(w):
    # Checks if the input is in our dictionary aong with title, upper and lower variations of the word
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    # If none of the above match, looks for close matches and asks the user if suggested match is correct.
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


# Continuously asks user for  new input until they ask to quit
while True:
    print("Enter .q to quit.")
    time.sleep(0.2)
    word = input("Enter Word: ").lower()
    if word == ".q":
        break

    # Calls translate function from above
    output = translate(word)

    # If multiple definitions are returned, puts them into a 1,2,3... list and prints them
    if type(output) == list:
        print("**********")
        count = 0
        for item in output:
            count += 1
            print(f"{count}. {item}")
        print("**********")
    # If just one word definitons is returned, prints this
    else:
        print("**********")
        print(f"1. {output}")
        print("**********")
