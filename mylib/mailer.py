import smtplib, ssl

class Mailer:

    """
    This script initiaties the email alert function.
    """
    def __init__(self):
    
        self.EMAIL = "lintotony7@gmail.com"
        self.PASS = ""
        self.PORT = 465
        self.server = smtplib.SMTP_SSL('smtp.gmail.com', self.PORT)

    def send(self, mail):
        self.server = smtplib.SMTP_SSL('smtp.gmail.com', self.PORT)
        self.server.login(self.EMAIL, self.PASS)
        SUBJECT = 'ALERT!'
        TEXT = f'Social distancing violations exceeded!'
        message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
        self.server.sendmail(self.EMAIL, mail, message)
        self.server.quit()
