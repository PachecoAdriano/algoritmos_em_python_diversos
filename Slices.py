#get user email address
email= input("What is your email address?: ").strip()

#slice out user name

user = email[:email.index("@")]

#slice domaisn name
domain = email[email.index("@") + 1:]

#format message
output = "Your username is {} and your domain name is {}".format(user, domain)
print(output)
