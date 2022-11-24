numbers_one = [12, 8, 4, 34, 30, 29]    # First list of numbers for first file
numbers_one = sorted(numbers_one)       # Numbers sorted in order
numbers_two = [33, 14, 66, 45, 12, 55]  # Second list of numbers for second file
numbers_two = sorted(numbers_two)       # Numbers sorted in order
list_one = ""       # Empty var to write files to
list_two = ""


with open("numbers1.txt", "w+") as num_1:   # Create new file and open as num_1
    for num in numbers_one:
        num_1.write("%i \n" % num)  # writes as int with line spaces

with open("numbers1.txt", "r") as num_1:
    read_list_one = num_1.read().splitlines()       # reads into list of strings w/o \n
    list_one = read_list_one

with open("numbers2.txt", "w+") as num_2:   # Create new file and open as num_2
    for num in numbers_two:
        num_2.write("%i \n" % num)

with open("numbers2.txt", "r") as num_2:
    read_list_two = num_2.read().splitlines()
    list_two = read_list_two

list_final = (list_one + list_two)      # Reading from text gives list
list_final = [int(item) for item in list_final]     # Converts list of str to list of int
list_final = sorted(list_final)

with open("all_numbers.txt", "w+") as all_num:      # Creating new file and open as all_num
    for num in list_final:
        all_num.write("%i \n" % num)      # Formats combined list as ints with spaces and writes them

# The trick to store the lists as individual numbers without [] in the file using % (format) i (int)
# came from StackOverflow
# I wonder if you know another way to have the same result or is this way okay?


