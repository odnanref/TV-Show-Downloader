#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

class Mailer(object):
    '''
    Send e-mail warning
    '''
    # Create a text/plain message
    msg = ""
    subject = ""
    Source = ""
    Destination = ""

    host = "localhost"
    port = 25
    password = ""
    username = ""
    ssl = False # determine if should or not use ssl

    def __init__(self, text, Subject = "", Config = [] ):
        if len(text) <= 0:
            raise Exception("Missing text")

        if len(Subject) <= 0:
            self.subject = "empty subject"
        else:
            self.subject = Subject

        if len(Config) > 0:
            for conf,val in Config.iteritems():
                if conf == 'host':
                    self.host = val
                elif conf == 'port':
                    self.port = val
                elif conf == 'username':
                    self.username = val
                elif conf == 'password':
                    self.password = val
                elif conf == 'source':
                    self.Source = val
                elif conf == 'destination':
                    self.Destination = val
                elif conf == 'ssl':
                    self.ssl = 1
                    
        self.msg = MIMEText(text)

    def send(self):
        '''
        Prep and send the mail
        '''
        self.msg['Subject'] = self.subject
        self.msg['From'] = self.Source
        self.msg['To'] = self.Destination

        # Send the message via our own SMTP server, but don't include the
        # envelope header.

        smtphost = self.host + ":" + str(self.port)

        s = smtplib.SMTP( smtphost )

        if self.ssl == 1:
            s.starttls()

        if len(self.username) > 0 and len(self.password) > 0 :
            s.login(self.username, self.password)

        s.sendmail(self.Source, [self.Destination], msg.as_string())
        s.quit()

