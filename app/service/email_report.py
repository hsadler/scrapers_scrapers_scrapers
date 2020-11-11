import smtplib


class EmailReport():

    
    @staticmethod
    def send_email(sender, password, recipients, subject, body):
        # prepare message
        message = "From: {0}\nTo: {1}\nSubject: {2}\n\n{3}".format(
            sender, 
            ", ".join(recipients), 
            subject, 
            body
        )
        # commit send
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(sender, password)
            server.sendmail(sender, recipients, message)
            server.close()
        except:
            print('failed to send mail')


    @classmethod
    def email_samtrygg_report(
        cls, 
        sender, 
        password,
        recipients,
        subject, 
        new_listings=[], 
        relevant_listings=[]
    ):
        formatted_email_body = 'test samtrygg email body...'
        cls.send_email(
            sender=sender,
            password=password,
            recipients=recipients,
            subject=subject,
            body=formatted_email_body
        )