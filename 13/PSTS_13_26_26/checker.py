from helper_methods import * 

n = 13

starter_triples = txt_to_list_of_triples('13/PSTS_13_26_26/data/starter_triples.txt',str_to_int=True)

triples = []
for i in range(n): 
    for T in starter_triples: 
        triples.append(sorted([(T[j]+i)%n for j in range(len(T))]))

is_PSTS_checker(triples,point_set = list(range(13)))

APCs = txt_to_list_of_lists_of_triples('13/PSTS_13_26_26/data/APCs.txt', str_to_int=True)

has_APCs_checker(triples, APCs)