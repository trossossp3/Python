
inpt = input('enter a number')
def test (n):
    if n is 1: return 1
    elif n is 0: return 1
    else: 
        return test(n-1) + test(n-2)
print(test(inpt))