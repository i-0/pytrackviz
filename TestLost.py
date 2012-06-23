#! /usr/bin/env python2.7
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import unittest
import lost

class TestLost(unittest.TestCase):

    def test_follower(self):
        test_cases = [
            {'list':[1,2,3], 'el':1, 'expected':2, 'desc':'Simple Happy Path'},
            {'list':[], 'el':1, 'expected':None, 'desc':'Empty List'},
            {'list':[1], 'el':1, 'expected':None, 'desc':'Last element has no follower'},
            {'list':[1,2,3], 'el':4, 'expected':None, 'desc':'Element not in list'},
            ]

        print "\n:: test follower"
        for t in test_cases:
            print '::\ttesting [ ', t['desc'], ' ] ...',
            expected = t['expected']
            actual = lost.follower(t['el'],t['list'])
            self.assertEquals(actual,expected)
            print ' passed'

    def test_find_edges(self):
        test_cases = [
            {'sub_graph':[1,2,3,4], 'node':1, 'expected':[2], 'desc':'Simple Happy Path find the edges of node'},
            {'sub_graph':[1,2,3,4], 'node':4, 'expected':[], 'desc':'Node has no edges'},
            #{'sub_graph':[1,2,1,3,1,4], 'node':1, 'expected':[2,3,4], 'desc':'Cyclyc graphs'}, # TODO: refine algorithm to support this kind of input
            ]

        print "\n:: test_find_edges"
        for t in test_cases:
            print '::\ttesting [ ', t['desc'], ' ] ...',
            expected = t['expected']
            actual = lost.find_edges(t['node'],t['sub_graph'])
            self.assertEquals(actual,expected)
            print ' passed'

if __name__ == '__main__':
    unittest.main()
