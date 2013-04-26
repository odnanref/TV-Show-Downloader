#!/usr/bin/env python
# -*- coding: utf-8 -*-

from EventDispatcher import Event

class DownloadEvent( Event ):
    """
    When subclassing Event class the only thing you must do is to define
    a list of class level constants which defines the event types and the 
    string associated to them
    """
    name = "DownloadEvent" # Identifies the event name

    PRESAVE         = "presave" # before saving to database
    POSTSAVE        = "postsave" # After Saved to database
    DOWNLOAD_READY  = "DOWNLOAD_READY" # Download exists and ready for download
    DOWNLOAD_DONE   = "DOWNLOAD_COMPLETED" # Download successfull

