import json
with open('s:\Downloads\Takeout\Historique des positions\Records.json') as f:
    locations = json.load(f)
    for location in locations["locations"] :
        lat="{:.6f}".format(location["latitudeE7"]*0.0000001)
        lng="{:.6f}".format(location["longitudeE7"]*0.0000001)
        time=location["timestamp"]
        print("<a href=https://www.google.com/maps/place/"+str(lat)+","+str(lng)+">"+time+"</a><br>")