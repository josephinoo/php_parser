# Yacc example

import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from pip._vendor.distlib.compat import raw_input

from php_lexico import tokens
def p_algoritmo(p):
    '''algoritmo : imprimir
                | asignacion
                | expresion
                | comparacion
                | sentenciaIf'''

def p_sentenciaIf(p):
    'sentenciaIf : LPAREN comparacion RPAREN COLON algoritmo '
def p_expresion(p):
    '''expresion : valor

    '''
def p_asignacion(p):
    'asignacion : VAR EQUAL expresion'
def p_expresion_aritmetica(p):
    'expresion : valor operadorMat expresion'

def p_comparacion(p):
    'comparacion : expresion operadorComp expresion'

def p_operadorMat(p):
    '''operadorMat : PLUS
                    | MINUS
                    | TIMES
                    | DIVIDE

    '''

def p_operadorComp(p):
    '''operadorComp : DEQUAL
                    | LESSEQUAL
                    | GREATEREQUAL
                    | ISEQUAL
                    | GREATER
                    | LESS

    '''

def p_valor(p):
    '''valor : NUM
             | VAR

    '''

def p_imprimir(p):
    'imprimir : PRINT LPAREN expresion RPAREN'
# Error rule for syntax errors
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
