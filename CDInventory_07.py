
# Title: Assignment07.py
# Desc: Working with classes and functions.
# Change Log: Eliana Arias-Dotson 2020, Jan 27 Created File
# Modified  : Eliana Arias-Dotson 2020, Jan 28 moved processing codes into functions
# Modified  : Eliana Arias-Dotson 2020, Jan 29 understanding flow
# Modified  : Eliana Arias-Dotson 2020, March 2 Workign script, editing docstrings 
# Modified  : Douglas Klos, 2020 March 3, Refactored functions, grading.
# Modified  : Eliana Arias-Dotson, 2020, March 7th-8th - Adding Exception clauses, pickling and cleaning up 
# Modified  : Eliana Arias-Dotson, 2020, March 9th - Cleaning up printing statements and test for submission
#------------------------------------------#
import pickle

# -- PROCESSING -- #
#Definition of Classes and functions:

class DataProcessor:
    """A set of functions to load, add and delete data from Magic Inventory"""
    @staticmethod
    def add_cd(cd_id, cd_title, cd_artist, table):  
        """Function to add new data to list.
        Args:
            cd_iD (string): ID representing the ID of the new CD
            cd_title (string): Title of the new CD
            cd_artist (string): Artist of the new CD
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime
    
        Returns:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime
        """
        new_cd = {'ID': cd_id, 'Title': cd_title, 'Artist': cd_artist}
        table.append(new_cd)
        return table
    
#function to delete delete_ID
    @staticmethod
    def delete_cd(cd_id, table):
        """Function to delete entry associated to a user data entry 
           to be deleted and searchs through the list of dict to delete the 
           ID entry 

        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime
        """
        # 3.5.1.2 ask user which ID to remove
        
        # 3.5.2 search thru table and delete CD
        intRowNr = -1
        blnCDRemoved = False
        try:
            for row in table:
                intRowNr += 1
                if row['ID'] != cd_id:
                    del table[intRowNr]
                    blnCDRemoved = False
                    #break
        except: 
            print('Could not find this CD!')
        else:
            if blnCDRemoved:
               print('The CD was removed')
        return table

        
class FileProcessor:
    """Processing the data to and from text file"""

    @staticmethod
    def read_file(file_name, table):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime
        """
        try:
            with open(file_name, 'r') as objFile:
            #objFile = open(file_name, 'r')
                table.clear()  # this clears existing data and allows to load data from file
                for line in objFile:
                    data = line.strip().split(',')
                    dicRow = {'ID': data[0], 'Title': data[1], 'Artist': data[2]}
                    table.append(dicRow)
                    # if we want to pickle the information on our dicRow:
                    pickle_out=open("dict.pickle","wb")
                    pickle.dump(dicRow,pickle_out)
                    pickle_out.close()
                objFile.close()
        except FileNotFoundError:
            print("The file {} could not be loaded, please check file location or create one".format(file_name))
        return table

    @staticmethod
    def write_file(file_name, table):
        
        """Function to write data to file from list

        Opens the data file with option to write, loops through the new row added to list 
        and adds the new entry to file
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None, Write to file 
        """
        try:
            with open(file_name, 'w') as objFile:
                for row in table:
                    lstValues = list(row.values())
                    lstValues[0] = str(lstValues[0])
                    objFile.write(','.join(lstValues) + '\n')
        except IOError:            
            print("Error! Couldnot find file or read data")
     
        

# -- PRESENTATION (Input/Output) -- #

class IO:
    """Handling Input / Output"""
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        try:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
            while choice not in ['l', 'a', 'i', 'd', 's', 'x']: 
                raise ValueError('That is not a valid choice!') 
        except ValueError as e:
            print(type(e))
            print('Please enter one of the offered options from menu') 
        else:   
            print("Thank you for entering a valid choise, please continue:")
            return choice
            
    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')

    @staticmethod
    def get_UserInput():
       """Function to accept User input

       Gets input from user for ID, Title and Artist to be save in table

       Args:
           None

       Returns:
           ID (string): ID representing the ID of the new CD
           Title (string): Title of the new CD
           Artist (string): Artist of the new CD
       """
       ValidID =False
       while not ValidID:
           try:
               ID = int(input('Enter ID: ').strip())
               if ID <=0:
                   raise ValueError('That is not a positive integer number!') 
           except ValueError:
               print('Please enter ID using positive integers')
           else:
               ValidID=True
       Title = input('What is the CD\'s title? ').strip()
       Artist = input('What is the Artist\'s name? ').strip()
       return ID, Title, Artist
    
        
# MAIN PROCESSING    
# -- DATA -- #
strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {}  # dictionary of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object
strID =None
strTitle = None
strArtist= None
        
# 1. When program starts, read in the currently saved Inventory
lstTbl = FileProcessor.read_file(strFileName, lstTbl)

# 2. start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break
    # 3.2 process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled. ')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstTbl = FileProcessor.read_file(strFileName, lstTbl)
            IO.show_inventory(lstTbl)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.3 process add a CD
    elif strChoice == 'a':
        strID, strTitle, strArtist = IO.get_UserInput()
        lstTbl = DataProcessor.add_cd(strID, strTitle, strArtist, lstTbl)
        IO.show_inventory(lstTbl)
        continue # start loop back at top.
    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.5 process delete a CD
    elif strChoice == 'd':
        # 3.5.1 get Userinput for which CD to delete
        # 3.5.1.1 display Inventory to user
        IO.show_inventory(lstTbl)
        # 3.5.1.2 ask user which ID to remove
        strIDDel = input('Which ID would you like to delete? ').strip()
        # 3.5.2 search thru table and delete CD
        lstTbl = DataProcessor.delete_cd(strIDDel, lstTbl)
        IO.show_inventory(lstTbl)
        continue  
    # 3.6 process save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstTbl)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        strYesNo = ' '
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        try:   
            while strYesNo not in ['y','n']: 
                raise ValueError('That is not a valid choice!') 
        except Exception as error:
            print('Please enter y for yes or n for no. No other inputs are valid')
            print(error)
        else:     
            if strYesNo == 'y':
            # 3.6.2.1 save data
                FileProcessor.write_file(strFileName, lstTbl)
                print('Data saved to file')
            if strYesNo=='n':
                input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')