import mapnik

# NOTE: works with >= Mapnik 2.3.x
# Geo interface added in 2.3.0: https://github.com/mapnik/mapnik/issues/2009

# Example 1: access the geometry from a feature
context = mapnik.Context()
feature = mapnik.Feature(context,1)
feature.add_geometries_from_wkt('POINT (0 0)')
print feature.__geo_interface__['geometry']

# Example 2: access the geometry directly from the mapnik.Path container
# first, lets make a multipoint geometry by adding another WKT
feature.add_geometries_from_wkt('POINT (1 1)')
paths = feature.geometries()
print paths.__geo_interface__

def print_featureset(fs):
	feat = fs.next()
	while (feat):
	    print feat.__geo_interface__
	    try:
	        feat = fs.next()
	    except StopIteration:
	        feat = None

# Example 3:  access via an inline Geo-CSV
csv = '''
id,wkt
1,"POINT(0 0)"
2,"POINT(1 1)"
'''
datasource = mapnik.Datasource(**{'type':'csv','inline':csv})
query = mapnik.Query(datasource.envelope())
fs = datasource.features(query)
print_featureset(fs)


# Example 3:  access via a shapefile
# uncomment and fix the path to point to a valid shapefile
#datasource = mapnik.Datasource(**{'type':'shape','file':'some/path/to/shapefile.shp'})
#query = mapnik.Query(datasource.envelope())
#print_featureset(datasource.features(query))
