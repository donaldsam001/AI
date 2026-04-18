# Cấu hình đồ thị (Ví dụ 1)
graph = {
    'A': {'type': 'OR',  'children': ['B', 'C', 'D']},
    'B': {'type': 'AND', 'children': ['E', 'F']},
    'C': {'type': 'OR',  'children': ['G']},
    'D': {'type': 'AND', 'children': ['H', 'I']},
    'F': {'type': 'OR',  'children': ['J']},
    'G': {'type': 'OR',  'children': ['K']},
    'I': {'type': 'OR',  'children': ['L']},
    'J': {'type': 'AND', 'children': ['M', 'N']},
    'N': {'type': 'OR',  'children': ['O']},
    
    'E': {'type': 'leaf', 'status': 'gd'},
    'H': {'type': 'leaf', 'status': 'gd'},
    'L': {'type': 'leaf', 'status': 'gd'},
    'M': {'type': 'leaf', 'status': 'gd'},
    'O': {'type': 'leaf', 'status': 'gd'},
    'K': {'type': 'leaf', 'status': 'kgd'}
}

# Khởi tạo dữ liệu
nhan = {node: 'kxd' for node in graph}
parents = {node: [] for node in graph}
for node, data in graph.items():
    if 'children' in data:
        for child in data['children']:
            parents[child].append(node)

# Các hàm lan truyền nhãn
def cap_nhat_nhan_don(n):
    if nhan[n] != "kxd": return
    if graph[n]['type'] == 'leaf': return
    
    c_labels = [nhan[c] for c in graph[n]['children']]
    if graph[n]['type'] == 'OR':
        if "gd" in c_labels: nhan[n] = "gd"
        elif all(l == "kgd" for l in c_labels): nhan[n] = "kgd"
    elif graph[n]['type'] == 'AND':
        if all(l == "gd" for l in c_labels): nhan[n] = "gd"
        elif "kgd" in c_labels: nhan[n] = "kgd"

def lan_truyen_nhan(n):
    if nhan[n] in ["gd", "kgd"]:
        for p in parents[n]:
            nhan_cu = nhan[p]
            cap_nhat_nhan_don(p)
            if nhan[p] != nhan_cu:
                lan_truyen_nhan(p)

# Thuật toán chính
def DFS_AND_OR_Optimal(n0):
    MO = [n0] # Danh sách MỞ (đóng vai trò Stack, rút ở đầu - index 0)
    
    print(f"| N | S | Child(S) | MO |")
    print(f"|---|---|---|---|")
    print(f"| 0 | $\\emptyset$ | $\\emptyset$ | {n0} |")
    
    N_step = 1
    while len(MO) > 0:
        # Trong biểu diễn này, để lấy B ra khỏi [B, C, D], ta pop(0)
        S = MO.pop(0) 
        
        children = graph[S].get('children', [])
        nodes_to_push = []
        child_str_list = []
        
        for c in children:
            if graph[c]['type'] == 'leaf':
                # Nút lá -> Đánh dấu * hoặc 0 để in ra
                if graph[c]['status'] == 'gd':
                    child_str_list.append(f"{c}*")
                else:
                    child_str_list.append(f"{c}_0")
                # XỬ LÝ QUAN TRỌNG: KHÔNG ĐƯA VÀO MO. Gán nhãn và lan truyền ngay!
                nhan[c] = graph[c]['status']
                lan_truyen_nhan(c)
            else:
                child_str_list.append(c)
                # Chỉ chuẩn bị nạp vào MO các nút chưa xác định và không phải lá
                if nhan[c] == 'kxd' and c not in MO:
                    nodes_to_push.append(c)
        
        child_str = ", ".join(child_str_list) if child_str_list else "$\\emptyset$"
        
        # DFS Stack: Nạp các nút con hợp lệ vào ĐẦU danh sách MỞ để ưu tiên duyệt sâu nhánh trái
        # Ví dụ: MO đang có [C, D], sinh ra F -> MO mới là [F, C, D]
        MO = nodes_to_push + MO
        
        # Cập nhật cho chính nút đang xét
        cap_nhat_nhan_don(S)
        lan_truyen_nhan(S)
        
        # Kiểm tra điều kiện dừng
        if nhan[n0] == 'gd' or nhan[n0] == 'kgd':
            print(f"| {N_step} | {S} | {child_str} | |")
            break
        else:
            mo_str = ", ".join(MO)
            print(f"| {N_step} | {S} | {child_str} | {mo_str} |")
            
        N_step += 1

# Chạy thử
DFS_AND_OR_Optimal('A')