def suy_dien_tien(GT, RULE, KL):
    # Bước 0: Khởi tạo tập FACTS từ Giả thiết (GT)
    # Screenshot 2026-05-08 101743.png: FACTS <- GT
    facts = set(GT)
    applied_rules = set()

    print(f"B0: Bắt đầu với FACTS: {facts}")
    
    while True:
        found_new_fact = False
        step = 0
        
        # Duyệt qua từng luật r trong tập RULE
        for i, rule in enumerate(RULE):
            left, right = rule
            
            # Điều kiện: left(r) là tập con của FACTS VÀ right(r) chưa có trong FACTS
            # Theo logic: (left(r) ⊆ FACTS) ^ (right(r) ∉ FACTS)
            if set(left).issubset(facts) and right not in facts:
                step += 1
                print(f"\nB{step}: ")
                print(f"Áp dụng luật r{i+1}: {' ^ '.join(left)} -> {right}")
                
                # Thêm right(r) vào FACTS
                facts.add(right)
                found_new_fact = True
                
                
                print(f"Cập nhật FACTS: {facts}")
                
                # Kiểm tra nếu KL đã có trong FACTS
                if KL in facts:
                    return "Thành công"
        
        # Nếu không còn luật nào thỏa mãn, thoát vòng lặp
        if not found_new_fact:
            break


            
    return "Thất bại"

# --- Chạy ví dụ từ Screenshot 2026-05-08 102529.png ---

# Tập các luật: mỗi luật gồm ([vế trái], vế phải)
# rules = [
#     (['a'], 'c'), # r1: a ^ b -> c
#     (['b'], 'd'),  # r2: b ^ c -> d
#     (['c'], 'e'),
#     (['b', 'c'], 'f'),
#     (['e', 'f'], 'g')
# ]

rules = [
    (['a', 'b'], 'c'),
    (['a', 'b'], 'o'),
    (['a', 'h'], 'd'),
    (['a', 'd'], 'm'),
    (['b', 'c'], 'e'),
    (['e', 'o'], 'm'),
]

gia_thiet = ['a', 'b']
ket_luan = 'm'

ket_qua = suy_dien_tien(gia_thiet, rules, ket_luan)
print(f"\nKết quả cuối cùng: {ket_qua}")