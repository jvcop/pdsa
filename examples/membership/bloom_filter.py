"""Example how to use Classical Bloom Filter."""

from pdsa.membership.bloom_filter import BloomFilter


LOREM_IPSUM = (
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    " Mauris consequat leo ut vehicula placerat. In lacinia, nisl"
    " id maximus auctor, sem elit interdum urna, at efficitur tellus"
    " turpis at quam. Pellentesque eget iaculis turpis. Nam ac ligula"
    " ut nunc porttitor pharetra in non lorem. In purus metus,"
    " sollicitudin tristique sapien."
)

if __name__ == '__main__':
    bf = BloomFilter(80000, 4)

    print(bf)
    print("Bloom filter uses {} bytes in the memory".format(bf.sizeof()))

    print("Filter contains approximately {} elements".format(bf.count()))

    print("'Lorem' {} in the filter".format(
        "is" if bf.test("Lorem") else "is not"))

    words = set(LOREM_IPSUM.split())
    for word in words:
        bf.add(word.strip(" .,"))

    print("Added {} words, in the filter approximately {} elements".format(
        len(words), bf.count()))

    print("'Lorem' {} in the filter".format(
        "is" if bf.test("Lorem") else "is not"))
