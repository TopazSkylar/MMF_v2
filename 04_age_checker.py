# functions go here
def not_blank(question):
    while True:
        response = input(question)

        # if the response is blank, outputs error
        if response == "":
            print("Sorry, this cannot be blank, please try again")
        else:
            return response


def int_check(question):
    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter an integer")


def string_checker(question, valid_ans_list=('yes', 'no'), num_letters=1):
    """Checks that users enter the full word or then, letter/s of a word from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            # checks user response to question
            # only accepts yes or no
            if response == item:
                return item

            # check if it's the 'n' letters
            elif response == item[:num_letters]:
                return item


# Main routine
payment_list = ["cash", "credit"]

tickets_sold = 0

while True:

    name = not_blank("Enter your name / xxx to quit: ")

    if name == "xxx":
        break

    age = int_check("Age: ")

    if 12 <= age <= 120:
        pass
    elif age < 12:
        print(f"{name} is too young")
        continue
    else:
        print(f"{name} is too old")
        continue

    pay_method = string_checker("Payment method: ", payment_list, 2)
    print(f"{name} has brought a ticket ({pay_method})")

    tickets_sold += 1
