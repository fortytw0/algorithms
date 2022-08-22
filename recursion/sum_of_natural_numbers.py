def sum_of_natural_numbers(number) : 

    # base case
    if number < 1 : 
        return 0

    else : 
        return number + sum_of_natural_numbers(number-1)

print(sum_of_natural_numbers(55))

