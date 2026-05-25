def backward_chaining_trace(gt, rules, kl):
    print(f"GT = {gt}; KL = {kl}")
    print("RULE = { " + "; ".join([f"r{i+1}: {' ^ '.join(r[0])} -> {r[1]}" for i, r in enumerate(rules)]) + " }")
    
    current_goals = list(kl)
    step = 0
    
    # B0: Khởi tạo
    print(f"B{step}: GOAL = {', '.join(current_goals)}")
    
    def solve(goal, step_count):
        if goal in gt:
            return True, step_count
        
        # Tìm luật có vế phải là goal
        for i, (left, right) in enumerate(rules):
            if right == goal:
                step_count += 1
                rule_name = f"r{i+1}"
                left_str = " ^ ".join(left)
                print(f"B{step_count}: Lấy {rule_name}: {left_str} -> {right}")
                
                # Xác định các đích mới không có trong GT
                new_sub_goals = [p for p in left if p not in gt]
                known_facts = [p for p in left if p in gt]
                
                if known_facts:
                    fact_str = ", ".join(known_facts)
                    print(f"   Đích mới {left_str}. Vì {fact_str} \u2208 GT ", end="")
                
                if not new_sub_goals:
                    print(f"nên GOAL = \u2205")
                    return True, step_count
                else:
                    print(f"nên GOAL = {', '.join(new_sub_goals)}")
                    
                    # Đệ quy chứng minh các đích mới
                    all_sub_proven = True
                    for sub in new_sub_goals:
                        success, step_count = solve(sub, step_count)
                        if not success:
                            all_sub_proven = False
                            break
                    
                    if all_sub_proven:
                        return True, step_count
        
        return False, step_count

    # Bắt đầu giải từ mục tiêu cuối cùng
    success_final = True
    total_steps = step
    for g in current_goals:
        success, total_steps = solve(g, total_steps)
        if not success:
            success_final = False
            break
            
    if success_final:
        print("\u279E Kết thúc thành công")
    else:
        print("\u279E Thất bại")

# # --- Chạy thử đúng ví dụ trong ảnh ---
# GT3 = {"a", "b"}
# KL3 = {"m"}
# RULES3 = [
#     (["a", "b"], "c"), # r1
#     (["a", "h"], "d"), # r2
#     (["b", "c"], "e"), # r3
#     (["a", "d"], "m"), # r4
#     (["a", "b"], "o"), # r5
#     (["o", "e"], "m")  # r6
# ]
# backward_chaining_trace(GT3, RULES3, KL3)


# Danh sách các luật từ r1 đến r8
GT= {"a", "c"}
KL = "i"
RULES_NEW = [
    (["a", "b"], "f"),          # r1: a ^ b -> f
    (["d", "f"], "i"),          # r2: d ^ f -> i
    (["b", "f"], "i"),          # r3: b ^ f -> i
    (["h", "a"], "f"),          # r4: h ^ a -> f
    (["f", "g", "h"], "i"),     # r5: f ^ g ^ h -> i
    (["a", "c"], "d"),          # r6: a ^ c -> d
    (["a", "d"], "g"),          # r7: a ^ d -> g
    (["a", "d"], "h")           # r8: a ^ d -> h
]

backward_chaining_trace(GT, RULES_NEW, KL)