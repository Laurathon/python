def list_manipulation(lst, command, location, value=None):
    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'remove', 'end')
        3

        >>> list_manipulation(lst, 'remove', 'beginning')
        1

        >>> lst
        [2]

    add: add item at beginning/end, and return list

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'add', 'beginning', 20)
        [20, 1, 2, 3]

        >>> list_manipulation(lst, 'add', 'end', 30)
        [20, 1, 2, 3, 30]

        >>> lst
        [20, 1, 2, 3, 30]

    Invalid commands or locations should return None:

        >>> list_manipulation(lst, 'foo', 'end') is None
        True

        >>> list_manipulation(lst, 'add', 'dunno') is None
        True
    """
    length=len(lst)
    if command == "add":
        if location =="beginning":
            if value =="None":
                return  #no value to add
            else:
                lst.insert(0,value)
                return lst     #add value to beginning of list
        elif location =="end":
            lst.append(value)
            return lst     # add value to end of list
        else:
            return
    elif command== "remove":  
        if location == "beginning":
            if value == "None":
                return   # nothing to delete
            else:
                lst.pop(0)   # remove from beginning of lst
                return lst
        elif location == "end":
            lst.pop()     # remove from end of list
            return lst
            
        else:
            return    

    #return "list is ",lst, " length is ",length