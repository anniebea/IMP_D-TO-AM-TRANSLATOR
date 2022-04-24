import IMP_py.IMP_DVisitor
from IMP_py.IMP_DParser import IMP_DParser


class CustomVisitor(IMP_py.IMP_DVisitor.IMP_DVisitor):
    def visitProgr(self, ctx: IMP_DParser.ProgrContext):
        return str(self.visitChildren(ctx))

    def visitAssign_stmt(self, ctx: IMP_DParser.Assign_stmtContext):
        result = "acode(" + str(ctx.getChild(0)) + "):STORE(" + str(self.visitExpr(ctx.getChild(2))) + ")"
        return result

    def visitCond_stmt(self, ctx: IMP_DParser.Cond_stmtContext):  # IF STATEMENT
        ifCond = str(self.visitLog_expr(ctx.getChild(1)))
        result = "bcode(" + ifCond + "):BRANCH(code(" + \
                 str(self.visitSeries(ctx.getChild(3))) + "),code(" + str(self.visitSeries(ctx.getChild(5))) + "))"
        return result

    def visitLoop(self, ctx: IMP_DParser.LoopContext):
        result = "LOOP(bcode(" + str(self.visitLog_expr(ctx.getChild(1))) + ")," \
                 "code(" + str(self.visitSeries(ctx.getChild(3))) + "))"
        return result

    def visitExpr(self, ctx: IMP_DParser.ExprContext):
        if str(ctx.getChildCount()) == "1":
            return str(self.visitTerm(ctx.getChild(0)))
        else:
            childVal0 = str(self.visitTerm(ctx.getChild(0)))
            childVal2 = str(self.visitTerm(ctx.getChild(2)))

            if str(ctx.getChild(1)) == "+":
                result = "acode(" + childVal2 + "):acode(" + childVal0 + "):ADD"
                return result
            else:
                result = "acode(" + childVal2 + "):acode(" + childVal0 + "):SUB"
                return result

    def visitTerm(self, ctx: IMP_DParser.TermContext):
        if str(ctx.getChildCount()) == "1":
            return str(self.visitElem(ctx.getChild(0)))
        else:
            if str(ctx.getChild(1)) == "*":
                childVal0 = str(self.visitElem(ctx.getChild(0)))
                childVal2 = str(self.visitElem(ctx.getChild(2)))
                result = "acode(" + childVal2 + "):acode(" + childVal0 + "):MULT"
                return result
            else:
                childVal0 = str(self.visitElem(ctx.getChild(0)))
                childVal2 = str(self.visitElem(ctx.getChild(2)))
                result = "acode(" + childVal2 + "):acode(" + childVal0 + "):DIV"
                return result

    def visitElem(self, ctx: IMP_DParser.ElemContext):
        if str(ctx.getChildCount()) == "1":  # NUMBER | VARNAME
            if ctx.VARNAME() is not None:
                return "FETCH(" + str(ctx.getChild(0)) + ")"
            elif ctx.NUMBER() is not None:
                return "PUSH(" + str(ctx.getChild(0)) + ")"
            else:
                return str(ctx.getChild(0))
        else:  # LPARENTHESIS expr RPARENTHESIS
            return self.visitExpr(ctx.getChild(1))

    def visitLog_expr(self, ctx: IMP_DParser.Log_exprContext):
        if str(ctx.getChildCount()) == "1":
            return str(self.visitLog_term(ctx.getChild(0)))
        else:
            result = "bcode(" + str(self.visitLog_term(ctx.getChild(2))) + ")" \
                    ":bcode(" + str(self.visitLog_term(ctx.getChild(0))) + "):OR"
            return result

    def visitLog_term(self, ctx: IMP_DParser.Log_exprContext):
        if str(ctx.getChildCount()) == "1":
            return str(self.visitLog_elem(ctx.getChild(0)))
        else:
            result = "bcode(" + str(self.visitLog_elem(ctx.getChild(2))) + ")" \
                    ":bcode(" + str(self.visitLog_elem(ctx.getChild(0))) + "):AND"
            return result

    def visitLog_elem(self, ctx: IMP_DParser.Log_elemContext):
        result = None
        if str(ctx.getChildCount()) == "1":  # BOOL | condition | VARNAME
            if ctx.condition() is not None:
                result = "bcode(" + str(self.visitCondition(ctx.getChild(0))) + ")"
            else:
                result = "bcode(" + str(ctx.getChild(0)) + ")"
        elif str(ctx.getChildCount()) == "2":  # NOT ( BOOL | condition | VARNAME )
            if ctx.condition() is not None:
                result = "bcode(" + str(self.visitCondition(ctx.getChild(1))) + "):NEG"
            else:
                result = "bcode(" + str(ctx.getChild(1)) + "):NEG"
        elif str(ctx.getChildCount()) == "3":  # LPARENTHESIS log_expr RPARENTHESIS
            result = self.visitLog_expr(ctx.getChild(1))
        elif str(ctx.getChildCount()) == "4":  # NOT LPARENTHESIS log_expr RPARENTHESIS
            result = "bcode(" + str(self.visitLog_expr(ctx.getChild(2))) + "):NEG"
        return result

    def visitCondition(self, ctx: IMP_DParser.ConditionContext):  # expr RELATION expr
        if str(ctx.getChildCount()) == "0":
            print("ERROR?????????????????")
            print("RELATION: " + str(ctx.getChild(0)) + str(ctx.getChild(1)) + str(ctx.getChild(2)))
            return None
        childVal1 = str(ctx.getChild(1))
        childVal0 = str(self.visitExpr(ctx.getChild(0)))
        childVal2 = str(self.visitExpr(ctx.getChild(2)))

        if childVal1 == "<>":
            return "acode(" + childVal2 + "):acode(" + childVal0 + "):EQ:NEG"
        elif childVal1 == '=<':
            return "acode(" + childVal2 + "):acode(" + childVal0 + "):LE"
        elif childVal1 == '>=':
            return "acode(" + childVal2 + "):acode(" + childVal0 + "):LE:NEG" \
                  ":acode(" + childVal2 + "):acode(" + childVal0 + "):EQ:OR"
        elif childVal1 == '=':
            return "acode(" + childVal2 + "):acode(" + childVal0 + "):EQ"
        elif childVal1 == '<':
            return "acode(" + childVal2 + "):acode(" + childVal0 + "):EQ:NEG" \
                  ":acode(" + childVal2 + "):acode(" + childVal0 + "):LE:AND"
        elif childVal1 == '>':
            return "acode(" + childVal2 + "):acode(" + childVal0 + "):LE:NEG"
        else:
            return None
