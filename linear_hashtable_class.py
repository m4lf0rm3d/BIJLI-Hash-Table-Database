
class LinearHashTable:
    def __init__(self, size) -> None:
        self.items = []
        self.items = [self.items.append(None) for i in range(size)]


    def search(self, phone):
        hashtable_index = phone % 800000
        if self.items[hashtable_index]:
            if self.items[hashtable_index][0] == phone:
                return self.items[hashtable_index]

            current = 0 if hashtable_index == len(self.items)-1 else hashtable_index + 1

            while self.items[current] != None or current == hashtable_index:
                if self.items[current][0] == phone:
                    return self.items[current]

                current = 0 if current == len(self.items)-1 else current + 1  

            return False
        return False

    def insert(self, data):

        hashtable_index = data[0] % 800000

        if not self.items[hashtable_index]:
            self.items[hashtable_index] = data
            return

        current = 0 if hashtable_index == len(self.items)-1 else hashtable_index + 1

        while self.items[current] != None:
            current = 0 if current == len(self.items)-1 else current + 1

        # print("Probes: ", data, current)
        self.items[current] = data
        

    def delete(self, phone):

        if not self.search(phone):
            raise Exception("Error! Phone Number does not Exist in our database!")

        hashtable_index = phone % 800000

        if self.items[hashtable_index][0] == phone:
            self.items[hashtable_index] = None
            return

        current = 0 if hashtable_index == len(self.items)-1 else hashtable_index + 1

        while self.items[current][0] != phone:
            current = 0 if current == len(self.items)-1 else current + 1  

        self.items[hashtable_index] = None
        


