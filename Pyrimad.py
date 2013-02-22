splitmin=input("please enter the minutes of your 2K split ")
splitsec=input("please enter the seconds of your 2K split ")
heart=input("please enter your maximum heartrate or if not known enter 1 ")
if heart==1:
    EstHeart=input("Please enter your age ")
    heart=220-EstHeart
splittot=splitmin*60+splitsec
import time
n=time.clock()
minute=60
z1max=.67
z1add=24
z2add=18
z2max=.74
z3max=.87
z1=minute*5
z2=minute*4
z3=minute*3
z4=minute*2
z5=minute*1
splitzoneone=splitsec+z1add
print ("Hold "+str(splitmin)+":"+str(splitzoneone)+" ")
print "hold your heart rate at "+str(heart*z1max)
time.sleep(z1)
splitzoneone=splitsec+z2add
print ("Hold "+str(splitmin)+":"+str(splitzoneone)+" ")
print "hold your heart rate at "+str(heart*z2max)
time.sleep(z2)
splitzoneone=splitsec+z1add
print ("Hold "+str(splitmin)+":"+str(splitzoneone)+" ")
print "hold your heart rate at "+str(heart*z1max)
time.sleep(z3)
splitzoneone=splitsec+z2add
print ("Hold "+str(splitmin)+":"+str(splitzoneone)+" ")
print "hold your heart rate at "+str(heart*z2max)
time.sleep(z4)
splitzoneone=splitsec+8
print ("Hold "+str(splitmin)+":"+str(splitzoneone)+" ")
print "hold your heart rate at "+str(heart*z3max)
time.sleep(z5)
splitzoneone=splitsec+z2add
print ("Hold "+str(splitmin)+":"+str(splitzoneone)+" ")
print "hold your heart rate at "+str(heart*z2max)
time.sleep(z4)
splitzoneone=splitsec+z1add
print ("Hold "+str(splitmin)+":"+str(splitzoneone)+" ")
print "hold your heart rate at "+str(heart*z1max)
time.sleep(z3)
splitzoneone=splitsec+z2add
print ("Hold "+str(splitmin)+":"+str(splitzoneone)+" ")
print "hold your heart rate at "+str(heart*z2max)
time.sleep(z2)
splitzoneone=splitsec+z1add
print ("Hold "+str(splitmin)+":"+str(splitzoneone)+" ")
print "hold your heart rate at "+str(heart*z1max)
time.sleep(z1)
print"rest"
time.sleep(z3)
splitzoneone=splitsec+z1add
print ("Hold "+str(splitmin)+":"+str(splitzoneone)+" ")
print "hold your heart rate at "+str(heart*z1max)
time.sleep(z1)
splitzoneone=splitsec+z2add
print ("Hold "+str(splitmin)+":"+str(splitzoneone)+" ")
print "hold your heart rate at "+str(heart*z2max)
time.sleep(z2)
splitzoneone=splitsec+z1add
print ("Hold "+str(splitmin)+":"+str(splitzoneone)+" ")
print "hold your heart rate at "+str(heart*z1max)
time.sleep(z3)
splitzoneone=splitsec+z2add
print ("Hold "+str(splitmin)+":"+str(splitzoneone)+" ")
print "hold your heart rate at "+str(heart*z2max)
time.sleep(z4)
splitzoneone=splitsec+8
print ("Hold "+str(splitmin)+":"+str(splitzoneone)+" ")
print "hold your heart rate at "+str(heart*z3max)
time.sleep(z5)
splitzoneone=splitsec+z2add
print ("Hold "+str(splitmin)+":"+str(splitzoneone)+" ")
print "hold your heart rate at "+str(heart*z2max)
time.sleep(z4)
splitzoneone=splitsec+z1add
print ("Hold "+str(splitmin)+":"+str(splitzoneone)+" ")
print "hold your heart rate at "+str(heart*z1max)
time.sleep(z3)
splitzoneone=splitsec+z2add
print ("Hold "+str(splitmin)+":"+str(splitzoneone)+" ")
print "hold your heart rate at "+str(heart*z2max)
time.sleep(z2)
splitzoneone=splitsec+z1add
print ("Hold "+str(splitmin)+":"+str(splitzoneone)+" ")
print "hold your heart rate at "+str(heart*z1max)
time.sleep(z1)
print"rest"
time.sleep(z3)
print "done"