light = input("type colour of light = Red ,Yellow , Green = ")
speed = float(input("type the speed of vehicels = "))

if ((light == "Red") and (0 < speed < 10)):
    print("Good - Wait turn light into Green")
elif ((light == "Red") and (speed > 10)):
     print("Alert XXX - Stop your card - Light is red")
elif ((light == "Yellow") and (0 < speed < 10)):
     print("ready to move ")
elif ((light == "Yellow") and (speed > 10)):
     print("Low Your speed - Wait to light turn into green")

elif ((light == "Green") and (speed < 10)):
     print("Good - Safe jpourney")

elif ((light == "Green") and (speed > 10)):
     print("Please go slow")