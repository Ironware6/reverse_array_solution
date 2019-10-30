#Clever way of Reversing an List in Python using Python negative indexes :-P

#By Ralphie Perez

num = [3,2,4,1,0,2,3,4,5,5]


def reverse_list(arr):
  new_list = []
  for n in range (len(arr)):
    reverb = arr[-1 + (-1 * n)]
    new_list.append(reverb)

  print(new_list)  


reverse_list(num)