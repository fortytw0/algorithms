

def decimal2binary(number:str) : 

    print('Current number : ' , number)

    # base case
    if number == '0' : 
        return '0'
    else : 

        rem = int(number)%2 
        quotient = int(number)//2

        # shrink problem
        return decimal2binary(str(quotient)) + str(rem) 


print(decimal2binary(3))