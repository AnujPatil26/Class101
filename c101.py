import time
seconds = input("Enter time in seconds ")
def countdown(seconds):
    while seconds > 0:
        mins = int(seconds/60)
        secs = int(seconds%60)
        timer = f'{mins} : {secs}'
        print(timer)
        time.sleep(1)
        seconds-=1
    print("Times Up")

countdown(int(seconds)) 


