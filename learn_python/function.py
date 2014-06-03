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

#>>> treemap(lambda x: x*x, [1, 2, [3, 4, [5]]])
#[1, 4, [9, 16, [25]]]
def tree_map(f, nested_list):
    n = len(nested_list)
    result = []
    for x in range(0,n):
        if isinstance(nested_list[x],list):
            result.append(tree_map(f, nested_list[x]))
        else:
            result.append(f(nested_list[x]))
    return result

def tree_reverse(nested_list):
    n = len(nested_list)
    if n-1 >= 0:
        print n-1, nested_list[n-1]
        tmp = tree_reverse(nested_list[:n-1])
        if isinstance(nested_list[n-1], list):
            if tmp:
                return [tree_reverse(nested_list[n-1])]+(tmp)
            else:
                return tree_reverse(nested_list[n-1])
        else:
            if tmp:
                return [nested_list[n-1]] + tmp
            else:
                return [nested_list[n-1]]

    return []

def tree_reverse2(nested_list):
    n = len(nested_list)
    result = []
    for x in range(n-1,-1,-1):
        if isinstance(nested_list[x], list):
            result.append(tree_reverse2(nested_list[x]))
        else:
            result.append(nested_list[x])
    return result

def unflatten(dictionary):
    resultDict = dict()
    for key, value in dictionary.iteritems():
        parts = key.split(".")
        d = resultDict
        for part in parts[:-1]:
            if part not in d:
                d[part] = dict()
            d = d[part]
        d[parts[-1]] = value
    return resultDict

d = {'a': 1, 'b': {'x': 2, 'y': {'d': 4, 'z': 5}}, 'c': 4}
d = {'a' : 'b', 'c.d' : 'z', 'c.e' : 1, 'c.d.e': 3}
#print flatten_dict(d)
#nested_list = [1,[2,3]]
#nested_list = [6, [[5, 4], 3], [2, 1]]
#nested_list = [[1, 2], [3, [4, 5]], 6, [6,7]]
#nested_list = [1, 2, 3, 4, 5, 6]
#nested_list = [[3,5],6, [[5, 4], 3], [2, 1]]
#print tree_reverse2(nested_list)
#print tree_map(lambda x: x*2, nested_list)
print unflatten(d)















