lines = [line.strip() for line in open('test.txt')]
count=0
m=0
for items in lines:
    count+=1
    print items.replace("$m",str(m))
    if count%18 ==0:
        m+=1
        #print m
    #print count
