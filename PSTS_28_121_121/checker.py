from helper_methods import * 

def checker(): 
    n = 28
    point_set = list(range(n))

    triples = txt_to_list_of_triples('PSTS_28_121_121/data/triples.txt',str_to_int=True)

    is_PSTS_checker(triples, point_set)

    APCs = txt_to_dict_of_APCs('PSTS_28_121_121/data/APCs.txt', str_to_int=True)

    is_APCs_checker(APCs, point_set)
    has_APCs_checker(triples, APCs)

if __name__ == '__main__': 
    checker()