num=int(input("enter the number of row:"))
row=0
while row<num:
    var=num-row-1
    while var>0:
        print(end=" ")
        var=var-1
    star=row+1
    while star>0:
        print("*",end=" ")
        star=star-1
    row=row+1
    print()
i = 0
while i <= 5:
    print(' '*i + ('* ')*(5-i))
    i += 1
