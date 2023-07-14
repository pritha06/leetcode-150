'''
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.
'''
'''approach:
HASHMAP ##
    #   1. Insertion operation in list is O(1) but not deletion
    #   2. So we create one Hashmap with key,index and other list
    #   3. for deleting we go to hashmap, get index, go to that index in list, swap that element with last element.
    #   4. save the index to last element in hashmap and delete list last element
'''
'''In order to have O(1) insert and remove operations, we need an unordered set or dict.
In order to have O(1) getRandom operations, we need a data structure with random access. That means we need a list. (vector in C)
The hardest part is connecting the two.

What we can do is have a dictionary (map in C) that for every value we store the index in the list of that value. This way, when we need to remove an element by its value, we know what element from the list to remove without having to traverse the whole list.
Removing an element from the middle of the list while preserving the order of everything else is O(N). But we don't need to preserve the order. So when removing an element from the middle of the list, we can just swap it with the last element of the list, then remove the last element of the list. This makes the remove operation O(1) as whole. Care must be taken to maintain the dictionary of indexes for the swap!
'''
import random

class RandomizedSet(object):

    def __init__(self):
        self.data_map={}
        self.data=[]
        self.length=0
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.data_map:
            return False
        self.data_map[val]=self.length
        self.length+=1
        self.data.append(val)
        return True

        
        
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        # for deleting we go to hashmap, 
        # get index, go to that index in list, 
        # swap that element with last element.
        #   save the index to last element in hashmap and delete list last element
        if val not in self.data_map:
            return False
        last_ele=self.data[-1]        
        index=self.data_map[val]
        self.data_map[last_ele]=index
        replace=self.data[index]
        replace,last_ele=last_ele,replace
        self.data.pop()
        self.data_map.pop(val)
        self.length-=1
        return True
        
        

    def getRandom(self):
        """
        :rtype: int
        """
        ri = random.randint(0, self.length - 1)
        return self.data[ri]
        # return random.choice(self.data)
        


# Your RandomizedSet object will be instantiated and called as such:


obj = RandomizedSet()
param_1 = obj.insert(1)
param_2 = obj.remove(2)
param_4 = obj.insert(2)
param_3 = obj.getRandom()
print(param_1)
print(param_2)
print(param_3)
print(param_4)