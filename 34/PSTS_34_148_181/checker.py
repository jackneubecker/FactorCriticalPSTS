from helper_methods import * 

def checker(): 
    n = 34 

    point_set = list(range(n))

    starter_triples = txt_to_list_of_triples('34/PSTS_34_148_181/data/starter_triples.txt', str_to_int=True)

    A1_triples = []
    for i in range(n-1): 
        for T in starter_triples: 
            A1_triples.append(sorted([(T[j]+i)%(n-1) for j in range(len(T))]))

    # we represent infty with 33 for compatibility with sorted() 
    A2_triples = [sorted([33, 2*i+1, 2*i+2]) for i in range(int((n-2)/2))]

    triples = A1_triples + A2_triples

    is_PSTS_checker(triples,point_set)

    APCs = txt_to_dict_of_APCs('34/PSTS_34_148_181/data/APCs.txt', str_to_int=True)

    is_APCs_checker(APCs, point_set)
    has_APCs_checker(triples, APCs)

    extra_starter_triples = txt_to_list_of_triples('34/PSTS_34_148_181/data/extra_starter_triples.txt', str_to_int=True)

    extra_triples = [] 
    for i in range(n-1): 
        for T in extra_starter_triples: 
            extra_triples.append(sorted([(T[j]+i)%(n-1) for j in range(len(T))]))

    extra_triples_checker(triples, extra_triples, point_set)

if __name__ == '__main__': 
    checker()