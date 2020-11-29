# Yacc example

import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from pip._vendor.distlib.compat import raw_input

from examen import tokens
def p_query(p):
    '''query : as
                | tomar
                | tomaror
              '''

def p_tomar(p):
    'tomar : selector FROM VAR WHERE VAR operadorComp valor '

def p_as(p):
    'as : selector VAR AS VAR FROM VAR '

def p_tomaror(p):
    'tomaror : selector FROM VAR WHERE VAR operadorComp valor orfunc '

def p_orfunc(p):
    'orfunc : OR VAR operadorComp valor  '
def p_selector(p):
    '''selector : SELECT
                    | DELETE


    '''

def p_operadorComp(p):
    '''operadorComp : EQUAL
                    | minusEQUAL
                    | plusEREQUAL


    '''

def p_valor(p):
    '''valor : NUM
             | VAR

    '''


def p_error(p):
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()

while True:
    try:
        s = raw_input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
