# my response to http://gis.stackexchange.com/questions/77974/how-to-convert-gml-to-geojson-using-python-and-ogr-with-geometry-transformation/77999#77999

# geo_interface
def records(file):  
    # generator 
    reader = ogr.Open(file)
    layer = reader.GetLayer()
    for i in range(layer.GetFeatureCount()):
        feature = layer.GetFeature(i)
        yield json.loads(feature.ExportToJson())

from osgeo import ogr
elem = records('test.gml')
features = [feat for feat in records("test.gml')]
# creation of the dictionary  
my_layer = {
    "type": "FeatureCollection",
     "features": features}
print my_layer
{'type': 'FeatureCollection', 'features': [{u'geometry': {u'type': u'LineString', u'coordinates': [[-0.95694033573220805, -0.290284677254464], [-0.28378378378378399, 0.33648648648648599], [0.39729729729729701, -0.064864864864864993], [0.99324324324324298, 0.48648648648648701]]}, u'type': u'Feature', u'properties': {u'id': None, u'fid': u'essai.0'}, u'id': 0}, {u'geometry': {u'type': u'LineString', u'coordinates': [[0.51422274119435496, 0.55873852866636098], [0.41724639928901802, 0.392759789636073], [0.32586484633975898, 0.39648964894012401], [0.21583399687024199, 0.366650774507713], [0.219563856174294, 0.30324316633883902]]}, u'type': u'Feature', u'properties': {u'id': None, u'fid': u'essai.1'}, u'id': 1}, {u'geometry': {u'type': u'LineString', u'coordinates': [[-0.37907856212595797, -0.028714311721736999], [-0.22428940100782399, -0.19842291005607601], [-0.10679883293020501, -0.32523812639382399], [-0.034066576501201998, -0.19469305075202401], [0.018151453755517001, -0.142475020495305], [0.083423991576417, -0.20215276936012699]]}, u'type': u'Feature', u'properties': {u'id': None, u'fid': u'essai.2'}, u'id': 2}, {u'geometry': {u'type': u'LineString', u'coordinates': [[-0.58235589419676004, 0.37597542276784202], [-0.37534870282190602, 0.52143993562584701], [-0.23361404926795301, 0.467356975717101], [-0.047121084065381999, 0.40021950824417601], [0.075964272968313998, 0.493465990845461]]}, u'type': u'Feature', u'properties': {u'id': None, u'fid': u'essai.3'}, u'id': 3}]}

import json
# json features
print json.dumps(my_layer)
'{"type": "FeatureCollection",.....

# write the GeoJSON file
with open("test.geojson", "w") as outfile:
    json.dump(my_layer,outfile)
