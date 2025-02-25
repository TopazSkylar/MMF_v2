import pandas
import random


# from datatime import date


# functions go here

# Decorates statements
def make_statement(statement, decoration):
    """Emphasises headings by adding decoration at the start and end"""

    return f"{decoration * 3} {statement} {decoration * 3}"


# checks if paid in cash or credit
def cash_credit(question):
    while True:
        response = input(question).lower()
        # checks user response to question
        # only accepts yes or no
        if response == "cash" or response == "ca":
            return "cash"

        elif response == "credit" or response == "cr":
            return "credit"

        else:
            print("Please choose a valid payment method ")


# program main heading
print(make_statement("Mini_Movie Fundraiser Program", "+"))


# shows instructions
def show_instructions():
    print(make_statement("Instructions", "|"))
    print('''\n

For each ticket enter ...
- The person's name (cannot be blank)
- Age (between 12 and 120)
- Payment method (cash / credit)

When you have entered all the users, type 'xxx' to quit.

the program will display the ticket detail including the cost of each ticket, the total cost 
and the total profit. 

This information will also be automatically written to a text file. 

**********************************************''')


# checks that the user response is not blank
def not_blank(question):
    while True:
        response = input(question)

        # if the response is blank, outputs error
        if response == "":
            print("Sorry, this cannot be blank, please try again")
        else:
            return response


# checks that the user inputs an integer
def int_check(question):
    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter an integer")


# checks that users enter a valid response (yes/no, cash/credit) based on a list of options
def string_checker(question, valid_ans_list, num_letters=1):
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

        print(f"Please enter {valid_ans_list})")


# currency formatting function
def currency(x):
    """Formats numbers as currency ($#.##)"""
    return "${:.2f}".format(x)


# main routine goes here
yes_no_list = ['yes', 'no']
payment_list = ["cash", "credit"]

# set maximum number of tickets below
MAX_TICKETS = 30
tickets_sold = 0

# Ticket Price List
CHILD_PRICE = 7.50
ADULT_PRICE = 10.50
SENIOR_PRICE = 6.50

# Credit card surcharge (currently 5%)
CREDIT_SURCHARGE = 0.05

# list to hold the ticket details
all_names = []
all_ticket_costs = []
all_surcharges = []

# Dictionary used to create data frame ie: column_name: list
mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": all_surcharges
}

# ask user if they want to see the instructions
instructions = string_checker("Do you want to read the instructions? ", yes_no_list, 1)

if instructions == "yes":
    show_instructions()

print()
# set maximum number of tickets below

# loop to sell tickets

while tickets_sold < MAX_TICKETS:
    print()

    # ask user for their name (check it's not blank)
    name = not_blank("Please enter your name or 'xxx' to quit : ")

    if name == 'xxx':
        if tickets_sold < 1:
            print("You must sell at least one ticket to exit")
            continue
        else:
            break

    age = int_check("Age: ")
    if 12 <= age <= 120:
        pass
    elif age < 12:
        print(f"{name} is too young")
        continue
    # ticket is $7.50 for users under 16
    if age < 16:
        price = CHILD_PRICE

    # ticket is $10.50 for users between 16 and 64
    elif age < 65:
        price = ADULT_PRICE

    # ticket price is $6.50 for seniors (65+)
    elif age <= 121:
        price = SENIOR_PRICE

    else:
        print(f"{name} is too old")
        continue

    pay_method = string_checker("Payment method: ", payment_list, 2)

    if pay_method == "cash":
        surcharge = 0

    # calculate 5% surcharge if users are paying using credit
    else:
        surcharge = price * CREDIT_SURCHARGE

    # add ticket name, cost and surcharge to lists
    all_names.append(name)
    all_ticket_costs.append(price)
    all_surcharges.append(surcharge)

    tickets_sold += 1

# # create data frame from dictionary to organise information
mini_movie_frame = pandas.DataFrame(mini_movie_dict)

# # Calculate the profit for each ticket
mini_movie_frame['Total'] = mini_movie_frame['Ticket Price'] + mini_movie_frame['Surcharge']
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# Choose a winner from a name list
winner_name = random.choice(all_names)

# find index of winner (i.e. position in list)
winner_index = all_names.index(winner_name)

# look up total amount won (ie: ticket price + surcharge)
ticket_won = mini_movie_frame.at[winner_index, 'Total']
profit_won = mini_movie_frame.at[winner_index, 'Profit']

# total won
total_won = mini_movie_frame.at[winner_index, 'Total']

# Calculate the total ticket cost (ticket + surcharge)
total_paid = mini_movie_frame['Total'].sum()
total_profit = mini_movie_frame['Profit'].sum()

# # Currency formatting (uses currency function)
add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

# Output movie frame without index
mini_movie_string = mini_movie_frame.to_string(index=False)
total_paid_string = f"Total Paid: ${total_paid:.2f}"
total_profit_string = f"Total Profit: ${total_profit:.2f}"


lucky_winner_string = f"Congrats {winner_name}.  Their ticket of ${total_won:.2f} is free!"
final_total_paid_string = f"Total Paid is now ${total_paid - ticket_won:.2f}"
final_profit_string = f"Total Profit is now ${total_profit - profit_won:.2f}"

if tickets_sold == MAX_TICKETS:
    num_sold_string = make_statement("You have sold all the tickets", ".")

else:
    num_sold_string = make_statement(f"You have sold {tickets_sold}/{MAX_TICKETS} tickets", "-")

# # set index at the end before printing
# mini_movie_frame = mini_movie_frame.set_index('Name')

# **** Get current date for heading and filename ****
# Get today's date
# today = date.today()
#
# # Get day, month and year as individual strings
# day = today.strftime("%d")
# month = today.strftime("%m")
# year = today.strftime("%Y")
#
heading_string = make_statement(" Mini Movie Fundraiser Ticket Data", "=")
ticket_details_heading = make_statement("Ticket Details", "-")
raffle_heading = make_statement("Raffle Winner", "-")
adjusted_sales_heading = make_statement("Adjusted Sales & Profit", "-")
adjusted_explanation = f"We have given away a ticket worth ${ticket_won:.2f} which means \nsales have decreased by " \
                       f"${ticket_won:.2f} and our profit \ndecreased by ${profit_won:.2f}"

# list of strings to be outputted / written to file
to_write = [heading_string, "\n",
            ticket_details_heading,
            mini_movie_string, "\n",
            total_paid_string,
            total_profit_string, "\n",
            raffle_heading,
            lucky_winner_string, "\n",
            adjusted_sales_heading,
            adjusted_explanation, "\n",
            final_total_paid_string,
            final_profit_string, "\n",
            num_sold_string]

# Print area
print()
for item in to_write:
    print(item)

# create file to hold data (add .txt extension)
file_name = "MMF_ticket_details"
write_to = "{}.txt".format(file_name)

text_file = open(write_to, "w+")

for item in to_write:
    text_file.write(item)
    text_file.write("\n")
# filename = "MMF_{}_{}_{}".format(year, month, day)
#
# # change frame to a string so that we can export it to file
# mini_movie_string = pandas.DataFrame.to_string(mini_movie_frame)
#
# # heading
# print(heading)
# print("The filename will be {},txt".format(filename))
#
# # create strings for printing....
# ticket_cost_heading = "\n----- Ticket Cost / Profit -----"
# total_ticket_sales = "Total Ticket Sales: ${}".format(total)
# total_profit = "Total Profit : ${}".format(profit)
#
# # edit text below!!!!!!!! Needs to work if we have unsold tickets
# sales_status = "\n*** All the tickets have been sold ***"
#
# winner_heading = "\n---- Raffle Winner ----"
# winner_text = "the winner of the raffle is {}. " \
#               "The have won %{}. ie: Their ticket is " \
#               "free".format(winner_name, total_won)
#
# # List holding content to print / write to file
# to_write = {heading, mini_movie_string, ticket_cost_heading, total_ticket_sales, total_profit, sales_status,
#             winner_heading, winner_text}
#
# # print output
# for item in to_write:
#     print(item)
#
# # write output to file




# # close file
# text_file.close()
