import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import os
class CovidData:
    """
    getting the covid 19 real time data from:
    url: https://www.nicd.ac.za/covid-19/ 
    * using webscraping with bs4 and requests modules
    """
    def __init__(self) -> None:
        # the url for the covid data
        self.url = "https://www.nicd.ac.za/covid-19/"
        self.html = requests.get(self.url)
        # get the content of the page and start scrapping
        self.soup = bs(self.html.content, 'html.parser')
        # find all the table rows and grab their data
        self.trs = self.soup.find_all("tr")
        self.df = pd.read_csv(os.path.join(os.getcwd(), "files/SouthAfricanCities.csv"), encoding='latin-1')
    
    def get_provinces_coords(self, apply_filter_on_unknown:bool =False)-> list:
        """
        get a dictionary of provinces with their long and lat coords
        """
        province_lat_long = list()
        for p in self.df.ProvinceName.unique():
            if not p in province_lat_long:
                province_lat_long.append({
                    "lat": self.df.loc[self.df.ProvinceName == p].iloc[0].Latitude,
                    "province": "KWA ZULU-NATAL" if p.upper() == "KWAZULU NATAL" else p.upper(),
                    "long": self.df.loc[self.df.ProvinceName == p].iloc[0].Longitude
                })
        return province_lat_long if not apply_filter_on_unknown else  list(filter(lambda x: x[0] != "UNALLOCATED" or x[0] == ["TOTAL"], province_lat_long))

    def __call__(self)->list:
        print("loading real time data...")
        data = []
        for index, tr in enumerate(self.trs):
            inner_soup = bs(str(tr),'html.parser')
            tds = inner_soup.find_all("td")
            if index == 0:
                tds = [td.string for td in tds]
                tds.extend(["LATITUDE", "LONGITUDE"])
                data.append(tds)
            else:
                tds = [td.string for td in tds]
                for l in self.get_provinces_coords():
                    if l["province"] == tds[0]:
                        tds.extend([j for j in l.values() if j != tds[0]])
                data.append(tds)
        print("done loading real time data...")
        return data