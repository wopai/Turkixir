
import sys


sys.path.append('C:\\Users\\Kerem Akman\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python39\\site-packages')


import langkit.gdb



langkit.gdb.setup(
    lib_name='libturkixirlang',
    astnode_names=['Turkixir_Node', 'Arg', 'Arg_Assoc', 'Arg_Gen', 'Kw_Args', 'Var_Args', 'As_Name_Node', 'Comp_If', 'Comp_Op_Kind', 'Comp_Op_Kind_Diamond', 'Comp_Op_Kind_Eq', 'Comp_Op_Kind_Gt', 'Comp_Op_Kind_Gte', 'Comp_Op_Kind_In', 'Comp_Op_Kind_Is', 'Comp_Op_Kind_Isnot', 'Comp_Op_Kind_Lt', 'Comp_Op_Kind_Lte', 'Comp_Op_Kind_Noteq', 'Comp_Op_Kind_Notin', 'Comprehension', 'Comp_For', 'Comp_ForL', 'Decorator', 'Dict_Assoc', 'Else_Part', 'Except_Part', 'Expr', 'And_Expr', 'And_Op', 'Bin_Op', 'Arith_Expr', 'Shift_Expr', 'Term', 'Call_Expr', 'Comp_Op', 'Concat_String_Lit', 'Dict_Comp', 'Dict_Lit', 'Dot', 'Ellipsis_Expr', 'Factor', 'If_Expr', 'Inline_Eval', 'Lambda_Def', 'List_Comp', 'List_Gen', 'List_Lit', 'Name', 'Dotted_Name', 'Id', 'Not_Op', 'Number_Lit', 'Or_Expr', 'Or_Op', 'Power', 'Set_Comp', 'Set_Lit', 'Slice_Expr', 'Ext_Slice_Expr', 'String_Lit', 'Subscript_Expr', 'Tuple_Lit', 'Xor_Expr', 'Yield_Expr', 'File_Node', 'Import_Star', 'Kw_Args_Flag', 'Kw_Args_Flag_Absent', 'Kw_Args_Flag_Present', 'NL', 'Op', 'Params', 'Rel_Name', 'Single_Param', 'Stmt', 'Assert_Stmt', 'Assign_Stmt', 'Aug_Assign_Stmt', 'Break_Stmt', 'Continue_Stmt', 'Decorated', 'Def_Stmt', 'Class_Def', 'Func_Def', 'Del_Stmt', 'Elif_Branch', 'Exec_Stmt', 'For_Stmt', 'Global_Stmt', 'If_Stmt', 'Import_From', 'Import_Name', 'Pass_Stmt', 'Print_Stmt', 'Raise_Stmt', 'Return_Stmt', 'Stream_Print_Stmt', 'Try_Stmt', 'While_Stmt', 'With_Stmt', 'Turkixir_Node_Base_List', 'Arg_List', 'As_Name_Node_List', 'Decorator_List', 'Dict_Assoc_List', 'Dot_List', 'Elif_Branch_List', 'Except_Part_List', 'Expr_List', 'Id_List', 'NL_List', 'Single_Param_List', 'String_Lit_List', 'Turkixir_Node_List', 'Var_Args_Flag', 'Var_Args_Flag_Absent', 'Var_Args_Flag_Present'],
    astnode_kinds={1: 'Arg_Assoc', 2: 'Arg_Gen', 3: 'Kw_Args', 4: 'Var_Args', 5: 'As_Name_Node', 6: 'Comp_If', 7: 'Comp_Op_Kind_Diamond', 8: 'Comp_Op_Kind_Eq', 9: 'Comp_Op_Kind_Gt', 10: 'Comp_Op_Kind_Gte', 11: 'Comp_Op_Kind_In', 12: 'Comp_Op_Kind_Is', 13: 'Comp_Op_Kind_Isnot', 14: 'Comp_Op_Kind_Lt', 15: 'Comp_Op_Kind_Lte', 16: 'Comp_Op_Kind_Noteq', 17: 'Comp_Op_Kind_Notin', 18: 'Comp_For', 19: 'Comp_ForL', 20: 'Decorator', 21: 'Dict_Assoc', 22: 'Else_Part', 23: 'Except_Part', 24: 'And_Expr', 25: 'And_Op', 26: 'Arith_Expr', 27: 'Shift_Expr', 28: 'Term', 29: 'Call_Expr', 30: 'Comp_Op', 31: 'Concat_String_Lit', 32: 'Dict_Comp', 33: 'Dict_Lit', 34: 'Dot', 35: 'Ellipsis_Expr', 36: 'Factor', 37: 'If_Expr', 38: 'Inline_Eval', 39: 'Lambda_Def', 40: 'List_Comp', 41: 'List_Gen', 42: 'List_Lit', 43: 'Dotted_Name', 44: 'Id', 45: 'Not_Op', 46: 'Number_Lit', 47: 'Or_Expr', 48: 'Or_Op', 49: 'Power', 50: 'Set_Comp', 51: 'Set_Lit', 52: 'Slice_Expr', 53: 'Ext_Slice_Expr', 54: 'String_Lit', 55: 'Subscript_Expr', 56: 'Tuple_Lit', 57: 'Xor_Expr', 58: 'Yield_Expr', 59: 'File_Node', 60: 'Import_Star', 61: 'Kw_Args_Flag_Absent', 62: 'Kw_Args_Flag_Present', 63: 'NL', 64: 'Op', 65: 'Params', 66: 'Rel_Name', 67: 'Single_Param', 68: 'Assert_Stmt', 69: 'Assign_Stmt', 70: 'Aug_Assign_Stmt', 71: 'Break_Stmt', 72: 'Continue_Stmt', 73: 'Decorated', 74: 'Class_Def', 75: 'Func_Def', 76: 'Del_Stmt', 77: 'Elif_Branch', 78: 'Exec_Stmt', 79: 'For_Stmt', 80: 'Global_Stmt', 81: 'If_Stmt', 82: 'Import_From', 83: 'Import_Name', 84: 'Pass_Stmt', 85: 'Print_Stmt', 86: 'Raise_Stmt', 87: 'Return_Stmt', 88: 'Stream_Print_Stmt', 89: 'Try_Stmt', 90: 'While_Stmt', 91: 'With_Stmt', 92: 'Arg_List', 93: 'As_Name_Node_List', 94: 'Decorator_List', 95: 'Dict_Assoc_List', 96: 'Dot_List', 97: 'Elif_Branch_List', 98: 'Except_Part_List', 99: 'Expr_List', 100: 'Id_List', 101: 'NL_List', 102: 'Single_Param_List', 103: 'String_Lit_List', 104: 'Turkixir_Node_List', 105: 'Var_Args_Flag_Absent', 106: 'Var_Args_Flag_Present'},
    prefix='libturkixirlang'
)