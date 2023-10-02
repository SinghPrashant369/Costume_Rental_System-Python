import Display
import Rent
item_return=[]
item_brand=[]
def giveCostume():
    name=input("Enter the name of borrower: ")
    a=name+"_Bill"".txt"
    print("")
    print("++++++++++++++++++++++++")
    print(a)
    print("++++++++++++++++++++++++")
    print("")
    try:
        with open(a,"r") as f:
            lines=f.readlines()
            lines=[a.strip("$") for a  in lines]

        with open(a,"r") as f:
            data=f.read()
            print(data)
    except:
        print("")
        print("The Borrower's name is incorrect")
        print("")
        giveCostume()
    validation_of_returnId(name)
#def validation_of_returnId(len_costume_dictionary):
def validation_of_returnId(name):
    Display.display_costume()
    costume_dictionary=Display.d
    len_costume_dictionary=len(costume_dictionary)
    continue_loop=True
    while continue_loop==True:
        Id_Option=input("Enter the ID of costume you want to return: ")
        try:
            Id_Option=int(Id_Option)
            if Id_Option>0 and Id_Option<=len_costume_dictionary:
                print("Costume ID is: ",Id_Option)
                
                #call he validation_of_Quantity
                validation_of_returnQuantity(Id_Option,name)
                continue_loop=False
                
            else:

                print("")
                print("++++++++++++++++++++++++++++++++++++")
                print("Please provide a valid costume ID!!!")
                print("++++++++++++++++++++++++++++++++++++")
                print("")
                Display.display_costume()
                continue_loop=True  
        except Exception as ae:
                print("")
                print(ae)
                print("+++++++++++++++++++++++++")
                print("Invalid Input!!!")
                print("Plase input an Option!!!!")
                print("+++++++++++++++++++++++++")
                print("")
                Display.display_costume()
                continue_loop=True
    #return Id_Option
def validation_of_returnQuantity(costume_Id,name):
    Id_Option=costume_Id
    costume_dictionary=Display.d
    len_costume_dictionary=len(Display.d)
    selected_item=costume_dictionary[Id_Option]
    continue_loop=True
    while continue_loop==True:
        quantity=int(input("Enter the quntity that you want to return: "))
        try:
            update_qty=int(selected_item[3])+quantity
            selected_item[3]=str(update_qty)
            item_return.append(selected_item[0])
            item_brand.append(selected_item[1])
            print("")
            print("Is the date of returning is more than 5 days?")
            choosen=input("Press Y for Yes otherwise press anything.")
            if(choosen.upper()=="Y"):
                day=int(input("By how many days that costume returned was late: "))
                perDayFine=3
                print(perDayFine)
                TotalFine=(perDayFine*day)
                print("total fiine: ",TotalFine)
 
                q=open("Returner_"+name+".txt","w")
                q.write("\t\t\t\t\t Costume Rental Shop\n")
                q.write("Returned By: "+name+"\n")
                q.write("Date:"+Rent.date_time()+"\n\n")
                q.write("Total fine: $"+str(TotalFine)+"\n")
                q.write("_______________________________________________________________\n")
                q.write("S.N\t\tCostume name\t\tcostume Brand\n")
                for sn in range(len(item_return)):
                    for i in range(len(item_return)):
                        for j in range(len(item_brand)):
                            q.write(str(sn+1)+"\t\t"+item_return[i]+"\t\t"+item_brand[j]+"\n")
                q.write("________________________________________________________________\n")         
                q.close()
                
              
            else:
                print("")
                print("Thank your for returning in time.")
                print("")

            

            #call stock_update() function
            stock_update()
            print(Display.d)
            print()
            print("")
            '''print("Do you want return more costume?")
            opt=input("Enter Y to return more otherwise enter anythin:")
            if opt.upper()=="Y":
                validation_of_returnId(name)
            else:
                print("Thank you")'''
            continue_loop=False
        except Exception as ae:
            print("")
            print("++++++++++++++++++++++++++")
            print("Invalid Input")
            print("Please input an Option invalid quatity")
            print("++++++++++++++++++++++++++")
            print("")
            continue_loop=True
def stock_update():
    print("")
    print("=============")
    print("Stock updated")
    print("=============")
    print("")
    f=open("Costume.txt","w")
    for value in Display.d.values():
        String=",".join(value)
        f.write(String)
        f.write("\n")
    f.close            
    
def generate_returnbill(name,item_return,item_brand):
    return_dateTime=Rent.date_time()
    print("")
    print("=========================================")
    print("\t\t Bill Details \t\t")
    print("=========================================")
    print("")
    print("Name of the customer: ",Name)
    print("Date and time of return: ",return_dateTime)
    print("Items that are returned: ",item_return)
    print("Brand of Items: ",item_brand)



    
    
                    
    

    
    

    
    
                    
    
