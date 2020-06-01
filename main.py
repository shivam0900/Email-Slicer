#getting input from the user
user_input=input('Enter your Email-Id: ')

#Slicing the username from the email id
user_name= user_input[:user_input.index('@')]

#slicing the domain
email_domain=user_input[user_input.index('@')+1:]

#printing the username and the domain name
print(f'\n\nYour Username is {user_name} and the domain is {email_domain}')

