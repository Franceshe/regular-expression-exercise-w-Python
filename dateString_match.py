import re
# use regular expression to match a date string
# Ignore output since it is just a tesing if
# regex matches
regex = r"([a-zA-Z]+) (\d+)"
if re.search(regex, "June 24"):
    match = re.search(regex, "June 24")
    print("Match at index %s, %s" %(match.start(), match.end()))
    # # This will print [0, 7), since it matches at the beginning and end of the 
    # string

    print("Full match: %s" %(match.group(0)))
    print("Month: %s" % (match.group(1)))
    print("Days: %s" % (match.group(2)) )
    # if non matchm None is returned
else:
    print("The regex pattern does not match.:(")
    
