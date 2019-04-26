import json
from difflib import get_close_matches
data = json.load(open("data.json"))


def crawler(word):
    word = word.lower()
    if word in data:
        return data[word]

    closer_word = get_close_matches(word, data.keys())[0]
    user_input = input(word + " Not found. Did you mean " +
                       closer_word + " Y - Yes | N - No ")
    user_input = user_input.lower()
    if user_input == "y":
        if closer_word in data:
            return data[closer_word]
    return "Not found - Try again"


def take_print():
    word = input("Enter word: ")
    output = crawler(word)
    if type(output) == list:
        for item in output:
            return item
    return output


print(take_print())
