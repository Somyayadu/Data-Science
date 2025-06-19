import smtplib
try:
    server =smtplib.SMTP("smtp.gmail.com",port=587)
    server.starttls()

    receiver_mail=input("enter the receiver the email")

    sender_email="somyayaduvanshi6@gmail.com"
    password="mjqy jpnr snfj zvwq"

    server.login(sender_email,password)

    subject=input("enter the subject : ")
    body=input("Enter the body ")
    message=f"subject:{subject}\n\n{body}"
    server.sendmail(sender_email,receiver_mail,message)
    print("mail sent successfully")
    server.quit()
except Exception as e:
    print("an error occured",e)