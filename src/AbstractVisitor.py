from abc import abstractmethod
from abc import ABCMeta

class AbstractVisitor(metaclass = ABCMeta):
  
  @abstractmethod
  def visitMain_MainInner(self, main):
    pass
  
  @abstractmethod
  def visitMain_MainInner_Empty(self):
    pass
  
  @abstractmethod
  def visitMainInner_InnerStatement_MainInner(self):
    pass
  
  @abstractmethod
  def visitMainInner_InnerStatement(self, mainInner):
    pass
  
  @abstractmethod
  def visitInnerStatement_FuncDecStatement(self, innerStatement):
    pass
  
  @abstractmethod
  def visitInnerStatement_Statement(self, innerStatement):
    pass
  
  @abstractmethod
  def visitFuncDecStatement_Function(self, funcDecStatement):
    pass

  @abstractmethod
  def visitFds_id_withAmpersand(self, fds_id):
    pass
  
  @abstractmethod
  def visitFds_id_noAmpersand(self, fds_id):
    pass
  
  @abstractmethod
  def visitFds_parameter_withParameter(self, fds_parameter):
    pass
  
  @abstractmethod
  def visitFds_parameter_noParameter(self):
    pass
  
  @abstractmethod
  def visitParameterList_Parameter_Mul(self, parameterList):
    pass
  
  @abstractmethod
  def visitParameterList_Parameter_Single(self, parameterList):
    pass
  
  @abstractmethod
  def visitParameterListColonParameter_Mul(self, parameterListColonParameter):
    pass
  
  @abstractmethod
  def visitParameterListColonParameter_Single(self, parameterListColonParameter):
    pass
  
  @abstractmethod
  def visitFds_statements_withStatements(self, fds_statements):
    pass
  
  @abstractmethod
  def visitFds_statements_noStatements(self):
    pass
  
  @abstractmethod
  def visitParameter_Var(self, parameter):
    pass
  
  @abstractmethod
  def visitInnerStatementMul_Mul(self, innerStatementMul):
    pass
  
  @abstractmethod
  def visitInnerStatementMul_Single(self, innerStatementMul):
    pass
  
  @abstractmethod
  def visitStatement_Expr(self, statement):
    pass
  
  @abstractmethod
  def visitExpr_Expr1(self, expr):
    pass
  
  @abstractmethod
  def visitExpr_Expr3(self, expr):
    pass
  
  @abstractmethod
  def visitExpr_Expr1_Expr2(self, expr):
    pass
  
  @abstractmethod
  def visitExpr2_ArithmeticOp(self, expr2):
    pass

  @abstractmethod
  def visitExpr2_ComparissionOp(self, expr2):
    pass

  @abstractmethod
  def visitComparissionOperator_Token(self, comparissonOp):
    pass
  
  @abstractmethod
  def visitExpr1_Variable(self, expr1):
    pass
  
  @abstractmethod
  def visitExpr1_Variable_Increment(self, expr1):
    pass
  
  @abstractmethod
  def visitExpr1_Variable_Decrement(self, expr1):
    pass
  
  @abstractmethod
  def visitExpr1_Increment_Variable(self, expr1):
    pass
  
  @abstractmethod
  def visitExpr1_Decrement_Variable(self, expr1):
    pass
  
  @abstractmethod
  def visitExpr1_FunctionCall(self, expr1):
    pass
  
  @abstractmethod
  def visitExpr1_ArrayDeclaration(self, expr1):
    pass
  
  @abstractmethod
  def visitExpr1_True(self, expr1):
    pass
  
  @abstractmethod
  def visitExpr1_False(self, expr1):
    pass
  
  @abstractmethod
  def visitExpr1_Scalar(self, expr1):
    pass
  
  @abstractmethod
  def visitVariable_Reference_Variable(self, variable):
    pass
  
  @abstractmethod
  def visitReferenceVariable_Compound(self, referenceVariable):
    pass
  
  @abstractmethod
  def visitCompoundVariableSingle(self, singleVariable):
    pass
  
  @abstractmethod
  def visitFunctionCall_NoParameter(self, functionCall):
    pass
  
  @abstractmethod
  def visitFunctionCall_WithParameter(self, functionCall):
    pass
  
  @abstractmethod
  def visitFCParameterList_Single(self, fcParameterList):
    pass
  
  @abstractmethod
  def visitFCParameterList_Mul(self, fcParameterList):
    pass
  
  @abstractmethod
  def visitFCParameterListColonParameter_Single(self, fcParameterListColonParameter):
    pass
  
  @abstractmethod
  def visitFCParameterListColonParameter_Mul(self, fcParameterListColonParameter):
    pass
  
  @abstractmethod
  def visitFunctionCallParameter_Expr(self, functionCallParameter):
    pass
  
  @abstractmethod
  def visitFunctionCallParameter_AmpersandVariable(self, functionCallParameter):
    pass
  
  @abstractmethod
  def visitScalar_Token(self, scalar):
    pass
  
  @abstractmethod
  def visitAssignOperator_Token(self, assignOp):
    pass
  
  @abstractmethod
  def visitArrayDec_NoPairList(self, arrayDec):
    pass
  
  @abstractmethod
  def visitArrayDec_WithPairList(self, arrayDec):
    pass
  
  @abstractmethod
  def visitArrayPairList_ArrayPair_Single(self, arrayPairList):
    pass
  
  @abstractmethod
  def visitArrayPairList_ArrayPair_Mul(self, arrayPairList):
    pass
  
  @abstractmethod
  def visitArrayPair_Expr(self, arrayPair):
    pass
  
  @abstractmethod
  def visitArrayPairList_Mul(self, arrayPairList):
    pass
  
  @abstractmethod
  def visitArrayPairListArr_Single(self, arrayPairList):
    pass
  
  @abstractmethod
  def visitStatementBlockOpt_Statement(self, statementBlockOpt):
    pass

  @abstractmethod
  def visitStatementBlockOpt_StatementMul(self, statementBlockOpt):
    pass

  @abstractmethod
  def visitstatementMulSingle(self, statementMul):
    pass
  
  @abstractmethod
  def visitstatementMulMul(self, statementMul):
    pass

  @abstractmethod
  def visitExprParentheses_Expr(self, exprParentheses):
    pass

  @abstractmethod
  def visitStatement_While(self, statement):
    pass

  @abstractmethod
  def visitWhileStatementSingle(self, whileStatement):
    pass

  @abstractmethod
  def visitStatement_Do_While(self, whilestatement):
    pass

  @abstractmethod
  def visitDoWhileStatementSingle(self, whilestatement):
    pass

  @abstractmethod 
  def visitStatement_If(self, statementIf):
    pass
    
  @abstractmethod
  def visitIfStatement_statement_if(self, ifStatement):
    pass

  @abstractmethod
  def visitStatementElseIf_Mul(self, statementElseIfMul):
    pass

  @abstractmethod
  def visitStatementIf_Mul(self, statementIfMul):
    pass

  @abstractmethod
  def visitStatementIf_Single(self, ifSingle):
    pass
  
  @abstractmethod
  def visitIfStatement_Else(self, IfStatementElse):
    pass
  
  @abstractmethod
  def visitStatementElse_Single(self, statementElse):
    pass

  @abstractmethod
  def visitIfStatement_StatementIf_Elseif(self, statementIfElseif):
    pass

  @abstractmethod
  def visitStatementElseIf_Single(self, StatementElseIf):
    pass
  
  @abstractmethod
  def visitIfStatement_Stm_If_Elseif_Else(self, ifConditional):
    pass

  @abstractmethod
  def visitStatement_For(self, statement):
    pass
  
  @abstractmethod
  def visitForStatement_For(self, forStatement):
    pass
  
  @abstractmethod
  def visitForParameters_Empty(self):
    pass
  @abstractmethod
  def visitForParameters_Left(self, forParameters):
    pass
  
  @abstractmethod
  def visitForParameters_Left_Mid(self, forParameters):
    pass

  @abstractmethod 
  def visitForParameters_Left_Right(self, forParameters):
    pass
  
  @abstractmethod
  def visitForParameters_Mid(self, forParameters):
    pass

  @abstractmethod 
  def visitForParameters_Mid_Right(self, forParameters):
    pass
    
  @abstractmethod
  def visitForParameters_Right(self, forParameters):
    pass

  @abstractmethod 
  def visitForParameters_Full(self, forParameters):
    pass

  @abstractmethod 
  def visitForExprOpt_Mul(self, forExprOpt):
    pass

  @abstractmethod 
  def visitForExprOpt_Single(self, forExprOpt):
    pass

  @abstractmethod 
  def visitForExprColonExpr_Single(self, forExprColonExpr):
    pass

  @abstractmethod 
  def visitForExprColonExpr_Mul(self, forExprColonExpr):
    pass

  @abstractmethod
  def visitStatement_Exit(self, statement):
    pass

  @abstractmethod
  def visitExit_ExitExpr(self, _exit):
    pass

  @abstractmethod
  def visitExit_Empty(self):
    pass
  
  @abstractmethod
  def visitExitExpr_Expr(self, exitExpr):
    pass

  @abstractmethod
  def visitExitExpr_Empty(self):
    pass

  @abstractmethod
  def visitStatement_Break(self, statement):
    pass

  @abstractmethod
  def visitBreak_Expr(self, _break):
    pass
  
  @abstractmethod
  def visitBreak_Empty(self):
    pass

  '''  
  @abstractmethod
  def visitStatementBlockOpt_ParenEmpty():
    pass
  
  @abstractmethod
  def visitParameter_Prefix_Var():
    pass
  
  @abstractmethod
  def visitParameter_Var_Sufix():
    pass
  
  @abstractmethod
  def visitParameter_Full():
    pass
  
  @abstractmethod
  def visitParameterPrefix_PType_Amp():
    pass
  
  @abstractmethod
  def visitParameterPrefix_Ampersand():
    pass
  
  @abstractmethod
  def visitParameterPrefix_PType():
    pass
  
  @abstractmethod
  def visitParameterType_Type():
    pass
  
  @abstractmethod
  def visitStaticScalar_CommonScalar():
    pass
  
  @abstractmethod
  def visitStaticScalar_Plus_Static():
    pass
  
  @abstractmethod
  def visitStaticScalar_Minus_Static():
    pass
  
  @abstractmethod
  def visitCommonScalar_Token():
    pass
  
  @abstractmethod
  def visitStatement_Continue():
    pass
  
  @abstractmethod
  def visitStatement_Return():
    pass
  
  @abstractmethod
  def visitStatementElse_Else():
    pass
  
  @abstractmethod
  def visitStatement_Foreach():
    pass
  
  @abstractmethod
  def visitStatement_Die():
    pass
  
  @abstractmethod
  def visitStatement_Global():
    pass
  
  @abstractmethod
  def visitIfStatement_Single():
    pass
  
  @abstractmethod
  def visitIfStatement_Complement():
    pass
  
  @abstractmethod
  def visitStatementIf_ExprParen():
    pass
  
  @abstractmethod
  def visitExprParentheses_Expr():
    pass
  
  @abstractmethod
  def visitIfStatemnet_Else():
    pass
  
  @abstractmethod
  def visitExpr_Minus_Expr1():
    pass
  
  @abstractmethod
  def visitExpr_Minus_Expr1_Expr2():
    pass
  
  @abstractmethod
  def visitExpr2_TernaryExpr():
    pass
  
  
  @abstractmethod
  def visitArithmeticOperator_Token():
    pass
  
  
  @abstractmethod
  def visitExpr3_TypeCast():
    pass
  
  @abstractmethod
  def visitExpr3_Var_Assign_Expr():
    pass
  
  @abstractmethod
  def visitExpr3_Var_Assign_Amp_Expr():
    pass
  
  @abstractmethod
  def visitTypeCastOp_Token():
    pass
  
  @abstractmethod
  def visitExpr1_ExprPar():
    pass
  
  @abstractmethod
  def visitArrayPair_Variable():
    pass
  
  @abstractmethod
  def visitArrayPair_Attr_AmpersandVariable():
    pass
  
  @abstractmethod
  def visitArrayPair_Attr_Expr():
    pass
  
  @abstractmethod
  def visitVariable_Simple_Indirect():
    pass
  
  @abstractmethod
  def visitReferenceVariable_Compound_Reference():
    pass
  
  @abstractmethod
  def visitSimpleIndirectReference_Mul():
    pass
  
  @abstractmethod
  def visitSimpleIndirectReference_Single():
    pass
  
  @abstractmethod
  def visitAmpersandVariable_WithAmp():
    pass
  
  @abstractmethod
  def visitAmpersandVariable_NoAmp():
    pass
  
  @abstractmethod
  def visitGlobalStatement_Mul():
    pass
  
  @abstractmethod
  def visitGlobalVar_Var():
    pass
  
  @abstractmethod
  def visitGlobalVar_DolarVar():
    pass
  
  @abstractmethod
  def visitGlobalVar_DolarExpr():
    pass
  
  @abstractmethod
  def visitGlobalVarMul_Single():
    pass
  
  @abstractmethod
  def visitGlobalVarMul_Mul():
    pass
   
  @abstractmethod
  def visitDie_Empty():
    pass
  
  @abstractmethod
  def visitContinue_Expr():
    pass
  
  @abstractmethod
  def visitContinue_Empty():
    pass
  
  @abstractmethod
  def visitReturn_Expr():
    pass
  
  @abstractmethod
  def visitReturn_Empty():
    pass
  
  @abstractmethod
  def visitCompoundVariableMul():
    pass
  
  @abstractmethod
  def visitReferenceVariableSelectorSingle():
    pass
  
  @abstractmethod
  def visitReferenceVariableSelectorMul():
    pass
  
  @abstractmethod
  def visitSelectorWithExpr():
    pass
  
  @abstractmethod
  def visitForeachStatement_NoAssoc():
    pass
  
  @abstractmethod
  def visitForeachStatement_WithAssoc():
    pass
  
  @abstractmethod
  def visitWhileStatementSingle():
    pass
  
  @abstractmethod
  def visitStatementBlockOpt_Statement():
    pass
  
  @abstractmethod
  def visitStatementBlockOpt_Empty():
    pass
   
'''