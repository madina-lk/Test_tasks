#!/usr/bin/python
# -*- coding: ascii -*-

import numpy


class RingBuffer:

    def __init__(self, size):
        """
                ??????????? ??????
                :param size: ?????? ??????? numpy
                :type size: int
                :param data: ??????, ??????????? ??????
                :type data: int
                :param index:
                :type index: int
        """

        self.data = numpy.zeros(size, dtype='i')
        self.index = 0
        self.size = 0

    def append(self, val):
        """
        ?????????? ???????? ? ?????
        :param val:
        :type val: int
        :return: None
        """
        self.data = numpy.roll(self.data, 1)
        self.data[0] = val

        self.size += 1

    def get(self):
        """ ?????????? ?????? ? ??????? ??????????? ? ?????
        :return: array
        :rtype: float
        """

        idx = (self.index + numpy.arange(self.data.size)) %self.data.size
        return self.data[idx]


def ringbuff_numpy_test():
    ringlen = 100000
    ringbuff = RingBuffer(ringlen)
    for i in range(50):
        ringbuff.append(20.0)

    return ringbuff.get()



import timeit
#
print(timeit.timeit('ringbuff_numpy_test()', setup="from task_2 import ringbuff_numpy_test"))
print(ringbuff_numpy_test())
#

# ringlen = 5
# ringbuff = RingBuffer(ringlen)
# print(ringbuff.get())
# ringbuff.append(20.0)
# ringbuff.append(40.0)
# ringbuff.append(50.0)
# ringbuff.append(40.0)
# ringbuff.append(20.0)
# ringbuff.append(21.0)
# print (ringbuff.get())
# # print (ringbuff_numpy_test())
