#! /usr/bin/env python2.7
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
#
# TrackData defines, stores and processes (Model, Controller) track data.
# Separating the Modell and the Controller components more, seems for the
# moment overeningeering.
#
# Restrictions: Only first level of lost users will be calcualted, the other
# levels are still work in progress.
#
# author: Christoph Gierling
# date 17.05.2012

import sqlalchemy
from sqlalchemy import create_engine

class TrackData:
    # TODO: Make configurable for future integrations with other templates
    known_tracks = [1, 10, 11, 20, 21, 211, 212, 213, 30, 40, 41, 50, 60, 70, 99]
    track_graphs = [
	[1, 10, 20, 30, 40, 50, 60, 70],
	[1, 10, 20, 30, 41, 70],
	[1, 10, 21, 211, 212, 30],
	[1, 10, 21, 211, 213, 70],
	[1 , 11],
    ]

    lost_tracks = {}
    track_count_map = {}

    def initTrackCountMap(self):
        """ Set all know tracks in track_count_map to 0."""
        for i in self.known_tracks:
            self.track_count_map[i] = 0

    def setTrackCountMap(self, track_count_map):
        self.track_count_map = track_count_map

    def getTracksData(self, track_source):
        """ Retrieve data from track_source and populate the track_count_map."""

        # connecto to DB and retrieve tracks data, if the map is not already
        # defined (mostly injected by setTrackCountMap() for testing purposes)
        if self.track_count_map == {}:
            engine_str = track_source[0]
            engine = create_engine(engine_str)

            sql = track_source[1]

            result = engine.execute(sql)

            # Rather primitive mapping from sql result set to internal data
            # structure, empty track ids are set to 0
            self.initTrackCountMap()
            for row in result:
                key = int(row[0])
                value = int(row[1])
                self.track_count_map[key] = value
        #else: map already populated

        # The following call adds fictive track ids to the number of lost
        # tracks, which will be later visualized as track states in the final
        # diagram.
        self.calculateLostTracks()

        return self.track_count_map


    def calculateLostTracks(self):
        """ Calculates how many users represented by their tracks, are lost
        after the different levels of the flow."""

        # TODO: wrap in a loop to support arbitrary depth, needs refinement in
        # the algorithm side
        level = 0       # current level to process
        tracks = {}     # gathers tracks sharing the same level
        start_state = self.track_graphs[0][0]
        tracks[0] = set([start_state])

        # validate track graph's hierarchy
        for t in self.track_graphs:
            if not t[level] == start_state:
                raise Exception('No common start state for all graphs in the track model.')

        # gather next level of states in a separate list, for now limited to the 1st level
        level = level + 1
        tracks[level] = set()
       
        for track_seq in self.track_graphs:
            tracks[level].add( track_seq[level] )

        # subtract all second level tracks from the start state count
        tmp_lost_tracks = 0
        for i in tracks[level]:
            if i in self.track_count_map:
                tmp_lost_tracks = tmp_lost_tracks + self.track_count_map[i]

        self.lost_tracks[level] = self.track_count_map[start_state] - tmp_lost_tracks

#         self.lost_tracks[level] = self.track_count_map[start_state] - sum(
#             [ self.track_count_map[i] for i in list(tracks[level]) if i in self.track_count_map ]
#         )

        # TODO: This mapping for the lost tracks to 9991, 9992, 9993,... is
        # little less than a hack. Take into consideration for adding deeper
        # processing. The track ids 999n corespond to track states in the dot
        # graph template, have a look there.
        self.track_count_map[9990+level] = self.lost_tracks[level]


        return self.lost_tracks
