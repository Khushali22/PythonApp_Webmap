import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat= list(data["LAT"])
lon= list(data["LON"])
elev = list(data["ELEV"])
#name = list(data["NAME"])

#html = """
#Volcano name:<br>
#<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
#Height: %s m
#"""
def color_producer(el):
    if(el>0 and el<=2000):
        return "green"
    elif(el>2000 and el<=4000):
        return "red"
    else:
        return "blue"
map = folium.Map(location=[21.838178,73.718925],zoom_start=6, tiles="Mapbox Bright")

fgv=folium.FeatureGroup(name="Volcanoes")
fgp=folium.FeatureGroup(name="population")
fgp.add_child(folium.GeoJson(data=open('world.json','r', encoding='utf-8-sig').read(),style_function=lambda x: {'fillColor':'yellow'
if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] <20000000
else 'red'}))
for lt,ln,el in zip(lat,lon,elev):
    #iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fgv.add_child(folium.CircleMarker(location=[lt,ln], radius=6, popup=folium.Popup(str(el)+" m"),
    fill_color=color_producer(el),color='grey', fill_opacity=0.7))
#fg.add_child(folium.Marker(location=[20.5,72.5], popup="Hi, I am a Marker", icon=folium.Icon(color='green')))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")
