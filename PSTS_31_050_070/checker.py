from helper_methods import * 

def checker(): 
    n = 31
    m = int((n-1)/3)

    point_set, triples = three_rotational_constructor(m)
    is_PSTS_checker(triples, point_set)

    APCs = three_rotational_APC_constructor(m)
    is_APCs_checker(APCs, point_set)
    has_APCs_checker(triples, APCs)

    extra_starter_triples = txt_to_list_of_triples('PSTS_31_050_070/data/extra_starter_triples.txt')
    extra_triples = three_rotational_extra_triple_constructor(m,extra_starter_triples)
    is_PSTS_checker(triples + extra_triples, point_set)

if __name__ == '__main__': 
    checker()