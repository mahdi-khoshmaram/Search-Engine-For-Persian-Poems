import os
from search import search
from indexer import index
from Evaluate import Eval


num =input("Enter one of numbers below:\n1.Search\n2.Index\n3.Statistics\n>>>")
se = input("Enter the method of preprocessing: ")
while True:
    if num == '1':
        input = input('Enter the query or the poem file name:')
        if input in os.listdir('./Poems'):
            with open(input, encoding="utf8") as fh:
                query = fh.read()
                search(query, se)
        else:
            print(search(input, se))
        # input("press enter to restart!")
        break

    if num == '2':
        index(se)
        input("press enter to restart!")
        break

    if num == '3':
        SElist= ['SE0','SE1','SE1_prime','SE2','SE2_prime','SE3','SE3_prime','SE4','SE4_prime']
        for i in SElist:
            Eval(i)
        input("press enter to restart!")
        break

    else:
        print('Enter between 1,2,3')
        continue

