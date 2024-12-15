from helper_methods import * 

def checker(): 
    n = 22
    point_set = list(range(n))

    triples = txt_to_list_of_triples('22/PSTS_22_63_73/data/triples.txt',str_to_int=True)

    is_PSTS_checker(triples, point_set)

    APCs = txt_to_dict_of_APCs('22/PSTS_22_63_73/data/APCs.txt', str_to_int=True)

    is_APCs_checker(APCs, point_set)
    has_APCs_checker(triples, APCs)

    extra_triples = txt_to_list_of_triples('22/PSTS_22_63_73/data/extra_triples.txt',str_to_int=True)

    extra_triples_checker(triples, extra_triples, point_set)

    for T in triples+extra_triples: 
        if 0 in T: 
            if 1 in T or 2 in T or 3 in T: 
                print("{0} has a bad pair. ")

if __name__ == '__main__': 
    checker()