def negate(literal):
    """Hàm lấy phủ định của một literal (VD: 'a' -> '~a', '~a' -> 'a')"""
    if literal.startswith('~'):
        return literal[1:]
    return '~' + literal

def resolve(c1, c2):
    """
    Hàm hợp giải (Resolution) 2 mệnh đề c1 và c2.
    Trả về danh sách các mệnh đề mới có thể sinh ra.
    """
    resolvents = []
    for l1 in c1:
        if negate(l1) in c2:
            # Lấy hợp của 2 mệnh đề và loại bỏ cặp literal đối ngẫu
            new_c = set(c1) | set(c2)
            new_c.remove(l1)
            new_c.remove(negate(l1))
            resolvents.append(frozenset(new_c))
    return resolvents

def format_clause(c):
    """Hàm định dạng mệnh đề để in ra màn hình cho đẹp"""
    if not c:
        return "□ (mệnh đề rỗng)"
    # Sắp xếp để in ra dễ nhìn (ưu tiên chữ cái)
    return " V ".join(sorted(list(c), key=lambda x: (x.replace('~', ''), len(x))))

def is_tautology(clause):
    """Kiểm tra xem mệnh đề có chứa cả 'A' và '~A' không (Mệnh đề hằng đúng)"""
    return any(negate(l) in clause for l in clause)

def robinson_algorithm(clauses):
    # P là danh sách các mệnh đề (dùng frozenset để có thể hash và loại bỏ trùng lặp)
    P = [frozenset(c) for c in clauses]
    P_set = set(P)
    
    print("B0: Tập mệnh đề ban đầu P = {")
    for i, c in enumerate(P):
        print(f"    {i+1}. {format_clause(c)}")
    print("}\n")
        
    print("Bắt đầu quá trình hợp giải:")
    clause_index = len(P)
    step = 1
    
    while True:
        print(f"\n--- B{step} ---")
        new_clauses_this_step = []
        n = len(P)
        
        # Duyệt qua tất cả các cặp mệnh đề trong P
        for i in range(n):
            for j in range(i + 1, n):
                resolvents = resolve(P[i], P[j])
                
                for res in resolvents:
                    # Nếu mệnh đề mới không phải hằng đúng và chưa từng xuất hiện
                    if not is_tautology(res) and res not in P_set:
                        clause_index += 1
                        new_clauses_this_step.append((res, i+1, j+1, clause_index))
                        P_set.add(res)
                        
                        print(f"{clause_index}. {format_clause(res):<25} RES({i+1}, {j+1})")
                        
                        # Điều kiện dừng B5: Sinh ra mệnh đề rỗng
                        if not res: 
                            print("\n=> Đã sinh ra mệnh đề rỗng (□). Chứng minh THÀNH CÔNG!")
                            return True
        
        # Nếu duyệt hết các cặp mà không sinh thêm được mệnh đề nào mới
        if not new_clauses_this_step:
            print("\n=> Q = P (Không thể sinh thêm mệnh đề mới). Chứng minh THẤT BẠI!")
            return False
            
        # Thêm các mệnh đề mới vào tập P để dùng cho bước tiếp theo
        for res, _, _, _ in new_clauses_this_step:
            P.append(res)
            
        step += 1

# ==========================================
# CÀI ĐẶT BÀI TOÁN TỪ VÍ DỤ 1 TRÊN SLIDE
# ==========================================
# Cấu hình bài toán:
# (a ^ b) -> c  <=> ~a V ~b V c
# (b ^ c) -> d  <=> ~b V ~c V d
# a             <=> a
# b             <=> b
# KL: d         => Phủ định KL: ~d

initial_clauses = [
    {'p'}, # 1
    {'~u'}, # 2
    {'~p', 'q'},             # 3
    {'~q', 'r'},             # 4
    {'~r', 's'},             # 5
    {'~u', '~s'}
]

if __name__ == "__main__":
    robinson_algorithm(initial_clauses)