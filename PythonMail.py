import smtplib

'''For 1 person'''
port = 465
smtp_server = "MAIL-SERVER" # "smtp.gmail.com" for gmail
sender_email = "MAILER"
receiver_email = "REVEICER"
password = input("Type your password and press enter:")
message = "MESSAGE"
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

'''For spamming people'''
def email_spam():
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

number = int(input("how many times do you want to spam?: "))
times = 0
gmail_user = 'EMAIL@EMAIL.com' # Add Email Here
gmail_password = 'PASSWORD'# Add Password Here

sent_from = gmail_user
to = ['123@gmail.com', '456@gmail.com']
subject = ('Important Message')
body = 'Spamming You All Day\n\nWith Regards, \nYou'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    while times < number:
        email_spam()
        print ('Email sent!')
        times = times + 1
except:
    print ('Something went wrong...')
