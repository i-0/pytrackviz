#! /usr/bin/env python2.7
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import unittest
import Configuration


class ConfigurationTests(unittest.TestCase):

    def test_parseConfigFile(self):

        print ":: TestConfiguration ...",

        conf = Configuration.Configuration()
        conf.args = {
            'config_file': file('test/sqlite.conf', 'r'),
            'date': '20120606',
            'template_files': file('dot_templates/new_basic_template.dot', 'r')
        }
        expected = 'sqlite:///track_stats_services.db'
        conf.parseConfigFile()
        actual = conf.getDbEngine()
        self.assertEqual(expected, actual)

        conf.args = {
            'config_file': file('test/mysql.conf', 'r'),
            'date': '20120606',
            'template_files': file('dot_templates/new_basic_template.dot', 'r')
        }

        expected = 'mysql://trackstatrepo:chorizo@192.168.1.126:3306/track_stats_services'

        conf.parseConfigFile()
        actual = conf.getDbEngine()

        self.assertEqual(expected, actual)
        print "passed"

    def nottest_parseCommandLine(self):
        """argparse is a reliable tool, only implement tests for found usage bugs"""

if __name__ == '__main__':
    unittest.main()
