import csv 
def get_cheapest_fruit(data: str) -> str:
    """
    This function returns the name of the cheapest fruit

    args:
        data: CSV file with the fruits data
    returns:
        str: name of the cheapest fruit
    """
    # your code here
    file = open('fruits.csv')
    reader = csv.reader(file)
    list1 = []
    list2 = [] 
    for row in reader:
        if row[1] != 'price':
            list1.append(row[0])
            list2.append(row[1])

    s = ''
    min = list2[0]
    for i in range(1,len(list2)):
        if float(list2[i]) < float(min):
            min = list2[i]
            s = list1[i]

    return s 

print(get_cheapest_fruit('fruits.csv'))