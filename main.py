"""
Latest eartquake detection data application
MODULARIZATION WITH FUNCTION
"""
import latest_earthquake

if __name__ == "__main__":
    print("Main Application\n")
    # result = latest_earthquake.data_extraction()
    # latest_earthquake.display_data(result)
    earthquake_in_indonesia = latest_earthquake.LatestEarthquakeNews()
    earthquake_in_indonesia.data_extraction()
    earthquake_in_indonesia.display_data()
