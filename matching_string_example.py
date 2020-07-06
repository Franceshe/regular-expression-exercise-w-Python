import re

# match a date string
regex = r"([a-zA-Z]+) (\d+)"
if re.search(regex, "June 24"):
    match = re.search(regex, "June 24")
    # retrieve where the pattern matches in the input string
    print("Match at index %s, %s" % (match.start(), match.end()))

    # So this will print "June 24"
    print("Full match: %s" % (match.group(0)))
    # So this will print "June"
    print("Month: %s" % (match.group(1)))
    # So this will print "24"
    print("Day: %s" % (match.group(2)))
else:
    # If re.search() does not match, then None is returned
    print("The regex pattern does not match. :(")
    
    
