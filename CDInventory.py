#------------------------------------------#
# Title: CDInventory.py
# Desc:  Script for Assignment 05
# Change Log: (Who, When, What)
# Andrew Kirkland, 2021-Feb-14, Created File
#------------------------------------------#

# Declare variabls

strChoice = '' # User input
dicRow1 = {'id': 1, 'Song': 'Fireman', 'Artist': 'Lil Wayne'}
dicRow = {}
dicRowNew = {}
new_CD_list = []
lstTbl = []  # list of lists to hold data
# TODO replace list of lists with list of dicts
lstRow = []  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    elif strChoice == 'l':
        # TODO Add the functionality of loading existing data
        print('ID, Song, Artist ')
        with open('CDInventory.txt','r') as f:
            for line in f:
                print(line, end = '')
            print()
    if strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data    
       dicRow['id'] = int(input('Enter an ID: '))
       dicRow['song'] = input('Enter a song: ')
       dicRow['Artist'] = input('Enter the artist: ')
       
       dicRowNew = [dicRow['id'],dicRow['song'],dicRow['Artist']]
       new_CD_list.append(dicRowNew)
       lstTbl.append(dicRow)
    
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, Song, Artist')
        for row in new_CD_list:
            for item in row:
               print(item, end = '| ')
            print()
    elif strChoice == 'd':
        with open('CDInventory.txt') as old, open('CDInventory.txt', 'w') as new:
            lines = old.readlines()
            new.writelines(lines[:-1])
        pass   
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open('CDInventory.txt', 'a')
        strRow = ''
        for item in new_CD_list:            
            strRow += ("{},{},{}\n".format(*item))
            
        strRow = strRow[:-1] + '\n'
        objFile.write(strRow)
        objFile.close()
    else:
        print('Please choose either l, a, i, d, s or x!')

