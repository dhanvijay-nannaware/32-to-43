# num=int(input("enter the number of row:"))
# row=0
# while row<num:
#     var=num-row-1
#     while var>0:
#         print(end=" ")
#         var=var-1
#     star=row+1
#     while star>0:
#         print("*",end=" ")
#         star=star-1
#     row=row+1
#     print()

i = 0
while i <= 5:
    print(' '*i + ('* ')*(5-i))
    # print(' '*0 +('*')*5)
    # print(' '*1 +('*')*4)
    # print(' '*2 +('*')*3)
    # print(' '*3 +('*')*2)
    # print(' '*4 +('*')*1)
    i += 1
