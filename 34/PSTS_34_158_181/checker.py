from helper_methods import * 
import importlib
import sys 

importlib.reload(sys.modules['helper_methods'])

n = 34 

starter_triples = txt_to_list_of_triples('34/PSTS_34_158_181/data/starter_triples.txt', str_to_int=True)

print(starter_triples)