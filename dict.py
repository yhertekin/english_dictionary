import json
from difflib import get_close_matches
data = json.load(open("data.json"))


def crawler(word):
    word = word.lower()
    if word in data:
        return str(data[word]).strip("[]")

    closer_word = get_close_matches(word, data.keys())[0]
    user_input = input(word + " Not found. Did you mean " +
                       closer_word + " Y - Yes | N - No ")
    user_input = user_input.lower()
    if user_input == "y":
        if closer_word in data:
            return str(data[closer_word]).strip("[]")
    return "Not found - Try again"


word = input("Enter word: ")
print(crawler(word))
