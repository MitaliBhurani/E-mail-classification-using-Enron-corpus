# Opening the Emails in Python

# importing the class Parser from the built-in library email.parser
from email.parser import Parser

file_to_read = "F:\\enron_mail_20150507\\maildir\\lay-k\\all_documents\\1"

# If we use "with" command then it will automatically close the file for us and also handles exceptions if any
with open(file_to_read, "r") as f:
    data = f.read()

# print(data)
# Parse the file using "Parser()" instance of the Parser class and using parsestr() function
email = Parser().parsestr(data)

print("\nTo: " , email['to'])
print("\n From: " , email['from'])

print("\n Subject: " , email['subject'])

# One problem is that it cannot parse the "body" & it will not print anything in output for email['body']
# Hence use the function email.get_payload() 
print("\n \n Body: " , email.get_payload())

