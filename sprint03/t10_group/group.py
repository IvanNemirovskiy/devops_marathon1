import copy
import itertools as it

def group(to_group, keys):  # function takes two arguments: a dict to_group and a list keys of fields to group by
    for i in range(len(keys)):
        r_dict = dict()
        grouped = it.groupby(to_group, key=lambda n: n[keys[i]])
        for k, v in grouped:
                r_dict.update({k: list(v)})
        # for keys[i],v in res_dict.items():
        #     if keys[i]
        # res_dict_n = res_dict.pop(keys[i])

        return r_dict    # returns new dict that is grouped by the fields provided in the list of fields(in the order of the list)