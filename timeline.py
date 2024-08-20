import datetime
import json
from dateutil import parser
import sys

with open(sys.argv[1]) as f:
    locations = json.load(f)
    for location in locations["timelineObjects"] :
        if "placeVisit" in location:
            try:
                print(str(parser.parse(location["placeVisit"]["duration"]["startTimestamp"]).strftime('%d/%m/%Y-%H:%M'))
                +" "
                +location["placeVisit"]["location"]["address"])
                
            except Exception as e:
                print(e)
                




'''lat="{:.6f}".format(location["latitudeE7"]*0.0000001)
lng="{:.6f}".format(location["longitudeE7"]*0.0000001)
time=location["timestamp"]
print("<a href=https://www.google.com/maps/place/"+str(lat)+","+str(lng)+">"+time+"</a><br>")'''
