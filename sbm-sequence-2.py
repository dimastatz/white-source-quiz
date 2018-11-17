from flask import Flask, request
app = Flask(__name__)


def find_sbm(seq):
    lst = sorted(enumerate(seq), key=lambda x: x[1])  # sort O(n*log(n))
    return scan_for_trend(lst)  # scan O(n)


def scan_for_trend(seq, min_n=None, max_n=None):
    if not seq:
        return False
    elif min_n and max_n and max_n > seq[0][0]:
        return True

    if not min_n or seq[0][0] < min_n:
        return scan_for_trend(seq[1:], seq[0][0], max_n)
    elif not max_n or seq[0][0] > max_n:
        return scan_for_trend(seq[1:], min_n, seq[0][0])


@app.route('/server', methods=['POST'])
def find_sbm_api():
    return 'Result: {}\n'.format(find_sbm(request.json['seq']))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)


