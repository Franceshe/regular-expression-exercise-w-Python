import re
# using re.sub()
# reverse the order of the day and month in a date
# string. 
regex = r"([a-zA-Z]+) (\d+)"

# replacedString = re.sub(pattern, replacement_pattern, input_str, count, flags=0)
print(re.sub(regex, r"\2 of \1", "June 24, August 9, Dec 12"))
