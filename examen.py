import sys
import ply.lex as lex
import ply.yacc as yacc

tokens = [
             # Open and Close Tag
             'SELECT', 'FROM', 'DELETE'
             # symbols
             'VAR', 'ATTR', 'AS', 'EQUAL', 'MINUSEQUAL', 'PLUSEQUAL', 'OR',
             'AND', 'CADENA', 'WHERE','NUM'
         ] + list(reserved.values())

t_PLUSEQUAL = r'>='
t_MINUSEQUAL = r'<='
def t_CADENA(t):
    r'(("[^"]*")|(\'[^\']*\'))'
    return t

def t_NUM(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

t_SELECT = r'SELECT'
t_DELETE = r'DELETE'
t_FROM = r'FROM'
t_AS = r'as'
t_AND = r'and'
t_OR = r'or'
t_OR = r'where'
t_EQUAL = r'='
def t_VAR(t):
    r'\$[a-zA-Z0-9_][a-zA-Z0-9_]*'
    return t

def t_ATTR(t):
    r'\$[a-zA-Z0-9_][a-zA-Z0-9_]*'
    return t

def get_lexer():
    return lex.lex()
lexer = lex.lex()