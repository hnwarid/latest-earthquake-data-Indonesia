import requests
from bs4 import BeautifulSoup


def data_extraction():
    """
    This package scrapes the latest earthquake data from BMKG Indonesia website
    Requires: BeautifulSoup4 and Requests
    Example data shown:
    Date: 06 Desember 2021
    Time: 09:39:55 WIB
    Magnitude: 4.9
    Depth: 10 km
    Location: LS = 8.72 LS BT = 118.36 BT
    Epicenter: Pusat gempa berada di Laut 23 Km Barat Daya Dompu
    Observed: Dirasakan (Skala MMI): III Dompu, III Bima
    """
    try:
        content = requests.get("https://bmkg.go.id")
    except Exception:
        return None

    if content.status_code == 200:
        soup = BeautifulSoup(content.text, "html.parser")
        latest_datetime = soup.find("span", {"class": "waktu"})
        latest_datetime = latest_datetime.text.split(", ")
        latest_date = latest_datetime[0]
        latest_time = latest_datetime[1]

        earthquake_data = soup.find("div", {"class": "col-md-6 col-xs-6 gempabumi-detail no-padding"})
        earthquake_data = earthquake_data.findChildren("li")
        i = 0
        latest_magnitude = None
        latest_depth = None
        latest_location = None
        latest_epicenter = None
        latest_observed = None
        for li in earthquake_data:
            if i == 1:
                latest_magnitude = li.text
            elif i == 2:
                latest_depth = li.text
            elif i == 3:
                latest_location = li.text.split(" - ")
            elif i == 4:
                latest_epicenter = li.text
            elif i == 5:
                latest_observed = li.text
            i += 1

        result = dict()
        result["date"] = latest_date
        result["time"] = latest_time
        result["magnitude"] = latest_magnitude
        result["depth"] = latest_depth
        result["location"] = latest_location
        result["epicenter"] = latest_epicenter
        result["observed"] = latest_observed
        return result
    else:
        return None


def display_data(result):
    if result is None:
        print("cannot find the latest earthquake data")
        return

    print("Latest earthquake according to BMKG")
    print("Date:", result["date"])
    print("Time:", result["time"])
    print("Magnitude:", result["magnitude"])
    print("Depth:", result["depth"])
    print("Location:", "LS =", result["location"][0], "BT =", result["location"][1])
    print("Epicenter:", result["epicenter"])
    print("Observed:", result["observed"])
    # print(f"Date {rslt["date"]}")
    # #format string method apparently does not work on python 3.8
    # to do: try using Python 3.9 and change the string concatenation with the string format method


if __name__ == "__main__":
    print("Test. \nThis is a latest earthquake data package")
    # Using the lines below this file will work on its own:
    # result = data_extraction()
    # display_data(result)
