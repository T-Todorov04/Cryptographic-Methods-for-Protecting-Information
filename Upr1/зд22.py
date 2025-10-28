import random
allNumbersTOTO= [random.randint(1, 50) for i in range(20000000)]
for i in range(1,50): print("Числото ", i , "се показва ", allNumbersTOTO.count(i), " пъти от ",len(allNumbersTOTO),"; Вероятността е ", round(allNumbersTOTO.count(i)/len(allNumbersTOTO)*100,3),"%")
#Използван език: Python