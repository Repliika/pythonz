# emails = open('emails.txt', "r")
# print(emails.read())
import utilities

with open('emails.txt') as emails: #giving it an alias so easy to reference
    email_list = []
    for email in emails:   
        email_list.append(email)
  
    print(utilities.email_clean(email_list))