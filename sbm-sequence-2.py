from flask import Flask, request
app = Flask(__name__)


def find_sbm(seq):
    lst = sorted(enumerate(seq), key=lambda x: (x[1], -x[0]))  # sort O(n*log(n))
    return scan(lst)  # scan O(n)


def scan(seq):
    if len(seq) < 3:
        return False
    elif seq[0][1] < seq[1][1] < seq[2][1] and seq[0][0] < seq[1][0] > seq[2][0]:
        return True
    return scan(seq[1:])


print(find_sbm([8, 10, 9, 8]))

# print(find_sbm([7, 8, 1, 2, 2]))
# print(find_sbm([7, 8, 1, 3, 2]))
# print(find_sbm([7, 9, 1, 2, 8]))
#
# print(find_sbm([1, 2, 3]))
# print(find_sbm([1, 2, 3, 2]))
# print(find_sbm([1, 2, 3, 7]))
# print(find_sbm([4, 1, 7, 8, 7, 2]))
# print(find_sbm([7, 2, 2, 3, 1, 2, 1, 2, 3, 7]))
# print(find_sbm([1, 2, 2, 4, -11, 1, 5, 1, 5, 7, 7, 10, 11, 12, 40, -10, -5]))


