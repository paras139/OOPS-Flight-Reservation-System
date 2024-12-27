# import numpy as np
# import pandas as pd
# from sklearn.linear_model import LinearRegression 
# import matplotlib.pyplot as plt
# from word2number import w2n
# from bs4 import BeautifulSoup as bs4
# import math
# import joblib
# import pickle
# import seaborn as sn

# df = pd.DataFrame({
#     'Name': ['Paras', 'som', 'Chaubey'],
#     "Age": [27, 27, 26]
# })
# print(df)

# fruit=['mango','banana','apple','pineapple'] 
# def print_list(list,idx=0):
#     if(idx == len(list)):
#      return
#     else:
#      print(list[idx])
#      print_list(list, idx+1)
# print(print_list(fruit))     
        
# n=5
# for i in range(0,n+1):
#     for j in range(0,n-i):
#       print(' ',end=' ')
#     for k in range(0,2*i-1):
#       if(k==0 or k==2*i-2 or i==1):
#         print('*',end=' ')
#       else:
#         print(' ',end=' ')                 
#     print()                    

# import os
# def find_word(a):
#       word= a
#       with open('demo.txt','r') as dem:
#        f=dem.read()
#        if(f.find(word)!=-1):
#           print('found')
#        else:
#           print('not found')  
 
# with open('demo.txt','r') as ap:
#    d=ap.read()
#    print(d)
# print(d.split(','))

# with open('demo.txt','r') as par:
#   c=par.read()
#   print(c)
#   num=''
#   for i in range(0,len(c)):
#     if (c[i]==","):
#       print(num)
#       num=''
#     else:
#       num+=c[i]  

# f=12
# g=18
# greater=0
# lcm=1
# if(f>g):
#   greater=f
# else:
#   greater=g 
# while(True):
#   if(greater%f==0 and greater%g==0):
#     lcm=greater
#     break
#   greater+=1
# print(lcm)
# for i in range(2,lcm):
#   if(f%i==0 and g%i==0):
#     hcf=i
# print(hcf)

# n=121
# duplicate=n
# rev=0
# while(n>0):
#   reminder= n%10
#   rev=(rev*10)+reminder
#   n =n//10
# if(duplicate==rev):
#   print("palindrome") 

# #2 sum with hashing
# a=[2,5,11,25,7]
# target=9
# def twosum(a,target):
#   dic={}
#   for i in range(len(a)):
#      first=a[i]
#      second=target-first
#      if(second in dic):
#         return(dic[second],i)
#      dic[first]=i
#   return None
# print(twosum(a, target))  

# #four sum problem
# a=[-2,-1,-1,1,1,2,2]

# target=0
# def foursum(a,target):
#  a.sort()
#  dic=[]
#  for i in range(len(a)):
#     if i>0 and a[i]==a[i-1]: continue
#     for j in range( i+1,len(a)):
#         if j>i+1 and a[j]==a[j-1]: continue
#         p=j+1
#         q=len(a)-1
#         while(p<q):
#             current_sum=a[i]+a[j]+a[p]+a[q]
#             if current_sum<target:
#                 p+=1
#             elif current_sum>target: 
#                 q-=1
#             else: 
#                 dic.append([a[i],a[j],a[p],a[q]])
#                 p,q=p+1,q-1
#             while p<q and a[p]==a[p-1]: p+=1
#             #while p<q and a[q]==a[q+1]:
#                        # q -= 1
#  return dic
# print(foursum(a,target))

# class student:
#   college_name='KJSCE'
#   def __init__(self,name,marks):
#     self.name = name 
#     self.marks = marks
#   def welcome(self):
#     print("Welcome,",self.name)  
#   def avg_marks(self):
#     sum=0
#     for i in self.marks:
#        sum+=i
#     print(self.name,'you avg score is',sum/3)   

# s1=student('porus',[99,77,89])
# s2=student('paras',[59,99,99])
# s1.welcome()
# print(s1.avg_marks())

# class bank_account():
#   def __init__(self,balance,accountno):
#     self.balance=balance
#     self.accountno=accountno
#   def debit(self,debitamount):
#     self.debitamount= debitamount
#     print('enter amount to debit:',debitamount)
#     self.balance-=debitamount
#     print('new available balance is',self.balance)
#   def credit(self,creditamount):
#     self.creditamount= creditamount
#     print('enter amount to credit:',creditamount)
#     self.balance+=creditamount
#     print('new available balance is',self.balance)
# c1=bank_account(10000,1234)
# c1.debit(1000)
# print(c1.balance,c1.accountno)
# c1.credit(400)
# print(c1.balance,c1.accountno)

# a='i love my india'
# b=''
# for i in range(len(a)):
#  if(a[i]==" "):
#   print(b)
#   b=''
#  else:
#   b+=a[i]

# from array import *
# p= array('i',[])
# n=int(input("enter size of an array"))
# for i in range(n):
#      x = int(input("enter value of array"))
#      p.append(x)
# print(p) 

# f=int(input('enter the number you want to find'))
# s=0
# for i in p:
#   if i==f:
#     print("we found at ",s)
#   else:
#     s+=1  

# from numpy import *
# a=linspace(1,15,16)
# print(a)

# a=['dewe','wasff','paras','fferfr','fergrtg','qweqw','r','rggrt','gegrt']
# def count_charmorethan5(list):
#   morethan5=0
#   lessthan5=0 
#   for i in list:   
#         if(len(i)>4):
#              morethan5+=1
#         else:
#             lessthan5+=1
#   print("morethan5 :{}".format(morethan5))  
#   print('lessthan5: {}'.format(lessthan5))        
#   return morethan5 & lessthan5
# count_charmorethan5(a)

# a=5
# b=4
# a,b=b,a
# sub=lambda a,b:a-b
# print(sub(a,b))

# def start():
#     print('helo world')
# print('myself')
# if __name__=='__main__':
#     start()

# a=[5,8,4,6,9,2]
# b=9
# for i in range(len(a)):
#    if a[i] == b:
#       print(a[i])
#    else:
#       print('not found')  

# import requests
# from bs4 import BeautifulSoup
# url ='https://webscraper.io/test-sites/e-commerce/allinone/computers'
# r=requests.get(url)
# soup = BeautifulSoup(r.text,'lxml')
# print(soup.div)

# ##selection sort
# a=[2,5,4,9,6,7,13,12]
# for i in range(len(a)):
#     minpos=i
#     for j in range(i,len(a)):
#         if a[i]>a[j]:
#             i=j
#     a[i],a[minpos]=a[minpos],a[i]        
#     # temp=a[i]
#     # a[i]=a[minpos]
#     # a[minpos]=temp    
#     # print(a)    
# print(a)

# #binary search need ascending order using recurrsion
# a=[2,5,4,9,6,7,13,12]
# a.sort()
# print(a)
# def binary_search(a,find,lb,ub):
#     if(lb<=ub):
#       mp=(lb+ub)//2
#       if(a[mp]<find):
#         return binary_search(a,find,mp+1,ub)
#       elif (a[mp]>find):
#         return binary_search(a,find,lb,mp-1)
#       elif(find==a[mp]):
#         return mp
#     return -1
# print(binary_search(a,12,0,(len(a)-1)))

# index=-1
# find=13
# a.sort()
# print(a)
# lb=0
# ub=len(a)-1
# while lb<=ub:
#      mb=(lb+ub)//2
#      if(a[mb]==find):
#         globals()['index']=mb
#         break  
#      else:
#         if a[mb]<find:
#             lb=mb+1
#         else:
#             a[mb]>find
#             ub=mb-1
# print(index)

# a='the sky is blue'
# word=''
# str=[]
# for ch in a:
#     if ch!=' ':
#         word+=ch
#     else:
#         str.append(word)
#         word=''    
# if word: #take the last word
#          str.append(word)
# print(str)         
# d= " ".join(str[::-1])
# print(d)   

# height=[1,8,6,2,5,4,8,3,7] 
# areag =0
# for i in range (len(height)):
#   for j in range(i+1,len(height)):
#     width=j-i
#     h=min(height[i],height[j])
#     area = width*h
#     areag=max(area,areag)
# print(areag)

# #2 pointer approach
# marea=0
# lp=0
# up=len(height)-1
# while(lp<up):
#     width=up-lp
#     h=min(height[lp],height[up])
#     c=min(height[lp],height[up])
#     area= width*h
#     marea=max(marea,area)
#     if(height[lp]<height[up]):
#         lp+=1
#     else:
#         up-=1    
# print(marea)  
# print(c)

# a=[1,2,3,4]
# product=1
# b=[1,1,1,1]
# for i in range(len(a)):
#   product=1
#   for j in range(len(a)):
#     if(i!=j):
#      product *=a[j]
#   b[i]=product   
# print(b)
# b=[1,1,1,1]
# prefix=[1,1,1,1]
# suffix=1
# for i in range(1,4):
#     b[i]=b[i-1]*a[i-1]
# print(b)    
# for i in range(2,-1,-1):
#     suffix*=a[i+1]
#     b[i]*=suffix
# print(b)    

# #peak index in mountain array not done

# ##single element in sorted array
# a=[1,1,2,3,3,4,4,8,8]
# if(len(a)==1): print(a[0])
# lb=0
# ub=(len(a)-1)
# while(lb<=ub):
#     mp=lb+((ub-lb)//2)
#     if(mp==0 and a[mp]!=a[1]):
#         print(a[0])
#     if(mp==len(a)-1 and a[mp]!=len(a)-2): #last number
#         print(a[len(a)-1])
#     if(a[mp]!=a[mp-1] and a[mp]!=a[mp+1]):
#         print(a[mp])
#     if(mp%2==0):#even
#         if(a[mp]==a[mp-1]):
#             ub=mp-1
#         else:
#             lb=mp+1    
#     else: #odd
#         if(a[mp]==a[mp-1]):
#             lb=mp+1
#         else:
#             ub=mp-1          

# ##painter allocation problem
# a = [40, 30, 10, 20]
# painters = 2

# def check(a, painters, maxallowedtime):
#     p = 1  # Start with one painter
#     time = 0
#     for i in range(len(a)):
#         if time + a[i] <= maxallowedtime:
#             time += a[i]
#         else:  # Assign a new painter
#             p += 1
#             time = a[i]
#             if p > painters:
#                 return False
#     return True

# def mintime(a, painters):
#     lb = max(a)      
#     ub = sum(a)     
#     ans = -1
#     while lb <= ub:
#         mp = (lb + ub) // 2
#         if check(a, painters, mp):
#             ans = mp
#             ub = mp - 1
#         else:
#             lb = mp + 1
#     return ans

# print(mintime(a, painters))

# ##agrassive cows problem
# c=3
# a=[1,2,8,4,9]
# def mindistance(a,c,mp):
#     a.sort()
#     distance=a[0]
#     cows=1
#     for i in range(len(a)):
#         if(a[i]-distance>=mp):
#             distance=a[i]
#             cows+=1
#         if(c==cows):
#          return True    
#     return False         
# def largestpossiblevalue (a,c):
#     a.sort()
#     lb=1
#     ub=max(a)-min(a)
#     ans=-1
#     while(lb<=ub):
#         mp=(lb+ub)//2
#         if(mindistance(a,c,mp)):
#           ans=mp  
#           lb=mp+1
#         else:
#           ub=mp-1  
#     return ans
# print(largestpossiblevalue(a,c))

# ##insertion sort
# a=[2,6,3,8,5]
# for i in range(1,len(a)):
#     current=a[i]
#     previous=i-1
#     while previous >= 0 and a[previous]>current:
#         a[previous+1]=a[previous]
#         previous-=1
#     a[previous+1]=current
# print(a)

# ##sort an array
# a=[2,0,2,1,1,0,1,2,0,0]
# count0=0
# count1=0
# count2=0
# for i in range(len(a)):
#     if a[i]==0:
#         count0+=1
#     elif a[i]==1:
#         count1+=1
#     else:
#         a[i]==2
#         count2+=1
# idx=0
# for i in range(count0):
#     a[idx]=0
#     idx+=1
# for i in range(count1):
#     a[idx]=1
#     idx+=1
# for i in range(count2):
#     a[idx]=2
#     idx+=1 
# ##dutch national flag algorithm
# low,med,high=0,0,len(a)-1
# while(med<=high):
#     if(a[med]==1):
#         med+=1
#     elif(a[med]==0):
#         a[low],a[med]=a[med],a[low]
#         med+=1
#         low+=1
#     else:
#         a[high],a[med]=a[med],a[high]
#         high-=1
# print(a)

# ##Next Permutation Problem lexicographically next
# a=[7,8,5,4,2]
# pivot=-1
# for i in range(len(a)-2,-1,-1):
#    if(a[i]<a[i+1]):
#     pivot= a[i]
#     break
# if pivot==-1:
#     a=a[::-1]
# for j in range(len(a)-1,i,-1):
#     if a[j]>a[i]:
#         break
# a[j],a[i]=a[i],a[j]
# left=i+1
# right = len(a)-1
# while left < right:
#        a[right], a[left] = a[left], a[right]
#        left, right = left + 1, right - 1
# print(a)

# ##remove all occurrence from string
# s='daabcbaabcbc'
# c='abc'
# while len(s)>0 and s.find(c)!=-1:
#      s=s.replace(c,'')  
# print(s)
   
# ##String Compression problem   
# chr=['a','a','a','b','b','c','c','c']
# b=[]
# i=0
# while(i<len(chr)-1):
#     count=1
#     while(i<len(chr)-1 and chr[i]==chr[i+1]):
#        count+=1
#        i+=1
#     b.append(chr[i])
#     if(count>1):
#         b.append(count)  
#     i+=1
# print(b)

# l1=[1,2,3]
# l2=[2,3,5]
# l3=[i for i in l1 if i in l2]
# print(l3)

# import numpy as np
# l3=np.array([['a','b','c'],['d','e','f'],[2,5,9]])
# x=np.where(l3=='9')
# print(x)

# def spiral_matrix(matrix):
#     result=[]
#     left,right=0,len(matrix[0])-1
#     top,bottom=0,len(matrix)-1
#     while(top<=bottom and left<=right):
#       for i in range(left,right+1):
#         result.append(matrix[top][i])
#       top+=1
#       for i in range(top,bottom+1):
#         result.append(matrix[i][right])  
#       right-=1
#       if(top<=bottom):
#         for i in range(right,left-1,-1):
#          result.append(matrix[bottom][i])  
#         bottom-=1
#       if(left<=right):
#         for i in range(bottom,top-1,-1):
#          result.append(matrix[i][left])
#         left+=1
#     return result   
# a = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],   
# ]
# print(spiral_matrix(a)) 

# #min max book allocation issue
# a=[12,34,67,90]
# students=2
# noofbooks=(len(a))
# if (noofbooks<students):
#     print(-1)
# else:    
#   def maxpage(a,students,max):
#     page,student=0,1
#     for i in range(len(a)):
#        if(a[i]+page<=max):
#         page+=a[i]
#        else:
#         page=a[i]
#         student+=1    
#     if student>students:
#         return False
#     return True     
#   ub=sum(a)
#   lb=max(a)
#   while(lb<=ub):
#     mp=(lb+ub)//2
#     if( maxpage(a,students,mp)):  
#      ub=mp-1
#      d=mp
#     else:
#       lb=mp+1    
#   print(d)

# #find word in board
# board = [
#   ['A', 'B', 'C', 'E'],
#   ['S', 'F', 'C', 'S'],
#   ['A', 'D', 'E', 'E']
# ]
# word = "SEE"
# def find_word(word,board):
#     rows,colmun=len(board),len(board[0])
#     def dfs(r,c,wordindex):
#         if(wordindex==len(word)):
#             return True
#         if(r<0 or c<0 or r>=rows or c>=colmun or board[r][c]!=word[wordindex]): #return back, backtrack eg: we find s in SEE but not e so backtrack
#             return False
#         temp=board[r][c]
#         board[r][c]='#'
#         found=(
#             dfs(r+1,c,wordindex+1) or
#             dfs(r,c+1,wordindex+1) or
#             dfs(r-1,c,wordindex+1) or
#             dfs(r,c-1,wordindex+1))
#         board[r][c]=temp
#         return found
#     for i in range(rows):
#         for j in range(colmun):
#             if(dfs(i,j,0)):
#                 return True
#     return False        
# print(find_word(word,board))

# a,b=4,2
# c=lambda a,b: a if a>b else b
# print(c(15,8))
# import functools
# a=[1,2,3,4]
# b=(list(map(lambda i:i*i,a))) #instead of lambda we can use any def function also
# print(b)
# #Filter funcation in python
# print([x for x in a if x>2]) 
# print(functools.reduce(lambda c,d:c*d,a))
# list1=[1,2,3,4]
# new_list = [x**2 for x in list1 if x > 2]
# print(new_list)

# n = int(input("Enter a number for n: "))
# size = 2 * n - 1  
# for i in range(size):
#     for j in range(size):
#         number = n - min(i, j, size - i - 1, size - j - 1)
#         print(number, end="")
#     print() 

# def rfib(n):
#     if n==0 or n==1:
#         return n
#     else: return rfib(n-1)+rfib(n-2)
# print (rfib(11))
        
# a= [1,2,4,5,6,8]
# def issorted(a,n):
#     if n==0 or n==1:
#         return True
#     else: return a[n-1]>=a[n-2] and issorted(a,n-1)   
# print(issorted(a,len(a))) 

# ##generate all subset using recurssion without duplicate value
# a=[]
# def get_subsets(subset,list1):
#     if not list1: 
#         #print(subset)
#         a.append(subset[:])
#         #storeallset(subset) 
#         return
#     get_subsets(subset,list1[1:])
#     get_subsets(subset+[list1[0]],list1[1:])
# get_subsets([],[1,2,3])
# print(a)

# ##generate all subset using recurssion with duplicate value (need to understand)
# def subsetsWithDup(list1):
#     result = set()  # Using a set to store unique subsets
#     list1.sort()     # Sort the input to manage duplicates
#     def backtrack(start, subset):
#         # Add the subset as a tuple (immutable) to the set
#         result.add(tuple(subset))
#         for i in range(start, len(list1)):
#             # Skip duplicates (similar check as before)
#             if i > start and list1[i] == list1[i - 1]:
#                 continue
#             # Include the current element and recurse
#             backtrack(i + 1, subset + [list1[i]])
#     backtrack(0, [])
#     return [list(subset) for subset in result]  # Convert tuples back to lists
# print(subsetsWithDup([1, 2, 2]))

# ##permutations 
# a=[1,2,3]
# def findperumataion (a):
#     s=[]
#     def backtrack(idx=0):
#        if idx==len(a):
#         s.append(a[:])
#         return
#        for i in range(idx,len(a)):
#         a[idx],a[i]=a[i],a[idx]
#         backtrack(idx+1)
#         a[idx],a[i]=a[i],a[idx]
#     backtrack()
#     return s
# print(findperumataion(a))
# a='asd'
# def permi(a):
#     c=[]
#     a=list(a)
#     def backtrack(idx=0):
#         if idx==len(a):
#             c.append(''.join(a))
#             return
#         for i in range (idx,len(a)):
#             a[idx],a[i]=a[i],a[idx]
#             backtrack(idx+1)
#             a[idx],a[i]=a[i],a[idx]
#     backtrack()
#     return c
# print(permi(a))

# ##NQueens backtracking  
# N=4
# def print_sol(board):
#     for row in board:
#       print(' '.join('Q' if cell else'.'for cell in row ))
#     print('\n')
# def is_safe(board,row,col):
#     for i in range (row): #Check this column on the upper rows
#         if board[i][col]:
#           return False
#     i,j=row,col
#     while(i>=0 and j>=0): # Check upper left diagonal
#        if board[i][j]:
#         return False
#        i-=1
#        j-=1
#     i,j=row,col
#     while(i>=0 and j<N): # Check upper right diagonal
#         if board[i][j]:
#             return False
#         i-=1
#         j+=1
#     return True
# def solve_nqueen(board,row):
#     if row>=N:
#         (print_sol(board))
#         return True
#     res=False
#     for col in range(N):
#         if is_safe(board,row,col):
#             board[row][col]=True # Place queen
#             res= solve_nqueen(board,row+1) or res
#             board[row][col]=False  # Backtrack
#     return res
# def solve():
#     board= [[False]*N for _ in range(N)]
#     if solve_nqueen(board,0):
#         print('solution found!')
#     else:
#         print('solution not found!')
# solve()

# ##play sudoku
# def solvesudoko(board):
#     def isvalid(board,row,col,num):
#         for i in range(1,9):
#          if board[i][col]==num or board[row][i]==num: return False
#         row_start,col_start= 3*(row//3),3*(col//3)
#         for i in range (row_start,row_start+3):
#             for j in range(col_start,col_start+3): #mistake 2
#                 if board[i][j]==num: return False
#         return True
#     def playtime():
#         for row in range(9):
#             for col in range(9):
#                 if board[row][col]=='.':
#                     for num in '123456789': #mistake 3
#                       if isvalid(board,row,col,num):
#                          board[row][col]=num
#                          if playtime(): #remember this
#                             return True
#                          board[row][col]='.'  # Backtrack
#                     return False
#         return True
#     playtime()             
# board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
# solvesudoko(board)              
# for i in board:
#     print(' '.join(i))

# ###tictanic survival problem
# import pandas as pd
# test=pd.read_csv('/Users/paras/Downloads/titanic/test.csv')
# data=pd.read_csv('/Users/paras/Downloads/titanic/train.csv')
# # print(data.info())
# # print(test.info())
# #data.Age.value_counts()
# data.drop(['Age','Name','Fare','Cabin','Ticket'],inplace=True, axis=1)
# test.drop(['Age','Name','Fare','Cabin','Ticket'],inplace=True, axis=1)
# c=[data,test]
# for i in c:
#     i.Embarked=i.Embarked.fillna('S')
# #print(data.Embarked.value_counts())
# gendermap={'male':0,'female':1}
# embarkedmap={'S':0,'Q':2,'C':1}  
# for i in c:
#     i['Sex']=i['Sex'].map(gendermap)
#     i['Embarked']=i['Embarked'].map(embarkedmap)
# ##print(data.info(),test.info())
# x_data=data.drop(['Survived','PassengerId'],axis=1)
# y_data=data['Survived']
# x_test=test.drop('PassengerId',axis=1)
# from sklearn.linear_model import LogisticRegression
# clf=LogisticRegression(random_state=0)
# clf.fit(x_data,y_data)
# y_pred=clf.predict(x_test)
# #print(y_pred)
# acc_logistic=round(clf.score(x_data,y_data)*100,2)
# print(acc_logistic)
# output = pd.DataFrame({"PassengerId": test["PassengerId"], "Survived": y_pred})
# output.to_csv("asubmission.csv",index=False)
# obesrvation=pd.read_csv('asubmission.csv')
# print(obesrvation.Survived.value_counts())


# ###understand linearregression use
# a=pd.read_csv('/Users/paras/Downloads/hiring.csv')
# print(a)
# a.experience= a.experience.fillna('zero')
# a.experience = a.experience.apply(w2n.word_to_num)
# import math
# median = math.floor(a['test_score(out of 10)'].mean())
# a['test_score(out of 10)']=a['test_score(out of 10)'].fillna(median)
# reg=LinearRegression()
# reg.fit(a[['experience','test_score(out of 10)','interview_score(out of 10)']],a['salary($)'])
# print(reg.predict([[5,9,9]]))

# ###Gradient descent & cost function
# def predict_using_sklean():
#     a=pd.read_csv('/Users/paras/Downloads/test_scores.csv')
#     x=a[['math']] #use double brackets to crate a 2D array
#     y=a['cs']
#     reg=LinearRegression()
#     reg.fit(x,y)
#     return reg.coef_,reg.intercept_
# def gradient_descent(x,y):
#     m_curr=0
#     b_curr=0
#     interation=100
#     n=len(x)
#     learning_rate=0.0002
#     cost_previous=0
#     for i in range(interation):
#         y_predicted=m_curr*x+b_curr
#         cost=(1/n)*sum([value**2 for value in (y-y_predicted)])
#         md = -(2/n)*sum(x*(y-y_predicted))
#         bd = -(2/n)*sum(y-y_predicted)
#         m_curr = m_curr - learning_rate * md
#         b_curr = b_curr - learning_rate * bd
#         if math.isclose(cost, cost_previous, rel_tol=1e-20):
#             break
#         cost_previous = cost
#         print ("m {}, b {}, cost {}, iteration {}".format(m_curr,b_curr,cost, i))
#     return m_curr, b_curr
# if __name__ == "__main__":
#     df = pd.read_csv('/Users/paras/Downloads/test_scores.csv')
#     x = np.array(df.math)
#     y = np.array(df.cs)
#     m, b=gradient_descent(x,y)
#     print("Using gradient descent function: Coef {} Intercept {}".format(m, b))
#     m_sklearn, b_sklearn=predict_using_sklean()
#     print("Using sklearn: Coef {} Intercept {}".format(m_sklearn,b_sklearn))

# ###predict price of a car with respect to age and milage
# a=pd.read_csv('/Users/paras/Downloads/carprices.csv')
# dumy=pd.get_dummies(a['Car Model'])
# ##print(dumy)
# b=pd.concat([a,dumy],axis=1)
# b=b.drop('Car Model',axis=1)
# x=b.drop('Sell Price($)',axis=1)
# y=b['Sell Price($)']
# model=LinearRegression()
# model.fit(x,y)
# print(x)
# print(model.predict([[69000,5,0,0,1]]))

# ###Employee retention using logistic regression
# data=pd.read_csv('/Users/paras/Downloads/HR_comma_sep.csv')
# from matplotlib import pyplot as plt
# ###print(data.head())
# left=data[data['left']==1]
# print(left.shape)
# retained=data[data['left']==0]
# print(retained.shape)
# c=data.drop(['salary','Department'],axis=1)
# pd.set_option('display.max_columns', None)
# print(c.groupby('left').mean()) #dependent factor are promotion,monthly hours,satisfaction level and salary
# ##pd.crosstab(data.salary,data.left).plot(kind='bar')
# ##plt.show()
# a=data[['satisfaction_level','average_montly_hours','promotion_last_5years','salary']]
# ##print(a)
# dumy=pd.get_dummies(a['salary'])
# print(dumy)
# s=pd.concat([a,dumy],axis='columns')
# s.drop(['salary'],axis='columns',inplace=True)
# print(s.head())
# x=s
# y=data.left
# from sklearn.model_selection import train_test_split
# x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)
# from sklearn.linear_model import LogisticRegression
# model=LogisticRegression()
# model.fit(x_train,y_train)
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_colwidth', None)
# print(model.predict(x_test))
# print(model.score(x_test,y_test))

# ###identify handwritten digit recogination 26 November 2024
# from sklearn.datasets import load_digits
# a=load_digits()
# print(dir(a))
# print(a.data[0])
# #plt.gray()
# #for i in range (5):
# #   plt.matshow(a.images[i])
# #   plt.show()
# print(a.target[0:5])
# from sklearn.model_selection import train_test_split
# x_train,x_test,y_train,y_test=train_test_split(a.data,a.target,test_size=0.2)
# print(len(x_train))
# print(len(x_test))
# from sklearn.linear_model import LogisticRegression
# m=LogisticRegression()
# m.fit(x_train,y_train)
# print(m.score(x_test,y_test))
# plt.matshow(a.images[77])
# #plt.show()
# print([a.target[77]]) 
# print([a.target[:5]])
# y_pred=m.predict(x_test)
# from sklearn.metrics import confusion_matrix
# cm=confusion_matrix(y_test,y_pred)
# print(cm)
# plt.figure(figsize=(10,7))
# sn.heatmap(cm,annot=True)
# plt.xlabel('Predicted')
# plt.ylabel('Truth')
# plt.show()
# from sklearn.datasets import load_iris
# a=load_iris()
# x=a.data
# y=a.target
# from sklearn.model_selection import train_test_split
# x_train,x_test,y_train,y_test=train_test_split(a.data,a.target,test_size=0.2)
# print(len(x_train))
# print(len(x_test))
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import classification_report,accuracy_score
# m=LogisticRegression()
# m.fit(x_train,y_train)
# print(m.score(x_test,y_test))
# y_pred=m.predict(x_test)
# y_pred = m.predict(x_test)
# accuracy = accuracy_score(y_test, y_pred)
# print(accuracy)
# print(classification_report(y_test, y_pred, target_names=a.target_names))
# sample_index=5
# sample_features = x_test[sample_index].reshape(1, -1)
# predicted_class = m.predict(sample_features)
# print(f"Sample features: {x_test[sample_index]}")
# print(f"Predicted class: {a.target_names[predicted_class[0]]}")
# print(predicted_class)

# #decision tree classification
# a=pd.read_csv('/Users/paras/Downloads/salaries.csv')
# #print(a.head())
# c=a.drop('salary_more_then_100k',axis=1)
# #print(c)
# target=a['salary_more_then_100k']
# from sklearn.preprocessing import LabelEncoder
# le_company= LabelEncoder()
# le_job=LabelEncoder()
# le_degree=LabelEncoder()
# c['company_n']=le_company.fit_transform(c['company'])
# c['job_n']=le_job.fit_transform(c['job'])
# c['degree_n']=le_degree.fit_transform(c['degree'])
# c=c.drop(['company','job','degree'],axis=1)
# print(c)
# from sklearn import tree
# m=tree.DecisionTreeClassifier()
# m.fit(c,target)
# m.score(c,target)
# print(m.predict([[2,1,0]]))

# #Support vector machine SVM
# from sklearn.datasets import load_iris
# a=load_iris()
# print(dir(a))
# print(a.feature_names)
# c=pd.DataFrame(a.data,columns=a.feature_names)
# pd.set_option('display.max_columns', None)
# print(c)
# c['target']=a.target
# print(c.head())
# print(a.target_names)
# print(c[c.target==1].head())
# c['flower_name']=c.target.apply(lambda x: a.target_names[x])
# print(c)
# c0=c[c.target==0]
# c1=c[c.target==1]
# c2=c[c.target==2]
# #print(c0.head())
# plt.xlabel('sepal length (cm)')
# plt.ylabel('sepal width (cm)')
# plt.scatter(c0['sepal length (cm)'],c0['sepal width (cm)'],color='green',marker='*')
# plt.scatter(c1['sepal length (cm)'],c1['sepal width (cm)'],color='blue',marker='.')
# #plt.show()
# #plt.scatter(c2['sepal length (cm)'],c2['sepal width (cm)'],color='red',marker='+')
# plt.xlabel('petal length (cm)')
# plt.ylabel('petal width (cm)')
# plt.scatter(c0['petal length (cm)'],c0['petal width (cm)'],color='green',marker='*')
# plt.scatter(c1['petal length (cm)'],c1['petal width (cm)'],color='blue',marker='.')
# #plt.show()
# from sklearn.model_selection import train_test_split
# x=c.drop(['target','flower_name'],axis=1)
# y=c.target
# x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
# print(len(x_train))
# from sklearn.svm import SVC
# m=SVC()
# m.fit(x_train,y_train)
# print(m.score(x_test,y_test))

# ##random forest algorithm pending
# ##15.Finding best model and hyper parameters 27 nov 2024
# from sklearn.datasets import load_digits
# a=load_digits()
# from sklearn import svm
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.linear_model import LogisticRegression
# from sklearn.naive_bayes import GaussianNB
# from sklearn.naive_bayes import MultinomialNB
# from sklearn.tree import DecisionTreeClassifier
# model_params={
#     'svm':{
#         'model':svm.SVC(gamma='auto'),
#         'params':{
#                   'C':[1,10,20],
#                   'kernel':['rbf','linear']
#                  }
#           },
#     'random_forest':{
#         'model':RandomForestClassifier(),
#         'params':{
#             'n_estimators':[1,5,10]
#         }
#     },
#     'logistic_regression':{
#         'model': LogisticRegression(),
#         'params':{
#             'C':[1,5,10]
#         }
#     },
#     'naive_bayes_gaussian':{
#         'model': GaussianNB(),
#         'params':{}  
#     },
#     'naive_bayes_multinomial':{
#         'model': MultinomialNB(),
#         'params':{}  },
#     'decision_tree':{
#         'model':DecisionTreeClassifier(),
#         'params':{
#             'criterion':['gini','entropy']
#         }
#     }   
# }
# from sklearn.model_selection import GridSearchCV
# scores=[]
# for i,j in model_params.items():
#     clf=GridSearchCV(j['model'],j['params'],cv=5, return_train_score=False)
#     clf.fit(a.data,a.target)
#     scores.append({
#         'model':i,
#         'best_score': clf.best_score_,
#         'best_params': clf.best_params_
#     })
# d=pd.DataFrame(scores,columns=['model','best_score','best_params'])
# print(d)

# #Naive Bayes Wine test 27 Nov 2024
# from sklearn.datasets import load_wine
# a=load_wine()
# print(dir(a))
# from sklearn.naive_bayes import GaussianNB,MultinomialNB
# from sklearn.model_selection import train_test_split
# c=pd.DataFrame(a.data,columns=a.feature_names)
# print(c)
# c['target']=a.target
# print(c[55:65])
# x_train,x_test,y_train,y_test=train_test_split(a.data,a.target,test_size=0.3,random_state=100)
# m=GaussianNB()
# m.fit(x_train,y_train)
# print(m.score(x_test,y_test))
# mn=MultinomialNB()
# mn.fit(x_train,y_train)
# print(mn.score(x_test,y_test))

# #PCA sumarize the data & predict out using sumarize data which decrease accuracy
# # 28 Nov 2024
# a=pd.read_csv('/Users/paras/Downloads/heart.csv')
# print(a.describe())
# pd.set_option('display.max_columns', None)
# #print(a[a.Cholesterol>(a.Cholesterol.mean()+3*a.Cholesterol.std())])
# a1=a[a.Cholesterol<=(a.Cholesterol.mean()+3*a.Cholesterol.std())]
# #print(a1.shape)
# #print(a[a.RestingBP>(a.RestingBP.mean()+3*a.RestingBP.std())])
# a2=a1[a1.RestingBP<=(a1.RestingBP.mean()+3*a1.RestingBP.std())]
# #print(a2.shape)
# #print(a2[a2.Oldpeak>(a2.Oldpeak.mean()+3*a2.Oldpeak.std())])
# a3=a2[a2.Oldpeak<=(a2.Oldpeak.mean()+3*a2.Oldpeak.std())]
# print(a3.shape)
# print(a3.ExerciseAngina.unique())
# print(a3.ST_Slope.unique())
# a3.ExerciseAngina.replace( {'N':0, 'Y':1}, inplace=True)
# a3.ST_Slope.replace( {'Down':1, 'Flat':1,'Up':3}, inplace=True)
# a3.RestingECG.replace( {'Normal':1, 'ST':1,'LVH':3}, inplace=True)
# a3.Sex.replace({'M':1, 'F':0}, inplace=True)
# print(a3.head())
# a4=pd.get_dummies(a3,drop_first=True)
# print(a4.head())
# x=(a4.drop('HeartDisease',axis=1))
# y=(a4.HeartDisease)
# print(x.head())
# print(y.head())
# from sklearn.preprocessing import StandardScaler
# scaler=StandardScaler()
# x_scaled=scaler.fit_transform(x)
# print(x_scaled)
# from sklearn.model_selection import train_test_split
# x_train,x_test,y_train,y_test=train_test_split(x_scaled,y,test_size=0.2)
# print(x_train.shape)
# print(x_test.shape)
# from sklearn.ensemble import RandomForestClassifier
# m=RandomForestClassifier()
# m.fit(x_train,y_train)
# print(m.score(x_test,y_test))
# from sklearn.decomposition import PCA
# pca=PCA(0.95)
# x_pca=pca.fit_transform(x)
# print(x_pca)
# x_pca_train,x_pca_test,y_pca_train,y_pca_test=train_test_split(x_pca,y,test_size=0.2)
# m_pca=RandomForestClassifier()
# m_pca.fit(x_pca_train,y_pca_train)
# print(m_pca.score(x_pca_test,y_pca_test))
# #bagging_heart_disease_prediction
# from sklearn.svm import SVC
# from sklearn.model_selection import cross_val_score
# scores=cross_val_score(SVC(),x,y,cv=5)
# print(scores.mean())
# from sklearn.ensemble import BaggingClassifier
# b_model=BaggingClassifier(estimator=SVC(), n_estimators=100, max_samples=0.8, random_state=0)
# scores=cross_val_score(b_model,x,y,cv=5)
# print(scores.mean())

# #rat in a maze problem
# def is_safe(maze, x, y, visited):
#     n = len(maze)
#     return 0 <= x < n and 0 <= y < n and maze[x][y] == 1 and not visited[x][y]
# def solve_maze(maze, x, y, path, visited, result):
#     n = len(maze)
#     # Base case: Reached the destination
#     if x == n - 1 and y == n - 1:
#         result.append(path)
#         return
#     # Mark the current cell as visited
#     visited[x][y] = True
#     # Move Down
#     if is_safe(maze, x + 1, y, visited):
#         solve_maze(maze, x + 1, y, path + 'D', visited, result)
#     # Move Left
#     if is_safe(maze, x, y - 1, visited):
#         solve_maze(maze, x, y - 1, path + 'L', visited, result)
#     # Move Right
#     if is_safe(maze, x, y + 1, visited):
#         solve_maze(maze, x, y + 1, path + 'R', visited, result)
#     # Move Up
#     if is_safe(maze, x - 1, y, visited):
#         solve_maze(maze, x - 1, y, path + 'U', visited, result)
#     # Backtrack: Unmark the current cell
#     visited[x][y] = False
# def find_paths(maze):
#     n = len(maze)
#     visited = [[False for _ in range(n)] for _ in range(n)]
#     result = []
#     if maze[0][0] == 1:  # Start only if the starting cell is open
#         solve_maze(maze, 0, 0, '', visited, result)
#     return result
# maze = [
#     [1, 0, 0, 0],
#     [1, 1, 0, 1],
#     [1, 1, 0, 0],
#     [0, 1, 1, 1]
# ]
# paths = find_paths(maze)
# print("Paths:", paths)

# class book:
#     def __init__(self,bookname,author,copies):
#         self.bookname=bookname
#         self.author=author
#         self.copies=copies
#     def __str__(self):
#         return f"{self.bookname} by {self.author} ({'availalbe' if {self.copies>0} else 'not availalbe'})"
# class library(book):
#     def __init__(self):
#         self.book1=[]
#     def viewbook(self):
#         for i in self.book1:
#             print(i)
#     def addbook(self,anyname):
#         self.book1.append(anyname)
#         print(f'book name:{anyname.bookname}')
#     def borrow_book(self,anyname):
#         for i in self.book1:
#             if i.copies>0 and i.bookname.lower()==anyname.lower():
#                 i.copies-=1
#                 print(f'You borrow {i.bookname}')
#                 return
#     def given_book(self,bookname):
#         for i in self.book1:
#             if i.copies>0 and i.bookname.lower()==bookname.lower():
#                 i.copies+=1
#                 print(f'You given {i.bookname}')
#                 return
#         print(f"'{bookname}' not found in library.")
# if __name__=='__main__':
#     lib = library()
#     lib.addbook(book("my firstbook", "paras shah", 3))
#     lib.viewbook()
#     lib.borrow_book("my firstbook")
#     lib.given_book("my firstbook")
    
# class rectange:
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#     def area(self):
#         return self.length*self.width
#     def peri(self):
#         return self.length*2+self.width*2
#     def cmp(self,otherrect):
#         if self.area()>otherrect.area():
#             return 'larger'
#         elif self.area()<otherrect.area():
#             return 'smaller'
#         else: return 'equal'
# r1=rectange(5,5)
# r2=rectange(10,5)
# r1.area()
# r1.peri()
# a= r1.cmp(r2)
# print(a)

# class shapes:
#     def __init__(self):
#         '''method to find area of shape'''
#         raise NotImplementedError('subclass must me implemented')
# class triangle(shapes):
#     def __init__(self,base,height):
#         self.base=base
#         self.height=height
#     def area(self):
#         return 0.5*self.base*self.height
# class square(shapes):
#     def __init__(self,side):
#         self.side=side
#     def area(self):
#         return self.side**2
# #if __name__=='__main__':
# t1=triangle(3,5)
# print(t1.area())

# class employee: 
#     def __init__(self,name,position,salary):
#         self.name=name
#         self.position=position
#         self.salary=salary
#     def __str__(self):
#         return f'{self.name} post is {self.position} with salary {self.salary}'
# class manager(employee):
#     def __init__(self,name,position,salary):
#         super().__init__(name,position,salary)
#         self.data=[]
#     def addemployee(self,manageremployee):
#         if isinstance(manageremployee,employee):
#             self.data.append(manageremployee)
#             print(f'Added {manageremployee} to {self.name} team')
#         else: print('Only emplyee data needed')
#     def displayemployee(self):
#         if not self.data:
#             print(f'{self.name}does not manage anybody')
#         else: 
#             print(f'Employees managed by{self.name}: ')
#             for i in self.data:
#                 print(f'{i.name} post is {i.position} with salaray {i.salary}')
# if __name__=='__main__':
#     e1=employee('paras','Software engineer','$250000')
#     e2=employee('pc','Software tester','$200000')
#     e3=employee('fg','HR','$100000')
#     m1=manager("caption",'team leader','$1000000')
#     m1.addemployee(e1)
#     m1.addemployee(e2)    
#     m1.addemployee(e3)
#     print(m1)

# class vehicle:
#     def __init__(self,speed,capacity):
#         self.speed=speed
#         self.capacity=capacity
#     def displayinfo(self):
#         return f'speed: {self.speed} km/hr having capacity: {self.capacity} litres'
# class car(vehicle):
#     def __init__(self,speed,capacity,trucksize):
#         super().__init__(speed,capacity)
#         self.trucksize=trucksize
#     def opentruck(self):
#         return f'the truck with {self.trucksize} litres'
# class bike(vehicle):
#     def __init__(self,speed,capacity,pop_wheelie):
#         super().__init__(speed,capacity)
#         self.pop_wheelie=pop_wheelie
#     def pop_wheelie(self):
#         return f'the truck with {self.pop_wheelie} litres' 
# if __name__=='__main__':
#     c1=car(180,40,400)
#     b2=bike(220,5,'Sport')
#     print(c1.displayinfo())
#     print(c1.opentruck())

##ECommerce system 24 Dec 24
# class Product:
#     def __init__(self,name,price,quantity):
#         self.name=name
#         self.price=price
#         self.quantity=quantity
#     def __str__(self):
#         availability=f'Available quantity: {self.quantity}' if self.quantity >0 else 'Out of stock'
#         return f"Product: {self.name} , price: {self.price}, ({availability})"
# class Cart():
#     def __init__(self):
#         self.products=[]
#     def add_product(self, product, quantity):
#         if not isinstance(product, Product):
#             print("Invalid item. Kindly add product only.") 
#             return
#         if product.quantity >= quantity:
#             product.quantity -= quantity
#             self.products.append((product, quantity))
#             print(f'Added product: {product.name} with quantity {quantity}')
#         else:
#             print(f'Insufficient quantity for {product.name}. Available quantity is {product.quantity}')
#     def remove_items(self,product_name):
#         for item in self.products:
#             product,quantity = item
#             if product_name==product.name:
#                 product.quantity+=quantity
#                 self.products.remove(item)
#                 print(f'Removed {product_name} from cart')
#                 return
#         print(f'{product_name} not found in cart.')
#     def view_cart(self):
#         if not self.products:
#             print('cart is empty')
#         else:
#             print('cart has below items')
#             for product,quantity in self.products:
#                 print(f'Product is {product.name}: {quantity} pcs at INR {product.price} each')
#     def totalsum(self):
#         total_sum=sum(product.price*quantity for product,quantity in self.products)
#         print(f"Total price of items in the cart: ${total_sum}")
#         return total_sum
# if __name__ == "__main__":
#     cart=Cart()
#     p1=Product('milk',10,200)
#     p2=Product('bread',5,1000)
#     cart.add_product(p1, 2)  
#     cart.add_product(p2, 3)
#     cart.view_cart()

###hospital management system 24 dec 24

# class Person():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __str__(self):
#         return (f'Name: {self.name} age is {self.age}')
# class Doctor(Person):
#     def __init__(self,name,age,specialization,schedule=None):
#         super().__init__(name,age)
#         self.specialization=specialization
#         self.schedule=schedule if schedule is not None else []
#     def asign_patient(self,patient,time):
#         self.schedule.append((patient,time))
#         print(f'Dr. {self.name} is assigned to patient {patient.name} at {time}')
#     def view_schedule(self):
#         if not self.schedule:
#             print(f'Dr. {self.name} is available')
#         else: 
#             print(f'Dr.{self.name} schedule is given below')
#             for i,time in self.schedule: 
#                 print(f'{i.name} age is {i.age} at Time: {time}')
# class Patient(Person):
#     def __init__(self,name,age,illness):
#         super().__init__(name,age)
#         self.illness=illness
#         self.asigned_doctor=None
#     def asign_doctor(self,doctor):
#         self.asigned_doctor=doctor
#         print(f'Dr. {doctor.name} is assigned to patient {self.name}')
#     def __str__(self):
#         doctor_info=f'Assigned Dr. {self.asigned_doctor.name}' if self.asigned_doctor else "no doctor assigned"
#         return f"{super().__str__()}, illness: {self.illness}, {doctor_info}"
# class Staff(Person):
#     def __init__(self,name,age,role):
#         super().__init__(name,age)
#         self.role=role
#     def __str__(self):
#        return f"{super().__str__()}, Role: {self.role}"
# class Hospital:
#     def __init__(self,name):
#         self.name=name
#         self.doctors=[]
#         self.patients=[]
#         self.staffs=[]
#     def add_doctors(self,doctor):
#         self.doctors.append(doctor)
#         print(f"Dr. {doctor.name} has been added to {self.name}.")
#     def add_patients(self,patient):
#         self.patients.append(patient)
#         print(f'{patient.name} has been added to {self.name}')
#     def add_staff(self,staff):
#         self.staffs.append(staff)
#         print(f'{staff.name} has been added to {self.name}')
#     def view_doctors(self):
#         print(f'Doctors at {self.name}:')
#         for i in self.doctors:
#             print(f'Dr. {i.name} having specialization at {i.specialization}')
#     def view_patient(self):
#         print(f' Patient at {self.name}')
#         for i in self.patients:
#             print(f'Patient are - {i} ')
#     def view_staff(self):
#         print(f' Staff at {self.name}')
#         for i in self.staffs:
#             print(f'- {i} ')
# if __name__=='__main__':
#     hospital=Hospital('City Hospital')
#     doc1=Doctor('Paras',50,'Cardiologist')
#     pat1 = Patient("John p", 30, "Heart Problem")
#     staff1 = Staff("Jane staff", 35, "Nurse")
#     hospital.add_doctors(doc1)
#     hospital.add_patients(pat1)
#     hospital.add_staff(staff1)
#     doc1.asign_patient(pat1, '5 pm')
#     pat1.asign_doctor(doc1)
#     doc1.view_schedule()
#     hospital.view_doctors()
#     hospital.view_patient()
#     hospital.view_staff()

###ATM Simulator 25 Dec 2024
# class Customer:
#     def __init__(self,name,account_no,balance,pin):
#         self.name=name
#         self.account_no=account_no
#         self.balance=balance
#         self.pin=pin
#     def __str__(self):
#         return f'Name: {self.name}, Account number: {self.account_no}, pin: {self.pin}'
#     def deposit(self,damount):
#         if damount>0:
#             self.balance+=damount
#         print(f'{damount} depositied successfully. New balance {self.balance}')
#     def check_balance(self,entered_pin):
#         if entered_pin==self.pin:
#             print(f'Available balance is {self.balance}')
#         else: print('Invalid pin')
#     def withdraw(self,amount,entered_pin):
#         if (self.pin==entered_pin):
#             if amount >0 and amount <=self.balance:
#                 print(f'INR{amount} withdrawn. Available balance {self.blance}')
#             elif amount > self.balance:
#                 print("Insufficient balance.")
#             else:
#                 print("Invalid withdrawal amount.")
#         else:print("Invalid Pin")
#     def change_pin(self,oldpin,newpin):
#         if (oldpin==self.pin):
#             if len(str(newpin))==4 and newpin.isdigit():
#                 self.pin=newpin
#                 print('ATM pin changed sucessfully')
#             else: print('pin must be 4 digits')
#         else: print("Invalid pin enter")
# if __name__=='__main__':
#   c1=Customer('Paras',999999,100000,'1390')
#   print('Welcome to ATM')
#   while (True):
#     print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Change PIN\n5. Exit")
#     choice=int(input('Enter your choice: '))
#     if choice==1:
#         pin= input('Enter your pin:')
#         c1.check_balance(pin)
#     elif choice==2:
#         damount=float(input('Enter the amount to deposit: '))
#         c1.deposit(damount)
#     elif choice==3:
#         pin=input('Enter the pin: ')
#         wamount=float(input('Enter the amount to withdraw: '))
#         c1.withdraw(wamount,pin)
#     elif choice == 4:
#             old_pin = input("Enter your current PIN: ")
#             new_pin = input("Enter your new PIN: ")
#             c1.change_pin(old_pin, new_pin)
#     elif choice == 5:
#             print("Thank you for using the ATM. Goodbye!")
#             break
#     else: print('Invalid choice')

###Flight Reservation System 26 Dec 24
# class Flight:
#     def __init__(self,flight_number,destination,seats_available):
#         self.flight_number=flight_number
#         self.destination=destination
#         self.seats_available=seats_available
#         self.passengers=[]

#     def display_flight_info(self):
#         print(f'Flight Number is :{self.flight_number}, destination:{self.destination}, Seats available: {self.seats_available}')

#     def book_ticket(self,passenger):
#         if self.seats_available>0:
#             self.seats_available-=1
#             self.passengers.append(passenger)
#             passenger.ticket_number=f'{self.flight_number}--{len(self.passengers)}'
#             print(f'{passenger.name},Ticket booked successfully! Ticket Number: {passenger.ticket_number}')
#         else:
#             print(f'Sorry, flight {self.flight_number} to {self.destination} is fully booked.')
    
#     def display_passenger_list(self):
#         if not self.passengers:
#             print(f'No passenger is {self.flight_number}')
#         else: 
#          print(f'Passenger in {self.flight_number}')
#          for i in self.passengers:
#              print(f'{i.name}: {i.ticket_number}')

# class Passenger():
#     def __init__(self,name):
#         self.name=name
#         self.ticket_number=None
#     def __str__(self):
#         return f'Passenger name:{self.name}, {self.ticket_number if self.ticket_number else "Not booked"}'
    
# class FlightReservationSystem:
#     def __init__(self):
#         self.flights=[]
#     def add_flight(self,flight):
#         self.flights.append(flight)
#         print(f'Flight {flight.flight_number} to destination {flight.destination}')
#     def view_avilable_flights(self):
#         print('All flights are given below')
#         for i in self.flights:
#             i.display_flight_info()
#     def find_flight(self,flight_number):
#         for i in self.flights:
#             if flight_number==i.flight_number:
#                 return i
#         return None
# if __name__=='__main__':
#     systems=FlightReservationSystem()
#     f1=Flight('P239','Mumbai',99)
#     f2=Flight('B199','Bangalore',88)
#     systems.add_flight(f1)
#     systems.add_flight(f2)
#     systems.view_avilable_flights()
#     p1=Passenger('Paras')
#     p2=Passenger('Som')
#     selected_flight=systems.find_flight('P239')
#     if selected_flight:
#         selected_flight.book_ticket(p1)
#         selected_flight.book_ticket(p2)
#     if selected_flight:
#         selected_flight.display_passenger_list()
#         systems.view_avilable_flights()


a='ilovemy india'
b=a.split('i') 
print(b)   


        

    





