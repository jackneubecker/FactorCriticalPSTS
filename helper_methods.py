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
    is contained in more than one triple. Elements of triples must be 
    comparable. """
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
                    pair = sorted([T[i],T[j]])
                    if pair in pairs: 
                        print("{0} contains a pair of points {1} which already occurs in another triple. ".format(T,pair))
                        is_PSTS = False
                    else: 
                        pairs.append(pair)
        if is_PSTS: 
            print("This is a PSTS. ")

def has_APCs_checker(triples, APCs): 
    """Takes a list of sorted triples and a list of APCs and checks that each 
    triple in each APC is a triple in the list of triples. Elements of triples 
    must be comparable. """
    valid_APCs = True
    for APC in APCs: 
        for T in APC: 
            T = sorted(T)
            if T not in triples: 
                print("{0} is not a triple in the PSTS. ".format(T))
                valid_APCs = False
    if valid_APCs == True: 
        print("All APCs are in the PSTS. ")