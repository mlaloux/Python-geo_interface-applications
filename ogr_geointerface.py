def records(shapefile):  
    # generator 
    reader = ogr.Open(shapefile)
    layer = reader.GetLayer(0)
    for i in range(layer.GetFeatureCount()):
        feature = layer.GetFeature(i)
        yield json.loads(featurel.ExportToJson())

>>> from osgeo import ogr
>>> a = records('point.shp')
>>> a.next()
{'geometry': {'type': 'Point', 'coordinates': (161821.09375, 79076.0703125)}, 'properties': {'DIP_DIR': 120, 'STRATI_TYP': 1, 'DIP': 30}}
