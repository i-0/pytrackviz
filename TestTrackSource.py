#! /usr/bin/env python2.7
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import unittest
import TrackSource

class TestTrackSource(unittest.TestCase):

    def test_getTrackSource_hp(self):

        print "\n:: TestTrackSource happy path...",
        track_source = TrackSource.TrackSource()

        country = 'ru'
        date = 20120606
        engine = 'mysql://tracktatrepo:chorizo@192.168.1.126:3306/track_stats_services'
        track_source.setDate(date)
        track_source.setCountry(country)
        track_source.setEngineString(engine)

        actual_engine, actual_sql = track_source.getTrackSource()
        expected_engine_str = 'mysql://tracktatrepo:chorizo@192.168.1.126:3306/track_stats_services'
 
        expected_sql = 'select trackId, count(trackId) from Tracking_Data_ru_20120606 where flowType = "commonflow" group by trackId'
        self.assertEqual(expected_sql, actual_sql)
        self.assertEqual(expected_engine_str, str(actual_engine))
        print "passed"

    def test_getTrackSource_sp(self):

        print "\n:: TestTrackSource sad path...",
        track_source = TrackSource.TrackSource()

        date = 20120606
        engine = 'mysql://tracktatrepo:chorizo@192.168.1.126:3306/track_stats_services'
        track_source.setDate(date)
        # do not set the country, and see what happens
        track_source.setEngineString(engine)

        try:
            actual_engine, actual_sql = track_source.getTrackSource()
            fail("Exception not caught!")
        except Exception:
            # all ok, exception caught!
            # TODO: Interesting, why does the code has an indent err of this bogus line is
            # missing?
            print "passed"

    def test_getTrackSource_check_types(self):

        print "\n:: TestTrackSource check types:"
        track_source = TrackSource.TrackSource()
        input = [
            {
                'test_case': 'date as string instead of int',
                'date':"2012060",
                'country': 'ru',
                'error':'Exception',
            },
            {
                'test_case': 'country as function instead of str',
                'country': self.test_getTrackSource_sp,
                'date': 2012060,
                'error':'Exception',
            },
            {
                'test_case': 'date as None',
                'country': 'ru',
                'date': None,
                'error':'Exception',
            },
            {
                'test_case': 'country as None',
                'country': None,
                'date': 1234,
                'error':'Exception',
            },
            {
                'test_case': 'all types are fine, same as happy path',
                'country': 'ru',
                'date': 20120606,
                'error': None,
            },
        ]

        engine = 'mysql://tracktatrepo:chorizo@192.168.1.126:3306/track_stats_services'

        for i in input:
            date = i['date']
            # print ':: date [', date, '] type [', type(date), ']'

            country =  i['country']
            # print ':: country [', country, '] type [', type(country), ']'

            track_source.setDate(date)
            track_source.setCountry(country)
            track_source.setEngineString(engine)

            print "::\tTest Case [", i['test_case'],"]",
            if i['error'] == 'Exception':
                try:
                    actual_engine, actual_sql = track_source.getTrackSource()
                    print " failed"
                    self.fail("Exception not caught!")
                except Exception:
                    # all ok, exception caught!
                    print " passed"

            elif i['error'] == None:
                try:
                    track_source.getTrackSource()
                    # only testing the exceptions behaviour not the internal
                    # processing for more details see the happy path test
                    print " passed"
                except Exception, err:
                    print " failed"
                    print "::\t\tException [ ",
                    print str(err),
                    print " ]"
                    self.fail("Exception caught!")

            else:
                raise Exception("Other test errors are not yet implemented!")

if __name__ == '__main__':
    unittest.main()
