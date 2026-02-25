# Author: Jigesh Sheoran
# Last Modified : 25/02/2026
# Experiment: Hash Table Search

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)
        self.table[index].append(key)

    def search(self, key):
        index = self.hash_function(key)
        if key in self.table[index]:
            return index
        else:
            return -1


# user input 
print("Hash Table Search Program")

size = int(input("Enter size of hash table:\n"))
ht = HashTable(size)

n = int(input("Enter number of elements to insert:\n"))
print("Enter elements:")

for _ in range(n):
    value = int(input())
    ht.insert(value)

key = int(input("Enter element to search:\n"))

result = ht.search(key)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")

print("Program executed successfully.")
