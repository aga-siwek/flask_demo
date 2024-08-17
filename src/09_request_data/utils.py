def dict_to_indexed_list(dic):
    un_indexed_list = dic.items()
    indexed_list = []

    for i, item in enumerate(un_indexed_list):
        data = (i + 1,) + item
        indexed_list.append(data)

    return indexed_list
