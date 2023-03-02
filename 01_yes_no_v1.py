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

print("done")