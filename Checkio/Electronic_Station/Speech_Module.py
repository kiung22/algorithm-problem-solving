FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"

def checkio(number):
    speech = []

    if number >= 100:
        speech.append(FIRST_TEN[int(str(number)[0]) - 1])
        speech.append(HUNDRED)
        number -= int(str(number)[0] + "00")

    if number >= 20:
        speech.append(OTHER_TENS[int(str(number)[0]) - 2])
        number -= int(str(number)[0] + "0")

    elif number >= 10:
        speech.append(SECOND_TEN[number - 10])
        number = 0

    if number >= 1:
        speech.append(FIRST_TEN[int(str(number)[0]) - 1])

    return " ".join(speech)
