import sys
import ast
import re

# https://docs.python.org/3/library/ast.html
# https://stackoverflow.com/questions/1515357/simple-example-of-how-to-use-ast-nodevisitor

class CullInputText(ast.NodeTransformer):
  def visit_Call(self, node):
    if isinstance(node.func, ast.Name) and node.func.id == 'input':
      return ast.Call(node.func,[],[])
    return ast.NodeTransformer.generic_visit(self, node)

class CullGlobalCode(ast.NodeTransformer):
  def generic_visit(self, node):
    return None

  def visit_Module(self, node):
    return super().generic_visit(node)

  def visit_Import(self, node):
    return node

  def visit_ImportFrom(self, node):
    return node

  def visit_ClassDef(self, node):
    return node

  def visit_FunctionDef(self, node):
    return node

  def visit_AsyncFunctionDef(self, node):
    return node

def get_header(from_file):
  with open(from_file,"r") as fd:
    lines = fd.read().splitlines()
  header = []
  for i in range(3):
    if len(lines) > i and re.match(r"\uFEFF?\s*#.*", lines[i]):
      header += [lines[i]]
  return header

def get_tree(from_file):
  with open(from_file,"r") as fd:
    root = ast.parse(fd.read(), filename=from_file)
  return root

def cull_input_text(root, meta_visitor):
  visitor = meta_visitor()
  visitor.visit(root)
  return root

if __name__ == '__main__':
  if len(sys.argv) != 4:
    sys.exit("COMMAND: [PYTHON] cull_input.py [input/global] [FROM_FILE] [TO_FILE]")

  cull_mode = sys.argv[1]
  from_file = sys.argv[2]
  to_file = sys.argv[3]

  header = get_header(from_file)
  root = get_tree(from_file)

  match cull_mode:
    case "input":
      root = cull_input_text(root, CullInputText)
    case "global":
      root = cull_input_text(root, CullGlobalCode)
    case _:
      sys.exit(f"Unrecognised cull mode: {cull_mode}")

  with open(to_file,"w") as fd:
    for line in header:
      fd.write(line + "\n")
    fd.write("\n")
    fd.write(ast.unparse(root))
