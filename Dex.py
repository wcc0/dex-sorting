import os
import sys
import csv


class Dex:
    """
    Main class - Linked List
    Stores Nodes
    Requires no arguments to construct
    """
    class Node:
        """
        Sub class - Node structure for Linked List
        Stores data on individual Pokemon
        Requires a list of data of format: [#,Name,Type 1,Type 2,Total,HP,Attack,Defense,Sp. Atk,Sp. Def,Speed]
        """

        def __init__(self, pkmn_stats):
            '''
            Node Constructor - run upon creating a new Node
            Initializes Node type variables (prev, next)
            Iniitializes all data variables
            Public
            '''
            self.next = None
            self.prev = None
            self.data = pkmn_stats
            self.num = int(pkmn_stats[0])
            self.name = pkmn_stats[1]
            self.main_type = pkmn_stats[2]
            self.subtype = pkmn_stats[3]
            self.hp = int(pkmn_stats[5])
            self.atk = int(pkmn_stats[6])
            self.deff = int(pkmn_stats[7])
            self.spatk = int(pkmn_stats[8])
            self.spdef = int(pkmn_stats[9])
            self.spd = int(pkmn_stats[10])
            
            self.total = self.hp + self.atk + self.deff + self.spatk + self.spdef + self.spd
            
    def __init__(self):
        '''
        Dex (Linked List) Constructor - run upon creating a new Dex
        Initializes Linked List type variables (front, back, cursor next, cursor previous, index, length)
        Stores no user data
        Private
        '''

        # Notice when constructing a Dex object, we create a dummy Node
        # This makes the first entry much easier to process
        # This also gives us a cls entry point to the front of the Dex
        self._front = self.Node([0] * 11)
        self._back = self.Node([0] * 11)
        self._front.next = self._back
        self._back.prev = self._front
        self._curPrev = self._front
        self._curNext = self._back
        self._index = 0
        self._len = 0

    def size(self):
        '''
        Dex:size()
        Returns the number of Nodes in Dex
        '''
        return self._len

    def pos(self):
        '''
        Dex:pos()
        Returns the index number of the cursor
        Ex:
            The cursor is represented as `|` and acts much like a typing cursor would
            1 2 | 3
            curPrev points to `2` and curNext points to `3`
        '''
        return self._index

    def moveFront(self):
        '''
        Dex:moveFront()
        Moves the cursor to the front of the Dex
        Updates the index to 0
        '''
        self._index = 0
        self._curPrev = self._front
        self._curNext = self._front.next

    def moveBack(self):
        '''
        Dex:moveBack()
        Moves the cursor to the back of the Dex
        Updates the index to size()
        '''
        index = self.size()
        curNext = self._back
        curPrev = self._back.prev

    def peekNext(self):
        '''
        Dex:peekNext()
        Returns the data of the Node in front of the cursor
        '''
        if self.pos() >= self.size():
            raise Exception("DexError: calling peekNext() at end of Dex\n")

        return self._curNext.data

    def moveNext(self):
        '''
        Dex:moveNext()
        Moves the cursor to the next Node
        Updates index +1
        '''
        if self.pos() >= self.size():
            raise Exception("DexError: calling moveNext() at end of Dex\n")

        self._curPrev = self._curNext
        self._curNext = self._curNext.next
        self._index += 1

        return self._curPrev.data

    def insertAfter(self, data):
        '''
        Dex:insertAter(list)
        Inserts a new Node after the cursor
        Updates length +1
        '''
        N = self.Node(data)

        if self._len == 0:
            self._curNext = N
            N.prev = self._front
            N.next = self._back
            self._front.next = N
            self._back.prev = N

        else:
            self._curNext.prev = N
            self._curPrev.next = N
            N.prev = self._curPrev
            N.next = self._curNext

        if self._index == self.size():
            self._back.prev = N

        elif self._index == 0:
            self._front.next = N

        self._curNext = N
        self._len += 1

    def insertBefore(self, data):
        '''
        Dex:insertBefore(list)
        Inserts a new Node before the Cursor
        Updates length +1
        Updates index +1
        '''
        N = self.Node(data)

        if self.size() == 0:
            self._curPrev = N
            N.prev = self._front
            N.next = self._back
            self._front.next = N
            self._back.prev = N
        else:
            self._curPrev.next = N
            self._curNext.prev = N
            N.prev = self._curPrev
            N.next = self._curNext

        if self.pos() == 0:
            self._front.next = N
        elif self.pos() == self.size():
            self._back.prev = N

        self._curPrev = N
        self._index += 1
        self._len += 1

    def eraseAfter(self):
        '''
        Dex:eraseAfter(self)
        Deletes the post-node
        Updates length -1
        '''
        if self.pos() >= self.size():
            raise Exception(f"DexError: calling eraseAfter() at end of list\n")
        
        self._curPrev.next = self._curNext.next
        self._curNext.next.prev = self._curPrev
        del self._curNext
        self._curNext = self._curPrev.next
        self._len -= 1
    
    def modify(self, stat, value):
        '''
        Dex:modify(self)
        Modifies the post-node's provided stat type by the users specifcation
        '''
        #HP[5],Attack,Defense,Sp. Atk,Sp. Def,Speed
        
        if stat == 1:
            self._curNext.hp = value
        elif stat ==  2:
            self._curNext.atk = value
        elif stat ==  3:
            self._curNext.deff = value
        elif stat ==  4:
            self._curNext.spatk = value
        elif stat ==  5:
            self._curNext.spdef = value
        elif stat ==  6:
            self._curNext.spd = value
        self._curNext.data[stat+4] = value
        self._curNext.total = 0
        for i in range(5, 11):
            self._curNext.total += int(self._curNext.data[i]) 
        print(f"""
Entry Modified
=====================================
#{self._curNext.num} - {self._curNext.name}
Type: {self._curNext.main_type}
Subtype: {self._curNext.subtype}
Stat Total: {self._curNext.total}
HP: {self._curNext.hp}
Atk: {self._curNext.atk}
Def: {self._curNext.deff}
Sp. Atk: {self._curNext.spatk}
Sp. Def: {self._curNext.spdef}
Spd: {self._curNext.spd}""")
        
    

    def lookup(self, u_filter, u_value):
        '''
        Dex:lookup(filter, value)
        Traverses the Dex to search for a specified Node
        Returns the index of the Node
        Returns -1 if the Node is not found
        '''
        filter_dict = {1: "Dex #", 2: "Name"}

        N = self._front.next
        self.moveFront()
        while N != self._back and self.size() != 0:
            if N.data[u_filter - 1] == u_value:
                os.system("cls")
                print(f"Found result for {filter_dict[u_filter]} at {u_value}")
                print(f"""
=====================================
#{N.num} - {N.name}
Type: {N.main_type}
Subtype: {N.subtype}
Stat Total: {N.total}
HP: {N.hp}
Atk: {N.atk}
Def: {N.deff}
Sp. Atk: {N.spatk}
Sp. Def: {N.spdef}
Spd: {N.spd}""")
                return 1
            self.moveNext()
            N = N.next

        self.moveBack()

        print(
            f"Search by {filter_dict[u_filter]} at {u_value} yielded no results")
        return 0

    def __str__(self):
        '''
        Dex:__self__()
        Used to define what happens when the built-in print() method is called on a Dex object
        '''
        s = ""

        N = self._front.next

        while N != self._back and self.size() != 0:
            s += f"""
=====================================
#{N.num} - {N.name}
Type: {N.main_type}
Subtype: {N.subtype}
Stat Total: {N.total}
HP: {N.hp}
Atk: {N.atk}
Def: {N.deff}
Sp. Atk: {N.spatk}
Sp. Def: {N.spdef}
Spd: {N.spd}
"""
            N = N.next
        return s


def sort(dex, data, opt=None):
    '''
    sort()
    Sorts a given Dex object per user specifications
    Returns a sorted Dex object
    '''
    dex = Dex()

    if opt == None:
        while opt not in [i for i in range(1, 11)]:
            try:
                opt = int(input("""
Please select a sorting option:
-------------------------------
1.  Dex #
2.  Name
3.  Type
4.  Stat Total
5.  HP
6.  Attack
7.  Defense
8.  Sp. Atk
9.  Sp. Def
10. Speed
> """))
                if opt not in [i for i in range(1, 11)]:
                    os.system("cls")
                    print("The following input was not accepted")

            except ValueError:
                os.system("cls")
                print("The following input was not accepted")

    sort_dict = {
        1: 0,
        2: 1,
        3: 2,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 10
    }

    # 9

    # D>12457
    if opt in [2, 3]:
        for row in data:
            dex.moveFront()

            if dex.size() == 0:
                dex.insertBefore(row)
                continue

            while dex.pos() < dex.size():
                if row[sort_dict[opt]] >= dex.peekNext()[sort_dict[opt]]:
                    dex.moveNext()
                else:
                    dex.insertBefore(row)
                    break

            if dex.pos() == dex.size():
                dex.insertBefore(row)
    else:
        for row in data:
            dex.moveFront()

            if dex.size() == 0:
                dex.insertBefore(row)
                continue

            while dex.pos() < dex.size():
                if int(row[sort_dict[opt]]) >= int(dex.peekNext()[sort_dict[opt]]):
                    dex.moveNext()
                else:
                    dex.insertBefore(row)
                    break

            if dex.pos() == dex.size():
                dex.insertBefore(row)

    return dex, opt


def main(): #--------------------------------------------------------------------------------------------
    '''
    Main program
    Requires a .csv in correct format to run
    '''
    
    # Argument check
    if len(sys.argv) < 2:
        print(f"Usage: python {__file__} [.csv]")
        exit(1)

    if ".csv" not in sys.argv[1]:
        print(f"Error: python {__file__} > {sys.argv[1]}")
        print(f"Must be .csv file")

    # Import csv to Dex object
    dex = Dex()
    reader = None
    sort_opt = 1

    #Default sort by dex #
    with open(sys.argv[1], 'r') as IN:
        next(IN)
        reader = csv.reader(IN)
        dex, sort_opt = sort(dex, reader, 1)
    IN.close()
    
    # dex.lookup(1, "151")
    # dex.eraseAfter()
    # print(dex)
    # exit(1)

    while 1:  # Main Loop
        user_input = input("""
Please select an option:
-------------------------
1. View Dex
2. Sort Dex
3. Lookup
4. Addition
5. Modify
6. Delete
7. Quit

> """)

        if user_input == '1': #View
            print(dex)
            input("Press Enter to continue...")
            os.system("cls")

        elif user_input == '2': #Sort
            os.system("cls")
            pkmn_data = []
            N = dex._front.next
            while N != dex._back and dex.size() != 0:
                pkmn_data.append(N.data)
                N = N.next
            dex, sort_opt = sort(dex, pkmn_data)
            input("Dex Sorted. Press Enter to continue...")
            os.system("cls")

        elif user_input == '3': #Lookup
            os.system("cls")
            filter_dict = {1: "Dex #", 2: "Name"}
            user_filter = 0
            while user_filter not in [1, 2]:
                try:
                    user_filter = int(input(f"""
What would you like to search by?
---------------------------------
1. {filter_dict[1]}
2. {filter_dict[2]}
> """))
                    if user_filter not in [1, 2]:
                        os.system("cls")
                        print("The following input is not accepted  ")
                        continue
                except ValueError:
                    os.system("cls")
                    print("The following input is not accepted  ")

            os.system("cls")
            user_value = input(
                f"Searching by {filter_dict[user_filter]}: ")
            dex.lookup(user_filter, user_value.lower().capitalize())
            input("Press Enter to continue...")

            os.system("cls")
            
        elif user_input == '4': #Addition
            new_pkmn = []
            
            os.system("cls")
            #[#,Name,Type 1,Type 2,Total,HP,Attack,Defense,Sp. Atk,Sp. Def,Speed]
            def get_input_int(input_str):
                while True:
                    try:
                        new_pkmn.append(int(input(input_str)))
                        break
                    except ValueError:
                        os.system("cls")
                        print("The following input is not accepted")
            print("Insert new Pokemon data:")
            print("------------------------")
            get_input_int("Dex #: ")
            new_pkmn[0] = str(new_pkmn[0])
            new_pkmn.append(input("Name: "))
            new_pkmn.append(input("Type 1: "))
            new_pkmn.append(input("Type 2: "))
            get_input_int("HP: ")
            get_input_int("Attack: ")
            get_input_int("Defense: ")
            get_input_int("Sp. Atk: ")
            get_input_int("Sp. Def: ")
            get_input_int("Speed: ")
            
            new_pkmn.insert(4, sum(new_pkmn[4:]))
            dex.moveFront()
            dex.insertAfter(new_pkmn)
            os.system("cls")
            print(f"""
Entry Added
=====================================
#{dex._curNext.num} - {dex._curNext.name}
Type: {dex._curNext.main_type}
Subtype: {dex._curNext.subtype}
Stat Total: {dex._curNext.total}
HP: {dex._curNext.hp}
Atk: {dex._curNext.atk}
Def: {dex._curNext.deff}
Sp. Atk: {dex._curNext.spatk}
Sp. Def: {dex._curNext.spdef}
Spd: {dex._curNext.spd}""")
            input("Press Enter to continue...")
            os.system("cls")
            pkmn_data = []
            N = dex._front.next
            while N != dex._back and dex.size() != 0:
                pkmn_data.append(N.data)
                N = N.next
            dex, sort_opt = sort(dex, pkmn_data, sort_opt)         
        elif user_input == '5': #Modify
            os.system("cls")
            filter_dict = {1: "Dex #", 2: "Name"}
            user_filter = 0
            try:
                user_filter = int(input(f"""
Select a search option:
------------------------------
1. {filter_dict[1]}
2. {filter_dict[2]}
> """))
                if user_filter not in [1, 2]:
                    os.system("cls")
                    print("The following input is not accepted  ")
                    continue
                
            except ValueError:
                os.system("cls")
                print("The following input is not accepted  ")

            os.system("cls")
            user_value = input(
                f"Searching by {filter_dict[user_filter]}: ")
            
            if dex.lookup(user_filter, user_value.lower().capitalize()) == 0:
                input("Press Enter to continue...")
                os.system("cls")
                continue
            
            user_filter = 0
            
            while user_filter not in range(1, 8):
                filter_dict = {
                    1 : "HP",
                    2 : "Attack",
                    3 : "Defense",
                    4 : "Sp. Atk",
                    5 : "Sp. Def",
                    6 : "Speed",
                    7 : "Cancel"
                }
                try:
                    user_filter = int(input(f"""
What would you like to modify?
---------------------------------
1. {filter_dict[1]}
2. {filter_dict[2]}
3. {filter_dict[3]}
4. {filter_dict[4]}
5. {filter_dict[5]}
6. {filter_dict[6]}
7. {filter_dict[7]}
> """))
                    if user_filter not in range(1,8) or user_filter <= 0:
                        os.system("cls")
                        print("The following input is not accepted  ")
                        continue
                except ValueError:
                    os.system("cls")
                    print("The following input is not accepted  ")
                    
            os.system("cls")
                
            if user_filter == 7:
                print("Operation Canceled")
                input("Press Enter to continue...")
                os.system("cls")
                continue
            
            user_value = ""
            
            while not user_value.isdigit():
                user_value = input(f"Enter a new {filter_dict[user_filter]} value: ")
                 
                if not user_value.isdigit():
                    os.system("cls")
                    print("The following input is not accepted\n")
            os.system("cls")
            dex.modify(user_filter, user_value)
            

        elif user_input == '6': #Delete
            os.system("cls")
            filter_dict = {1: "Dex #", 2: "Name"}
            user_filter = 0
            try:
                user_filter = int(input(f"""
Select an option to delete by:
------------------------------
1. {filter_dict[1]}
2. {filter_dict[2]}
> """))
                if user_filter not in [1, 2]:
                    os.system("cls")
                    print("The following input is not accepted  ")
                    continue
                
            except ValueError:
                os.system("cls")
                print("The following input is not accepted  ")

            os.system("cls")
            user_value = input(
                f"Searching by {filter_dict[user_filter]}: ")
            if dex.lookup(user_filter, user_value.lower().capitalize()) == 0:
                input("Press Enter to continue...")
                os.system("cls")
                continue
                
            if input("\nType \"Delete\" to confirm deletion.\n>") == "Delete":
                os.system("cls")
                dex.eraseAfter()
                print("Entry deleted\n")
            else:
                os.system("cls")
                print("Operation canceled")
            
            input("Press Enter to continue...")
            os.system("cls")
            
        elif user_input == '7': #Quit
            os.system("cls")
            print("Goodbye.")
            exit(1)
        else:
            os.system("cls")
            print("The following input is not accepted")


if __name__ == "__main__":
    main()
