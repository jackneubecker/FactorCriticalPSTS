from helper_methods import * 

def checker(): 
    n = 16
    point_set = list(range(n))

    triples = txt_to_list_of_triples('PSTS_16_29_35/data/triples.txt',str_to_int=True)

    is_PSTS_checker(triples, point_set)

    APCs = txt_to_dict_of_APCs('PSTS_16_29_35/data/APCs.txt', str_to_int=True)

    is_APCs_checker(APCs, point_set)
    has_APCs_checker(triples, APCs)

    extra_triples = txt_to_list_of_triples('PSTS_16_29_35/data/extra_triples.txt',str_to_int=True)

    extra_triples_checker(triples, extra_triples, point_set)

if __name__ == '__main__': 
    checker()