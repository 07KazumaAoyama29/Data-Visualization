from pathlib import Path
import json

import plotly.express as px
#--------グラフを描画（レンダリング）する方法をブラウザ表示に設定----------
import plotly.io as pio
pio.renderers.default = 'browser'
#---------------------------------------------------------------------

#データを文字列として読み込み
path = Path("eq_data_30_day_m1.geojson")
contents = path.read_text(encoding="utf-8")
all_eq_data = json.loads(contents)

#データセットにあるすべての地震を調べる
all_eq_dicts = all_eq_data["features"]

mags, lons, lats, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict["properties"]["mag"]
    lon = eq_dict["geometry"]["coordinates"][0]
    lat = eq_dict["geometry"]["coordinates"][1]
    eq_title = eq_dict["properties"]["title"]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    eq_titles.append(eq_title)

title = "世界の地震"
fig = px.scatter_geo(lat = lats, lon = lons, size = mags, title = title,
                     color = mags,
                     color_continuous_scale="Viridis",
                     labels={"color": "マグニチュード"},
                     projection="natural earth",
                     hover_name=eq_titles,
                    )
fig.show()