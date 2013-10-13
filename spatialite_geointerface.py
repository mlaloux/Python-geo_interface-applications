from pyspatialite import dbapi2 as db
conn = db.connect('test_db.sqlite')
conn.row_factory = db.Row
cur = conn.cursor()

def records(result):
      for i in result:
           atr=dict(zip(i.keys()[:-1],list(i)[:-1]))    
           yield dict(geometry=list(i)[-1],properties=atr)


sql = "SELECT dip_dir,strati,dip, AsGeoJSON(geom) from  point"
rs = cur.execute(sql)
c = records(rs) 
c.next()
{'geometry': u{'type': 'Point', 'coordinates': (161821.09375, 79076.0703125)}, 'id': '0', 'properties': {'dip_dir': 120, 'strati_typ': 1, 'dip': 30}}
