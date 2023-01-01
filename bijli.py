from banner import *
from hashtable_probing_method_input import *
from linked_hashtable_functions_input import *
from read_database_linear import *
from linear_hashtable_functions_input import *
from linked_list_hashtable_class import *
from read_database_linked import *


# printing BIJLI banner
printBanner()

#getting method
preferred_method = inputMethod()

if preferred_method == 1:

    # making linear Hash Table
    linear_hashtable = makeLinearHashTable()

    #reading Database
    readDatabaseLinear(linear_hashtable)

    #show options
    showOptions(linear_hashtable)


if preferred_method == 2:

    # making Linked List Hash Table
    linked_hashtable = makeLinkedHashTable()

    #reading Database
    readDatabaseLinked(linked_hashtable)

    #show options
    showOptionsLinked(linked_hashtable)
