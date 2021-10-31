from flask import Flask, render_template
import numpy as np
import pandas as pd 
import folium
from dataset import CovidData
# Reading the dataframe
df = pd.read_csv("./files/covid-19-dataset-1.csv")

za_df = df.loc[df.Country_Region == "South Africa"]
za_lat = -30.559989
za_long = 22.937508

covid = CovidData()

markers_data = covid()[1:-2]
stats_data = [i[:-2] if len(i) > 4 else i for i in covid() ]

za_map = folium.Map(location=[za_lat, za_long], zoom_start=6)
def circle_maker(x):
    pass

for index, marker in enumerate(markers_data):
    colors = ["green", "purple", "yellow", "lightseagreen", "cornflowerblue", "pink", "YlGn", "brown", "black"]
    color = colors[index]

    html = f"""
    <body style="background-color: black;padding:0; ">
    <b style="color: white;">{marker[0]}</b>
    <p style="color: white;">confirmed: {marker[1]}</p>
    <p style="color: white;">deaths: {marker[2]}</p>
    <p style="color: white;">recoveries: {marker[3]}</p>
    </body>
    """
    iframe = folium.IFrame(html,
                       width=200 , height=160)
    popup = folium.Popup(iframe)
    folium.Marker(
        location=[*marker[-2:]],
        popup=popup,
        tooltip = f"show cases in {str(marker[0]).capitalize()} ",
        icon=folium.Icon(color=color, icon="info-sign"),
        color= color
    ).add_to(za_map)

html_map=za_map._repr_html_()

app = Flask(__name__)
app.config.from_object("config.Development")


@app.route('/', methods=["GET", "POST"])
def home():
    return render_template("html/index.html", cmap=html_map, data=stats_data)

if __name__ == "__main__":
    app.run(port=3000)
