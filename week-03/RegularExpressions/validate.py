import re


email = input("What's your email? ").strip()

# using "@" and "." to determine that the input is an email or not
##if "@" in email and "." in email:
##    print("valid")
##else:
##    print("Invalid")


###username, domain = email.split("@")

#if (username) and ("." in domain):
###if (username) and (domain.endswith(".edu")):
###    print("Valid")
###else:
###    print("Invalid")


####if re.search(r"^[^@]+@[^@]+\.com$", email):
if re.search(r"^\w+@(\w+\.)?\w+\.com$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")