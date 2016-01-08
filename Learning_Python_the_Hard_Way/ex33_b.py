def list_append(size):
    i = 0
    nums = []
    while i < size:
        print "At the top i is %d" % i
        nums.append(i)
    
        i = i + 1
        print "Numbers now:", nums
        print "At the bottom i is %d" % i
    return nums   
    
size = int(raw_input("size: "))
numbers = list_append(size)

print "The numbers: "

for num in numbers:
    print num
