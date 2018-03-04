first_term = int(input("Enter first term of an AP : "))
no_of_terms = int(input("Enter no. of terms of AP : "))
com_diff = int(input("Enter common difference of AP : "))
print("AP series ", end = " : ")
sum = 0
for i in range(1,no_of_terms + 1):
    term = first_term + ((i - 1) * com_diff)
    sum = sum + term
    print(term,end=" ")
    i = i + 1


print("\n")
print('Sum of {0} terms of an AP with first term {1} and commom difference {2} is {3}'.format(no_of_terms,first_term,com_diff,sum))