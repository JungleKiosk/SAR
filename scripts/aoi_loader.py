import geopandas as gpd
import ee

def load_shapefile(filepath):
    gdf = gpd.read_file(filepath).to_crs(epsg=4326)  # Convert to WGS84
    geom = gdf.geometry.unary_union  # Combine geometries
    return ee.Geometry(geom.__geo_interface__)