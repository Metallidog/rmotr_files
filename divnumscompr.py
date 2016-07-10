def divisible_numbers(a_list, a_list_of_terms):
    #z_list = [x for x in a_list for y in a_list_of_terms if x%y != 0]
    #return [x for x in a_list if x not in z_list]
    return [a for a in a_list if a not in (x for x in a_list for y in a_list_of_terms if x%y != 0)]
    

print (divisible_numbers([12,11,10,9,8,7,6,5,4,3,2,1], [2,3]))
print (divisible_numbers([16,12,11,10,9,8,7,6,5,4,3,2,1], [2,3,4]))
print (divisible_numbers([], [5,7]))
print (divisible_numbers([], []))
