#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ---------------------------
# On a Download successfull 
# Send alert e-mail
# ---------------------------

import DownloadEvent
from Mailer import Mailer

class MailerListener(object):
    '''
    Listens for Download and sends e-mail

    These are the configuration details for the config
    in the global section add and change the bellow:

    ; config for mail listener
    mail_host= localhost
    mail_port=
    mail_username = something
    mail_password = somepass
    mail_from = mymail@localhost.localdomain
    mail_to = mymail@localhost.localdomain
    mail_ssl = 0

    '''

    _config = {}

    def update(self, DownloadEvent):
        print " just got event " + DownloadEvent.name
        episode = DownloadEvent.data['episode']
        message = "Hello this is tvshow Downloader\n" + \
        "I found " + episode.get_name() + " for download\n From season: " + \
        str(episode.get_season()) + "\n Episode number: " + str(episode.get_episode_number()) + "\n"

        message += " the magnet url is:\n " + episode.get_magnet()

        mailer = Mailer( message, "New episode " + episode.get_name(), self.getConfig() )
        mailer.send()


    def getConfig(self):
        return self._config

    def setConfig(self, Config):
        try:
            host = Config.getGlobal("mail_host")
            if len(host) > 0:
               self._config["host"] = host

            port = Config.getGlobal("mail_port")
            if len(port) > 0:
               self._config["port"] = port
            username = Config.getGlobal("mail_username")
            if len(username) > 0:
               self._config["username"] = username

            password = Config.getGlobal("mail_password")
            if len(password) > 0 :
               self._config["password"] = password

            mail_from = Config.getGlobal("mail_from")
            if len(mail_from) > 0:
                self._config['source'] = mail_from

            mail_to = Config.getGlobal("mail_to")
            if len(mail_to) > 0:
                self._config['destination'] = mail_to

            ssl = Config.getGlobal("mail_ssl")
            if ssl == "1" or ssl.lower() == "true":
                self._config['ssl'] = 1

        except Exception, e:
            print 'Exception raised MailerListener config\n dependency related: ' + str(e)

