import Resources.Functions.ProbabilisticGreedy as pg
import Resources.Functions.UtilityFunctions as uf
import Resources.Functions.HammingFunctions as hf

def GRASP(sequences,threshold):
    metric = hf.min_Hamming_Distance(sequences,threshold)
    for i in range(10):
        print(f'Iteration {i}')
        #build a  greedy randomized solution x:
        x=pg.Probabilistic_Greedy(sequences,threshold)
        print('x: ',x)
        #make a local search on x to obtain a local optimum x*:
        #x=localSearchPhase(x)

        #if x* is better than the best solution found so far, update the best solution:
        if i==0:
            best=x
        else:
            print(f'x: {x}')
            print(f'metric: {metric}')
            a=uf.answer_Quality(sequences,x,metric)
            b=uf.answer_Quality(sequences,best,metric)
            if a>b:
                print('new best')
                best=x
    return best,uf.answer_Quality(sequences,best,metric)


    return True
def constructionPhase():
    return True
def localSearchPhase():
    return True