# Create hashmap class
class HashMap:
    # Initialize hashmap and set the size of the hashmap to 8
    # Big O = O(n)
    def __init__(self):
        self.size = 8
        self.map = []
        # This for loop will actually create the hashmap and run through as many times as we specified in the size
        for i in range(self.size):
            self.map.append([])

    # Method to print data from hashmap
    # Big O = O(n^2)
    def lookup(self):
        # This method will go through each item in the hashmap and then each item will go through its own nested for loop to then print out the status data of the packages in the hashmap
        for item in self.map:
            for i in range(len(item)):
                print("Package " + item[i][1][0] + ": " + item[i][1][8])

    # Method to insert item into hashmap
    # Big O = O(n)
    def insert(self, key, package):
        # This method will create the hash variable by taking in the passed in key and running the assign_hash method which will determine which hash we will insert the package data into.
        hash = self.assign_hash(key)
        package = [key, package]

        # Run a for loop to iterate through the entire map and check if the hash matches the key in the package
        for i in self.map[hash]:
            if i[0] == key:
                i[1] = package
        # Finally append the hashmap with the package data
        self.map[hash].append(package)

    # This method takes the parameter key from the insert method, and then creates a formula for assigning the hash. In my formula, I turn the key into an int, and then use
    # the modulo of the size to attempt to create a well sorted and even hashmap
    # Big O = O(1)
    def assign_hash(self, key):
        hash_key = 0
        hash_key += (int(key))
        hash = hash_key % self.size
        return hash

    # This method will return an item from the hashmap based on the key provided
    # Big O = O(n)
    def get(self, key):

        # Call the assign_hash method
        hash = self.assign_hash(key)

        # Iterate through hashmap for a specific hash provided by the assign_hash method, and if the hash matches the key, then return the next package data in i[1]
        for i in self.map[hash]:
            if i[0] == key:
                return i[1]

    # Print function for printing entire hashmap
    # Big O = O(1)
    def print(self):
        # Iterate through each item in hashmap and print it
        for item in self.map:
            print(item)


