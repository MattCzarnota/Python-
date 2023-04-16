def sample(*args,limit:int=10)-> int:
    
    new_list = []
    for arg in args:
        if arg > limit:
            new_list.append(arg)
    return new_list

print(sample(12,3,4,5,10,limit=9))
