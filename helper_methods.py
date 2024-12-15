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

def txt_to_dict_of_APCs(filename, str_to_int = False): 
    """Takes a .txt file representing a list of APCs and converts 
    this to a dictionary of APCs with each APC represented by a list of triples. 
    Each line in the txt file is prefixed by the point which is missed by the 
    APC, then a semi-colon (;), then a list of comma-separated triples, with 
    space-separated elements of each triple. Optionally converts elements of 
    the triples to integers. """
    with open(filename) as f: 
        lines = f.read().splitlines()
    dict_of_APCs = {}
    for line in lines: 
        line = line.strip().split(';')
        missed_pt = line[0].strip()
        if str_to_int: 
            missed_pt = int(missed_pt)
        APC_str = line[1].strip()
        list_A = []
        A = APC_str.split(sep=',')
        for a in A: 
            a = a.strip()
            T = a.split(sep=' ')
            if str_to_int: 
                for i in range(len(T)): 
                    T[i] = int(T[i])
            list_A.append(T)
        if missed_pt in dict_of_APCs: 
            raise ValueError("{0} occurs as the missed point multiple times. ".format(missed_pt))
        else: 
            dict_of_APCs[missed_pt] = list_A
    return dict_of_APCs

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
                valid_elements = False
                raise ValueError("{0} contains an element {1} which is not a point. ".format(T,x))
    if valid_elements == True: 
        is_PSTS = True
        pairs = {}
        for T in triples: 
            for i in range(len(T)): 
                for j in range(i+1,len(T)): 
                    pair = tuple(sorted([T[i],T[j]]))
                    if pair in list(pairs.keys()): 
                        is_PSTS = False
                        raise ValueError("{0} contains a pair of points {1} which already occurs in another triple {2}. ".format(T,pair, pairs[pair]))
                    else: 
                        pairs[pair] = T
        if is_PSTS: 
            print("This is a PSTS({0}) with {1} triples. ".format(len(point_set), len(triples)))

def is_APCs_checker(APCs, point_set): 
    """Takes a list of APCs and checks that each APC is in fact an APC. That is, 
    that each point in the point_set occurs exactly once. """
    valid_APCs = True
    for missed_pt, APC in APCs.items(): 
        point_set_copy = point_set.copy()
        if missed_pt not in point_set: 
            valid_APCs = False
            raise ValueError("{0} is not in the point set. ".format(missed_pt))
        else: 
            point_set_copy.remove(missed_pt)
            for T in APC: 
                for x in T: 
                    if x not in point_set: 
                        valid_APCs = False
                        raise ValueError("{0} is not in the point set. ".format(x))
                    else: 
                        point_set_copy.remove(x)
        if point_set_copy != []: 
            valid_APCs = False
            raise ValueError("{0} are not included in {1}. ".format(point_set_copy, APC))
    if valid_APCs: 
        print("Each of the {0} given APCs is a disjoint set of triples containing every point except the missed point exactly once. ".format(len(APCs)))

def has_APCs_checker(triples, APCs): 
    """Takes a list of triples and a dict of APCs and checks that each 
    triple in each APC is a triple in the list of triples. Elements of triples 
    must be comparable. """
    sorted_triples = []
    for T in triples: 
        sorted_triples.append(sorted(T))
    valid_APCs = True
    for missed_pt in APCs: 
        APC = APCs[missed_pt]
        for T in APC: 
            T = sorted(T)
            if T not in sorted_triples: 
                valid_APCs = False
                raise ValueError("{0} is in the APC missing {1} but is not a triple in the PSTS. ".format(T, missed_pt))
    if valid_APCs == True: 
        print("Each of the triples in the {0} given APCs are in the PSTS. ".format(len(APCs)))

def extra_triples_checker(triples, extra_triples, point_set): 
    """Takes a list of triples and a list of extra_triples and checks that 
    the extra triples can be added to the set of triples while still being 
    a PSTS on the given point_set. Assumes triples is a valid set of triples 
    for a PSTS on point_set. """
    valid_elements = True
    for T in extra_triples: 
        for x in T: 
            if x not in point_set: 
                valid_elements = False
                raise ValueError("{0} contains an element {1} which is not a point. ".format(T,x))
    if valid_elements == True: 
        is_PSTS = True
        pairs = []
        for T in triples: 
            for i in range(len(T)): 
                for j in range(i+1,len(T)): 
                    pairs.append(sorted([T[i],T[j]]))
        for T in extra_triples: 
            for i in range(len(T)): 
                for j in range(i+1,len(T)): 
                    pair = sorted([T[i],T[j]])
                    if pair in pairs: 
                        is_PSTS = False
                        raise ValueError("{0} contains a pair of points {1} which already occurs in another triple. ".format(T,pair))
                    else: 
                        pairs.append(pair)
        if is_PSTS: 
            print("The {0} extra triples can be added to obtain a PSTS({1}) with any number of triples between {2} and {3} inclusively. ".format(len(extra_triples), len(point_set), len(triples), len(triples) + len(extra_triples)))

def three_rotational_constructor(m): 
    """Takes an integer m >= 8 and constructs a factor-critical PSTS(3m+1) 
    with (5/3)(3m) triples. Returns the point set and the set of triples. """
    point_set = ['{0}_{1}'.format(x,i) for i in range(1,m+1) for x in ['a','b','c']]
    point_set.append('infty')
    triples = []
    for i in range(m): 
        triples.append(['a_{0}'.format((2+i)%m + 1), 'a_{0}'.format((3+i)%m + 1), 'c_{0}'.format((1+i)%m + 1)])
        triples.append(['b_{0}'.format((1+i)%m + 1), 'b_{0}'.format((4+i)%m + 1), 'a_{0}'.format((2+i)%m + 1)])
        triples.append(['c_{0}'.format((2+i)%m + 1), 'c_{0}'.format((3+i)%m + 1), 'b_{0}'.format((1+i)%m + 1)])
        triples.append(['infty', 'a_{0}'.format((1+i)%m + 1), 'b_{0}'.format((2+i)%m + 1)])
        triples.append(['a_{0}'.format((1+i)%m + 1), 'b_{0}'.format((1+i)%m + 1), 'c_{0}'.format((1+i)%m + 1)])
    return point_set, triples

def three_rotational_APC_constructor(m): 
    """Takes an integer m >= 8 and constructs the necessary APCs to verify 
    that the PSTS(3m+1) constructed by three_rotational_constructor(m) is 
    factor-critical. """
    A4_base = [['a_2', 'a_3', 'c_1'], ['a_7', 'a_8', 'c_6'], 
               ['b_4', 'b_7', 'a_5'], ['b_5', 'b_8', 'a_6'], 
               ['c_2', 'c_3', 'b_1'], ['c_4', 'c_5', 'b_3'], 
               ['c_7', 'c_8', 'b_6'], ['infty', 'a_1', 'b_2']]
    B5_base = [['a_2', 'a_3', 'c_1'], ['a_5', 'a_6', 'c_4'],
               ['b_3', 'b_6', 'a_4'], ['c_2', 'c_3', 'b_1'], 
               ['c_5', 'c_6', 'b_4'], ['a_7', 'b_7', 'c_7'], 
               ['a_8', 'b_8', 'c_8'], ['infty', 'a_1', 'b_2']]
    C4_base = [['a_2', 'a_3', 'c_1'], ['a_6', 'a_7', 'c_5'],
               ['b_3', 'b_6', 'a_4'], ['b_4', 'b_7', 'a_5'],
               ['c_2', 'c_3', 'b_1'], ['c_6', 'c_7', 'b_5'],
               ['a_8', 'b_8', 'c_8'], ['infty', 'a_1', 'b_2']]
    for i in range(9,m+1): 
        A4_base.append(['a_{0}'.format(i), 'b_{0}'.format(i), 'c_{0}'.format(i)])
        B5_base.append(['a_{0}'.format(i), 'b_{0}'.format(i), 'c_{0}'.format(i)])
        C4_base.append(['a_{0}'.format(i), 'b_{0}'.format(i), 'c_{0}'.format(i)])
    
    APCs = {'a_4':A4_base, 'b_5':B5_base, 'c_4':C4_base}
    return APCs

def three_rotational_extra_triple_constructor(m,extra_starter_triples):
    """Takes an integer m >= 8 and constructs the orbit of the triples in 
    extra_starter_triples under the action of pi. Elements of 
    extra_starter_triples should be of the form ['x_i', 'y_j', 'z_k'], 
    with x,y,z elements of {a,b,c}, and i,j,k integers 
    from 1 to m inclusive. """
    # TODO: figure out infinity blocks and short order blocks
    extra_triples = []
    for T in extra_starter_triples: 
        if T[0] == 'infty': 
            y = T[1].split('_')[0]
            j = int(T[1].split('_')[1])
            z = T[2].split('_')[0]
            k = int(T[2].split('_')[1])
            for ell in range(m): 
                extra_triples.append(sorted(['infty', 
                                             '{0}_{1}'.format(y,(j+ell)%m + 1), 
                                             '{0}_{1}'.format(z,(k+ell)%m + 1)]))
        elif T[1] == 'infty': 
            x = T[0].split('_')[0]
            i = int(T[0].split('_')[1])
            z = T[2].split('_')[0]
            k = int(T[2].split('_')[1])
            for ell in range(m): 
                extra_triples.append(sorted(['{0}_{1}'.format(x,(i+ell)%m + 1), 
                                             'infty', 
                                             '{0}_{1}'.format(z,(k+ell)%m + 1)]))
        elif T[2] == 'infty': 
            x = T[0].split('_')[0]
            i = int(T[0].split('_')[1])
            y = T[1].split('_')[0]
            j = int(T[1].split('_')[1])
            for ell in range(m): 
                extra_triples.append(sorted(['{0}_{1}'.format(x,(i+ell)%m + 1), 
                                             '{0}_{1}'.format(y,(j+ell)%m + 1), 
                                             'infty']))
        else: 
            x = T[0].split('_')[0]
            i = int(T[0].split('_')[1])
            y = T[1].split('_')[0]
            j = int(T[1].split('_')[1])
            z = T[2].split('_')[0]
            k = int(T[2].split('_')[1])
            for ell in range(m): 
                extra_triples.append(sorted(['{0}_{1}'.format(x,(i+ell)%m + 1), 
                                      '{0}_{1}'.format(y,(j+ell)%m + 1), 
                                      '{0}_{1}'.format(z,(k+ell)%m + 1)]))
    duplicate_free_extra_triples = []
    for T in extra_triples: 
        if T not in duplicate_free_extra_triples: 
            duplicate_free_extra_triples.append(T)
    return duplicate_free_extra_triples