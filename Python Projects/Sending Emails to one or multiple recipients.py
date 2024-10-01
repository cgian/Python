# Python program that can send emails to one or multiple recipients using an email account
# note: the code is set for Gmail

#importing the required module
import smtplib

# set up the SMTP server
smtp_server = 'smtp.example.com'
port = 587  # For SSL
server = smtplib.SMTP('smtp.gmail.com',587)

# create SMTP session
server.starttls()

# asking login details
sender_address = input('enter your email: ')
pssw = input('enter your regular password or app password: ')

# Login to the Server
server.login(sender_address, pssw)

print('login success')

# entering the address or multiple addresses
recipients_address_list = []
while True:
    recipients_address_list.append(input('insert recipient: '))
    while True:
        continuation = input('do you want to add another recipient? (yes/no) ')
        if continuation == 'yes':
            break
        elif continuation == 'no':
            break
        else:
            print('wrong entry')
    if continuation == 'no':
        break
    else:
        None

# here we compose the email
subject = input('insert subject of the email: ')
body = input('insert the message you want to send: ')
to_addresses = ', '.join(recipients_address_list)
content = f'To: {to_addresses}\nFrom: {sender_address}\nSubject: {subject}\n\n{body}'

# send the Email
server.sendmail(sender_address, recipients_address_list, content)
print(f'the email has been sent to {to_addresses}')

# close the SMTP Session
server.quit()

