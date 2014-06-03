def flatten_list(a, result):
    if result is None:
        result = []
    for x in a:
        if isinstance(x, list):
            flatten_list(x,result)
        else:
            result.append(x)
    return result


def flatten_dict(d,result=None):
    if result is None:
        result = {}

    for k,v in d.items():
        if isinstance(v, dict):
            tmp = flatten_dict(v)
            for k1,v1 in tmp.items():
                key = '%s.%s' % (k,k1)
                result[key] = v1
        else:
            result[k] = v
    return result

def unflattern_dict(d, result=None):
    pass

def tree_map(lambda_function, nested_list):
    pass

def tree_reverse(nested_list):
    n = len(nested_list)
    if n == 1:
        return nested_list[:]
    if n > 1:
        return nested_list[n-1:] + tree_reverse(nested_list[:n-1])

d = {'a': 1, 'b': {'x': 2, 'y': {'d': 4, 'z': 5}}, 'c': 4}
print flatten_dict(d)
#nested_list = [6,3, 2, 1]
#nested_list = [6, [[5, 4], 3], [2, 1]]
#[[1, 2], [3, [4, 5]], 6]
#[6, [[5, 4], 3], [2, 1]]
#print tree_reverse(nested_list)
