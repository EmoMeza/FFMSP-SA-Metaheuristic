import Resources.Functions.UtilityFunctions as uf
import Resources.Services.FileManager as fm
import Resources.Functions.GRASP as grasp
import sys

def main():
    file_name=sys.argv[2]
    threshold=sys.argv[4]
    sequences=fm.open_File_By_Name(file_name)
    threshold=0.8
    sequence,quality=grasp.GRASP(sequences,threshold)
    print(f'Best solution: {sequence} and the quality is {quality}')
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