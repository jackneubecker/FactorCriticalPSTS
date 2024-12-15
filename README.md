# FactorCriticalPSTS
Repository for data files and correctness checking scripts accompanying the designs provided in [*Partial Steiner triple systems with an almost parallel class missing any given point*, Darryn Bryant, Sara Davies and Jack Neubecker, *preprint*]. 

# Structure of the repository
There is a separate folder for each construction in the paper. The folder name is of the form `PSTS_n_xxx_yyy`, where n is the order of the design, xxx is the minimum number of triples constructed, and yyy is the maximum number of triples constructed. 

If you only need this repository for the purpose of avoiding typing out long lists of triples, these can be found in the subfolders named `data` which contain the relevant `.txt` files. Files in `data` have been given an appropriate name so you should be able to find what you need easily. For consistency, we have data files for every construction, even for constructions with lists of triples which are quite short. For files storing a list of triples, elements of each triple are space-separated, and triples are line-separated. For files storing a list of APCs, each APC is line-separated. On each line, first, the missed point is provided and then separated from the rest of the line by a semi-colon (`;`). Then, the triples which form an APC are comma-separated, with elements space-separated. 

Every folder also has a python script `checker.py` which can be run by itself to construct the design and run the appropriate checks. 

`helper_methods.py` contains a few methods which are used by other scripts. Broadly speaking, there are methods for: 
* extracting data from data files, 
* checking properties of a construction, and 
* frequent operations in some constructions. 
Even if you would like to write and run your own checks, perhaps comparing with these methods will be helpful. 

Finally, `meta_checker.py` is a script which executes all of the other checker scripts. This should run without error. 