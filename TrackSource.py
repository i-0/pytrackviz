#! /usr/bin/env python2.7
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
#
# TrackSource provides the applications with means to generate an
# sqlalchemy engine and a simple sql statement with date and country as
# parameters.
#
# Usage:
#   First set a date YYYYMMDD (for example 20120513) for and a country at
#   the moment 'de', 'uk', 'ru' and 'za' are supported.
#
#   Second call the getTrackSource(engine) method.
#
# Restrictions:
#   At  the moment only SQL data sources are supported, also only MySQL
#   and sqlite are supported as DB back ends.
#
# TODO:
#    Implement other data sources as log files and CSV files as data
#    sourcs.
#
# author: Christoph Gierling
# date:   15.06.2012


class TrackSource(object):
    """Gathers the parameters to access the track data and prepares the
    retrieval process, for the moment as SQL statement. The engine and
    sql fields are used by TrackData to populate the TrackData
    objects."""
    country = None  # string containing the country code
                    # {'de','uk','za',ru'}

    date = None     # integer encoded as YYYYMMDD, for example 20120606

    engine_str = None   # string as entry parameter for sqlalchemy's
                    # create_engine method, for exmaple
                    # 'sqlite:///:memory:' (see sqlalchemy doc)
    sql = 'select trackId, count(trackId) from Tracking_Data_%s_%d where flowType = "commonflow" group by trackId' #  %s <= country, %d <= date

    def setDate(self, date):
        """Sets the date parameter which is used used to resolve the
        table name for example Tracking_Data_ru_2012060"""
        self.date = date

    def setCountry(self, country):
        """Sets the country parameter which is used to resolve the table
        name for example Tracking_Data_ru_2012060"""
        self.country = country

    def setEngineString(self, engine_str):
        """Sets the egine which is later returned to TrackData, in order
        to get the track data from the DB."""
        self.engine_str = engine_str

    def getTrackSource(self):
        """Return the engine string and the SQL string pointing to the
        date and country specified"""
        return (self.engine_str, self.getSQL())

    def getSQL(self):
        """Getter which interpolates country and date in the SQL base
        string, used by the getTrackSource method"""
        if type(self.date) == int and type(self.country) == str:
            return self.sql % (self.country, self.date)
        else:
            raise Exception('Error: You cannot call getSQL() without setting a country as string  and date as int.')
