# -*- coding: UTF-8 -*-
a = [9,8,7,6,5,4,3,2,1,0]
b = [19,18,17,61,110,14,13,21,11,10]
c = [3,2,1]

def StupidSort(a):
    k = 0
    while k < len(a):
        for i in range(len(a)-1):
          if a[i] > a[i+1]:
             a[i],a[i+1] = a[i+1],a[i]
             k = 0
          else:
             k+=1
    return a

def GhnomeSort(a):
   i = 1
   j = 2
   while i < len(a):
     if a[i-1] < a[i]:
       i = j
       j = j + 1
     else:
            a[i-1],a[i] = a[i],a[i-1]
            i = i - 1;
            if i == 0:
                i = j;
                j = j + 1;
   return a

def BubbleSort(a):
    k = len(a)
    while k > 0:
        for i in range(k-1):
          if a[i] > a[i+1]:
             a[i],a[i+1] = a[i+1],a[i]
        k -=1
    return a

def ShakerSort(a):
    left = 0
    right = len(a) - 1
    while(left <= right):
        for i in range(left,right,+1):
            if a[i] > a[i+1]:
             a[i],a[i+1] = a[i+1],a[i]
        right -= 1
        for i in range(right,left,-1):
            if a[i-1] > a[i]:
               a[i],a[i-1] = a[i-1],a[i]
        left += 1
    return a

def MergeSort(a):
    i = 0
    j = 0
    k = 0
    if len(a)>1:
       mid = len(a)/2
       left = a[:mid]
       right = a[mid:]

       MergeSort(left)
       MergeSort(right)

       while i < len(left) and j < len(right):
             if left[i] < right[j]:
                a[k] = left[i]
                i += 1
             else:
                a[k] = right[j]
                j += 1
             k += 1
       while i < len(left):
             a[k] = left[i]
             i += 1
             k += 1
       while j < len(right):
             a[k] = right[j]
             j += 1
             k += 1
    return a    


def SelectionSort(a):
   for k in range(len(a)-1):
    m = k 
    i = k + 1
    while i < len(a):
       if a[i] < a[m]:
          m = i
       i += 1  
    a[k],a[m] = a[m],a[k]
   return a

def listmerge(a,b):     
    for l in b:
        a.append(l)
    return a

#a.extend(b)
#print(a)

print("BubbleSort:"+str(BubbleSort(a)))
print("ShakerSort:"+str(ShakerSort(a)))
print("MergeSort:"+str(MergeSort(a)))
print("SelectionSort:"+str(SelectionSort(a)))
