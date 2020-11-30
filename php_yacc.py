import sys
import ply.yacc as yacc
import php_lexico

VERBOSE = 1
# Joseph Avila precedencias https://www.dabeaz.com/ply/ply.html 6.6
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
    ('right', 'PRIVATE', 'PROTECTED', 'PUBLIC')
)
# Joseph Avila para el open tad y close tag de php


def p_program(p):
    '''program : OPENTAG declaration_list CLOSETAG'''
    pass

# Joseph Avila, toda lista de declaraciones que puede tener


def p_declaration_list(p):
    '''declaration_list : declaration
                            | declaration declaration_list
    '''
    pass

# Joseph Avila para la declaracion de variables


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




# Joseph avila para echo , puede estar vacio o no


def p_echo_stmt(p):
    '''echo_stmt : echo_stmt ECHO echo_params SEMI
                             | empty
    '''
    pass

# Joseph Avila , parametros que puede tener la opcion de print en php


def p_echo_params(p):
    '''echo_params : echo_param
                    | echo_param DOT echo_params'''

# Joseph Avila que parametros soporta echo


def p_echo_param(p):
    '''echo_param : STRING
                    | IDVAR
                    | NUM
                    | boolean
                    | fun_declaration
                    | fun_call
                    '''
    pass

# Joseph Avila declarcion delos headers


def p_header_declaration(p):
    '''header_declaration : REQUIRE LPAREN STRING RPAREN SEMI
                      | INCLUDE LPAREN STRING RPAREN SEMI
'''
    pass

# Joseph Avila para declarar clases en php


def p_class_declaration(p):
    '''class_declaration : area CLASS ID LBLOCK attributes RBLOCK
                                             | CLASS ID LBLOCK attributes RBLOCK
    '''
    pass

# Joseph Avila atributos


def p_attributes(p):
    '''attributes : attribute
                    | attribute attributes
    '''
    pass

# Joseph Avila lista de atributos


def p_attribute1(p):
    '''attribute : attribute area var_declaration
                             | area var_declaration
                             | attribute area fun_declaration
                             | area fun_declaration
                             | fun_declaration
    '''
    pass

# Joseph Avila el are en php, puede ser INCLUDE PRIVATE OR PROTECTE, puede ser para clases o funciones


def p_area(p):
    '''area : PRIVATE
                    | PUBLIC
                    | PROTECTED
    '''
    pass

# Joseph Avila para la declaracion de variables


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
                   | IDVAR IGUAL array_declare SEMI
                   | AMPERSANT IDVAR SEMI var_declaration
                   | AMPERSANT IDVAR IGUAL IDVAR SEMI  selection_stmt
                   | AMPERSANT IDVAR SEMI
                   | assing_var IGUAL simple_expression SEMI
                   | IDVAR IGUAL simple_expression SEMI
                   | fun_call SEMI
    '''
    pass


def p_array_declare(p):
    '''array_declare : ARRAY LPAREN array_values RPAREN
    '''
    pass

def p_array_values(p):
    '''array_values : array_value
                    | array_value COMMA array_values
    '''
    pass

def p_array_value(p):
    '''array_value : factor DARROW factor
    '''
    pass

def p_assing_var(p):
    '''assing_var : var
                    | var ARROW ID
                    | var DARROW ID
    '''
    pass

# Joseph Avila PARA IGUAL


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

# Angel Jumbo declaracion de funciones


def p_fun_declaration(p):
    '''fun_declaration : FUNCTION ID LPAREN params RPAREN
                                       | FUNCTION ID LPAREN params RPAREN compount_stmt
    '''
    pass

# Angel Jumbo llamado de funciones


def p_fun_call(p):
    '''fun_call : ID LPAREN params RPAREN
                    | assing_var LPAREN params RPAREN'''


def p_params(p):
    '''params : param_list
                      | empty
    '''
    pass


def p_param_list(p):
    '''param_list : param
                    | param COMMA param_list
    '''
    pass


def p_param(p):
    '''param : IDVAR
         | IDVAR LBRACKET RBRACKET
         | term
'''
    pass


def p_compount_stmt(p):
    '''compount_stmt : LBLOCK echo_stmt local_declarations echo_stmt statement_list echo_stmt RBLOCK'''
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
    '''expression_stmt : expression SEMI'''
    pass

# Angel Jumbo estructuras de control


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
    '''iteration_stmt : FOR LPAREN var_declaration expression SEMI additive_expression RPAREN statement '''
    pass


def p_iteration_stmt_2(p):
    '''iteration_stmt : WHILE LPAREN expression RPAREN statement'''
    pass


def p_iteration_stmt_3(p):
    '''iteration_stmt : DO LBLOCK statement SEMI RBLOCK WHILE LPAREN expression RPAREN'''
    pass


# DANIEL SANCHEZ PARA COMPARACION RETUN
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
                              | fun_call
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

# DANIEL SANCHEZ PARA COMPARACION


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

# DANIEL SANCHEZ PARA EXPRESIONES ADITIVAS


def p_additive_expression(p):
    '''additive_expression : additive_expression addop term
                                       | term
                                       | term MINUSMINUS
                                   | term PLUSPLUS
                                   | fun_call
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

# Joseph Avila , para factores , cuando se enceuntre en tres (factor)


def p_factor(p):
    '''factor : LPAREN expression RPAREN
                      | var
                      | NUM
                      | STRING
                      | boolean
                      | IDVAR LPAREN args RPAREN
    '''
    pass

# Joseph Avila para los arguementos


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

# DANIEL SANCHEZ PARA BOOLEAN


def p_boolean(p):
    '''boolean : TRUE
                       | FALSE
    '''
    pass

# Angel Jumbo creacion de clases


def p_tclass(p):
    '''typeclass : ID IDVAR EQUAL NEW constructor SEMI
                | IDVAR EQUAL NEW constructor SEMI '''
    pass


# DANIEL SANCHEZ PARA  DISENO DE CONSTRUCTORES
def p_costructor(p):
    '''constructor : ID LPAREN RPAREN
                               | ID LPAREN args RPAREN
    '''
    pass


def p_empty(p):
    '''empty :'''
    pass


def p_error(p):
    if VERBOSE:
        if p is not None:
            print(p)
            print(
                chr(27)+"[1;31m"+"\t ERROR: Syntax error - Inesperado token" + chr(27)+"[0m")
            print("\t\tLine: "+str(p.lexer.lineno)+"\t=> "+str(p.value))
            file=open("tmp",'w')
            file.write(chr(27)+"[1;31m"+"\t ERROR: Syntax error - Inesperado token" + chr(27)+"[0m")
            file.write("\t\tLine: "+str(p.lexer.lineno)+"\t=> "+str(p.value))
            file.close
        else:

            print("\t\tLine:  "+str(php_lexico.lexer.lineno))

    else:
        raise Exception('syntax', 'error')
    return "data"

def get_yacc():
    return yacc.yacc()

tokens = php_lexico.tokens

lexer = php_lexico.get_lexer()
parser = yacc.yacc()
# Joseph el parser, con argumentos
def executeArg():
    if (len(sys.argv) > 1):
        script = sys.argv[1]

        scriptfile = open(script, 'r')
        scriptdata = scriptfile.read()

        print(chr(27)+"[0;36m"+"INICIA ANALISIS SINTACTICO"+chr(27)+"[0m")
        result = parser.parse(scriptdata)
        errors=open("tmp","r")
       # print(result)
        print(result)
        print("Hola bebe, no tienes errores sintacticos")
        print(chr(27)+"[0;36m"+"TERMINA ANALISIS SINTACTICO"+chr(27)+"[0m")
    else:
        print(chr(27)+"[0;31m"+"Pase el archivo de script PHP como parametro:")
        print(chr(27)+"[0;36m"+"\t$ python php_parser.py" +
              chr(27)+"[1;31m"+" <filename>.php"+chr(27)+"[0m")
def executeFunction(datafile):
        scriptfile = open(datafile, 'r')
        scriptdata = scriptfile.read()

        print(chr(27)+"[0;36m"+"INICIA ANALISIS SINTACTICO"+chr(27)+"[0m")
        result = parser.parse(scriptdata)
        errors=open("tmp","r")


        print(result)
        print("Hola bebe, no tienes errores sintacticos")
        print(chr(27)+"[0;36m"+"TERMINA ANALISIS SINTACTICO"+chr(27)+"[0m")
        return errors.read()


if __name__ == '__main__':
    executeArg()

