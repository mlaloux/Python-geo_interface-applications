import shapefile
reader= shapefile.Reader("/Users/Shared/Dropbox/coupe_profile/strati2.shp")
elem = reader.shapeRecords()[0]


def mapping_feature(reader,feature):
    properties = {}
    geom = feature.shape.__geo_interface__ 
    fields = reader.fields[1:]  
    fields = [field[0] for field in fields] 
    atr = dict(zip(fields, feature.record))
    return dict(geometry=geom,properties=atr)
    
mapping_feature(reader,elem)
{'geometry': {'type': 'Point', 'coordinates': (272070.600041, 155389.38792000001)}, 'properties': {'DIRECTION': 130, 'PENDAGE': 30, 'TYPE': 'incl'}}

