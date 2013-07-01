# shema comme Fiona


import fiona
c = fiona.open('strati2.shp')
c.schema
{'geometry': 'Point', 'properties': {u'DIRECTION': 'int', u'PENDAGE': 'int', u'TYPE': 'str:10'}}




import shapefile
reader = shapefile.Reader('strati2.shp')
def schema(sf):
   return dict(geometry=sf.shapes()[1].__geo_interface__['type'], properties=sf.fields[1:])

print schema(reader)
{'geometry': 'Point', 'properties': [['PENDAGE', 'N', 2, 0], ['DIRECTION', 'N', 3, 0], ['TYPE', 'C', 10, 0]]}


def schema2(layer):
   tt = dict()
   tt['geometry'] = reader.shapes()[1].__geo_interface__['type']
   tt['properties'] =dict((d[0],d[1:]) for d in reader.fields[1:])
   return tt

schema2(reader)
{'geometry': 'Point', 'properties': {'DIRECTION': ['N', 3, 0], 'PENDAGE': ['N', 2, 0], 'TYPE': ['C', 10, 0]}}
