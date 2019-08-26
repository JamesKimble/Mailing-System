import smtplib
import time

###########
## Email ##
###########


def details():
    global email
    global pwrd

    time.sleep(2)
    email = input("\nWhat email address do you want to use?\n: ")

    if (email == "YOUR EMAIL ADDRESS"):
        code = "YOUR ACCOUNT PASSWORD"
        pwrd = code
    elif (email == "YOUR OTHER EMAIL ADDRESS"):
        code = "YOUR OTHER ACCOUNT PASSWORD"
        pwrd = code
    else:
        time.sleep(1.5)
        print("\nSorry. That email address is invalid. Please use either of the following email addresses:\n")
        time.sleep(1.5)
        print("1. YOUR EMAIL ADDRESS")
        print("2. YOUR OTHER EMAIL ADDRESS")
        time.sleep(3)
        details()


details()

time.sleep(1)
print("\nCurrently logged in as: " + email)
time.sleep(2)
recipitent = input("\nEnter the recipitent's email address\n: ")
customSubject = input("\n\nPlease enter your subject\n: ")
customBody = input("\n\nPlease enter your message\n: ")


def send_mail():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(email, pwrd)

    subject = customSubject
    body = customBody

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        email,
        recipitent,
        msg

    )
    print("\nYour email has been sent!\n")

    server.quit()


send_mail()
