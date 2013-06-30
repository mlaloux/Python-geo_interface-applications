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
