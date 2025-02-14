# main routine starts here

# Initialise ticket numbers
MAX_TICKETS = 3
tickets_sold = 0

while tickets_sold < MAX_TICKETS:
    name = input("Please enter your name or 'xxx' to quit : ")

    tickets_sold += 1

    if name == 'xxx':
        break

# Output number of tickets sold
if tickets_sold == MAX_TICKETS:
    print("Congratulations you have sold all the tickets")
else:
    print("You have sold {} ticket/s. There are {} ticket/s remaining".format(tickets_sold, MAX_TICKETS - tickets_sold))
