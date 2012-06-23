#! /usr/bin/env python2.7
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import unittest
import TemplateProcessor

class TestTemplateProcessor(unittest.TestCase):

    def test_getTrackSource(self):

        print ":: TestTemplateProcessor ...",

        template_processor = TemplateProcessor.TemplateProcessor()

        template_processor.setMatcher()
        lines_to_match = [
            '22 [label="user_redirected_to_mts | id: 22 | {{trackCount_22}} "];',
            '11 [label="UserAlreadySubs | id: 11 | {{trackCount_11}} "];',
        ]
        for line in lines_to_match:
            self.assertTrue(template_processor.matcher.search(line))

        print "passed"



if __name__ == '__main__':
    unittest.main()
