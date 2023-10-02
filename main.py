import Display
import Rent
import Return
#creating a functin mainFn 
def mainFn():     
    print("+++++++++++++++++++++++++++++++++++++")
    print("Welcome to Costome Rental Application")
    print("+++++++++++++++++++++++++++++++++++++\n\n")

    
    def main_Menu():
        #iterate till the while loop is true
        while True:
            print("Select a desirable option")
            print("(1) || Press 1 to rent a costume.")
            print("(2) || Press 2 to return a costume.")
            print("(3) || Press 3 to exit.")
            option=input("Enter an Option from 1 to 3: ")
            try:
                option=int(option)
                if option==1:
                    print("")
                    print("Let's rent a costume")
                    print("")
                    Display.display_costume()
                    costume_dictionary=Display.d   #dictionary
                    len_costume_dictionary=len(costume_dictionary) #length of dictionary
                    option=Rent.validation_of_Id(len_costume_dictionary)
                    print("")
                elif option==2:
                    print("")
                    print("Let's return a costume")
                    Display.display_costume()
                    costume_dictionary=Display.d
                    len_costume_dictionary=len(costume_dictionary)
                    #Return.validation_of_returnId(len_costume_dictionary)
                    Return.giveCostume()
                    
                    print("")
                elif option==3:
                    print("")
                    print("\t\t Thank you for using our application\t\t")
                    print("")
                    break
                else:
                    print("")
                    print("Invalid Input!!!")
                    print("Please select the value as per the provided options.")
                    print("")
            except Exception as ae:
                print("")
                print(ae)
                print("Please provide a value given in option.")
                print("")
    main_Menu()
mainFn()








