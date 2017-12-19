def bubbleSort(alist):
    for i in range(len(alist)-1,0,-1):
        for i in range(i):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                print ' '.join(alist)
            
alist = raw_input('').rstrip()
alist = alist.split(' ')

bubbleSort(alist)


