

#yoink! https://levelup.gitconnected.com/create-your-own-expression-parser-d1f622077796
import enum
from math import sqrt, sin, cos
import re
from typing import List, Set

import random



class TokenType(enum.Enum):
    ident = 0
    numeric = 1
    operator = 2
    
supportedConsts = {"PI": 3, "e": 3}
supportedOps = {
    "sqrt" : sqrt,
    "sin": sin,
    "cos": cos
}

T = TokenType
ident = re.compile(r"^[A-Za-z_]")
num = re.compile(r"^[0-9.]")

tokenRe = re.compile(r"[0-9]+(\.[0-9]*)?|[A-Za-z_][A-Za-z_0-9]*|\S")
#matches, decimal number, or identifiers, or not whitespace / any operator
class Token:
    def __init__(self, text, index) -> None:
        self.text = text
        self.index = index
        
        if ident.match(text):
            self.type = T.ident
        elif num.match(text):
            self.type = T.numeric
        else:
            self.type = T.operator
            
    def __str__(self) -> str:
        return f"token({self.text}, {self.index})"
            
            
class Expression: 
    def __init__(self, opToken, args) -> None:
        self.opToken = opToken
        self.args = args
        
    def eval(self):
        pass

class NumExp(Expression):
    def __init__(self, val) -> None:
        super().__init__(None, [val])
        
    def eval(self):
        val = float(self.args[0].text)
        return val + random.random() / 1000 * random.choice([-1, 1])

class AddExp(Expression):
    def __init__(self,token, left, right) -> None:
        super().__init__(token, [left, right])
        
    def eval(self):
        return self.args[0].eval() + self.args[1].eval()

class SubExp(Expression):
    def __init__(self,token, left, right) -> None:
        super().__init__(token, [left, right])
        
    def eval(self):
        return self.args[0].eval() - self.args[1].eval()

class MulExp(Expression):
    def __init__(self,token, left, right) -> None:
        super().__init__(token, [left, right])

    def eval(self):
        return self.args[0].eval() * self.args[1].eval()
    
class DivExp(Expression):
    def __init__(self,token, left, right) -> None:
        super().__init__(token, [left, right])

    def eval(self):
        return self.args[0].eval() / self.args[1].eval()

class NegExp(Expression):
    def __init__(self,token, val) -> None:
        super().__init__(token, [val])

    def eval(self):
        return - self.args[0].eval()
    
class IdentExp(Expression):

    def __init__(self, opToken : Token) -> None:
        super().__init__(opToken, [])
    
    def eval(self):
        if self.opToken.text in supportedConsts:
            return supportedConsts[self.opToken.text]
        raise RuntimeError(f"constant not supported: {self.opToken.text}")

class FuncExp(Expression):
    
    def __init__(self, opToken, args) -> None:
        super().__init__(opToken, args)
    
    def eval(self):
        try: 
            return  supportedOps[self.opToken.text](*[arg.eval() for arg in self.args])
        except KeyError:
            raise RuntimeError(f"operation not supported: {self.opToken.text}")
        except ValueError:
            raise RuntimeError(f"too many or too few arguments for: {self.eval}, args: {self.args}")

class PowExp(Expression):
    def __init__(self, opToken, left, right) -> None:
        super().__init__(opToken, [left, right])
    
    def eval(self):
        return self.args[0].eval() ** self.args[1].eval()

class Parser:
    
    def __init__(self, input) -> None:
        self.tokens = self.parseToTokens(input)
        self.tokenIndex = 0
        
    def parseToTokens(self, text) -> List[Token]:
        tokens = []
        i = 0
        index = 0
        while match := tokenRe.search(text, index):
        
            index = match.end()
            tokens.append(Token(match.group(0), i))
            i += 1
        return tokens

    def parseEquation(self):
        exp = self.parseAddExp()
        
        if self.tokenIndex < len(self.tokens):
            raise Exception("error: not all tokens are consumed by parser")
        
        return exp
    
    def parseAddExp(self):
        
        left = self.parseMulExp()
        
        while token := self.NextTokenIs({"+", "-"}):
            right = self.parseMulExp()
            if token.text =="+":
                left = AddExp(token, left, right)
            else:
                left = SubExp(token, left, right)
        return left

    def parseMulExp(self):
        # mulexpr ::= powexpr { mulop powexpr }
        
        left = self.parsePowExp()
        
        while token := self.NextTokenIs(["*", "/"]):
            right = self.parsePowExp()
            
            if token.text == '*':
                left = MulExp(token, left, right)
            else:
                left = DivExp(token, left, right)
        return left # at this point no more tokens are found to the right, so return left.

    def parsePowExp(self):
        # powexpr ::= "-" powexpr | "+" powexpr | atom [ "^" powexpr ]
        while self.NextTokenIs({"+"}):
            pass
        
        if token := self.NextTokenIs({'-'}):
            arg = self.parsePowExp()
            return NegExp(token, arg)
        
        base = self.parseAtom() #parsing base of the exponent
        if token := self.NextTokenIs(["^"]):
            power = self.parsePowExp() #power could be another exponential, or a atom, in which case will be dealt by the line above.
            return PowExp(token, base, power)
        
        return base # there is no exponential here :x
    def parseAtom(self):
        # atom ::= ident [ "(" expr ")" ] | numeric | "(" expr ")"
        token = self.GetNextToken()
        if token.type == T.ident:
            if self.NextTokenIs({'('}):
                args = self.parseAddExp()
                self.ExpectToken(")")
                return FuncExp(token, [args])
            return IdentExp(token)
        
        if token.type == T.numeric:
            return NumExp(token)

        if token.text == '(':
            exp = self.parseAddExp()
            self.ExpectToken(')')
            return exp
        
        raise Exception(f"unexpected token: {token.text}")
    
    def peekNextToken(self):
        if self.tokenIndex < len(self.tokens):
            return self.tokens[self.tokenIndex]
        return None
    
    def GetNextToken(self):
        if out := self.peekNextToken():
            self.tokenIndex+=1
            return out
        raise Exception("unexpected end of expression")
    
    def NextTokenIs(self, validList: Set[Token]):
        try:
            if self.tokens[self.tokenIndex].text in validList:
                self.tokenIndex +=1
                return self.tokens[self.tokenIndex-1]
            
        except Exception as e:
            return None
        
    def ExpectToken(self, text):
        token = self.peekNextToken()
        
        if not token or token.text != text:
            raise Exception(f"expect {text}, got {token.text if token else 'None'}")
        
        self.tokenIndex +=1
        return self.tokens[self.tokenIndex -1]
    
if __name__ == "__main__":
    try:
        eq = Parser("-1").parseEquation()
        print(eq.eval())
    except Exception as e:
        print(e)
