import functools


def multiplier(num_list):

        if not isinstance(num_list, list) or not isinstance(all(num_list), (int, float) ):
            raise ValueError("The given data is invalid.")
        else:
            return functools.reduce(lambda a, b: a*b, num_list)



        # res = 1
        # for x in num_list:
        #     res = res * x
        # print(res)
