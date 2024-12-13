def txt_to_list_of_triples(filename, str_to_int = False): 
    """Takes a .txt file representing a list of triples and converts this to 
    a list of triples represented by lists. Each line is a triple, 
    and elements of each triple are space-separated. Optionally converts 
    elements of the triples to integers. """
    with open(filename) as f: 
        lines = f.read().splitlines()
    triples = []
    for line in lines: 
        line = line.strip()
        T = line.split(sep=' ')
        if str_to_int: 
            for i in range(len(T)): 
                T[i] = int(T[i])
        triples.append(T)
    return triples

def txt_to_list_of_lists_of_triples(filename, str_to_int = False): 
    """Takes a .txt file representing a list of lists of triples and converts 
    this to a list of lists of triples represented by lists. Each line is 
    a list of comma-separated triples, and elements of each triple are 
    space-separated. Optionally converts elements of the triples to 
    integers. """
    with open(filename) as f: 
        lines = f.read().splitlines()
    list_of_lists = []
    for line in lines: 
        line = line.strip()
        list_A = []
        A = line.split(sep=',')
        for a in A: 
            a = a.strip()
            T = a.split(sep=' ')
            if str_to_int: 
                for i in range(len(T)): 
                    T[i] = int(T[i])
            list_A.append(T)
        list_of_lists.append(list_A)
    return list_of_lists

def is_PSTS_checker(triples, point_set): 
    """Takes a list of triples and a set of points point_set and 
    checks that the triples are subsets of the point_set, and determines if
    the set of triples is a PSTS, or if a pair of points 
    is contained in more than one triple. """
    valid_elements = True
    for T in triples: 
        for x in T: 
            if x not in point_set: 
                print("{0} contains an element {1} which is not a point. ".format(T,x))
                valid_elements = False
    if valid_elements == True: 
        is_PSTS = True
        pairs = []
        for T in triples: 
            for i in range(len(T)): 
                for j in range(i+1,len(T)): 
                    if [T[i],T[j]] in pairs: 
                        print("{0} contains a pair of points which already occurs in another triple. ".format(T))
                        is_PSTS = False
                    else: 
                        pairs.append([T[i],T[j]])
                        pairs.append([T[j],T[i]])
        if is_PSTS: 
            print("This is a PSTS. ")

    # pairs = []
    # n = len(point_set)
    # for i in range(n): 
    #     for j in range(i+1,n): 
    #         pairs.append([point_set[i],point_set[j]])

    # is_PSTS = True
    # for T in triples: 
    #     try: 
    #         pairs.remove([T[0],T[1]])
    #         pairs.remove([T[0],T[2]])
    #         pairs.remove([T[1],T[2]])
    #     except ValueError: 
    #         print("This pair of points appears in another triple.")
    #         is_PSTS = False
    
    # if is_PSTS: 
    #     if pairs == []: 
    #         print("This is an STS. ")
    #     else: 
    #         print("This is a PSTS.")