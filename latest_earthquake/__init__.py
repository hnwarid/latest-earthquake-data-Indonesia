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
        print(content.text)
        # soup = BeautifulSoup(content)
        # print(soup.prettify())
        rslt = dict()
        rslt["date"] = "06 Desember 2021"
        rslt["time"] = "09:39:55 WIB"
        rslt["magnitude"] = 4.9
        rslt["location"] = {"ls": 8.72, "bt": 118.36}
        rslt["epicenter"] = "Pusat gempa berada di Laut 23 Km Barat Daya Dompu"
        rslt["observed"] = "Dirasakan (Skala MMI): III Dompu, III Bima"
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
    print("Location:", "LS =", rslt["location"]["ls"], "BT =", rslt["location"]["bt"])
    print("Epicenter:", rslt["epicenter"])
    print("Observed:", rslt["observed"])
    # print(f"Date {rslt["date"]}")
    # #format string method apparently does not work on python 3.8
    # to do: try using Python 3.9 and change the string concatenation using the string format method


if __name__ == "__main__":
    print("Test. \nThis is a latest earthquake data package")
