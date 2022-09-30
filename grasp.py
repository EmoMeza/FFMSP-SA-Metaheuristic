import Resources.Services.FileManager as fm
import Resources.Functions.HammingFunctions as hf
import Resources.Functions.GraspFunctions as grsp
import sys
from time import sleep
import time
import threading
from Resources.Functions.GraspFunctions import solutions




def timer(seconds):

    for i in range(seconds):
        # hour = int((seconds-i)/3600)
        # minute = int(((seconds-i)%3600)/60)
        # second = int(((seconds-i)%3600)%60)
        # print("Time: %02d:%02d:%02d" % (hour, minute, second))
        sleep(1)
    return True
    
    




def main():
    file_name=sys.argv[2]
    seconds=sys.argv[4]
    t=threading.Thread(target=timer,args=[int(seconds)])
    sequences=fm.open_File_By_Name(file_name)
    threshold=0.8
    t.start()
    metric=hf.min_Hamming_Distance(sequences,threshold)
    current_time=time.time()
    grsp.GRASP(sequences,threshold,t,metric,current_time)
    #print the quality and time of all the solutions found during the execution and also print the answer on the last line
    for solution in solutions:
        print(f'Quality: {solution[1]} Time: {solution[2]}')
        if(solution==solutions[-1]):
            print(f'Best Solution Found: {solution[0]}')
    return 0

if __name__ == '__main__':
    if(len(sys.argv)==1):
        print("Incorrect execution:\tNo Arguments\n")
        print("For help, enter the following argument:")
        print("\tpython3 grasp.py -h")

    elif(len(sys.argv)==2 and sys.argv[1]=="-h"):
        print("\t\t\t~~~~~~~~")
        print("\t\t\t| Help |")
        print("\t\t\t~~~~~~~~\n")
        print("For correct execution of the program, you must enter the following arguments:\n")
        print("\tpython3 grasp.py -i [Filename] -t [MaxTimeInSeconds]\n")
        print("Example: python3 grasp.py -i sequences.txt -t 6000")
        print("This program will display the time and quality of the solution obtained")

    elif((len(sys.argv)==5 and sys.argv[1]=="-i" and sys.argv[3]=="-t")):
        main()
    else:
        print("Incorrect execution")
        print("For help, enter the following argument:")
        print("python3 grasp.py -h")
        