def vv_to_soil_moisture(img, a=-10.0, b=50.0):
    """
    formula: SM = a * VV + b
    """
    return img.multiply(a).add(b).rename("SoilMoisture")
