import json
import os

if os.path.exists('emojis.json'):
    with open('emojis.json', 'r') as file:
        emojis = json.load(file)
else:
    raise FileNotFoundError("Import 'emojis.json' to run")

def emoticon(input: str, yielding = False):
    if not input or input.isspace():
        return ""
    if input in list(emojis.keys()):
        return(emojis[input])
    elif yielding:
        yields = {}
        for emojiName in list(emojis.keys()):
            if input in emojiName:
                yields[emojiName] = emojis[emojiName]
        return yields
    else:
        for emojiName in list(emojis.keys()):
            if input in emojiName:
                return(emojis[emojiName])
        else:
            return(f"Emoji {input} not found.")

if __name__ == '__main__':
    while True:
        reqEmoj = input("Search for an emoji: ")
        print(emoticon(reqEmoj))

