# get user email address

email = input("What is your email? :").strip()

# slice out user name

user = email[:email.index("@")]

print(user)


# slice domain name

domain = email[email.index("@") + 1 :]

print(domain)

# format message

output = "Your username is {} and your domain name is {}".format(user, domain)

# display output message

print(output)
