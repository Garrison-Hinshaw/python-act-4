def max_num(a,b,c):
    return ([a,b,c])

print (max_num(5,56,115))

def mult_list(list):
   if len(list) == 0: 
    return 0
   product = list[0] 

   if len(list) > 1:
    for i in list[1:]:
        product = product * i
   return product

print(mult_list([1,2,3]))

