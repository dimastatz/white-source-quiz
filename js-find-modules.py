import os
from slimit import ast
from slimit.parser import Parser
from slimit.visitors import nodevisitor


def is_require_local(node):
    return isinstance(node, ast.FunctionCall) \
           and node.identifier.value == 'require' \
           and node.args[0].value.startswith("'.")


def parse_file(file_name):
    with open(file_name) as fd:
        tree = Parser().parse(fd.read())
        return [x.args[0].value for x in nodevisitor.visit(tree) if is_require_local(x)]


def parse_folder_files(folder):
    files = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(".js")]
    result = [parse_file(x) for x in files]
    return set([item for sublist in result for item in sublist])


if __name__ == '__main__':
    path = '/Users/dimastatz/Documents/dev/sit/white-source-quiz/'
    print(parse_folder_files(path))

