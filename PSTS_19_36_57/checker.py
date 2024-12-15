from helper_methods import * 

def checker(): 
    n = 19

    point_set = list(range(1,n+1))
    starter_triples = txt_to_list_of_triples('PSTS_19_36_57/data/starter_triples.txt',str_to_int=True)

    triples = []
    for T in starter_triples: 
        T_orbit = []
        for i in range(9): 
            T_i = []
            for x in T: 
                if x == 19: 
                    T_i.append(19)
                elif x == 9: 
                    T_i.append(1)
                elif x == 18: 
                    T_i.append(10)
                else: 
                    T_i.append(x+1)
            if sorted(T_i) not in T_orbit: 
                T_orbit.append(sorted(T_i))
            T = T_i.copy()
        triples.extend(T_orbit)
    is_PSTS_checker(triples, point_set)

    APCs = txt_to_dict_of_APCs('PSTS_19_36_57/data/APCs.txt', str_to_int=True)

    is_APCs_checker(APCs, point_set)
    has_APCs_checker(triples, APCs)

    extra_starter_triples = txt_to_list_of_triples('PSTS_19_36_57/data/extra_starter_triples.txt',str_to_int=True)
    extra_triples = []
    for T in extra_starter_triples: 
        T_orbit = []
        for i in range(9): 
            T_i = []
            for x in T: 
                if x == 19: 
                    T_i.append(19)
                elif x == 9: 
                    T_i.append(1)
                elif x == 18: 
                    T_i.append(10)
                else: 
                    T_i.append(x+1)
            if sorted(T_i) not in T_orbit: 
                T_orbit.append(sorted(T_i))
            T = T_i.copy()
        extra_triples.extend(T_orbit)

    extra_triples_checker(triples, extra_triples, point_set)

if __name__ == '__main__': 
    checker()