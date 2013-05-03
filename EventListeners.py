#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# ADD HERE Your event Listeners
#

from DownloadEvent import DownloadEvent
from MailerListener import MailerListener

class EventListeners(object):
    Listeners = {}

    def __init__(self, ConfManager):
        DL = MailerListener()
        DL.setConfig(ConfManager)
        self.Listeners[DownloadEvent.DOWNLOAD_READY] = DL.update

    def add(self, TYPE, EventListener, ConfManager = None):
        if ConfManager != None:
            EventListener.setConfig(ConfManager)

        self.Listeners[TYPE] = EventListener

    def getAll(self):
        return self.Listeners

