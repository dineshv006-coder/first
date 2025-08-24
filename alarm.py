import datetime
import time

alarm = int(input("Enter how many minitues of break you want :"))
studytime = int(input("Specify how many minutes you will study: "))
st = int(input("Enter how many time you do this :"))

end = 1
while  end < st+1 :
    startingtime = datetime.datetime.now()
    print(f"\nYour {end }study session is started ")
    print("You Started at :",startingtime)

    time.sleep(studytime*60)
    print("Time to Take a break 5 Minitues!")
    time.sleep(alarm*60)
    print("Your break time is completed")

    again_startingtime = datetime.datetime.now()
    print("It's time for study ", again_startingtime)
    
    end += 1
    
    
print("Your Study time is over ... ")
