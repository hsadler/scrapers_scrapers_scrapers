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
            server.sendmail(sender, recipients, message.encode('utf8'))
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
        email_body_parts = []
        # format new listings
        email_body_parts.append('NEW LISTINGS:\n')
        for listing in new_listings:
            email_body_parts.append(listing.get_title())
            email_body_parts.append('\t{}'.format(listing.get_web_link()))
            email_body_parts.append('\tcity: {}'.format(listing.get_city()))
            email_body_parts.append('\tprice: {}'.format(listing.get_price()))
            email_body_parts.append('\trooms: {}'.format(listing.get_rooms()))
            email_body_parts.append('\tsq meters: {}'.format(listing.get_sq_meters()))
            email_body_parts.append('\n')
        # format relevant listings
        email_body_parts.append('RELEVANT LISTINGS:\n')
        for listing in relevant_listings:
            email_body_parts.append(listing.get_title())
            email_body_parts.append('\t{}'.format(listing.get_web_link()))
            email_body_parts.append('\tcity: {}'.format(listing.get_city()))
            email_body_parts.append('\tprice: {}'.format(listing.get_price()))
            email_body_parts.append('\trooms: {}'.format(listing.get_rooms()))
            email_body_parts.append('\tsq meters: {}'.format(listing.get_sq_meters()))
            email_body_parts.append('\n')
        # format email body from parts
        formatted_email_body = '\n'.join(email_body_parts)
        
        # testing:
        # print(formatted_email_body)
        # return
        # formatted_email_body = 'testing agian...'

        # send email
        cls.send_email(
            sender=sender,
            password=password,
            recipients=recipients,
            subject=subject,
            body=formatted_email_body
        )