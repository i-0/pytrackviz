#! /usr/bin/env python2.7
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
#
# TemplateProcessor substitutes a placeholder for tracks of the from
# {{trackCount_<id>}} with the count stored in the TrackData object.
#
# author:Christoph Gierling
# date: 17.05.2012

import re

class TemplateProcessor:

    track_data = None
    track_count_map = None # just a shortcut for the moment, make private
    var_delim_pattern = '^.*{{trackCount_([0-9]+)}}\s.*$'
    matcher = None
    template_file = None
    date = None

    def setTrackData(self, track_data):

        self.track_data = track_data
        self.track_count_map = self.track_data.track_count_map

    def setMatcher(self, matcher=None):

        if matcher == None:
            self.matcher = re.compile(self.var_delim_pattern)
        else:
            self.matcher = matcher

    def setDate(self, date):

        self.date = date

    def setTemplateFile(self, template_file):

        self.template_file = template_file

    def process(self):
        """Loop over the provided file and print the processed dot template"""

        for line in self.template_file:
            self.print2dot(line, self.matcher, self.track_count_map, self.date)

        self.template_file.close()

    def print2dot(self, line, matcher, trackCount, date):
        """Substitue placeholder with count if line has a placeholder, else print the line."""

        m = matcher.search(line)
        if m:
            track_id = m.group(1)
            placeholder = '{{trackCount_' + track_id + "}}"
            if int(track_id) in self.track_count_map:
                line = line.replace(placeholder, str(trackCount[int(track_id)]))
            else:
                line = line.replace(placeholder, "0")
        # FIXME: perhaps separate static part of template from non-static too boost some performance, but remember D. Knuth!
        if line.find('{{date}}'):
            line = line.replace('{{date}}', str(date))

        print line
