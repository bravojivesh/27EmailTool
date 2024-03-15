list=[1,2,3,4,5]
x=iter(list)
# y=next(x) #this will store the first element in the iterator

for _ in range(len(list)):
    print (x)
    print(next(x)) #Since the first element has already been called, "y=next(x)", this line
    #will print 2 and up.
    #if the line y=next(x) is commented, it will be 1,2,3,4,5
    # y is not the same as next(x). y will always store the first element in the iterator.