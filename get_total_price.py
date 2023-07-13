import csv 

def get_total_price(data:str)->float:
    """
    This function returns the total price of the fruits

    args:
        data: CSV file with the fruits data
    returns:
        float: fruits total price
    """
    f = open('fruits.csv')
    rearder = list(csv.reader(f))[1:]
    sum = 0
    for row in rearder:
        sum+=float(row[1])
    
    return sum 

print(get_total_price('fruits.csv'))