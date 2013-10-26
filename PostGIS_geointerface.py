# for PostGIS version < 9
import psycopg2
import psycopg2.extras
from json import loads
def records(result):
      for i in result:
           atr=dict(zip(i.keys()[:-1],list(i)[:-1]))
           yield dict(geometry=loads(list(i)[-1]),properties=atr)

conn = psycopg2.connect("dbname='testpostgis'host='localhost' user='me'",cursor_factory=psycopg2.extras.DictCursor)
cur = conn.cursor()
sql = """SELECT "dip_dir","strati","dip", ST_AsGeoJSON(the_geom) from from point;"""
cur.execute(sql)
c = records(cur.fetchall())
c.next()
{'geometry': {u'type': u'Point', u'coordinates': [161821.09375, 79076.0703125]}, 'properties': {'dip_dir': 120, 'strati_typ': 1, 'dip': 30}}

