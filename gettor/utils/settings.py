# -*- coding: utf-8 -*-
"""
This file is part of GetTor, a service providing alternative methods to download
the Tor Browser.

:authors: Hiro <hiro@torproject.org>
          please also see AUTHORS file
:copyright: (c) 2008-2014, The Tor Project, Inc.
            (c) 2014, all entities within the AUTHORS file
:license: see included LICENSE for information
"""

import json
import os

from . import strings


class Settings(object):
    """
    This class stores all of the settings for GetTor
    """
    def __init__(self, config):


        # If a readable config file was provided, use that instead
        if config and os.path.isfile(config):
            self.filename = config
        else:
            # Default config
            default_config = "/home/gettor/gettor/gettor.conf.json"
            self.filename = self.build_filename(default_config)

        # Dictionary of available languages,
        # mapped to the language name, in that language
        self._available_locales = strings.get_locales()
        self._version = strings.get_version()
        self._settings = {}

    def build_filename(self, file):
        """
        Returns the path of the settings file.
        """
        return strings.get_resource_path(file, strings.find_run_dir())

    def load(self):
        """
        Load the settings from file.
        """

        # If the settings file exists, load it
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                  self._settings = json.load(f)
            except:
                pass
        else:
            self._settings = {
              "platforms": ["linux", "osx", "windows"],
              "dbname": "/srv/gettor.torproject.org/home/gettor/gettor.db",
              "email_parser_logfile": "/srv/gettor.torproject.org/home/gettor/log/email_parser.log",
              "email_requests_limit": 30,
              "twitter_requests_limit": 1,
              "sendmail_interval": 10,
              "twitter_interval": 10,
              "sendmail_addr": "gettor@torproject.org",
              "sendmail_host": "localhost",
              "sendmail_port": 587,
              "consumer_key": "",
              "consumer_secret": "",
              "access_key": "",
              "access_secret": "",
              "test_hid": "",
              "twitter_handle": "get_tor",
              "twitter_messages_endpoint": "https://api.twitter.com/1.1/direct_messages/events/list.json",
              "twitter_new_message_endpoint": "https://api.twitter.com/1.1/direct_messages/events/new.json"
            }

    def get(self, key):
        return self._settings[key]
