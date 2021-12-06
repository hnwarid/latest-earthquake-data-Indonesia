"""
Latest eartquake detection data application
MODULARIZATION WITH FUNCTION
"""
from latest_earthquake import data_extraction, display_data

if __name__ == "__main__":
    print("Main Application")
    result = data_extraction()
    display_data(result)
