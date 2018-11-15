from flask import Flask, request
app = Flask(__name__)


def find_sbm(seq):
    if seq:
        min1, seq1 = scan(seq, lambda s: len(s) < 2 or s[0] < s[1])
        max1, seq1 = scan(seq1, lambda s: len(s) < 2 or s[0] > s[1])
        result = min1 and max1 and scan(seq1, lambda s: min1 < s[0] < max1)[0] is not None
        return find_sbm(seq1) if not result else result
    else:
        return False


def scan(seq, stop_condition):
    if not seq or stop_condition(seq):
        return None if not seq else seq[0], seq[1:] if seq else []
    else:
        return scan(seq[1:], stop_condition)


@app.route('/server', methods=['POST'])
def find_sbm_api():
    content = request.json['seq']
    return 'Result: {}\n'.format(find_sbm(content))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)




