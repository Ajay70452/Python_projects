import time

def countDown(t):
    print("Wanna use a stopwatch?")


    while t:
        mins, secs = divmod(t,60)
        timer = "{:02d}:{:02d}".format(mins,secs)
        print(timer)
        time.sleep(1)
        t = t-1

t = int(input("Enter time in seconds : "))

countDown(t)


