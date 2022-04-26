import sys
import customVisitor

from IMP_py.IMP_DLexer import IMP_DLexer
from IMP_py.IMP_DParser import IMP_DParser
from antlr4 import *
from antlr4.tree.Trees import Trees


def main(argv):
    inputFile = FileStream(argv[1])

    lexer = IMP_DLexer(inputFile)
    stream = CommonTokenStream(lexer)
    parser = IMP_DParser(stream)
    tree = parser.progr()  # progr - start rule
    treeString = Trees.toStringTree(tree, None, parser)
    treeString = treeString.replace("( ", "")
    treeString = treeString.replace(" )", "")

    print("\n")
    print("============IMP_D string tree, created using ANTLR4============")
    print(treeString)
    print("===============================================================")

    # Visitor rules
    visitor = customVisitor.CustomVisitor()
    result = visitor.visit(tree)

    print("\n")
    print("====================TRANSLATED AM STRING=======================")
    print(result)
    print("===============================================================")

if __name__ == "__main__":
    main(sys.argv)

"""
LKD aprēķins IMP_D sintaksē:
while not x=y do
    if x=<y then y:=y-x
    else x:=x-y fi
od

LKD aprēķins AM sintaksē:
LOOP(FETCH(y):FETCH(x):EQ:NEG,FETCH(y):FETCH(x):LE:BRANCH(FETCH(x):FETCH(y):SUB:STORE(y),FETCH(y):FETCH(x):SUB:STORE(x)))

LOOP(FETCH(x):FETCH(y):EQ:NEG,FETCH(x):FETCH(y):LE:BRANCH(FETCH(y):FETCH(x):SUB:STORE(y),FETCH(x):FETCH(y):SUB:STORE(x)))
"""