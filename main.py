import pandas as pd
from pandas import read_excel
from itertools import combinations, permutations
from itertools import chain


# to get the last taple :k for num of combinations ffl for fillterd first table
def apriori(c, ffl):
    l = ffl.keys()
    if (c >2):
        l = set(chain(*ffl.keys()))

    nl = combinations(l, c)

    nextlevel = {}
    for item in nl:
        #item=[item]
        count = 0
        for record in records:

            if (set(item).issubset(set(record))):
                count += 1
                # dict = dict.fromkeys(unique_item, count)
        nextlevel[item] = int(count)

    fnl = {}
    for k, v in nextlevel.items():
        if v >= minsupp:
            fnl[k] = v

    print("fnl")
    print(fnl)
    unique = set(chain(*fnl.keys()))

    if len(fnl) == 1:
        print(ffl)
        return fnl
    elif len(fnl) == 0:
        print("ffl")
        print(ffl)
        return ffl
    elif len(unique) > c:  # بالطريقه ديه حتي لو انا معايا 4 item هيقف لما الكومبينيشن تجيب 4
        if (c==2):
            return apriori((c + 1), fnl)
        return (fnl)


def assosiation (last,n):
    assosiations = []
    lll=last.keys()
    for i in lll:
      assosiations.append(list(permutations(i, n)))

    return assosiations


def calc_conf(assos,n):
    supl = 0
    supr = 0
    if n==2:
        for i in assos:
            for j in i:
                left = j[0]
                right = j[1]
                supl = firstlevel[left]
                supr = firstlevel[right]
                if (supr != 0):
                    conf = supl / supr
                    if conf >= minconf:
                        print(j)
                        print(conf)
    if n >= 3:

        for i in assos:
            left = []
            right = []
            supl = 0
            supr = 0
            for j in i:
                supl = 0
                supr = 0
                left = [(j[0])]
                right = (j[1:])

                for record in records:
                    if (set(left).issubset(set(record))):
                        supl += 1
                    if (set(right).issubset(set(record))):
                        supr += 1

                if (supr != 0):
                    conf = supl / supr
                    if conf >= minconf:
                        print("left", left, "right", right)
                        print(conf)

                left = (j[0], j[1])
                right = [(j[-1])]
                supl = 0
                supr = 0
                for record in records:
                    if (set(left).issubset(set(record))):
                        supl += 1
                    if (set(right).issubset(set(record))):
                        supr += 1

                if (supr != 0):
                    conf = supl / supr
                    if conf >= minconf:
                        print("left", left, "right", right)
                        print(conf)

if __name__ == "__main__":
    # load the data
    df = pd.read_excel('CoffeeShopTransactions.xlsx', sheet_name='Sheet1')
    df.drop(['Date', 'Time', 'TransactionNumber'], axis='columns', inplace=True)

    # take first 50 records to try at first
    records = []
    for i in range(0, 9958):
        records.append([str(df.values[i, j]) for j in range(0, 3)])


    minsupp = int(input("Enter your minsupp: "))
    minconf = float(input("Enter your minconf: "))

    # get items(unique)
    unique_item = df.Item3.unique()
    # first level table
    firstlevel = {}
    for item in unique_item:
        count = 0
        for record in records:
            if item in record:
                count += 1
                # dict = dict.fromkeys(unique_item, count)
        firstlevel[item] = int(count)

    # fillterd first table
    ffl = dict()
    for k, v in firstlevel.items():
        if v >= minsupp:
            ffl[k] = v

    print(ffl)  # print frist level

    last = apriori(2, ffl)
    print(last)
    for i in last:
        n =len(i)

    assos=assosiation(last,n)

    calc_conf(assos,n)
