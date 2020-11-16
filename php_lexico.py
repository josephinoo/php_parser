import sys
import ply.lex as lex

reserved = {
    "__halt_compiler":"__HALT_COMPILER",
    "abstract":"ABSTRACT",
    "array":"ARRAY",
    "as":"AS",
    "break":"BREAK",
    "callable":"CALLABLE",
    "case":"CASE",
    "catch":"CATCH",
    "class":"CLASS",
    "clone":"CLONE",
    "const":"CONST", 
    "continue":"CONTINUE", 
    "declare":"DECLARE", 
    "default":"DEFAULT", 
    "die":"DIE", 
    "do":"DO",
    "echo":"ECHO", 
    "else":"ELSE", 
    "elseif":"ELSEIF", 
    "empty":"EMPTY", 
    "enddeclare":"ENDDECLARE", 
    "endfor":"ENDFOR", 
    "endforeach":"ENDFOREACH", 
    "endif":"ENDIF",
    "endswitch":"ENDSWITCH", 
    "endwhile":"ENDWHILE", 
    "eval":"EVAL", 
    "exit":"EXIT", 
    "extend":"EXTENDS", 
    "closetagal":"CLOSETAGAL", 
    "for":"FOR", 
    "foreach":"FOREACH",
    "function":"FUNCTION", 
    "global":"GLOBAL", 
    "goto":"GOTO", 
    "if":"IF", 
    "implements":"IMPLEMENTS", 
    "include":"INCLUDE", 
    "include_once":"INCLUDE_ONCE",
    "instanceof":"INSTANCEOF", 
    "insteadof":"INSTEADOF", 
    "interface":"INTERFACE", 
    "isset":"ISSET", 
    "list":"LIST", 
    "namespace":"NAMESPACE", 
    "new":"NEW",     
    "print":"PRINT", 
    "private":"PRIVATE", 
    "protected":"PROTECTED", 
    "public":"PUBLIC", 
    "require":"REQUIRE", 
    "require_once":"REQUIRE_ONCE", 
    "return":"RETURN",
    "static":"STATIC", 
    "switch":"SWITCH", 
    "throw":"THROW", 
    "trait":"TRAIT", 
    "try":"TRY", 
    "unset":"UNSET", 
    "use":"USE", 
    "var":"VAR", 
    "while":"WHILE", 
    "xor":"XOR",
    "true":"TRUE",
    "false":"FALSE",
    "finally":"FINALLY",

    
    
}


tokens = [
    # Open and Close Tag
    'OPENTAG', 'CLOSETAG',
    # symbols
    'PLUS', 'PLUSPLUS', 'PLUSEQUAL', 'MINUS', 'MINUSMINUS', 'MINUSEQUAL', 'TIMES',
    'TIMESTIMES', 'DIVIDE', 'LESS', 'LESSEQUAL', 'GREATER', 'GREATEREQUAL', 'EQUAL',
    'DEQUAL', 'DISTINT', 'ISEQUAL', 'SEMI', 'COMMA', 'LPAREN', 'RPAREN', 'LBRACKET',
    'RBRACKET', 'LBLOCK', 'RBLOCK', 'COLON', 'AMPERSANT', 'HASHTAG', 'DOT', 'QUOTES',
    'APOSTROPHE', 'DOT_DOT',

             'IS_IDENTICAL', 'IS_NOT_IDENTICAL',
   
    #operartors 
     'MUL_EQUAL', 'DIV_EQUAL', 'MOD_EQUAL', 'PLUS_EQUAL',
    'MINUS_EQUAL', 'SL_EQUAL', 'SR_EQUAL', 'AND_EQUAL', 'OR_EQUAL',
    'XOR_EQUAL', 'CONCAT_EQUAL',
    
            
    #reservadas con definiciones multiples
    
    "AND","OR",
    
    # others
    'COMMENTS', 'COMMENTS_C99', 'ID', 'IDVAR', 'NUM', 'STRING', 'VOID','ARROW',        
]+ list(reserved.values())


t_ignore = " \t"
#reservadas con definiciones multiples
def t_AND(t):
    r'and|AND|\&\&'
    return t
 
def t_OR(t):
    r'or|OR|\|\|'
    return t

   # others
def t_VOID(t):
    r'VOID|void'
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print(chr(27)+"[1;31m"+"\t ERROR: Illegal character"+chr(27)+"[0m")
    print("\t\tLine: "+str(t.lexer.lineno)+"\t=> " + t.value[0])
    t.lexer.skip(1)


def t_OPENTAG(t):
    r'(<\?(php)?)'
    return t


def t_CLOSETAG(t):
    r'\?>'
    return t



t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUAL = r'='
t_DISTINT = r'!'
t_LESS = r'<'
t_GREATER = r'>'
t_SEMI = r';'
t_COMMA = r','
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBLOCK = r'{'
t_RBLOCK = r'}'
t_COLON = r':'
t_AMPERSANT = r'\&'
t_HASHTAG = r'\#'
t_DOT = r'\.'
t_QUOTES = r'\"'
t_APOSTROPHE = r'\''


t_MUL_EQUAL = r'\*='
t_DIV_EQUAL = r'/='
t_MOD_EQUAL = r'%='
t_PLUS_EQUAL = r'\+='
t_MINUS_EQUAL = r'-='
t_SL_EQUAL = r'<<='
t_SR_EQUAL = r'>>='
t_AND_EQUAL  = r'&='
t_OR_EQUAL = r'\|='
t_XOR_EQUAL = r'\^='
t_CONCAT_EQUAL = r'\.='


def t_LESSEQUAL(t):
    r'<='
    return t


def t_GREATEREQUAL(t):
    r'>='
    return t


def t_DEQUAL(t):
    r'!='
    return t


def t_ISEQUAL(t):
    r'=='
    return t

def t_IS_IDENTICAL(t):
    r'==='
    return t

def t_IS_NOT_IDENTICAL(t):
    r'!=='
    return t


def t_MINUSMINUS(t):
    r'--'
    return t


def t_PLUSPLUS(t):
    r'\+\+'
    return t


def t_TIMESTIMES(t):
    r'\*\*'
    return t


def t_DOT_DOT(t):
    r'::'
    return t


# RE OTHERS


def t_COMMENTS(t):
    r'\/\*([^*]|\*[^\/])*(\*)+\/'
    t.lexer.lineno += t.value.count('\n')


def t_COMMENTS_C99(t):
    r'(\/\/|\#)(.)*?\n'
    t.lexer.lineno += 1


def t_IDVAR(t):
    r'\$[a-zA-Z0-9_][a-zA-Z0-9_]*'
    return t


def t_NUM(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t


def t_ID(t):
    r"[a-zA-Z0-9_][a-zA-Z0-9_]*"
    t.type = reserved.get(t.value, 'ID')
    return t


def t_STRING(t):
    r'(("[^"]*")|(\'[^\']*\'))'
    return t

def t_ARROW(t):
    r'\->\b'
    return t

lexer = lex.lex()
if __name__ == '__main__':

    if (len(sys.argv) > 1):
        script = sys.argv[1]

        scriptfile = open(script, 'r')
        scriptdata = scriptfile.read()
        lexer.input(scriptdata)

        print(chr(27)+"[0;36m"+"INICIA ANALISIS LEXICO"+chr(27)+"[0m")
        i = 1
        while True:
            tok = lexer.token()
            if not tok:
                break
            print("\t"+str(i)+" - "+"Line: "+str(tok.lineno) +
                  "\t"+str(tok.type)+"\t->  "+str(tok.value))
            i += 1

        print(chr(27)+"[0;36m"+"TERMINA ANALISIS LEXICO"+chr(27)+"[0m")

    else:
        print(chr(27)+"[0;31m"+"Pase el archivo de script PHP como parametro:")
        print(chr(27)+"[0;36m"+"\t$ python php_lexer.py" +
              chr(27)+"[1;31m"+" <filename>.txt"+chr(27)+"[0m")
