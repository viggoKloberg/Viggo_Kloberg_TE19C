vinkel = float(input("ange en vinkel v i grader, där 0° < v < 360°: "))

if vinkel < 90 and vinkel > 0:
    print("spetsig")
elif vinkel == 90:
    print("rät")
elif vinkel > 90 and vinkel < 180:
    print("trubbig")
else:
    print("varken eller")
    