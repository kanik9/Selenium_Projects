import smtplib as mail


def SendMail():
    s_object = mail.SMTP("smtp.gmail.com",587)
    s_object.starttls()
    s_object.login("vijay123456789ram@gmail.com", "Test_password")

    subject = "Practice mail"
    body = "This is my mail from my python script "
    message = "Subject{}\n\n{}".format(subject,body)
    s_object.sendmail("vijay123456789ram@gmail.com", ['vkanik5@gmail.com','kanikvijay.it20@jecrc.ac.in'], message)
    print("successfully send")
    s_object.quit()
