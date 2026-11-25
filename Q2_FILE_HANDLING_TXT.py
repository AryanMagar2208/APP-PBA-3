#write a python script to read a text file and indentify the longest line along with its line number.


def find_longest_line(filename):
    longest_line = ""
    longest_line_number = 0

    with open(filename, "r") as file:
        for line_number, line in enumerate(file, start=1):
            line = line.rstrip("\n")

            if len(line) > len(longest_line):
                longest_line = line
                longest_line_number = line_number

    print("Longest line number:", longest_line_number)
    print("Longest line:", longest_line)


filename = "lines.txt"

find_longest_line(filename)
