####################################################################
## FUNCTION FOR DIFFERENTIATING CASES OF DUPLICATE COLUMN
## add _(incremental_integer) at the tail of the duplicated column
###################################################################
## sub_function for getting the list of the duplicated string
def list_duplicates(seq):
    d = {}
    for i in seq:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    dups = []
    for i in d:
        if d[i] > 1:
            dups.append(i)
    return dups

## sub_function adding _(incremental_integer) at the tail of the duplicated_string
def differentiate_duplicate(col_list, dup_string):
    i = 1
    for x in range(len(col_list)):
        if(col_list[x] == dup_string):
            col_list[x] = col_list[x]+'_'+str(i)
            i = i + 1
    return col_list

##MAIN UNIQUIFY FUNCTION##
##CALL THIS FUNCTION TO THE LIST
def uniquify_list(col_list):
    duplicate_list = list_duplicates(col_list)
    for dupl in duplicate_list:
        differentiate_duplicate(col_list, dupl)
    return col_list