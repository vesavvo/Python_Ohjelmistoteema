import requests
import config

def output_status(json):
    print ("================================================")
    print ("Trip ID    : " + json["id"])
    print ("Pilot      : " + json["player"])
    print ("Money      : " + str(json["money"]))
    print ("Location   : " + json["location"]["ident"] + " - " + json["location"]["name"])
    print ("Link       : ")
    print ("------------------------------------------------")
    print ("Weather    : " + json["location"]["weather"]["type"])
    print ("Temperature: " + str(json["location"]["weather"]["temperature"]) + "'C")
    print ("Humidity   : " + str(json["location"]["weather"]["humidity"]))
    print ("Wind speed : " + str(json["location"]["weather"]["wind_speed"]))

    print("------------------------------------------------")
    print ("Possible destinations:")
    nearby = json["location"]["nearby_airports"]
    for a in nearby:
        print (a["ident"] + " - " + a["name"])



    print ("================================================")
    return



name = input("Enter your name (default=" + config.default_name + "): ")
if (name==""):
    name = config.default_name
initial_airport = input("Enter initial airport (default="+ config.default_starting_point + "): ")
if (initial_airport==""):
    initial_airport = config.default_starting_point

# http://127.0.0.1:5000/newgame?loc=EFKE&player=Urpopekka
request = "http://127.0.0.1:5000/newgame?loc=" + initial_airport + "&player=" + name

while True:
    print (request)
    response = requests.get(request).json()
    print(response)
    output_status(response)

    default_destination = response["location"]["nearby_airports"][0]["ident"]
    destination = input("Enter next destination (default=" + default_destination + "): ")
    if destination=="":
        destination = default_destination
    print ("Generating flight plan to " + destination)

    # http://127.0.0.1:5000/flyto?game=p5eiPgQPT9jbIt1TlqzH&dest=EFHK
    request = "http://127.0.0.1:5000/newgame?loc=" + initial_airport + "&player=" + name

