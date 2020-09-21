gånger = float(input("hur många gånger har du åkt buss denna månaden?"))
kostnad = gånger*30
if kostnad > 775:
    print(f"Det kostar {kostnad}kr, det är värt det att köpa månadskort")
else:
    print(f"Det kostar {kostnad}kr, det är inte värt det att köpa månadskort")