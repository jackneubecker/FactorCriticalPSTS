from helper_methods import * 
import importlib
import sys 

importlib.reload(sys.modules['helper_methods'])

n = 43
point_set = list(range(n))

starter_triples = txt_to_list_of_triples('43/PSTS_43_86_301/data/starter_triples.txt',str_to_int=True)

triples = []
for i in range(n): 
    for T in starter_triples: 
        triples.append(sorted([(T[j]+i)%n for j in range(len(T))]))

is_PSTS_checker(triples,point_set = list(range(n)))

APCs = txt_to_dict_of_APCs('43/PSTS_43_86_301/data/APCs.txt', str_to_int=True)

is_APCs_checker(APCs, list(range(n)))
has_APCs_checker(triples, APCs)

extra_starter_triples = txt_to_list_of_triples('43/PSTS_43_86_301/data/extra_starter_triples.txt',str_to_int=True)

extra_triples = []
for i in range(n): 
    for T in extra_starter_triples: 
        extra_triples.append(sorted([(T[j]+i)%n for j in range(len(T))]))

extra_triples_checker(triples, extra_triples, point_set)