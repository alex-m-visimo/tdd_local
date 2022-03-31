file = "random_nums.txt"


def read_ints():
    data = []
    with open(file, "r") as f:
        lines = f.readlines()
    for line in lines:
        data.append(int(line))
    return data


def count():
    data = read_ints()
    return len(data)


print(count())


def summation():
    data = read_ints()
    return sum(data)


print(summation())


def average():
    data = read_ints()
    return summation() / count()


print(average())


def minimum():
    data = read_ints()
    return min(data)


print(minimum())


def maximum():
    data = read_ints()
    return max(data)


print(maximum())
import unittest
import numpy as np


class Test(unittest.TestCase):
    def test_harmonic_mean(
        self,
    ):
        target = 2.76923078
        self.assertLess(harmonic_mean() - target, 0.01)


def test_variance(self):
    target = 2.0 / 3.0
    self.assertLess(variance() - target, 0.01)


def test_stdv(self):
    target = np.sqrt(2.0 / 3.0)
    self.assertLess(standard_dev() - target, 0.01)


def harmonic_mean():
    data_list = read_ints()
    print(data_list)
    total = 0
    for d in data_list:
        total += 1.0 / float(d)
    total = total / len(data_list)
    return 1.0 / total


def variance():
    av = average()
    data_list = read_ints()
    var = 0.0
    for d in data_list:
        var += (d - av) ** 2
    return var / count()


def standard_dev():
    return np.sqrt(variance())


file = "test_ints.txt"
unittest.main()
