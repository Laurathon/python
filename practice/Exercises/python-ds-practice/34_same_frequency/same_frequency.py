def sort_num_List(num):
        numList =[]
        for x in str(num):
            numList.append(x)
        return sorted(numList)

def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
   
    return sort_num_List(num1) == sort_num_List(num2)
    
   