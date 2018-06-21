# Jelle Bosscher - 10776583
# functions.py hold all functions used for the project

# helper function to turn the CSV formatted dict to use in python
def csv_dict_to_py_dict(csv_string):
    if '::' in csv_string:
        py_dict = dict((key, int(value)) for key, value in (item.split('::') for item in csv_string.split('||')))
    elif ':' in csv_string:
        py_dict = dict((key, int(value)) for key, value in (item.split(':') for item in csv_string.split('|')))
    return py_dict



