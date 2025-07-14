import ee

import ee

def get_s1_vv_image(aoi, start_date, end_date, pass_type='ASCENDING'):
    """Restituisce un'immagine Sentinel-1 VV media"""
    collection = ee.ImageCollection('COPERNICUS/S1_GRD') \
        .filterBounds(aoi) \
        .filterDate(start_date, end_date) \
        .filter(ee.Filter.eq('instrumentMode', 'IW')) \
        .filter(ee.Filter.eq('orbitProperties_pass', pass_type)) \
        .filter(ee.Filter.eq('polarization', 'VV')) \
        .select('VV') \
        .median() \
        .clip(aoi)
    return collection
