import time
import json
from difflib import get_close_matches
data = json.load(open("data.json"))


def dictionary(para):  # parameter
    para = para.lower()  # we can do this early during the input as well
    if para in data:
        return data[para]
    elif para == "coder":
        return f"He is a man of unparalleled integrity,\nwhose honesty and character have never been in question, \nexcept by those who don’t know him. --{para}"
    elif len(get_close_matches(para, data.keys())) > 0:
        userInput = input(
            f"Sorry we didn't find any {para} "+"Do you mean %s ? Y/N: " % get_close_matches(para, data.keys())[0])
        if userInput == "Y":
            return data[get_close_matches(para, data.keys())[0]]
        else:
            return f"I'm damn sure you are wrong check again: "
    else:
        return f"Your word {para} doesn't exist.  "


word = input("Enter the word: ")
print(dictionary(word))

print("Thank You...\n Program will close automatically after 5 sec")
time.sleep(5)
print("Sayonara........")
