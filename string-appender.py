# A program to print out a set of messages entered by the user.
def is_question(phrase):
    if phrase.lower().startswith(("who", "what", "when", "where", "how", "why")):
        return True
    else:
        return False


string_list = []
while True:
    addString = input("Input a message: ")
    if addString == "\end":
        break
    else:
        punctuation = "."
        if is_question(addString):
            punctuation = "?"

        string_list.append(addString.capitalize() + punctuation)

print(" ".join(string_list))
