"""
Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.


Example 1:

Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]

Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]


Constraints:

0 <= key, value <= 10^6
At most 10^4 calls will be made to put, get, and remove.
"""


class MyHashMap:

    def __init__(self):
        self.table = [None for _ in range(10 ** 6 + 1)]

    def put(self, key: int, value: int) -> None:
        self.table[key] = value

    def get(self, key: int) -> int:
        if self.table[key] is None:
            return -1
        else:
            return self.table[key]

    def remove(self, key: int) -> None:
        self.table[key] = None


class MyHashMap2:

    def __init__(self):
        self.BUCKET = 1000
        self.bucket = [[] for _ in range(self.BUCKET)]

    def get_bucket(self, key):
        return self.bucket[key % self.BUCKET]

    @staticmethod
    def find_idx(bucket, key):
        if not bucket:
            return -1
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                return i
        return -1

    def put(self, key: int, value: int) -> None:
        bucket = self.get_bucket(key)
        idx = self.find_idx(bucket, key)
        if idx == -1:
            bucket.append([key, value])
        else:
            bucket[idx] = [key, value]

    def get(self, key: int) -> int:
        bucket = self.get_bucket(key)
        idx = self.find_idx(bucket, key)
        if idx == -1:
            return -1
        else:
            return bucket[idx][1]

    def remove(self, key: int) -> None:
        bucket = self.get_bucket(key)
        idx = self.find_idx(bucket, key)
        if idx != -1:
            bucket.pop(idx)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)