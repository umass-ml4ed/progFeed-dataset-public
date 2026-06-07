import sys
import ast

# https://docs.python.org/3/library/ast.html
# https://stackoverflow.com/questions/1515357/simple-example-of-how-to-use-ast-nodevisitor

class CullInputText(ast.NodeTransformer):
  def visit_Call(self, node):
    if isinstance(node.func, ast.Name) and node.func.id == 'input':
      return ast.Call(node.func,[],[])
    return ast.NodeTransformer.generic_visit(self, node)

def cull_input_text(from_file, to_file):
  with open(from_file,"r") as fd:
    t = ast.parse(fd.read(), filename=from_file)
  v = CullInputText()
  v.visit(t)
  with open(to_file,"w") as fd:
    fd.write(ast.unparse(t))

if __name__ == '__main__':
  if len(sys.argv) != 3:
    sys.exit("COMMAND: [PYTHON] cull_input.py [FROM_FILE] [TO_FILE]")
  
  cull_input_text(sys.argv[1],sys.argv[2])
