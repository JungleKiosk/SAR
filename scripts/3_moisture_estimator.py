def vv_to_soil_moisture(vv_db):
    """
    Converte il valore VV (in dB) in umidità del suolo (% volumetrico).
    Formula empirica da letteratura (adattabile).
    """
    return -4.33 * vv_db - 38.3
