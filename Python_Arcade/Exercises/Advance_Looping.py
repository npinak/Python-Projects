''' Problem 1: Write code that will print ten asterisks (*) in a row:

* * * * * * * * * *'''

#for i in range(1,10,1):
#    print("*",end=" ")
#   continue

'''Problem 2: Write code that will print the following:

* * * * * * * * * *
* * * * *
* * * * * * * * * * * * * * * * * * * * '''
#
# for row in range(10):
#     print("*",end=" ")
# print()
# for row in range(5):
#     print("*",end=" ")
# print()
# for row in range(20):
#     print("*",end=" ")


"""Problem 3: Use two “for” loops, one of them nested inside the other, to print the following 10x10 rectangle:

* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *"""

# for j in range(1,10,1):
#     for i in range(1,10,1):
#        print("*",end=" ")
#        continue
#     print()
#     continue

"""Problem 4: Use two “for” loops, one of them nested, to print the following 5x10 rectangle:

* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *"""

# for j in range(1,10,1):
#     for i in range(1,5,1):
#       print("*",end=" ")
#       continue
#     print()
#     continue

'''Problem 5: Use two for loops, one of them nested, to print the following 20x5 rectangle:

* * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * *'''

# for j in range(1,5,1):
#     for i in range(1,20,1):
#         print("*",end=" ")
#         continue
#     print()
#     continue

'''Write code that will print the following:

0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9'''

# for j in range(1,10,1):
#     for i in range(1,10,1):
#         print(i, end= " ")
#         continue
#     print()
#     continue

'''Problem 7

Adjust the prior program to print:
0 0 0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1
2 2 2 2 2 2 2 2 2 2
3 3 3 3 3 3 3 3 3 3
4 4 4 4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5 5
6 6 6 6 6 6 6 6 6 6
7 7 7 7 7 7 7 7 7 7
8 8 8 8 8 8 8 8 8 8
9 9 9 9 9 9 9 9 9 9'''

# for j in range(1,10,1):
#     for i in range(1,10,1):
#         print(j, end= " ")
#         continue
#     print()
#     continue

'''Problem 8

Write code that will print the following:

0
0 1
0 1 2
0 1 2 3
0 1 2 3 4
0 1 2 3 4 5
0 1 2 3 4 5 6
0 1 2 3 4 5 6 7
0 1 2 3 4 5 6 7 8
0 1 2 3 4 5 6 7 8 9'''


# for i in range(0,11,1):
#     for j in range(i):
#         print(j, end=" ")
#         continue
#     print()
#     continue


'''Problem 9

Write code that will print the following:

0 1 2 3 4 5 6 7 8 9
  0 1 2 3 4 5 6 7 8
    0 1 2 3 4 5 6 7
      0 1 2 3 4 5 6
        0 1 2 3 4 5
          0 1 2 3 4
            0 1 2 3
              0 1 2
                0 1
                  0'''

for i in range(11,0,-1):
    for j in range(0,i,-1):
        print(j)
    # for j in range(i):
    #     print(j,end="")
# for row in range(10):
#
#     for j in range(row):
#         print(" ", end=" ")
#
#     for j in range(10 - row):
#         print(j, end=" ")
#
#     print()d