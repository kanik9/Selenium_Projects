import imaplib
import email


# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# ------------------------------------------------

class ReadMail():
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com", 993)
        mail.login("vijay123456789ram@gmail.com", "Test_password")
        mail.select('inbox')

        type, data = mail.search(None, 'ALL')
        mail_ids = data[0]

        id_list = mail_ids.split()
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])


        for i in range(latest_email_id,first_email_id, -1):
            typ, data = mail.fetch(i, '(RFC822)' )

            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_string(response_part[1])
                    email_subject = msg['subject']
                    email_from = msg['from']
                    print('From : ' + email_from + '\n')
                    print('Subject : ' + email_subject + '\n')

    except Exception as e:
        print(str(e))



