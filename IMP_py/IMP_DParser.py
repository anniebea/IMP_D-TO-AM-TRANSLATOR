# Generated from C:/Users/anitr/OneDrive/Documents/__University/6sem/PVSUS/MD3/IMP_D-TO-AM-TRANSLATOR\IMP_D.g4 by ANTLR 4.10.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,21,116,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,1,0,
        1,1,1,1,1,1,5,1,32,8,1,10,1,12,1,35,9,1,1,2,1,2,1,2,3,2,40,8,2,1,
        3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,
        5,1,5,1,6,1,6,1,6,5,6,63,8,6,10,6,12,6,66,9,6,1,7,1,7,1,7,5,7,71,
        8,7,10,7,12,7,74,9,7,1,8,3,8,77,8,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        3,8,86,8,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,5,10,95,8,10,10,10,12,
        10,98,9,10,1,11,1,11,1,11,5,11,103,8,11,10,11,12,11,106,9,11,1,12,
        1,12,1,12,1,12,1,12,1,12,3,12,114,8,12,1,12,0,0,13,0,2,4,6,8,10,
        12,14,16,18,20,22,24,0,0,115,0,26,1,0,0,0,2,28,1,0,0,0,4,39,1,0,
        0,0,6,41,1,0,0,0,8,45,1,0,0,0,10,53,1,0,0,0,12,59,1,0,0,0,14,67,
        1,0,0,0,16,76,1,0,0,0,18,87,1,0,0,0,20,91,1,0,0,0,22,99,1,0,0,0,
        24,113,1,0,0,0,26,27,3,2,1,0,27,1,1,0,0,0,28,33,3,4,2,0,29,30,5,
        16,0,0,30,32,3,4,2,0,31,29,1,0,0,0,32,35,1,0,0,0,33,31,1,0,0,0,33,
        34,1,0,0,0,34,3,1,0,0,0,35,33,1,0,0,0,36,40,3,6,3,0,37,40,3,8,4,
        0,38,40,3,10,5,0,39,36,1,0,0,0,39,37,1,0,0,0,39,38,1,0,0,0,40,5,
        1,0,0,0,41,42,5,20,0,0,42,43,5,1,0,0,43,44,3,20,10,0,44,7,1,0,0,
        0,45,46,5,2,0,0,46,47,3,12,6,0,47,48,5,3,0,0,48,49,3,2,1,0,49,50,
        5,4,0,0,50,51,3,2,1,0,51,52,5,5,0,0,52,9,1,0,0,0,53,54,5,6,0,0,54,
        55,3,12,6,0,55,56,5,7,0,0,56,57,3,2,1,0,57,58,5,8,0,0,58,11,1,0,
        0,0,59,64,3,14,7,0,60,61,5,14,0,0,61,63,3,14,7,0,62,60,1,0,0,0,63,
        66,1,0,0,0,64,62,1,0,0,0,64,65,1,0,0,0,65,13,1,0,0,0,66,64,1,0,0,
        0,67,72,3,16,8,0,68,69,5,13,0,0,69,71,3,16,8,0,70,68,1,0,0,0,71,
        74,1,0,0,0,72,70,1,0,0,0,72,73,1,0,0,0,73,15,1,0,0,0,74,72,1,0,0,
        0,75,77,5,15,0,0,76,75,1,0,0,0,76,77,1,0,0,0,77,85,1,0,0,0,78,86,
        3,18,9,0,79,86,5,12,0,0,80,81,5,17,0,0,81,82,3,12,6,0,82,83,5,18,
        0,0,83,86,1,0,0,0,84,86,5,20,0,0,85,78,1,0,0,0,85,79,1,0,0,0,85,
        80,1,0,0,0,85,84,1,0,0,0,86,17,1,0,0,0,87,88,3,20,10,0,88,89,5,11,
        0,0,89,90,3,20,10,0,90,19,1,0,0,0,91,96,3,22,11,0,92,93,5,9,0,0,
        93,95,3,22,11,0,94,92,1,0,0,0,95,98,1,0,0,0,96,94,1,0,0,0,96,97,
        1,0,0,0,97,21,1,0,0,0,98,96,1,0,0,0,99,104,3,24,12,0,100,101,5,10,
        0,0,101,103,3,24,12,0,102,100,1,0,0,0,103,106,1,0,0,0,104,102,1,
        0,0,0,104,105,1,0,0,0,105,23,1,0,0,0,106,104,1,0,0,0,107,114,5,19,
        0,0,108,114,5,20,0,0,109,110,5,17,0,0,110,111,3,20,10,0,111,112,
        5,18,0,0,112,114,1,0,0,0,113,107,1,0,0,0,113,108,1,0,0,0,113,109,
        1,0,0,0,114,25,1,0,0,0,9,33,39,64,72,76,85,96,104,113
    ]

class IMP_DParser ( Parser ):

    grammarFileName = "IMP_D.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':='", "'if'", "'then'", "'else'", "'fi'", 
                     "'while'", "'do'", "'od'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'and'", "'or'", "'not'", 
                     "';'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "WEAKOP", "STRONGOP", "RELATION", "BOOL", 
                      "CONJUNCTION", "DISCJUNCTION", "NOT", "SEMICOLON", 
                      "LPARENTHESIS", "RPARENTHESIS", "NUMBER", "VARNAME", 
                      "WS" ]

    RULE_progr = 0
    RULE_series = 1
    RULE_stmt = 2
    RULE_assign_stmt = 3
    RULE_cond_stmt = 4
    RULE_loop = 5
    RULE_log_expr = 6
    RULE_log_term = 7
    RULE_log_elem = 8
    RULE_condition = 9
    RULE_expr = 10
    RULE_term = 11
    RULE_elem = 12

    ruleNames =  [ "progr", "series", "stmt", "assign_stmt", "cond_stmt", 
                   "loop", "log_expr", "log_term", "log_elem", "condition", 
                   "expr", "term", "elem" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    WEAKOP=9
    STRONGOP=10
    RELATION=11
    BOOL=12
    CONJUNCTION=13
    DISCJUNCTION=14
    NOT=15
    SEMICOLON=16
    LPARENTHESIS=17
    RPARENTHESIS=18
    NUMBER=19
    VARNAME=20
    WS=21

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def series(self):
            return self.getTypedRuleContext(IMP_DParser.SeriesContext,0)


        def getRuleIndex(self):
            return IMP_DParser.RULE_progr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgr" ):
                listener.enterProgr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgr" ):
                listener.exitProgr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgr" ):
                return visitor.visitProgr(self)
            else:
                return visitor.visitChildren(self)




    def progr(self):

        localctx = IMP_DParser.ProgrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_progr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.series()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SeriesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IMP_DParser.StmtContext)
            else:
                return self.getTypedRuleContext(IMP_DParser.StmtContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(IMP_DParser.SEMICOLON)
            else:
                return self.getToken(IMP_DParser.SEMICOLON, i)

        def getRuleIndex(self):
            return IMP_DParser.RULE_series

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSeries" ):
                listener.enterSeries(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSeries" ):
                listener.exitSeries(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSeries" ):
                return visitor.visitSeries(self)
            else:
                return visitor.visitChildren(self)




    def series(self):

        localctx = IMP_DParser.SeriesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_series)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.stmt()
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IMP_DParser.SEMICOLON:
                self.state = 29
                self.match(IMP_DParser.SEMICOLON)
                self.state = 30
                self.stmt()
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_stmt(self):
            return self.getTypedRuleContext(IMP_DParser.Assign_stmtContext,0)


        def cond_stmt(self):
            return self.getTypedRuleContext(IMP_DParser.Cond_stmtContext,0)


        def loop(self):
            return self.getTypedRuleContext(IMP_DParser.LoopContext,0)


        def getRuleIndex(self):
            return IMP_DParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = IMP_DParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stmt)
        try:
            self.state = 39
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [IMP_DParser.VARNAME]:
                self.enterOuterAlt(localctx, 1)
                self.state = 36
                self.assign_stmt()
                pass
            elif token in [IMP_DParser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 37
                self.cond_stmt()
                pass
            elif token in [IMP_DParser.T__5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 38
                self.loop()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARNAME(self):
            return self.getToken(IMP_DParser.VARNAME, 0)

        def expr(self):
            return self.getTypedRuleContext(IMP_DParser.ExprContext,0)


        def getRuleIndex(self):
            return IMP_DParser.RULE_assign_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign_stmt" ):
                listener.enterAssign_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign_stmt" ):
                listener.exitAssign_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = IMP_DParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(IMP_DParser.VARNAME)
            self.state = 42
            self.match(IMP_DParser.T__0)
            self.state = 43
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cond_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def log_expr(self):
            return self.getTypedRuleContext(IMP_DParser.Log_exprContext,0)


        def series(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IMP_DParser.SeriesContext)
            else:
                return self.getTypedRuleContext(IMP_DParser.SeriesContext,i)


        def getRuleIndex(self):
            return IMP_DParser.RULE_cond_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCond_stmt" ):
                listener.enterCond_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCond_stmt" ):
                listener.exitCond_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCond_stmt" ):
                return visitor.visitCond_stmt(self)
            else:
                return visitor.visitChildren(self)




    def cond_stmt(self):

        localctx = IMP_DParser.Cond_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_cond_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(IMP_DParser.T__1)
            self.state = 46
            self.log_expr()
            self.state = 47
            self.match(IMP_DParser.T__2)
            self.state = 48
            self.series()
            self.state = 49
            self.match(IMP_DParser.T__3)
            self.state = 50
            self.series()
            self.state = 51
            self.match(IMP_DParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def log_expr(self):
            return self.getTypedRuleContext(IMP_DParser.Log_exprContext,0)


        def series(self):
            return self.getTypedRuleContext(IMP_DParser.SeriesContext,0)


        def getRuleIndex(self):
            return IMP_DParser.RULE_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoop" ):
                listener.enterLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoop" ):
                listener.exitLoop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop" ):
                return visitor.visitLoop(self)
            else:
                return visitor.visitChildren(self)




    def loop(self):

        localctx = IMP_DParser.LoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(IMP_DParser.T__5)
            self.state = 54
            self.log_expr()
            self.state = 55
            self.match(IMP_DParser.T__6)
            self.state = 56
            self.series()
            self.state = 57
            self.match(IMP_DParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Log_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def log_term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IMP_DParser.Log_termContext)
            else:
                return self.getTypedRuleContext(IMP_DParser.Log_termContext,i)


        def DISCJUNCTION(self, i:int=None):
            if i is None:
                return self.getTokens(IMP_DParser.DISCJUNCTION)
            else:
                return self.getToken(IMP_DParser.DISCJUNCTION, i)

        def getRuleIndex(self):
            return IMP_DParser.RULE_log_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLog_expr" ):
                listener.enterLog_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLog_expr" ):
                listener.exitLog_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLog_expr" ):
                return visitor.visitLog_expr(self)
            else:
                return visitor.visitChildren(self)




    def log_expr(self):

        localctx = IMP_DParser.Log_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_log_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.log_term()
            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IMP_DParser.DISCJUNCTION:
                self.state = 60
                self.match(IMP_DParser.DISCJUNCTION)
                self.state = 61
                self.log_term()
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Log_termContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def log_elem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IMP_DParser.Log_elemContext)
            else:
                return self.getTypedRuleContext(IMP_DParser.Log_elemContext,i)


        def CONJUNCTION(self, i:int=None):
            if i is None:
                return self.getTokens(IMP_DParser.CONJUNCTION)
            else:
                return self.getToken(IMP_DParser.CONJUNCTION, i)

        def getRuleIndex(self):
            return IMP_DParser.RULE_log_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLog_term" ):
                listener.enterLog_term(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLog_term" ):
                listener.exitLog_term(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLog_term" ):
                return visitor.visitLog_term(self)
            else:
                return visitor.visitChildren(self)




    def log_term(self):

        localctx = IMP_DParser.Log_termContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_log_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.log_elem()
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IMP_DParser.CONJUNCTION:
                self.state = 68
                self.match(IMP_DParser.CONJUNCTION)
                self.state = 69
                self.log_elem()
                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Log_elemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(IMP_DParser.ConditionContext,0)


        def BOOL(self):
            return self.getToken(IMP_DParser.BOOL, 0)

        def LPARENTHESIS(self):
            return self.getToken(IMP_DParser.LPARENTHESIS, 0)

        def log_expr(self):
            return self.getTypedRuleContext(IMP_DParser.Log_exprContext,0)


        def RPARENTHESIS(self):
            return self.getToken(IMP_DParser.RPARENTHESIS, 0)

        def VARNAME(self):
            return self.getToken(IMP_DParser.VARNAME, 0)

        def NOT(self):
            return self.getToken(IMP_DParser.NOT, 0)

        def getRuleIndex(self):
            return IMP_DParser.RULE_log_elem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLog_elem" ):
                listener.enterLog_elem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLog_elem" ):
                listener.exitLog_elem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLog_elem" ):
                return visitor.visitLog_elem(self)
            else:
                return visitor.visitChildren(self)




    def log_elem(self):

        localctx = IMP_DParser.Log_elemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_log_elem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==IMP_DParser.NOT:
                self.state = 75
                self.match(IMP_DParser.NOT)


            self.state = 85
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 78
                self.condition()
                pass

            elif la_ == 2:
                self.state = 79
                self.match(IMP_DParser.BOOL)
                pass

            elif la_ == 3:
                self.state = 80
                self.match(IMP_DParser.LPARENTHESIS)
                self.state = 81
                self.log_expr()
                self.state = 82
                self.match(IMP_DParser.RPARENTHESIS)
                pass

            elif la_ == 4:
                self.state = 84
                self.match(IMP_DParser.VARNAME)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IMP_DParser.ExprContext)
            else:
                return self.getTypedRuleContext(IMP_DParser.ExprContext,i)


        def RELATION(self):
            return self.getToken(IMP_DParser.RELATION, 0)

        def getRuleIndex(self):
            return IMP_DParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = IMP_DParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.expr()
            self.state = 88
            self.match(IMP_DParser.RELATION)
            self.state = 89
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IMP_DParser.TermContext)
            else:
                return self.getTypedRuleContext(IMP_DParser.TermContext,i)


        def WEAKOP(self, i:int=None):
            if i is None:
                return self.getTokens(IMP_DParser.WEAKOP)
            else:
                return self.getToken(IMP_DParser.WEAKOP, i)

        def getRuleIndex(self):
            return IMP_DParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = IMP_DParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.term()
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IMP_DParser.WEAKOP:
                self.state = 92
                self.match(IMP_DParser.WEAKOP)
                self.state = 93
                self.term()
                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IMP_DParser.ElemContext)
            else:
                return self.getTypedRuleContext(IMP_DParser.ElemContext,i)


        def STRONGOP(self, i:int=None):
            if i is None:
                return self.getTokens(IMP_DParser.STRONGOP)
            else:
                return self.getToken(IMP_DParser.STRONGOP, i)

        def getRuleIndex(self):
            return IMP_DParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = IMP_DParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.elem()
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IMP_DParser.STRONGOP:
                self.state = 100
                self.match(IMP_DParser.STRONGOP)
                self.state = 101
                self.elem()
                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(IMP_DParser.NUMBER, 0)

        def VARNAME(self):
            return self.getToken(IMP_DParser.VARNAME, 0)

        def LPARENTHESIS(self):
            return self.getToken(IMP_DParser.LPARENTHESIS, 0)

        def expr(self):
            return self.getTypedRuleContext(IMP_DParser.ExprContext,0)


        def RPARENTHESIS(self):
            return self.getToken(IMP_DParser.RPARENTHESIS, 0)

        def getRuleIndex(self):
            return IMP_DParser.RULE_elem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElem" ):
                listener.enterElem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElem" ):
                listener.exitElem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElem" ):
                return visitor.visitElem(self)
            else:
                return visitor.visitChildren(self)




    def elem(self):

        localctx = IMP_DParser.ElemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_elem)
        try:
            self.state = 113
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [IMP_DParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self.match(IMP_DParser.NUMBER)
                pass
            elif token in [IMP_DParser.VARNAME]:
                self.enterOuterAlt(localctx, 2)
                self.state = 108
                self.match(IMP_DParser.VARNAME)
                pass
            elif token in [IMP_DParser.LPARENTHESIS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 109
                self.match(IMP_DParser.LPARENTHESIS)
                self.state = 110
                self.expr()
                self.state = 111
                self.match(IMP_DParser.RPARENTHESIS)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





