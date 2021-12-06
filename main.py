"""
Latest eartquake detection data application
MODULARIZATION WITH FUNCTION
"""
import latest_earthquake

if __name__ == "__main__":
    print("Main Application")
    result = latest_earthquake.data_extraction()
    latest_earthquake.display_data(result)
