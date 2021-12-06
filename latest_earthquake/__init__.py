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
    rslt = dict()
    rslt["date"] = "06 Desember 2021"
    rslt["time"] = "09:39:55 WIB"
    rslt["magnitude"] = 4.9
    rslt["location"] = {"ls": 8.72, "bt": 118.36}
    rslt["epicenter"] = "Pusat gempa berada di Laut 23 Km Barat Daya Dompu"
    rslt["observed"] = "Dirasakan (Skala MMI): III Dompu, III Bima"

    return rslt


def display_data(rslt):
    print("Latest earthquake according to BMKG")
    print("Date:", rslt["date"])
    # print(f"Date {rslt["date"]}")
    # #format string method apparently does not work on python 3.8
    print("Time:", rslt["time"])
    print("Magnitude:", rslt["magnitude"])
    print("Location:", "LS =", rslt["location"]["ls"], "BT =", rslt["location"]["bt"])
    print("Epicenter:", rslt["epicenter"])
    print("Observed:", rslt["observed"])
