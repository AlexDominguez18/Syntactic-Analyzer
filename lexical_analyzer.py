import states

class LexicalAnalyzer():

    def __init__(self):
        self.__state = states.INITIAL
        self.__is_float = True
        self.__results = []
    
    def analyze(self, text):
        text = text + '$'
        #Starting to analyze
        i = 0
        while (i <= (len(text) - 1) and self.__state == states.INITIAL):
            lexeme = ''
            token = 'Error'
            number = -1
            while (i <= (len(text) - 1) and self.__state != states.ESCAPE):
                #In the initial state
                if self.__state == states.INITIAL:
                    if text[i].isspace():
                        self.__state = states.INITIAL
                    elif text[i].isalpha() or text[i] == '_':
                        self.__state = states.ID
                        lexeme += text[i]
                        token = 'id'
                        number = 1
                    elif text[i].isnumeric():
                        self.__state = states.CONSTANT
                        lexeme += text[i]
                        token = 'constante'
                        number = 13
                    elif text[i] == ';':
                        self.__state = states.SEMICOLON
                        lexeme += text[i]
                        token = 'punto y coma'
                        number = 2
                    elif text[i] == ',':
                        self.__state = states.COMMA
                        lexeme += text[i]
                        token = 'coma'
                        number = 3
                    elif text[i] == '.':
                        self.__state = states.DOT
                        lexeme += text[i]
                    elif text[i] == '(':
                        self.__state = states.ESCAPE
                        lexeme += text[i]
                        token = 'parentesis izquierdo'
                        number = 4
                    elif text[i] == ')':
                        self.__state = states.ESCAPE
                        lexeme += text[i]
                        token = 'parentesis derecho'
                        number = 5
                    elif text[i] == '{':
                        self.__state = states.ESCAPE
                        lexeme += text[i]
                        token = 'llave izquierda'
                        number = 6
                    elif text[i] == '}':
                        self.__state = states.ESCAPE
                        lexeme += text[i]
                        token = 'llave derecha'
                        number = 7
                    elif text[i] == '+' or text[i] == '-':
                        self.__state = states.ADD_OR_SUB
                        lexeme += text[i]
                        token = 'operador suma'
                        number = 14
                    elif text[i] == '|':
                        self.__state = states.PIPE
                        lexeme += text[i]
                    elif text[i] == '&':
                        self.__state = states.ANDPERSAND
                        lexeme += text[i]
                    elif text[i] == '*' or text[i] == '/':
                        self.__state = states.MUL_OR_DIV
                        lexeme += text[i]
                        token = 'operador multiplicacion'
                        number = 16
                    elif text[i] == '=':
                        self.__state = states.ASSIGN_OPERATOR
                        lexeme += text[i]
                        token = 'asignacion'
                        number = 8
                    elif text[i] == '>' or text[i] == '<' or text[i] == '!':
                        self.__state = states.RELATIONAL_OPERATOR
                        lexeme += text[i]
                        token = 'operador relacional'
                        number = 17
                    elif text[i] == '$':
                        self.__state = states.ESCAPE
                        lexeme += text[i]
                        token = 'pesos'
                        number = 18
                    else:
                        self.__state = states.ERROR
                        lexeme += text[i]
                        token = 'error'
                    i += 1
                #State for ID's
                elif self.__state == states.ID:
                    if text[i].isalpha() or text[i].isnumeric() or text[i] == '_':
                        self.__state = states.ID
                        lexeme += text[i]
                        token = 'id'
                        i += 1
                    else:
                        self.__state = states.ESCAPE
                #State for constants
                elif self.__state == states.CONSTANT:
                    if text[i].isnumeric():
                        self.__state = states.CONSTANT
                        lexeme += text[i]
                        token = 'constante'
                        i += 1
                    elif text[i] == '.' and not self.__is_float:
                        self.__state = states.DOT
                        self.__is_float = True
                    elif text[i] == '.' and self.__is_float:
                        self.__state = states.DOT
                        lexeme += text[i]
                        self.__is_float = False
                        i += 1
                    else:
                        self.__state = states.ESCAPE
                #State for dot
                elif self.__state == states.DOT:
                    if text[i].isnumeric():
                        self.__state = states.CONSTANT
                        lexeme += text[i]
                        token = 'constante'
                        number = 13
                        i += 1
                    else:
                        if not self.__is_float:
                            self.__is_float = True
                        self.__state = states.ESCAPE
                #State for ;
                elif self.__state == states.SEMICOLON:
                    if text[i] == ';':
                        self.__state = states.SEMICOLON
                        lexeme += ';'
                        token = 'punto y coma'
                        i += 1
                    else:
                        self.__state = states.ESCAPE
                #State for ,
                elif self.__state == states.COMMA:
                    if text[i] == ',':
                        self.__state = states.COMMA
                        lexeme += ','
                        token = 'coma'
                        i += 1
                    else:
                        self.__state = states.ESCAPE
                #State for +,-
                elif self.__state == states.ADD_OR_SUB:
                    if text[i] == '+' or text[i] == '-':
                        self.__state = states.ESCAPE
                        lexeme += text[i]
                        token = 'operador suma'
                        i += 1
                    else:
                        self.__state = states.ESCAPE
                #State for |
                elif self.__state == states.PIPE:
                    if text[i] == '|':
                        self.__state = states.LOGIC_OPERATOR
                        lexeme += text[i]
                        token = 'operador logico'
                        number = 15
                        i += 1
                    else:
                        self.__state == states.ESCAPE
                #State for &
                elif self.__state == states.ANDPERSAND:
                    if text[i] == '&':
                        self.__state = states.LOGIC_OPERATOR
                        lexeme += text[i]
                        token = 'operador logico'
                        number = 15
                        i += 1
                    else:
                        self.__state = states.ESCAPE
                #State for =
                elif self.__state == states.ASSIGN_OPERATOR:
                    if text[i] == '=':
                        self.__state = states.RELATIONAL_OPERATOR
                        lexeme += text[i]
                        token = 'operador relacional'
                        number = 17
                        i += 1
                    else:
                        self.__state = states.ESCAPE
                #State for <,>,!
                elif self.__state == states.RELATIONAL_OPERATOR:
                    if text[i] == '=':
                        self.__state = states.RELATIONAL_OPERATOR
                        lexeme += text[i]
                        token = 'operador relacional'
                        i += 1
                    else:
                        self.__state = states.ESCAPE
                else:
                    break
            
            self.__state = states.INITIAL
            self.__results.append({
                "token": token,
                "lexeme": lexeme,
                'number': number
            })
            self.change_tokens()

    def change_tokens(self):
        for item in self.__results:
            if item['lexeme'] == "if":
                item['token'] = "condicional SI"
                item['number'] = 9
            elif item['lexeme'] == "while":
                item['token'] = "ciclo MIENTRAS"
                item['number'] = 10
            elif item['lexeme'] == "return":
                item['token'] = "retorno"
                item['number'] = 11
            elif item['lexeme'] == "else":
                item['token'] = "condicional SI NO"
                item['number'] = 12
            elif item['lexeme'] == "int":
                item['token'] = "tipo de dato"
                item['number'] = 0
            elif item['lexeme'] == "float":
                item['token'] = "tipo de dato"
                item['number'] = 0
            elif item['lexeme'] == "char":
                item['token'] = "tipo de dato"
                item['number'] = 0
            elif item['lexeme'] == "void":
                item['token'] = "tipo de dato"
                item['number'] = 0
            else:
                pass
    
    def get_results(self):
        return self.__results
    
    def clear(self):
        self.__results = []
