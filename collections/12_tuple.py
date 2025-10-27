def ftuple():
    tuple = (True, 'A', "Anderson", (3 + 3j), ["green", "yellow"],  {'1':"Anderson"}, (1,2,3))
    print(tuple)
    print(tuple[3])
    print(tuple[:3])
    print(tuple[3:])
    print(tuple * 2)
    print(tuple[:7] + (1,2,3))


def ftuples():
    vtuple = ['hdsghdgs', 'jhdasjhdsj', 'klakldsakds', 'bcxvbcxv', 'gdsfgdfsgdas', 'rweqrewqr']
    print(len(tuple(vtuple)))
    print(max(tuple(vtuple)))
    print(min(tuple(vtuple)))
