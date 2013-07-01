# shema comme Fiona

import fiona
c = fiona.open('strati2.shp')
c.schema
{'geometry': 'Point', 'properties': {u'DIRECTION': 'int', u'PENDAGE': 'int', u'TYPE': 'str:10'}}


import shapefile
reader = shapefile.Reader('strati2.shp')

def schema(reader):
      properties = dict((d[0],d[1:]) for d in reader.fields[1:])
      return { 'type' : 'Feature',
               'properties' : properties,
               'geometry' : reader.shapes()[1].__geo_interface__['type']}

shapefile.Reader.schema = property(lambda self: schema(self))
reader.schema
{'geometry': 'Point', 'type': 'Feature', 'properties': {'DIRECTION': ['N', 3, 0], 'PENDAGE': ['N', 2, 0], 'TYPE': ['C
', 10, 0]}}

def schema2(reader):
      properties = dict((d[0],d[1:]) for d in reader.fields[1:])
      return {'properties' : properties,
               'geometry' : reader.shapes()[1].__geo_interface__['type']}
               
shapefile.Reader.schema2 = property(lambda self: schema2(self))
               
