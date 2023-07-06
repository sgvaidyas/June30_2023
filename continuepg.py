'''for i in range(20):
    #it will skip the iteration where num is completely
    #divisible by 4
    if i%4==0:
        continue
    print(i)
    print("------------")
'''


i=1
while i<20:
    if i%4==0:
        i+=1   #if this is not provided it will go to infinite loop
        continue
    print(i)
    print("-----------")
    i+=1









