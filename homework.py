# In class exercise 3:

import re
filename = "names.txt"

with open(filename, "r") as file:
    lines = file.readlines()

print("==============")
print("Full Name / Twitter")
print("==============\n")

for line in lines:
    match = re.match(r"^([A-Z][a-zA-Z'-]+)\s([A-Z][a-zA-Z'-]+)\s/\s@([a-zA-Z0-9]+)$", line)
    if match:
        first_name = match.group(1)
        last_name = match.group(2)
        twitter_handle = match.group(3)
        print(f"{first_name} {last_name} / @{twitter_handle}")
    else:
        print("None")

# Regex Project

# Use python to read the file regex_test.txt and print the last name on each line using regular expressions and groups (return None for names with no first and last name, or names that aren't properly capitalized)  

import re

filename = "regex_test.txt"

with open(filename, "r") as file:
    lines = file.readlines()

for line in lines:
    match = re.match(r"^[A-Z][a-zA-Z]*\s([A-Z][a-zA-Z]*)$", line)
    if match:
        last_name = match.group(1)
        print(last_name)
    else:
        print("None")
