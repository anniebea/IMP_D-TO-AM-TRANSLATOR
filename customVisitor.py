import IMP_py.IMP_DVisitor
from IMP_py.IMP_DParser import IMP_DParser


class CustomVisitor(IMP_py.IMP_DVisitor.IMP_DVisitor):
    def visitProgr(self, ctx: IMP_DParser.ProgrContext):
        return str(self.visitChildren(ctx))

    def visitSeries(self, ctx: IMP_DParser.SeriesContext):
        result = str(self.visitStmt(ctx.getChild(0)))
        for i in range(2, ctx.getChildCount(), 2):
            result = result + ";" + str(self.visitStmt(ctx.getChild(i)))
        return result

    def visitStmt(self, ctx: IMP_DParser.StmtContext):
        if ctx.cond_stmt() is not None:
            return self.visitCond_stmt(ctx.getChild(0))
        elif ctx.loop() is not None:
            return self.visitLoop(ctx.getChild(0))
        elif ctx.input_stmt() is not None:
            return self.visitInput_stmt(ctx.getChild(0))
        elif ctx.output_stmt() is not None:
            return self.visitOutput_stmt(ctx.getChild(0))
        elif ctx.assign_stmt() is not None:
            return self.visitAssign_stmt(ctx.getChild(0))

        return self.visitChildren(ctx)

    def visitAssign_stmt(self, ctx: IMP_DParser.Assign_stmtContext):
        result = str(self.visitExpr(ctx.getChild(2))) + ":STORE(" + str(ctx.getChild(0)) + ")"
        return result

    def visitCond_stmt(self, ctx: IMP_DParser.Cond_stmtContext):  # IF STATEMENT
        ifCond = str(self.visitLog_expr(ctx.getChild(1)))
        result = ifCond + ":BRANCH(" + \
                 str(self.visitSeries(ctx.getChild(3))) + "," + str(self.visitSeries(ctx.getChild(5))) + ")"
        return result

    def visitLoop(self, ctx: IMP_DParser.LoopContext):
        result = "LOOP(" + str(self.visitLog_expr(ctx.getChild(1))) + "," \
                 "" + str(self.visitSeries(ctx.getChild(3))) + ")"
        return result

    def visitExpr(self, ctx: IMP_DParser.ExprContext):
        result = str(self.visitTerm(ctx.getChild(0)))
        for i in range(2, ctx.getChildCount(), 2):
            if str(ctx.getChild(i-1)) == "+":
                result = str(self.visitTerm(ctx.getChild(i))) + ":" + result + ":ADD"
            else:
                result = str(self.visitTerm(ctx.getChild(i))) + ":" + result + ":SUB"
        return result

    def visitTerm(self, ctx: IMP_DParser.TermContext):
        result = str(self.visitElem(ctx.getChild(0)))
        for i in range(2, ctx.getChildCount(), 2):
            if str(ctx.getChild(i-1)) == "*":
                result = str(self.visitElem(ctx.getChild(i))) + ":" + result + ":MULT"
            else:
                result = str(self.visitElem(ctx.getChild(i))) + ":" + result + ":DIV"
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
        result = str(self.visitLog_term(ctx.getChild(0)))
        for i in range(2, ctx.getChildCount(), 2):
            result = str(self.visitLog_term(ctx.getChild(i))) + ":" + result + ":OR"
        return result

    def visitLog_term(self, ctx: IMP_DParser.Log_exprContext):
        result = str(self.visitLog_elem(ctx.getChild(0)))
        for i in range(2, ctx.getChildCount(), 2):
            result = str(self.visitLog_elem(ctx.getChild(i))) + ":" + result + ":AND"
        return result

    def visitLog_elem(self, ctx: IMP_DParser.Log_elemContext):
        result = None
        if str(ctx.getChildCount()) == "1":  # BOOL | condition | VARNAME
            if ctx.condition() is not None:
                result = "" + str(self.visitCondition(ctx.getChild(0)))
            else:
                result = "" + str(ctx.getChild(0))
        elif str(ctx.getChildCount()) == "2":  # NOT ( BOOL | condition | VARNAME )
            if ctx.condition() is not None:
                result = str(self.visitCondition(ctx.getChild(1))) + ":NEG"
            else:
                result = str(ctx.getChild(1)) + ":NEG"
        elif str(ctx.getChildCount()) == "3":  # LPARENTHESIS log_expr RPARENTHESIS
            result = self.visitLog_expr(ctx.getChild(1))
        elif str(ctx.getChildCount()) == "4":  # NOT LPARENTHESIS log_expr RPARENTHESIS
            result = str(self.visitLog_expr(ctx.getChild(2))) + ":NEG"
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
            return childVal2 + ":" + childVal0 + ":EQ:NEG"
        elif childVal1 == '=<':
            return childVal2 + ":" + childVal0 + ":LE"
        elif childVal1 == '>=':
            return childVal2 + ":" + childVal0 + ":LE:NEG" \
                  ":" + childVal2 + ":" + childVal0 + ":EQ:OR"
        elif childVal1 == '=':
            return "" + childVal2 + ":" + childVal0 + ":EQ"
        elif childVal1 == '<':
            return "" + childVal2 + ":" + childVal0 + ":EQ:NEG" \
                  ":" + childVal2 + ":" + childVal0 + ":LE:AND"
        elif childVal1 == '>':
            return "" + childVal2 + ":" + childVal0 + ":LE:NEG"
        else:
            return None

    def visitInput_stmt(self, ctx: IMP_DParser.Input_stmtContext):
        varlist = self.visitVarlist(ctx.getChild(1))
        result = ""
        for i in varlist:
            result = result + ":READ(" + i + ")"
        result = result[1:]
        return result

    def visitOutput_stmt(self, ctx: IMP_DParser.Output_stmtContext):
        varlist = self.visitVarlist(ctx.getChild(1))
        result = ""
        for i in varlist:
            result = result + ":WRITE(" + i + ")"
        result = result[1:]
        return result

    def visitVarlist(self, ctx: IMP_DParser.VarlistContext):
        result = [str(ctx.getChild(0))]
        for i in range(2, ctx.getChildCount(), 2):
            result.append(str(ctx.getChild(i)))
        return result
