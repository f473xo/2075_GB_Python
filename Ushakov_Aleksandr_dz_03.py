def thesaurus(*args) -> dict:
    dict_out = {}
    for name in sorted(args):
        key = name[0]
        dict_out.update({key: []})
    for elem in dict_out.keys():
        names = []
        for i in sorted(args):
            if elem == i[0]:
                names.append(i)
        dict_out.update({elem: names})
    return dict_out


print(thesaurus("Иван", "Мария", "Петр", "Илья"))
