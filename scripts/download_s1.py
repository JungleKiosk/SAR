import ee

def get_s1_vv_image(aoi, start_date, end_date):
    collection = ee.ImageCollection("COPERNICUS/S1_GRD") \
        .filterBounds(aoi) \
        .filterDate(start_date, end_date) \
        .filter(ee.Filter.eq('instrumentMode', 'IW')) \
        .filter(ee.Filter.listContains('transmitterReceiverPolarisation', 'VV')) \
        .filter(ee.Filter.eq('orbitProperties_pass', 'DESCENDING')) \
        .select('VV')
    
    return collection.mean()
