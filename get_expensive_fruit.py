import csv 
def get_expensive_fruit(data: str) -> str:
    """
    This function returns the name of the most expensive fruit

    args:
        data: CSV file with the fruits data
    returns:
        str: name of the most expensive fruit
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
    max = list2[0]
    for i in range(1,len(list2)):
        if float(list2[i]) > float(max):
            max = list2[i]
            s = list1[i]

    return s 

print(get_expensive_fruit('fruits.csv'))