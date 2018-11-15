from flask import Flask, request
app = Flask(__name__)


def find_sbm(seq):
    min1, max1, seq = scan(seq[1:], seq[0], lambda x, y: x < y)
    max2, min2, seq = scan(seq[1:], max1, lambda x, y: x > y)
    return [min1, max2, min2] if max2 and min2 and min1 < max2 > min2 else []


def scan(seq, start, compare):
    if not start or len(seq) == 0:
        return start, None, seq
    elif compare(start, seq[0]):
        return start, seq[0], seq
    else:
        return scan(seq[1:], seq[0] if not compare(start, seq[0]) else start, compare)


@app.route('/server', methods=['POST'])
def find_sbm_api():
    content = request.json['seq']
    return 'Result: {}\n'.format(len(find_sbm(content)) > 0)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)




