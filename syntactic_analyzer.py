import os
from stack import Stack

RIGHT = 1
LEFT = 0

class SyntacticAnalyzer():

    def __init__(self):
        self.table = []
        self.rules = []
        self.get_table()
        self.get_rules()
    
    def get_table(self):
        path_file = os.path.join(os.path.dirname(__file__), 'rules/GR2slrTable.txt')
        f = open(path_file, 'r')
        for line in f.readlines():
            self.table.append( [ int (x) for x in line.split('\t') ] )
        f.close()

    def get_rules(self):
        path_file = os.path.join(os.path.dirname(__file__), 'rules/GR2slrRulesId.txt')
        f = open(path_file, 'r')
        for line in f.readlines():
            self.rules.append( [ int (x) for x in line.split('\t') ] )
        f.close()
    
    def is_accepted(self, code):
        stack = Stack()
        #Initial push
        stack.push(0)
        #Analyzing
        i = 0
        while i < len(code):
            row = stack.top()
            column = code[i]['number']
            action = self.table[row][column]
            print(code[i])
            print(stack)
            print(f'row = {row}, column = {column}, action = {action}')
            #Displacement case
            if action > 0:
                stack.push(code[i]['number'])
                stack.push(action)
                i += 1
            #Reduction case
            elif action < -1:
                row = action
                row = row * -1
                row = row - 1
                rule = self.rules[row][RIGHT] * 2
                j = 0
                while (j < rule):
                    stack.pop()
                    j += 1
                column = self.rules[row][LEFT]
                newRow = stack.top()
                stack.push(self.rules[row][LEFT])
                stack.push(self.table[newRow][column])
            #Empty cell
            elif action == 0:
                return False
            #Case accepted
            elif action == -1:
                return True
