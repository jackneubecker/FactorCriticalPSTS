from helper_methods import * 
import importlib
import sys 

importlib.reload(sys.modules['helper_methods'])

n = 25
m = int((n-1)/3)

point_set, triples = three_rotational_constructor(m)
is_PSTS_checker(triples, point_set)

APCs = three_rotational_APC_constructor(m)
is_APCs_checker(APCs, point_set)
has_APCs_checker(triples, APCs)

extra_starter_triples = [['a_4', 'b_1', 'b_2'], ['infty', 'c_1', 'c_5']]
extra_triples = three_rotational_extra_triple_constructor()