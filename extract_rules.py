from sympy import symbols, Implies, And, Or, Not, to_cnf

# 1. Khai báo các ký hiệu
a, b, c, d, f, g, h, i = symbols('a b c d f g h i')

# 2. Tập hợp các biểu thức gốc từ Screenshot 2026-05-08 110058.png
expressions = [
    And(a, c),                          # a ^ c (Đây là sự kiện/facts)
    Implies(a, Implies(b, f)),          # a -> (b -> f)
    Implies(And(Or(d, b), f), i),       # (d v b) ^ f -> i
    Or(Not(h), Not(a), f),              # ~h v ~a v f
    Implies(And(f, g, h), i),           # f ^ g ^ h -> i
    Or(Not(a), d, Not(c)),              # ~a v d v ~c
    Implies(And(a, d),And(g, h))                     # g ^ h (Đây là sự kiện/facts)
]

def extract_rules(expr_list):
    rules = []
    for expr in expr_list:
        # Chuyển biểu thức về dạng CNF và tách các mệnh đề hội (And)
        cnf_expr = to_cnf(expr)
        clauses = cnf_expr.args if isinstance(cnf_expr, And) else [cnf_expr]
        
        for clause in clauses:
            # Chỉ xử lý các mệnh đề có tính chất của một "Luật" (có tiền đề và kết luận)
            # Một luật chuẩn (Horn clause) thường là một Or của các phủ định và tối đa 1 khẳng định
            if isinstance(clause, Or):
                premises = set()
                conclusion = None
                
                for literal in clause.args:
                    if isinstance(literal, Not):
                        # Phủ định của phủ định là khẳng định (tiền đề)
                        premises.add(str(literal.args[0]))
                    else:
                        # Biến không có Not là kết luận
                        conclusion = str(literal)
                
                # Chỉ thêm vào danh sách rules nếu có cả tiền đề và kết luận
                if premises and conclusion:
                    rules.append((premises, conclusion))
                    
    return rules

# 3. Thực hiện phân rã
rules = extract_rules(expressions)

# 4. In kết quả theo định dạng yêu cầu
print("rules = [")
for r in rules:
    print(f"    ({r[0]}, '{r[1]}'),")
print("]")