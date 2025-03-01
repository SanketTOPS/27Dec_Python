import re


email = "sanket1991@gmail.com"
email_pattern = "[a-z0-9]+[@]+[a-z]+[\.]+[a-z]"

x = re.findall(email_pattern, email)

if x:
    print("Valid email!")
else:
    print("Error!Invalid Email...")
