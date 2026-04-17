import numpy as np
from scipy.stats import norm

def inventory_calc(forecast, std, lead_time=7, service_level=0.95):
    """
    Calculate Safety Stock and Reorder Point
    """

    # Z-score based on service level
    z = norm.ppf(service_level)

    # Demand during lead time
    demand_lead_time = forecast[:lead_time].sum()

    # Safety Stock
    safety_stock = z * std * np.sqrt(lead_time)

    # Reorder Point
    reorder_point = demand_lead_time + safety_stock

    return safety_stock, reorder_point