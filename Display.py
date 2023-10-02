

costume_dic={}
def display_costume():
    #This flag is for user
    count=0
    #this is used to count number of data in dictionary
    print("=========================================================")
    print("ID \t Costume Name \t Costume Brand \t Price \tQuantity")
    print("=========================================================")
    #open the file from Costume.txt,set the txt file in reading mode and it is in same location of .py files
    file=open("Costume.txt","r")
    #read all the data from the a field
    costume_data=file.read()
    #splitting the number of string according to new lines and put them in a list
    costume_data=costume_data.split("\n")

    #This while loop is used to remove empty string in a list
    while("" in costume_data):
        costume_data.remove("")
    for i in range(len(costume_data)):
        count=count+1
        costume_dic[count]=costume_data[i].split(",")

    for key,value in costume_dic.items():
        print(key,end="\t")
        for i in value:
            print(i,end="\t")
        print("\n")
    print("========================================================")
    print("\n")
        
    #_____________
    return costume_dic
#display_costume()
d=costume_dic

   

    


