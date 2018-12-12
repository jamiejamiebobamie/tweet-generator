#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(???) Why and under what conditions?""" #Big-O runtime = O(n^2) // quadratic, all conditions except if you only have one bucket / one key
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets: #O(n)
            for key, value in bucket.items(): #O(n)
                all_keys.append(key) #O(1)
        return all_keys #O(1)

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(???) Why and under what conditions?""" #Big-O runtime = O(n) // linear, except if you have only one bucket
        valArr = []
        for bucket in self.buckets:
            for key, value in bucket.items(): #O(n)
                valArr.append(value) #O(1)
        return valArr #O(1)

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(???) Why and under what conditions?""" #On^2 / quadratic
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets: #O(n)
            all_items.extend(bucket.items()) #O(n)
        return all_items #O(1)

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(???) Why and under what conditions?""" #O(n^2)
        count = 0
        for bucket in self.buckets: #O(n) dependent on amount of buckets (linear)
            if bucket.is_empty() == False:
                count += bucket.length() #O(n) dependent on amount of nodes (linear)
        return count
        # TODO: Loop through all buckets
        # TODO: Count number of key-value entries in each bucket

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(???) Why and under what conditions?"""
        if self.buckets[self._bucket_index(key)].find(lambda item: item[0] == key) != None:
            return True
        else:
            return False
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        if self.buckets[self._bucket_index(key)].find(lambda item: item[0] == key) != None:
            return self.buckets[self._bucket_index(key)].find(lambda item: item[0] == key)[1]
        else:
            raise KeyError('Key not found: {}'.format(key))

        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, return value associated with given key
        # TODO: Otherwise, raise error to tell user get failed
        # Hint: raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(???) Why and under what conditions?"""
        if self.buckets[self._bucket_index(key)].find(lambda item: item[0] == key) != None:
            self.buckets[self._bucket_index(key)].delete(self.buckets[self._bucket_index(key)].find(lambda item: item[0] == key))
            self.buckets[self._bucket_index(key)].append((key,value))
        else:
            self.buckets[self._bucket_index(key)].append((key,value))
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, update value associated with given key
        # TODO: Otherwise, insert given key-value entry into bucket

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        if self.buckets[self._bucket_index(key)].find(lambda item: item[0] == key) != None:
            self.buckets[self._bucket_index(key)].delete(self.buckets[self._bucket_index(key)].find(lambda item: item[0] == key))
        else:
            raise KeyError('Key not found: {}'.format(key))

#none of this is right. my issue is that once we have a key, like 'Sarah' we hash it using the hash function. then the value is 'Sara''s name hashed? what are we storing?

        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, delete entry associated with given key
        # TODO: Otherwise, raise error to tell user delete failed
        # Hint: raise KeyError('Key not found: {}'.format(key))


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
