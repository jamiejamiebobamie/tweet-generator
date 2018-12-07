#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data #take in data, initialize the Node attribute data
        self.next = None #initialize the Node attribute to be 'None' by default

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data) #declare a method that allows a Node to 'introduce' itself by the data it holds


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None #intialize the head attribute of the linked list
        self.tail = None #initialize the tail attribute of the linked list

        if items is not None: #if the items passed into the class upon initialization is not 'None'
            for i, item in enumerate(items): # go through the list
                if i == 0: #if it's the first item in the list...
                    self.head = item #make it the head
                self.append(item) #call the linked list class method 'append' on each of the items

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()] # create a list comprehension of strings of all the items
        return '[{}]'.format(' -> '.join(items)) # return a formatted string of all the nodes in the order of what they point to

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items()) # 'return a string representation of this linked list. (see docstring)'

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = [] # intialize an empty array
        node = self.head # init the variable 'node' and set it equal to the head
        while node is not None: # while the variable 'node' is not the last one
            items.append(node.data) # append the node's data to the array 'items'
            node = node.next # set the variable 'node' to the node that it points to (the next one)
        return items # return the array of each node's DATA

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None # return a boolean if the linked list is empty

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(???) Why and under what conditions?"""
        count = 0 #init the variable 'count'
        node = self.head # https://github.com/DacioRomero/CS-1.2/blob/master/Code/linkedlist.py
        while node is not None: # (for each data in the array produced by 'items()') <-- what i was doing
            count += 1 # increment the counter by one
            node = node.next # Dacio iterates through the nodes. I was iterating through the data
        return count # return the count

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        newNode = Node(item) # instantiate a new instance of the class Node

        if self.tail != None: # if there is a tail...
            self.tail.next = newNode # tell the tail to point to the new Node

        else: # if there is NOT a tail...
            self.head = newNode # make the new Node the head

        self.tail = newNode # make the new Node the tail

        # dacio's uses the self.is_empty() method == better:

        # if self.is_empty(): # O(1)
            # self.head = newNode
        # else:
            # self.tail.next = newNode
#
        # self.tail = newNode



    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        newNode = Node(item) # instantiate a new instance of the class Node
        if self.head != None: # if the linked list is not empty
            newNode.next = self.head # point the new node to the front of the list
        else:
            self.tail = newNode
        self.head = newNode # make the new Node the front of the list


    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        for data in self.items(): # iterate through the array of data produced by the method items()
            if quality(data) is True: # if the data equals the quality we're looking
                node = self.head # init the variable 'node' and set it equal to the head
                while node is not None: # while the variable 'node' is not the last one
                    if node.data == data:
                        return node.data
                    node = node.next # set the variable 'node' to the node that it points to (the next one)
            else:
                continue
        return None

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""

        last = self.head #set the last variable (last == the node iterated before the current one)
        current = self.head # and the current variable to be self.head, the first node
        if self.head != None: #if list is not empty...



            while current != None: # while the node is not the last one in the linked list...

                if current.data == item: # if the current node's data equals the data you're looking for...

                    if current == self.head and current == self.tail: # and there's only one item left in the list
                        self.head = None # set the head to None
                    elif current == self.head:
                        self.head = current.next

                    last.next = current.next # if there are other nodes in the linked list and we've found the node to delete
                                            # point the last node's next to the current node's next

                    if current.next == None: # if current node (the one being deleted) is the tail of the linked list
                        self.tail = last # set the tail of the linked list to the last node (the one before the current node)

                        if self.tail == current: # if the tail and the current node are the same (if there's only one node and it's being deleted...)
                            self.tail = None # set the tail to None

                # if the current node's data DOES NOT equal the data you're looking for...
                last = current # set the 'last' node to the current node
                current = current.next # set the 'current' node to the next node
                print("TAIL: " + str(self.tail)) # print the tail of the linked list "Oh what a tale we will tell together, you and I!""
            else:
                return ValueError('Item not found: {}'.format(item)) #if we've iterated through the entire list and haven't found the node with the data
                print((last, current))
        else:
            raise ValueError('Item not found: {}'.format(item)) #if the linked list is empty
            print((self.head, self.tail))
        raise ValueError('Item not found: {}'.format(item)) #if the linked list is empty

def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))
        ll.delete('X')

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
