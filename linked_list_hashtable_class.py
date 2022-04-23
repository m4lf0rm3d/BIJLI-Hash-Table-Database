
class LinkedListHashTable:
    def __init__(self, size) -> None:
        self.items = []
        for i in range(size):
            self.items.append([])

    def search(self, phone):
        hashtable_index = phone % 800000

        current_index_list = self.items[hashtable_index]
        for probes_data in current_index_list:

            if probes_data[0] == phone:
                return probes_data

        return False

    def insert(self, data):

        hashtable_index = data[0] % 800000

        if self.search(data[0]):
            raise Exception("Given number already exist!")

        self.items[hashtable_index].append(data)
        

    def delete(self, phone):

        if not self.search(phone):
            raise Exception("Error! Phone Number does not Exist in our database!")

        hashtable_index = phone % 800000
        inside_remove_index = 0
        for i in range(len(self.items[hashtable_index])):
            if self.items[hashtable_index][i][0] == phone:
                inside_remove_index = i
                break

        self.items[hashtable_index].pop(inside_remove_index)

        
        


