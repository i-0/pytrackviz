#! /usr/bin/env python2.7
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
# Christoph Gierling
import datetime
from datetime import date

def store(tracks, country, date):
    import sqlalchemy
    from sqlalchemy import create_engine, Table, MetaData, Integer, String, Column
    
    engine = 'sqlite:///track_stats_services.db'
    db = create_engine(engine)
    db.echo = False
    metadata = MetaData(db)
    tableName = 'Tracking_Data_%s_%s' % (country, date)
    print ":: Creating a the table [", tableName, "] with some fake track data, this can take some time ..."
    table = Table(tableName, metadata,
        Column('id', Integer, primary_key=True),
        Column('trackId', Integer),
        Column('flowType', String(45)),
        )
    table.create(checkfirst=True)
    
    for track in tracks:
        print "\t",str(track)
        for i in range (track['count']):
            ins = table.insert()
            ins.execute(**track['row'])

    print ":: Done!"

tracks = [
    {'row':{'trackId':  1, 'flowType':'commonflow'}, 'count':100 },
    {'row':{'trackId': 10, 'flowType':'commonflow'}, 'count': 85 },
    {'row':{'trackId': 11, 'flowType':'commonflow'}, 'count': 10 }, # 10 users lost
    {'row':{'trackId': 20, 'flowType':'commonflow'}, 'count': 70 },
    {'row':{'trackId': 21, 'flowType':'commonflow'}, 'count': 15 },
    {'row':{'trackId':211, 'flowType':'commonflow'}, 'count': 15 },
    {'row':{'trackId':212, 'flowType':'commonflow'}, 'count': 10 },
    {'row':{'trackId':213, 'flowType':'commonflow'}, 'count':  5 },
    {'row':{'trackId': 30, 'flowType':'commonflow'}, 'count': 79 },
    {'row':{'trackId': 40, 'flowType':'commonflow'}, 'count':  5 },
    {'row':{'trackId': 41, 'flowType':'commonflow'}, 'count': 55 },
    {'row':{'trackId': 50, 'flowType':'commonflow'}, 'count':  4 },
    {'row':{'trackId': 60, 'flowType':'commonflow'}, 'count':  3 },# 1 user lost to an Exception
    {'row':{'trackId': 70, 'flowType':'commonflow'}, 'count': 13 },
    {'row':{'trackId': 99, 'flowType':'commonflow'}, 'count':  1+1},
]
country = 'ru'
today = int(date.today().strftime('%Y%m%d')) # date as int in format [ 20120614 ]
store(tracks, country, today)
