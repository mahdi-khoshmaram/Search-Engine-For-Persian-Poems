from Assesment import assesment
from search import search

def Eval(method):
    tests= assesment()
    TP,FP,FN=0,0,0
    for test in tests:
        tp,fp,fn,avg_Precision=0,0,0,0
        realOutput = search(test[0],method)
        expectedOutput = test[1]
        for result in expectedOutput:
            if result in realOutput :
                tp+=1
                realOutput.remove(result)
            else:
                fn+=1
        fp +=  len(realOutput)
        avg_Precision+= tp / (tp+fp)
        # print(tp / (tp+fp))
        FP+=fp
        TP+=tp
        FN+=fn
    precision = TP / (TP+FP)
    recall = TP / (TP +FN)
    f_measure = (2*precision*recall/precision+recall)
    avg_Precision = avg_Precision / len(tests)

    # with open('finalResults.txt','a') as fh:
    #         fh.write(f'{method}\nprecision= {precision}\nrecal= {recall}\nFmeasure= {f_measure}\navg_precision= {avg_Precision}\n\n')
    # with open('temp.txt','a') as h:
    #     h.write(f'{precision,recall,f_measure,avg_Precision}\n')
    return precision, recall, f_measure, avg_Precision   



# SElist= ['SE0','SE1','SE1_prime','SE2','SE2_prime','SE3','SE3_prime','SE4','SE4_prime']

# print('Please wait...')
# for se in SElist:
#     print(f'Evaluating {se}')
#     Eval(se)
