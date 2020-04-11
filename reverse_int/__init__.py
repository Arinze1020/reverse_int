def reverse(num):
    assert (isinstance(num, int)), "Value Error Suppose to be an Integer."
    resver = 0
    while (num>0):
        rem = num%10
        resver  = (resver *10)+rem
        num = num//10
    return resver 
    

    