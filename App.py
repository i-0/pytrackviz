#! /usr/bin/env python2.7
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import Configuration
import TrackSource
import TrackData
import TemplateProcessor


class App(object):

    def __init__(self):
        pass

    def start(self):
        # process configuration
        conf = Configuration.Configuration()
        conf.parseCommandLineArgs()
        conf.parseConfigFile()

        # prepare track source, for the moment only
        # SQL DBs are supported but log files are thinkable
        track_source = TrackSource.TrackSource()
        engine_str = conf.getDbEngine()
        track_source.setEngineString(engine_str)
        track_source.setDate(conf.getDate())
        track_source.setCountry(conf.getCountry())
        final_engine_str, final_sql = track_source.getTrackSource()

        # retireve track data
        track_data = TrackData.TrackData()
        engine_and_sql = (final_engine_str, final_sql)
        track_data.getTracksData(engine_and_sql)

        # choose dot template
        template_processor = TemplateProcessor.TemplateProcessor()

        template_file = conf.getTemplates()

        template_processor.setTemplateFile(template_file)

        # process template with data
        template_processor.setDate(conf.getDate())
        template_processor.setTrackData(track_data)
        template_processor.setMatcher()

        template_processor.process()  # prints template to std out


def main():
    app = App()
    app.start()

if __name__ == "__main__":
    main()
