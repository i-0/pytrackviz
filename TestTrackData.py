#! /usr/bin/env python2.7
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import unittest
import TrackData

class TestTrackData(unittest.TestCase):
    
    def test_initTrackCount(self):

        print ":: Testing TrackData ...",

        td = TrackData.TrackData()
        td.initTrackCountMap()
        for t in td.track_count_map:
            self.assertTrue(td.track_count_map[t] == 0)

        expected_tracks = td.known_tracks.sort()
        actual_tracks = td.track_count_map.keys().sort()

        self.assertEqual(expected_tracks, actual_tracks)
        print "passed"

if __name__ == '__main__':
    unittest.main()
