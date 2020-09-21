import random as rnd
poäng = rnd.randint (0,65)
klass = ["me","myself","I"]
if (poäng > 60):
    betyg = "A"
elif (poäng >=56):
    betyg = "B"
elif (poäng >= 51):
    betyg = "C"
elif (poäng >= 41):
    betyg = "D"
elif (poäng >= 31):
    betyg = "E"
else:
    betyg = "F"
elev = rnd.choice(klass)
print(f"eleven {elev} fick {poäng} poäng och betyget {betyg}")