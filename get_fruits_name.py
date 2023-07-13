import csv
def get_frutis_name(data:str)->list:
    """
    This function returns the names of the fruits

    args:
        data: CSV file with the fruits data
    returns:
        list: list of fruits names
    """
    file = open('fruits.csv')
    reader = csv.reader(file)
    list1 = []
    for row in list(reader)[1:]:
        if row[0] != 'price':
            list1.append(row[0])

    return list1 

print(get_frutis_name('fruits.csv'))