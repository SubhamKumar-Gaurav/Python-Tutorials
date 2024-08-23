# import math
# import os
# import random
# import re
# import sys
#
#
#
# if __name__ == '__main__':
#     t = int(input().strip())
#
#     for t_itr in range(t):
#         n = int(input().strip())
#         a = 0
#         b = 0
#         c = 0
#         for i in range(n) :
#             if i%3==0 :
#                 a=a+i
#         for i in range(n) :
#             if i%5==0 :
#                 b=b+i
#         for i in range(n) :
#             if i%15==0 :
#                 c=c+i
#         print(a+b-c)



# import math
# import os
# import random
# import re
# import sys
#
#
#
# if __name__ == '__main__':
#     t = int(input().strip())
#
#     for t_itr in range(t):
#         n = int(input().strip())
#         m3=set(range(0,n,3))
#         m5=set(range(0,n,5))
#         m15=set(range(0,n,15))
#         print(sum(m3)+sum(m5)-sum(m15))



# T=int(input())
#
# for i in range(T) :
#     x,y=map(int , input().split())
#     a=x*y
#     print(a)


# T=int(input())
#
# for i in range(T) :
#     n=int(input())
#     l=[[i] for i in range(1,100000) ]
#
# import math
# N=int(input())
#
# l=[(i,j) for i in range(1,10000) for j in range(1,10000) if (i*i)-(j*j)==N  ]
# sums=[]
# for s in l :
#     tuplesum=sum(s)
#     sums.append(tuplesum)
# print(min(sums))


N=int(input())

for i in range(N) :
    a=int(input())
k=int(input())
l=[a]

for j in range(N) :
    if l[j]==k :
        print(j)

