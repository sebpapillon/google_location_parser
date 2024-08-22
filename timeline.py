#!/usr/bin/env python
import datetime
import json
from dateutil import parser
import sys
from lat_lon_parser import parse

with open(sys.argv[1]) as f:
    index=0
    locations = json.load(f)
    for location in locations["timelineObjects"] :
        if "placeVisit" in location:
            try:
                print("visit")
                print(str(parser.parse(location["placeVisit"]["duration"]["startTimestamp"]).strftime('%d/%m/%Y-%H:%M'))
                +" - " 
                +str(parser.parse(location["placeVisit"]["duration"]["endTimestamp"]).strftime('%d/%m/%Y-%H:%M'))
                +" "
                +location["placeVisit"]["location"]["address"])
                print()
                
            except Exception as e:
                print(e)
        
        if "activitySegment" in location:
            try:
                print("activity")
                print(str(parser.parse(location["activitySegment"]["duration"]["startTimestamp"]).strftime('%d/%m/%Y-%H:%M'))
                +" - " 
                +str(parser.parse(location["activitySegment"]["duration"]["endTimestamp"]).strftime('%d/%m/%Y-%H:%M')))
                for point in location["activitySegment"]["waypointPath"]["waypoints"]:
                    print("{:.6f}".format(point["latE7"]*0.0000001)+" "+"{:.6f}".format(point["lngE7"]*0.0000001))
                    print(parse("{:.6f}".format(point["latE7"]*0.0000001)))
            except Exception as e:
                print("exception with "+str(e)+" at index "+str(index))
            print()
        
        index+=1




'''lat="{:.6f}".format(location["latitudeE7"]*0.0000001)
lng="{:.6f}".format(location["longitudeE7"]*0.0000001)
time=location["timestamp"]
print("<a href=https://www.google.com/maps/place/"+str(lat)+","+str(lng)+">"+time+"</a><br>")'''
