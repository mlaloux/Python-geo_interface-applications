Python Geo_interface applications
=================================

The __geo_interface__  (GeoJSON-like) protocol was  proposed by [Sean Gillies](https://gist.github.com/2217756) and can be used in Python with:

* [**Shapely**](https://github.com/Toblerity/Shapely)
* [**Fiona**](https://github.com/Toblerity/Fiona)
* [**descartes**](https://bitbucket.org/sgillies/descartes/)
* [**geojson**](https://github.com/sgillies/geojson)
* [**osgeo.ogr**](http://www.gdal.org/ogr/classOGRGeometry.html#a28609fce6bd422b16182eab58ff4e812)
* [**pygeoif**](https://github.com/cleder/pygeoif)
* [**PySAL**](http://pythonhosted.org/PySAL/users/tutorials/shapely.html?highlight=geojson)
* [**ArcPy**](http://gis.stackexchange.com/questions/10201/arcpy-geometry-geo-interface-and-asshape-function-loss)
* [**Papyrus**](https://papyrus.readthedocs.org/en/master/creating_mapfish_views.html)
* [**PyShp**](https://pypi.python.org/pypi/pyshp/1.1.7), implemented since version 1.1.7  by Christian Lederman (https://github.com/cleder/pyshp)  
* Karim Bahgat has created a tempory fork of PyShp that can write new shapes based on geoJSON:
[**Pyshp-fork-speedup-and-geojson-write**](https://github.com/karimbahgat/Pyshp-fork-speedup-and-geojson-write)
* [**QGIS**](http://www.qgis.org/) with the new API with [monkey patching]( http://nathanw.net/2013/06/25/qgis-geo-interface/) by Nathan Woodrow or with generators in [GeoJSON, nouveau lingua franca en géomatique ?](https://portailsig.org/content/geojson-nouveau-lingua-franca-en-geomatique.html) by Martin Laloux
* [**mapnik**](http://mapnik.org/)  implemented by Dane Springmeyer 
* [**rasterstats**](https://github.com/perrygeo/python-raster-stats)
* [**SpatiaLite**](http://www.gaia-gis.it/gaia-sins/) implemented here
* [**PostGIS**](http://postgis.net/) implemented here
* [**GeoDjango**](https://docs.djangoproject.com/en/dev/ref/contrib/gis/geos/)
* [**pygml**](https://pypi.org/project/pygml/)
* [**geodaisy**](https://pypi.org/project/geodaisy/)



Applications
-------------

One big advantage of the protocol is its ability to quickly examine the contents of a shapefile as dictionaries:

### with Fiona:

```python

    >>> import fiona   
    >>> f = fiona.open('point.shp')  
    >>> f.next()  
    {'geometry': {'type': 'Point', 'coordinates': (161821.09375, 79076.0703125)}, 'id': '0', 'properties': {u'DIP_DIR': 120, u'STRATI_TYP': 1, u'DIP': 30}}
    >>> f.next()['geometry']['coordinates']  
    (161485.09375, 79272.34375)  
    >>> f.next()['properties']['DIP']  
    55  
```
    
### with PyShp:

```python

    def records(filename):  
        # generator 
        reader = shapefile.Reader(filename)  
        fields = reader.fields[1:]  
        field_names = [field[0] for field in fields]  
        for sr in reader.shapeRecords():  
            geom = sr.shape.__geo_interface__  
            atr = dict(zip(field_names, sr.record))  
            yield dict(geometry=geom,properties=atr)    
        

    >>> import shapefile
    >>> a = records('point.shp')
    >>> a.next()
    {'geometry': {'type': 'Point', 'coordinates': (161821.09375, 79076.0703125)}, 'properties': {'DIP_DIR': 120, 'STRATI_TYP': 1, 'DIP': 30}}
    >>> a.next()['geometry']['coordinates']
    (161485.09375, 79272.34375)
    >>> a.next()['properties']['DIP']
    55
    
```

### with osgeo.ogr

```python

    def records(file):  
        # generator 
        reader = ogr.Open(file)
        layer = reader.GetLayer(0)
        for i in range(layer.GetFeatureCount()):
            feature = layer.GetFeature(i)
            yield json.loads(feature.ExportToJson())
            
    >>> from osgeo import ogr
    >>> a = records('point.shp')
    >>> a.next()
    {'geometry': {'type': 'Point', 'coordinates': (161821.09375, 79076.0703125)}, 'properties': {'DIP_DIR': 120, 'STRATI_TYP': 1, 'DIP': 30}}
```   

### with PyQGIS API2:   

```python

    layer = qgis.utils.iface.activeLayer()  
    def records(layer):  
        fields = layer.pendingFields()   
        field_names = [field.name() for field in fields]   
        for elem in layer.getFeatures():  
              geom= elem.geometry()  
              atr = dict(zip(field_names, elem.attributes()))  
              yield dict(geometry=geom.exportToGeoJSON(),properties=atr)  
              
    c = records(layer) 
    c.next() 
    {'geometry': {'type': 'Point', 'coordinates': (161821.09375, 79076.0703125)}, 'id': '0', 'properties': {u'DIP_DIR': 120, u'STRATI_TYP': 1, u'DIP': 30}}
```    

### conversion to shapely or pygeoif geometry

with **shapely** (Sean Gillies, as with **pygeoif** of Christian Lederman):

```python

    >>> from shapely.geometry import shape    
    >>> a = records('point.shp') 
    >>> print shape( a.next()['geometry'])
    POINT (161821.09375 79076.0703125)
```
