student_number = int(input("How many students do you have?\n"))     # Get number of students from user

with open("reg_form.txt", "w") as f:    # Open file as f
    for i in range(student_number):     # Loop to ask for student id a number of time = above input
        student_id = input("What is your student ID?\n")
        f.write(f"{student_id}\n\n...........................\n\n")

f.close()

# I used double \n to makes space between names and for the signature on dotted lines
# Is there a more visually pleasing way to do multiple lines rather than repeated \n?
# I imagine its using * ?
