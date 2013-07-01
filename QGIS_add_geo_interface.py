# modified from Nathan Woodrow's [Adding __geo_interface__ to QGIS geometry and feature ](http://nathanw.net/2013/06/25/qgis-geo-interface/)
# avoid the usage of eval. It is better to use json.loads() to parse JSON Data into dictionary.


import json

def mapping_feature(feature):
    geom = feature.geometry()
    properties = {}
    fields = [field.name() for field in feature.fields()]
    properties = dict(zip(fields, feature.attributes()))
    return { 'type' : 'Feature',
             'properties' : properties,
             'geometry' : geom.__geo_interface__}

def mapping_geometry(geometry):
    geo = geometry.exportToGeoJSON()
    # not eval as Nathan Woodrow but json.loads()
    return json.loads(geo)

QgsFeature.__geo_interface__ = property(lambda self: mapping_feature(self))
QgsGeometry.__geo_interface__ = property(lambda self: mapping_geometry(self))

layer = iface.activeLayer()
f = layer.selectedFeatures()[0]
f
<qgis.core.QgsFeature object at 0x0D70B8E8>
f.__geo_interface__
{'geometry': {u'type': u'Point', u'coordinates': [271066.032148, 154475.631377]}, 'type': 'Feature', 'properties': {u'DIRECTION': 145, u'PENDAGE': 55, u'TYPE': u'incl'}}

dict((field.name(),{field.typeName():field.length()}) for field in layer.pendingFields() )
{u'DIRECTION': {u'Integer': 3}, u'PENDAGE': {u'Integer': 2}, u'TYPE': {u'String': 10}}
# problème avec les real (10:2) exemple
layer.type()
0 # = point
