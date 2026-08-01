import ast
import operator

def calcular_seguro(expr):
    ops = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul, ast.Div: operator.truediv}
    node = ast.parse(expr, mode='eval').body
    def eval_(node):
        if isinstance(node, ast.BinOp):
            return ops[type(node.op)](eval_(node.left), eval_(node.right))
        elif isinstance(node, ast.Num):
            return node.n
        raise TypeError(node)
    return eval_(node)
