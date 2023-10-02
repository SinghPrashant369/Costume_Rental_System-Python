import Display
import datetime
item_rent=[]
item_brand=[]
item_price=[]
def validation_of_Id(len_costume_dictionary):
    grant=False
    while grant==False:
        try:
            Id_Option=int(input("Enter the ID of costume you want to rent: "))
            if Id_Option>0 and Id_Option<=len_costume_dictionary:
                print("Costume ID is",Id_Option)       
                qnt=0
                costume_dictionary=Display.d
                selected_item=costume_dictionary[Id_Option]
                if qnt==int(selected_item[3]):
                    print("")
                    print("++++++++++++++++++++++++++++++++++++++++++++++++")
                    print("Sorry! This item is not available at the moment.")
                    print("++++++++++++++++++++++++++++++++++++++++++++++++")
                    print("")
                    break
                #_________________________________________________________
                print("")
                print("++++++++++++++++++++")
                print("Costume is available")
                print("++++++++++++++++++++")
                print("")

                quantity=int(input("Enter the quantity of costume: "))
                validation_of_Quantity(quantity,Id_Option)
                grant=True
            else:
                print("")
                print("++++++++++++++++++++++++++++++++++++")
                print("Please provide a valid costume ID!!!")
                print("++++++++++++++++++++++++++++++++++++")
                print("")
                Display.display_costume()
                grant=False
        except Exception as ae:
            print("")
            print(ae)
            print("+++++++++++++++++++++++++")
            print("Invalid Input!!!")
            print("Please input an Option!!!!")
            print("+++++++++++++++++++++++++")
            print("")
            Display.display_costume()
    return Id_Option

def validation_of_Quantity(qty,Opt):
    quantity=qty
    Id_Option=Opt
    len_costume_dictionary=len(Display.d)
    costume_dictionary=Display.d
    selected_item=costume_dictionary[Id_Option]
    if quantity<=int(selected_item[3]):
        print("Quantity is available")
        update_qty=int(selected_item[3])-quantity
        selected_item[3]=str(update_qty)

        item_rent.append(selected_item[0])
        item_brand.append(selected_item[1])
        item_price.append(float(selected_item[2].strip().strip("$"))*quantity)

        #call stock_update() function
        stock_update()
        print(Display.d)
        loop=True
        while loop==True:
            print("")
            choice=input("Do you want to rent further items?\nEnter 'Yes' to rent additional items if not then enter anything : ")
            if choice.upper()=="YES":
                Display.display_costume()
                validation_of_Id(len_costume_dictionary)
            else:
                generate_bill()
                
                #_____________________________
                print("")
                print("++++++++++++++++++++++++++++++++++++++++++++++++++")
                print("Thank you for choosing our rental product.")
                print("If yor want to rent some more Items then press 1: ")
                print("Otherwise press 3 to exit.")
                print("++++++++++++++++++++++++++++++++++++++++++++++++++")
                print("")
                #____________________________
            loop=False
                    
        
    else:
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Quantity provided is greater than what we have in stock!!!")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print(Display.d)
        print("")

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
def date_time():
    current_dt=datetime.datetime.now()
    YYYY=str(current_dt.year)
    MM=str(current_dt.month)
    DD=str(current_dt.day)
    hrs=str(current_dt.hour)
    minutes=str(current_dt.minute)
    sec=str(current_dt.second)
    rent_dt=YYYY+"-"+MM+"-"+DD+" "+hrs+":"+minutes+":"+sec
    return rent_dt

#_____________________    
#_______________________
def generate_bill():
    #________________________
    customer_name=input("Enter your name: ")
    #_________________________
    rent_dateTime=date_time()
    
    print("")
    print("=============================================================")
    print("\t\t Bill Details \t\t")
    print("=============================================================")
    print("")
    print("*************************************************************")
    print("Name of the customer: ",customer_name)
    print("Date and time of borrow: "+rent_dateTime)
    #print("Items in rent are: ",item_rent)
    #________________________________________________
    unique_item_list=[*set(item_rent)]
    print("Items in rent are: ",unique_item_list)
    #________________________________________________
    #print("Brands of Items are: ",item_brand)
    #_______
    unique_brand_list=[*set(item_brand)]
    print("Brands of Items are: ",unique_brand_list)
    #________
    
    print("Total Amount: $",sum(item_price))
    print("*************************************************************")

    print("")
    print("\t","♨︎------------------------------------♨︎")
    print("\t","|Rent details bill has been generated|")
    print("\t","♨︎------------------------------------♨︎")
    print("")
    #____________________________________________________
    generateTxtBill(customer_name,rent_dateTime,unique_item_list,unique_brand_list)

def generateTxtBill(CustomerName,date_time,items,brands):
     file = open(CustomerName+"_Bill"+".txt", "w")
     file.write("Customer Name: ")
     file.write(CustomerName+"\n")
     file.write("Date Time of borrow: "+date_time+"\n")
     file.write("Total Price: $")
     file.write(str(sum(item_price)))
     file.write("\n")
     file.write("Items in rent are: ")
     file.write("\n")
     #for printing the s.n items and it's brand
     for sn in range(len(items)):
         for i in range(len(items)):
             for j in range(len(brands)):
                 if sn==i==j:
                     file.write(str(sn+1)+". "+items[i]+":-"+brands[j])
                     file.write("\n")
     file.close()


#__________________





            
            
                

            
