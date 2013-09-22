#! /usr/bin/env python2.7

import ConfigParser
import argparse


class Configuration(object):

    args = {
        'config_file': None,
        'template_files': None,
        'date': None,
    }

    db = {
        'db_user': None,
        'db_pwd': None,
        'db_port': None,
        'db_ip': None,
        'db_table_name': None,
        'db_engine': None,
        'db_type': None,
    }

    def parseCommandLineArgs(self):
        """ Parse the 3 command line arguments, with help from argparse. Those
        parameters are stores in the args maps."""

        parser = argparse.ArgumentParser()
        parser.add_argument(
            '--inputfile', '-f',
            nargs=1, type=file,
            help='File containing the track graph in dot format to process.',
            required=True
        )

        parser.add_argument(
            '--configfile', '-c',
            nargs=1, type=file,
            help='File containing the DB connection settings.',
            required=True
        )

        parser.add_argument(
            '--date', '-d',
            nargs=1, type=int,
            help='The date in format YYYYMMDD, for example 20120521 for 2012-05-21.',
            required=True
        )
        arguments = parser.parse_args()

        self.args['template_files'] = arguments.inputfile[0]  # TODO: change to support multiple files
        self.args['config_file'] = arguments.configfile[0]

        # TODO: Implement a way to validate the date (regex, date parser)
        self.args['date'] = arguments.date[0]

    def parseConfigFile(self):

        config = ConfigParser.SafeConfigParser()

        # conver to name, argparse stores a file handle, but ConfigParser excepts a file name
        config_file_name = self.args['config_file'].name

        config.read(config_file_name)

        self.db['country'] = config.get('ServiceConfiguration', 'country', None)
        self.db['db_type'] = config.get('track_stats_services_DB', 'db_type', None)

        if self.db['db_type'] == 'mysql':
            self.db['db_pwd'] = config.get('track_stats_services_DB', 'password', None)
            self.db['db_user'] = config.get('track_stats_services_DB', 'user', None)
            self.db['db_port'] = config.get('track_stats_services_DB', 'port', None)
            self.db['db_ip'] = config.get('track_stats_services_DB', 'IP', None)
            self.db['db_table_name'] = config.get('track_stats_services_DB', 'table_name', None)

        elif self.db['db_type'] == 'sqlite':
            self.db['db_name'] = config.get('track_stats_services_DB', 'db_name', None)

        # TODO: instead of adding more elif stmnts, think about a flat hierarchy of Configuration Objects

    def getDbEngine(self):
        """Returns the final engine string as used by create_engine from
        sqlalchemy."""

    # TODO: complicated, at time use interpolation directly in the conf file
        if self.db['db_engine'] is not None:
            return self.db['db_engine']

        elif self.db['db_type'] == 'mysql':
            # TODO: change to use engine_from_config based on kwargs
            engine = self.db['db_type'] + "://" + self.db['db_user'] + ":" + self.db['db_pwd'] + "@" + self.db['db_ip'] + ":" + self.db['db_port'] + "/" + self.db['db_table_name']

        elif self.db['db_type'] == 'sqlite':
            engine = self.db['db_type'] + ":///" + self.db['db_name']
        else:
            raise Exception("Error: Unknown DB type, check the configuration file!")

        return engine

    def getCountry(self):
        return self.db['country']

    def getDate(self):
        return self.args['date']

    def getTemplates(self):
        return self.args['template_files']

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
