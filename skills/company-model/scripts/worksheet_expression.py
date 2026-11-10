"""Parse the supported worksheet expression subset with Excel precedence.

Produces Python AST nodes for the existing safe interpreter, never Python eval.
Worksheet unary negation binds before power; equal-precedence powers associate left.
"""
import ast
import re


TOKEN=re.compile(r'\s*(?:(\d+(?:\.\d*)?(?:[eE][+-]?\d+)?|\.\d+(?:[eE][+-]?\d+)?)|("(?:[^"]|"")*")|([A-Za-z_][A-Za-z_0-9]*)|(<=|>=|<>|[+*/^(),=<>%&-]))')
OPS={'+':ast.Add,'-':ast.Sub,'*':ast.Mult,'/':ast.Div,'^':ast.Pow,'&':ast.BitAnd,
     '=':ast.Eq,'<>':ast.NotEq,'<':ast.Lt,'<=':ast.LtE,'>':ast.Gt,'>=':ast.GtE}
PRECEDENCE={'=':10,'<>':10,'<':10,'<=':10,'>':10,'>=':10,'&':15,'+':20,'-':20,'*':30,'/':30,'^':40}


def parse(text):
    tokens=[]; pos=0
    while pos<len(text):
        if not text[pos:].strip(): break
        match=TOKEN.match(text,pos)
        if not match: raise ValueError('Unsupported worksheet syntax near '+text[pos:pos+24])
        number,string,name,op=match.groups(); pos=match.end()
        tokens.append(('number',number) if number else ('string',string) if string else ('name',name) if name else ('op',op))
    index=0
    def peek(value): return index<len(tokens) and tokens[index][1]==value
    def expression(minimum=0):
        nonlocal index
        if index>=len(tokens): raise ValueError('Incomplete worksheet expression')
        kind,value=tokens[index]; index+=1
        if value in ('+','-') and kind=='op':
            node=ast.UnaryOp(op=ast.UAdd() if value=='+' else ast.USub(),operand=expression(50))
        elif value=='(':
            node=expression()
            if not peek(')'): raise ValueError('Unclosed worksheet parenthesis')
            index+=1
        elif kind=='number': node=ast.Constant(value=float(value) if any(c in value for c in '.eE') else int(value))
        elif kind=='string': node=ast.Constant(value=value[1:-1].replace('""','"'))
        elif kind=='name':
            if peek('('):
                index+=1; args=[]
                if not peek(')'):
                    args.append(expression())
                    while peek(','): index+=1; args.append(expression())
                if not peek(')'): raise ValueError('Unclosed worksheet function')
                index+=1; node=ast.Call(func=ast.Name(id=value),args=args,keywords=[])
            elif value.upper() in ('TRUE','FALSE'): node=ast.Constant(value=value.upper()=='TRUE')
            else: node=ast.Name(id=value)
        else: raise ValueError('Unsupported worksheet operand '+value)
        while index<len(tokens):
            op=tokens[index][1]
            if op=='%':
                if 60<minimum: break
                index+=1; node=ast.BinOp(left=node,op=ast.Div(),right=ast.Constant(value=100)); continue
            precedence=PRECEDENCE.get(op,-1)
            if precedence<minimum: break
            index+=1; right=expression(precedence+1)
            node=ast.Compare(left=node,ops=[OPS[op]()],comparators=[right]) if precedence==10 else ast.BinOp(left=node,op=OPS[op](),right=right)
        return node
    result=expression()
    if index!=len(tokens): raise ValueError('Unexpected worksheet token '+tokens[index][1])
    return result
