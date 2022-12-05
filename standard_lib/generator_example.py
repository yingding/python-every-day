"""
Reference:
python generator by mCoding
https://www.youtube.com/watch?v=tmeKsb2Fras

"""
from typing import Iterator, NamedTuple
import os

def get_values():
    # yield will pause the generator and return a value
    yield "hello"
    yield "world"
    yield 123

def example2_get_values():
    # for loop to call the next on generator automatically
    for x in get_values():
        print(x)    

def example_get_values():
    gen = get_values()
    print(gen)
    # use the next to resume the generator
    print(next(gen))
    print(next(gen))
    print(next(gen))

"""
https://www.w3schools.com/python/python_iterators.asp
"""
class MyRange:
    def __init__(self, stop: int):
        self.start = 0
        self.stop = stop

    def __iter__(self) -> Iterator[int]:
        curr = self.start
        while curr < self.stop:
            yield curr
            curr += 1 

def range_example():
    for n in MyRange(5):
        print(n)  


class MyDataPoint(NamedTuple):
    x: float
    y: float
    z: float


def mydata_reader(file):
    for row in file:
        cols = row.rstrip().split(",")
        cols = [float(c) for c in cols]
        yield MyDataPoint._make(cols)


def reader_example():
    with open(os.path.join(
        os.path.dirname(__file__),"data","mydata.txt")) as file:
        for row in mydata_reader(file):
            print(row)


if __name__ == "__main__":
    # example_get_values()
    # example2_get_values()
    # range_example()
    reader_example()
    # todo : https://youtu.be/tmeKsb2Fras?t=300