import time

light = "RED"

if light == "RED":
    print("RED- Stop")
time.sleep(4)
light = "RED + AMBER"

if light == "RED + AMBER":
    print("RED + AMBER- Slow down")
time.sleep(2)
light = "AMBER"

if light == "AMBER":
    print("AMBER- Get ready")
time.sleep(3)
light = "GREEN"

if light == "GREEN":
    print("GREEN- Go")
time.sleep(3)
light = "AMBER"

if light == "AMBER":
    print("AMBER- Prepare to stop")
time.sleep(2)

