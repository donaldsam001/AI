class Expr:
    # Nạp chồng toán tử để viết biểu thức dễ dàng hơn: ~ (Not), | (Or), & (And)
    def __invert__(self): return Not(self)
    def __or__(self, other): return Or(self, other)
    def __and__(self, other): return And(self, other)

class Var(Expr):
    def __init__(self, name): self.name = name
    def __str__(self): return self.name
    def __eq__(self, o): return isinstance(o, Var) and self.name == o.name
    def __hash__(self): return hash(self.name)

class Not(Expr):
    def __init__(self, val): self.val = val
    def __str__(self): return f"¬{self.val}"
    def __eq__(self, o): return isinstance(o, Not) and self.val == o.val
    def __hash__(self): return hash(("not", self.val))

class Or(Expr):
    def __init__(self, l, r): self.l, self.r = l, r
    def __str__(self): return f"{self.l} ∨ {self.r}"
    def __eq__(self, o): return isinstance(o, Or) and self.l == o.l and self.r == o.r
    def __hash__(self): return hash(("or", self.l, self.r))

class And(Expr):
    def __init__(self, l, r): self.l, self.r = l, r
    def __str__(self): return f"{self.l} ∧ {self.r}"
    def __eq__(self, o): return isinstance(o, And) and self.l == o.l and self.r == o.r
    def __hash__(self): return hash(("and", self.l, self.r))

class Problem:
    def __init__(self, label, VT, VP):
        self.label = label
        self.VT = list(VT)
        self.VP = list(VP)

def format_p(p):
    vt_str = ", ".join(str(x) for x in p.VT) if p.VT else "∅"
    vp_str = ", ".join(str(x) for x in p.VP) if p.VP else "∅"
    return f"{vt_str} → {vp_str}"

def format_P(P):
    return ";\n".join([f"({p.label}, VP) = {format_p(p)}" for p in P])

def has_intersection(p):
    # Trả về True nếu tồn tại phần tử chung giữa VT và VP
    return any(x in p.VP for x in p.VT)

def can_chuyen(p):
    # Kiểm tra xem có phép phủ định (¬) ở lớp ngoài cùng của VT hoặc VP không
    return any(isinstance(x, Not) for x in p.VT + p.VP)

def apply_chuyen(p):
    new_vt = []
    new_vp = list(p.VP)
    
    # Chuyển ¬ từ Vế Trái sang Vế Phải
    for x in p.VT:
        if isinstance(x, Not):
            new_vp.append(x.val)
        else:
            new_vt.append(x)

    final_vp = []
    # Chuyển ¬ từ Vế Phải sang Vế Trái
    for x in new_vp:
        if isinstance(x, Not):
            new_vt.append(x.val)
        else:
            final_vp.append(x)

    return Problem(p.label, new_vt, final_vp)

def can_tach(p):
    # Tách nếu VT chứa Tuyển (∨) hoặc VP chứa Hội (∧)
    return any(isinstance(x, Or) for x in p.VT) or any(isinstance(x, And) for x in p.VP)

def apply_tach(p):
    # Tìm và tách phần tử đầu tiên thỏa mãn
    for i, x in enumerate(p.VT):
        if isinstance(x, Or):
            vt1, vt2 = p.VT.copy(), p.VT.copy()
            vt1.pop(i); vt2.pop(i)
            vt1.insert(i, x.l); vt2.insert(i, x.r)
            
            lb = p.label.replace("VT", "")
            return Problem(f"VT{lb}1", vt1, p.VP), Problem(f"VT{lb}2", vt2, p.VP)
            
    for i, x in enumerate(p.VP):
        if isinstance(x, And):
            vp1, vp2 = p.VP.copy(), p.VP.copy()
            vp1.pop(i); vp2.pop(i)
            vp1.insert(i, x.l); vp2.insert(i, x.r)
            
            lb = p.label.replace("VT", "")
            return Problem(f"VT{lb}1", p.VT, vp1), Problem(f"VT{lb}2", p.VT, vp2)

def solve_wang_hao(initial_VT, initial_VP):
    P = [Problem("VT", initial_VT, initial_VP)]
    step = 1

    while P:
        p = P.pop(0) # LIFO lấy ra bài toán nhánh gần nhất

        if p.label != "VT":
            print(f"B{step} Lấy ({p.label}, VP) = {format_p(p)}")

        # Kiểm tra đóng nhánh (Giao của VT và VP khác rỗng)
        if has_intersection(p):
            if p.label != "VT":
                print(f"{p.label} ∩ VP ≠ ∅ tức là {p.label} → VP")
            step += 1
            continue

        # Hàm CHUYỂN
        if can_chuyen(p):
            p = apply_chuyen(p)
            print(f"{p.label} ∩ VP = ∅ → CHUYEN({p.label}, VP) {format_p(p)}")
            if has_intersection(p):
                print(f"{p.label} ∩ VP ≠ ∅ tức là {p.label} → VP")
                step += 1
                continue

        # Hàm TÁCH
        if can_tach(p):
            if p.label == "VT":
                print(f"B{step} {p.label} ∩ VP = ∅ → TACH({p.label}, VP)")
            else:
                print(f"{p.label} ∩ VP = ∅ → TACH({p.label}, VP)")
            
            p1, p2 = apply_tach(p)
            P.insert(0, p2)
            P.insert(0, p1)
            print(f"P = {{ {format_P(P)} }}")
        else:
            if not has_intersection(p):
                print("Không thành công (Không thể chứng minh)")
                return

        step += 1

    print("Bài toán được chứng minh")

# ==========================================
# KHỞI TẠO BÀI TOÁN - VÍ DỤ 1
# ==========================================
if __name__ == "__main__":
    r = Var('r')
    u = Var('u')
    q = Var('q')
    p = Var('p')
    s = Var('s')

    # Theo Ví dụ 1:
    # VT = { ¬r ∨ u ; ¬u ∨ w ; r ∨ w }
    # VP = { w }
    VT = [~p | q, ~q | r, ~r | s, ~u | ~s]
    VP = [~p, u]

    print("--- TRUY VẾT THUẬT TOÁN VƯƠNG HẠO ---")
    solve_wang_hao(VT, VP)