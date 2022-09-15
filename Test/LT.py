with open('input_val') as f:
    file_contents = f.readline()
    file_without_samsung = file_contents.split('samsung')

    for i in file_without_samsung:
        print(i)



    #samsung,'OEM Samsung Chrome Washing Machine Washplate Pulsator Cap Shipped With WA52M7750AV, WA52M7750AV/A4, WA52M7750AW, WA52M7750AW/A4',91995

    #extract combo list from the main item
    #extract price from the combo string containg brand_name, prod_name, price
    #key value pair for price, string containg brand_name, prod_name




