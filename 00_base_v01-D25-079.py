# functions go here

# checks user has entered yes / no to a question
show_instructions = ""
while show_instructions.lower() != "xxx":
    # Ask the user if they have played before
    show_instructions = input("Do you want to read the instructions? ").lower()

    # If they say yes, output 'display instructions'
    if show_instructions == "yes" or show_instructions == "y":
        show_instructions = "yes"
        print("display instructions")

    elif show_instructions == "no" or show_instructions == "n":
        pass


    # If they say no continue
    else:
        print("Please answer yes / no")

# main routine starts here

# set maximum number of tickets below
MAX_TICKETS = 3

# loop to sell tickets
tickets_sold = 0
while tickets_sold < MAX_TICKETS:
    name = input("Please enter your name or 'xxx' to quit: ")

    if name == 'xxx':
        break

    tickets_sold += 1

# output number of tickets sold
if tickets_sold == MAX_TICKETS:
    print("Congratulations you have sold all the tickets!")
else:
    print("You have sold {} ticket/s. There is {} ticket/s "
          "remaining.".format(tickets_sold, MAX_TICKETS - tickets_sold))
