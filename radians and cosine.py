import math

print "This program will return a given angle's radian-equivalent measurement and cosine."

done=False
while not done:
  i = input("input number of degrees: ")
  
  numRadians = i/180*math.pi
  cos = math.cos(numRadians)
  
  print "radians =",numRadians
  print "cos(theta) =",cos
  
  checkDone = raw_input("Press enter to restart. Type anything to quit: ")
  if len(checkDone) > 0:
    done = True
