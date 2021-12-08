import requests
from bs4 import BeautifulSoup


def data_extraction():
    """
    Date: 06 Desember 2021
    Time: 09:39:55 WIB
    Magnitude: 4.9
    Depth: 10 km
    Location: LS=8.72 BT=118.36
    Epicenter: Pusat gempa berada di Laut 23 Km Barat Daya Dompu
    Observed: Dirasakan (Skala MMI): III Dompu, III Bima
    :return:
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
        result = soup.find("div", {"class": "col-md-6 col-xs-6 gempabumi-detail no-padding"})
        result = result.findChildren("li")
        i = 0
        latest_magnitude = None
        latest_depth = None
        latest_location = None
        latest_epicenter = None
        latest_observed = None
        for li in result:
            if i == 1:
                latest_magnitude = li.text
            elif i == 2:
                latest_depth = li.text
            elif i == 3:
                latest_location = li.text.split(" - ")
            elif i == 4:
                latest_epicenter = li.text
            elif i ==5:
                latest_observed = li.text
            i += 1

        # latest_magnitude = soup.find("span", {"class": "ic magnitudo"})
        # latest_magnitude = latest_magnitude.text
        # latest_location = soup.find("span", {"class": "ic koordinat"})

        rslt = dict()
        rslt["date"] = latest_date  # "06 Desember 2021"
        rslt["time"] = latest_time  # "09:39:55 WIB"
        rslt["magnitude"] = latest_magnitude  # 4.9
        rslt["depth"] = latest_depth  # 7.0
        rslt["location"] = latest_location  # {"ls": 8.72, "bt": 118.36}
        rslt["epicenter"] = latest_epicenter  # "Pusat gempa berada di Laut 23 Km Barat Daya Dompu"
        rslt["observed"] = latest_observed  # "Dirasakan (Skala MMI): III Dompu, III Bima"
        return rslt
    else:
        return None


def display_data(rslt):
    if rslt is None:
        print("cannot find the latest earthquake data")
        return

    print("Latest earthquake according to BMKG")
    print("Date:", rslt["date"])
    print("Time:", rslt["time"])
    print("Magnitude:", rslt["magnitude"])
    print("Depth:", rslt["depth"])
    print("Location:", "LS:", rslt["location"][0], "BT =", rslt["location"][1])
    print("Epicenter:", rslt["epicenter"])
    print("Observed:", rslt["observed"])
    # print(f"Date {rslt["date"]}")
    # #format string method apparently does not work on python 3.8
    # to do: try using Python 3.9 and change the string concatenation using the string format method


if __name__ == "__main__":
    print("Test. \nThis is a latest earthquake data package")
