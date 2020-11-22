def findMaxMinNumber(left, right, our_number, our_units_counter): 

    numbers = [] # a list of numbers in our interval that have the same number of units as in our number

    for number in range(left, right+1): 

        temp = number   # variable for counring units 
        units_counter = 0   # counter for counting units 
  
        # Traverse for every bit of number in our interval and counting units 
        while temp: 
            if temp & 1: 
                units_counter +=1
            temp = temp >> 1
        
        # Adding number in list if the number of units is the same as the amount of our number
        if units_counter == our_units_counter and number != our_number:
            numbers.append(number)
            
    return (min(numbers), max(numbers)) # retunr min/max number of list 

# Our input data
left_interval = 1
right_interval = 50
our_number = 15

our_units_counter = 0   # counter for counting units in our binary number 
temp = our_number   # variable for counting units in our binary number 

# Traverse for every bit of our number and counting units 
while temp: 
    if temp & 1: 
        our_units_counter +=1
    temp = temp >> 1

result = findMaxMinNumber(left_interval, right_interval, our_number, our_units_counter)

print('Min number =', result[0], '\nMax number =', result[1]) # result 