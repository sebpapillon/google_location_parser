import datetime
import json
from dateutil import parser

with open('2014_AUGUST.json') as f:
    locations = json.load(f)
    for location in locations["timelineObjects"] :
        if "placeVisit" in location:
            try:
                print(location["placeVisit"]["duration"]["startTimestamp"]
                +" "
                +location["placeVisit"]["location"]["address"])
                print("date is")
                print(parser.parse(location["placeVisit"]["duration"]["startTimestamp"]))
            except:
                print("address is unknown")
                
print(datetime.datetime.utcnow().isoformat())
print(datetime.datetime(2024,8,20))




'''lat="{:.6f}".format(location["latitudeE7"]*0.0000001)
lng="{:.6f}".format(location["longitudeE7"]*0.0000001)
time=location["timestamp"]
print("<a href=https://www.google.com/maps/place/"+str(lat)+","+str(lng)+">"+time+"</a><br>")'''