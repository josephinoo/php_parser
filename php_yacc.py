import sys
import ply.yacc as yacc
import php_lexico

VERBOSE = 1

precedence = (
    ('left', 'INCLUDE', 'REQUIRE'),
    ('left', 'COMMA'),
    ('left', 'EQUAL', 'PLUSEQUAL', 'MINUSEQUAL'),
    ('left', 'SEMI'),
    ('left', 'OR'),
    ('left', 'XOR'),
    ('left', 'AND'),
    ('nonassoc', 'ISEQUAL', 'DEQUAL'),
    ('nonassoc', 'LESS', 'LESSEQUAL', 'GREATER', 'GREATEREQUAL'),
    ('left', 'PLUS', 'MINUS'),
    ('right', 'LBRACKET'),
    ('nonassoc', 'NEW', 'CLONE'),
    ('left', 'ELSEIF'),
    ('left', 'ELSE'),
    ('right', 'PRIVATE', 'PROTECTED', 'PUBLIC'),
)


def p_program(p):
    'program : OPENTAG declaration_list CLOSETAG'
    pass


def p_declaration_list(p):
    '''declaration_list : declaration
                            | declaration declaration_list
    '''
    pass


def p_declaration(p):
    '''declaration : var_declaration
                               | fun_declaration
                               | area fun_declaration
                               | header_declaration
                               | class_declaration
                               | echo_stmt
                               | selection_stmt
                           | iteration_stmt
                               | typeclass
    '''
    pass

def p_expression(p):

    pass


def p_echo_stmt(p):
    '''echo_stmt : echo_stmt ECHO STRING SEMI
                             | echo_stmt ECHO IDVAR SEMI
                             | empty
                             | echo_stmt ECHO NUM SEMI
                             | echo_stmt ECHO boolean SEMI
                             | echo_stmt ECHO fun_declaration SEMI
    '''
    pass


def p_header_declaration(p):
    '''header_declaration : REQUIRE LPAREN STRING RPAREN SEMI
                      | INCLUDE LPAREN STRING RPAREN SEMI
'''
    pass


def p_class_declaration(p):
    '''class_declaration : area CLASS ID LBLOCK attributes RBLOCK
                                             | CLASS ID LBLOCK attributes RBLOCK
    '''
    pass

def p_attributes(p):
    '''attributes : attribute
                    | attribute attributes
    '''
    pass

def p_attribute1(p):
    '''attribute : attribute area var_declaration
                             | area var_declaration
                             | attribute area fun_declaration
                             | area fun_declaration
                             | fun_declaration
    '''
    pass


def p_area(p):
    '''area : PRIVATE
                    | PUBLIC
                    | PROTECTED
    '''
    pass


def p_var_declaration(p):
    '''var_declaration : IDVAR SEMI var_declaration
                   | IDVAR SEMI
                   | TIMESTIMES IDVAR SEMI
                   | TIMESTIMES IDVAR SEMI var_declaration
                   | assing_var IGUAL NUM SEMI var_declaration
                   | assing_var IGUAL NUM SEMI
                   | assing_var IGUAL STRING SEMI var_declaration
                   | assing_var IGUAL STRING SEMI
                   | assing_var IGUAL boolean SEMI var_declaration
                   | assing_var IGUAL boolean SEMI
                   | assing_var IGUAL IDVAR SEMI var_declaration
                   | assing_var IGUAL IDVAR SEMI
                   | AMPERSANT IDVAR SEMI var_declaration
                   | AMPERSANT IDVAR IGUAL IDVAR SEMI  selection_stmt
                   | AMPERSANT IDVAR SEMI
                   | assing_var IGUAL simple_expression SEMI
    '''
    pass

def p_assing_var(p):
    '''assing_var : var
                    | var ARROW ID
    '''
    pass

def p_IGUAL(p):
    ''' IGUAL : EQUAL
                | MUL_EQUAL
                | DIV_EQUAL
                | CONCAT_EQUAL
                | MOD_EQUAL
                | PLUS_EQUAL
                | MINUS_EQUAL
    '''
    pass




def p_fun_declaration(p):
    '''fun_declaration : FUNCTION ID LPAREN params RPAREN
                                       | FUNCTION ID LPAREN params RPAREN compount_stmt
    '''
    pass


def p_params(p):
    '''params : param_list
                      | empty
    '''
    pass


def p_param_list(p):
    '''param_list : param_list COMMA param_list
                              | param
    '''
    pass


def p_param(p):
    '''param : IDVAR
         | IDVAR LBRACKET RBRACKET
'''
    pass


def p_compount_stmt(p):
    'compount_stmt : LBLOCK echo_stmt local_declarations echo_stmt statement_list echo_stmt RBLOCK'
    pass


def p_local_declarations(p):
    '''local_declarations : local_declarations var_declaration
                                              | empty
    '''
    pass


def p_statement_list(p):
    '''statement_list : statement_list statement
                                      | empty
    '''
    pass


def p_statement(p):
    '''statement : expression_stmt
                             | compount_stmt
                             | selection_stmt
                             | iteration_stmt
                         | return_stmt
                         | class_declaration
                             | echo_stmt
    '''
    pass


def p_expression_stmt(p):
    'expression_stmt : expression SEMI'
    pass


def p_selection_stmt_1(p):
    '''selection_stmt : IF LPAREN expression RPAREN statement
                                      | IF LPAREN expression RPAREN statement selection
    '''
    pass


def p_selection(p):
    '''selection : ELSE statement
                             | ELSEIF statement selection
     '''
    pass


def p_selection_stmt_2(p):
    '''selection_stmt : SWITCH LPAREN var RPAREN statement
                                      | CASE NUM COLON statement BREAK SEMI
                                       | CASE STRING COLON statement BREAK SEMI
                                      | DEFAULT COLON statement BREAK SEMI
    '''
    pass


def p_iteration_stmt_1(p):
    'iteration_stmt : FOR LPAREN var_declaration SEMI expression SEMI additive_expression RPAREN statement '
    pass


def p_iteration_stmt_2(p):
    'iteration_stmt : WHILE LPAREN expression RPAREN statement'
    pass


def p_iteration_stmt_3(p):
    'iteration_stmt : DO LBLOCK statement SEMI RBLOCK WHILE LPAREN expression RPAREN'
    pass


def p_return_stmt(p):
    '''return_stmt : RETURN SEMI
                               | RETURN expression SEMI
    '''
    pass


def p_expression(p):
    '''expression : assing_var EQUAL expression
                              | simple_expression
                              | assing_var EQUAL AMPERSANT IDVAR
                          | expression AND expression
                              | expression OR expression
                              | assing_var
    '''
    pass

def p_var(p):
    '''var : IDVAR
               | IDVAR LBRACKET expression RBRACKET
    '''
    pass


def p_simple_expression(p):
    '''simple_expression : additive_expression relop additive_expression
                                             | additive_expression
    '''
    pass


def p_relop(p):
    '''relop : LESS
                     | LESSEQUAL
                     | GREATER
                     | GREATEREQUAL
                     | DEQUAL
                     | DISTINT
                     | ISEQUAL
                     | IS_IDENTICAL
                     | IS_NOT_IDENTICAL
                     | SR_EQUAL
                     | SL_EQUAL
                     | AND_EQUAL
                     | OR_EQUAL
                     | XOR_EQUAL
                     | CONCAT_EQUAL
                     
    '''
    pass


def p_additive_expression(p):
    '''additive_expression : additive_expression addop term
                                       | term
                                       | term MINUSMINUS
                                   | term PLUSPLUS
    '''
    pass


def p_addop(p):
    '''addop : PLUS
                     | MINUS
    '''
    pass


def p_term(p):
    '''term : term mulop factor
                    | factor
    '''
    pass


def p_mulop(p):
    '''mulop : TIMES
                     | DIVIDE
    '''
    pass


def p_factor(p):
    '''factor : LPAREN expression RPAREN
                      | var
                      | NUM
                      | STRING
                      | boolean
                      | IDVAR LPAREN args RPAREN
    '''
    pass


def p_args(p):
    '''args : args_list
                    | empty
                    | VOID
    '''
    pass


def p_args_list(p):
    '''args_list : args_list COMMA expression
                             | expression
    '''
    pass


def p_boolean(p):
    '''boolean : TRUE
                       | FALSE
    '''
    pass


def p_tclass(p):
    'typeclass : ID IDVAR EQUAL NEW constructor SEMI'
    pass


def p_costructor(p):
    '''constructor : ID LPAREN RPAREN
                               | ID LPAREN args RPAREN
    '''
    pass


def p_empty(p):
    'empty :'
    pass


def p_error(p):
    if VERBOSE:
        if p is not None:
            print(
                chr(27)+"[1;31m"+"\t ERROR: Syntax error - Unexpected token" + chr(27)+"[0m")
            print("\t\tLine: "+str(p.lexer.lineno)+"\t=> "+str(p.value))
        else:
            print(chr(27)+"[1;31m"+"\t ERROR: Syntax error"+chr(27)+"[0m")
            print("\t\tLine:  "+str(php_lexico.lexer.lineno))

    else:
        raise Exception('syntax', 'error')

tokens=php_lexico.tokens

lexer = php_lexico.get_lexer()
parser = yacc.yacc()

if __name__ == '__main__':
    if (len(sys.argv) > 0):
        script = sys.argv[1]

        scriptfile = open(script, 'r')
        scriptdata = scriptfile.read()

        print(chr(27)+"[0;36m"+"INICIA ANALISIS SINTACTICO"+chr(27)+"[0m")
        result  = parser.parse(scriptdata)
        print(result)
        print("Hola bebe, no tienes errores sintacticos")
        print(chr(27)+"[0;36m"+"TERMINA ANALISIS SINTACTICO"+chr(27)+"[0m")

    else:
        print(chr(27)+"[0;31m"+"Pase el archivo de script PHP como parametro:")
        print(chr(27)+"[0;36m"+"\t$ python php_parser.py" +
              chr(27)+"[1;31m"+" <filename>.php"+chr(27)+"[0m")
