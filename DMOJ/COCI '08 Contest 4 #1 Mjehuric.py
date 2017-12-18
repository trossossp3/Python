alist = raw_input('').rstrip()
alist = alist.split(' ')

def bubble (alist):
   # if alist = [1,2,3,4,5]:
       # print alist
    #
        for i in range (0, len(alist) -1):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
print alist    

bubble(alist)
   