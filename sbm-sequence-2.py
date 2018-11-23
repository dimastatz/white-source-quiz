from flask import Flask, request
app = Flask(__name__)


def find_sbm(seq):
    return scan(seq, set(), False)


def scan(seq, known_range, is_up_trend):
    if not seq or len(seq) < 2:
        return False
    elif seq[1] in known_range:  # 0(1)
        return True
    else:
        known_range = add_set(known_range, is_up_trend, seq[0], seq[1])
        return scan(seq[1:], known_range, seq[0] < seq[1])


def add_set(s, include_min, min_n, max_n):
    r = range(min_n, max_n) if include_min else range(min_n + 1, max_n)
    return s | set(r)


@app.route('/server', methods=['POST'])
def find_sbm_api():
    return 'Result: {}\n'.format(find_sbm(request.json['seq']))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)


# print(find_sbm([8, 10, 9, 8]))
# print(find_sbm([7, 8, 1, 2, 2]))
# print(find_sbm([7, 8, 1, 3, 2]))
# print(find_sbm([7, 9, 1, 2, 8]))
# print(find_sbm([1, 2, 3]))
# print(find_sbm([1, 2, 3, 2]))
# print(find_sbm([1, 2, 3, 7]))
# print(find_sbm([4, 1, 7, 8, 7, 2]))
# print(find_sbm([7, 2, 2, 3, 1, 2, 1, 2, 3, 7]))
# print(find_sbm([1, 2, 2, 4, -11, 1, 5, 1, 5, 7, 7, 10, 11, 12, 40, -10, -5]))


