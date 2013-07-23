# simple

import shapefile

# read the shapefile
reader = shapefile.Reader("strati.shp")
fields = reader.fields[1:]
field_names = [field[0] for field in fields]
buffer = []
for sr in reader.shapeRecords():
     atr = dict(zip(field_names, sr.record))
     geom = sr.shape.__geo_interface__
     buffer.append(dict(type="Feature", geometry=geom, properties=atr))

# write the GeoJSON file
from json import dumps
geojson = open("pyshp-demo.json", "w")
geojson.write(dumps({"type": "FeatureCollection","features": buffer}, indent=2) + "\n")
geojson.close()


# with coroutines

from json import dumps
    
def coroutine(func):
     def start(*args,**kwargs): 
         cr = func(*args,**kwargs) 
         cr.next() 
         return cr 
     return start
     
def pipe(source, following):
     for elem in source:
          following.send(elem)
          following.close()
         
@coroutine
def writer(fileobj):
     buffer = []
     try:
          while True:
               result = (yield)
               buffer.append(result)
     except GeneratorExit:
          fileobj.write(dumps({"type": "FeatureCollection","features": buffer}, indent=2) + "\n")
          fileobj.close()

def records(filename):
     # generator
     reader = shapefile.Reader(filename)
     fields = reader.fields[1:]
     field_names = [field[0] for field in fields]
     for sr in reader.shapeRecords():
         atr = dict(zip(field_names, sr.record))
         geom = sr.shape.__geo_interface__
         yield dict(type="Feature", geometry=geom, properties=atr)
         
import shapefile
a = records("strati.shp")
pipe(a,writer(open("pyshp-demo.json", "w")))




