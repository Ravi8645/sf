# %%
import mmh3
from bitarray import bitarray
import math


class BloomFilter:
    def __init__(self, size, hash_functions):
        self.size = size
        self.hash_functions = hash_functions
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)
        self.num_items = 0

    def add(self, item):
        for i in range(self.hash_functions):
            index = mmh3.hash(item, i) % self.size
            self.bit_array[index] = 1
        self.num_items += 1

    def contains(self, item):
        for i in range(self.hash_functions):
            index = mmh3.hash(item, i) % self.size
            if not self.bit_array[index]:
                return False
        return True

    def false_positive_rate(self, num_test_items):
        false_positives = 0
        for i in range(num_test_items):
            test_item = str(i)
            # Generate a test item that is not in the Bloom filter
            if test_item in self:
                false_positives += 1
        return false_positives / num_test_items

    def theoretical_false_positive_rate(self):
        rate = (1 - math.exp(-self.hash_functions *
                             self.num_items / self.size))**self.hash_functions
        return rate

    def __contains__(self, item):
        return self.contains(item)


# %%
# Create a Bloom filter with size = 1000 and hash_functions = 3
bloom_filter = BloomFilter(size=1000, hash_functions=3)

# Add some items to the Bloom filter
bloom_filter.add("apple")
bloom_filter.add("banana")
bloom_filter.add("cherry")

# Check if an item is present in the Bloom filter
print("apple" in bloom_filter)  # True
print("grape" in bloom_filter)  # False

# Calculate the false positive rate of the Bloom filter
print("Theoretical False positive rate:",
      bloom_filter.theoretical_false_positive_rate())
print("False positive rate:", bloom_filter.false_positive_rate(100))

# Create a new Bloom filter with size = 10000 and hash_functions = 5
bloom_filter2 = BloomFilter(size=10000, hash_functions=5)

# Add some items to the new Bloom filter
bloom_filter2.add("cat")
bloom_filter2.add("dog")
bloom_filter2.add("elephant")

# Check if an item is present in the new Bloom filter
print("cat" in bloom_filter2)  # True
print("fish" in bloom_filter2)  # False

# Calculate the false positive rate of the new Bloom filter
print("Theoretical False positive rate:",
      bloom_filter2.theoretical_false_positive_rate())
print("False positive rate:", bloom_filter2.false_positive_rate(1000))


# %%
