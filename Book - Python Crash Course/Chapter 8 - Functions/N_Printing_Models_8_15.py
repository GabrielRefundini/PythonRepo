# Put the functions for the example printing_models.py 
# in a separate file called printing_functions.py. 
# Write an import statement at the top of printing_models.py, 
# and modify the file to use the imported functions.

import N_Printing_Functions_8_15 as pf

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)