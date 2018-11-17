from flask import Flask, request
app = Flask(__name__)


def find_sbm(seq):
    lst = sorted(enumerate(seq), key=lambda x: x[1])  # sort O(n*log(n))
    return scan_for_trend(lst)  # scan O(n)


def is_stop_cond(min_n, seq, max_n):
    return min_n and max_n and max_n[0] > seq[0][0] > min_n[0] \
           and min_n[1] != seq[0][1] and max_n != seq[0][1] and max_n[1] != min_n[1]


def scan_for_trend(seq, min_n=None, max_n=None):
    if not seq:
        return False
    elif is_stop_cond(min_n, seq, max_n):
        return True

    if not min_n or seq[0][0] <= min_n[0]:
        return scan_for_trend(seq[1:], seq[0])
    elif not max_n or seq[0][0] >= max_n[0]:
        return scan_for_trend(seq[1:], min_n, seq[0])
    else:
        return scan_for_trend(seq[1:], min_n, max_n)


@app.route('/server', methods=['POST'])
def find_sbm_api():
    return 'Result: {}\n'.format(find_sbm(request.json['seq']))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
