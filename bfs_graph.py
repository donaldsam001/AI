# Cấu hình đồ thị từ Ví dụ 1
graph_vidu1 = {
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

# 1. Khởi tạo nhãn (gán ngay nhãn cho các nút lá)
nhan = {node: 'kxd' for node in graph_vidu1}
for node, data in graph_vidu1.items():
    if data['type'] == 'leaf':
        nhan[node] = data['status']

# 2. Tạo danh sách nút cha để lan truyền ngược
parents = {node: [] for node in graph_vidu1}
for node, data in graph_vidu1.items():
    if 'children' in data:
        for child in data['children']:
            parents[child].append(node)

# 3. Hàm cập nhật nhãn cho 1 nút
def cap_nhat_nhan_don(n):
    if nhan[n] != "kxd": return
    data = graph_vidu1[n]
    if data['type'] == 'leaf': return
    
    c_labels = [nhan[c] for c in data['children']]
    if data['type'] == 'OR':
        if "gd" in c_labels: nhan[n] = "gd"
        elif all(l == "kgd" for l in c_labels): nhan[n] = "kgd"
    elif data['type'] == 'AND':
        if all(l == "gd" for l in c_labels): nhan[n] = "gd"
        elif "kgd" in c_labels: nhan[n] = "kgd"

# 4. Hàm lan truyền nhãn lên trên
def lan_truyen_nhan(n):
    if nhan[n] in ["gd", "kgd"]:
        for p in parents[n]:
            nhan_cu = nhan[p]
            cap_nhat_nhan_don(p)
            if nhan[p] != nhan_cu:
                lan_truyen_nhan(p)

# 5. Thuật toán BFS AND/OR in dạng bảng
def BFS_AND_OR_Table(n0):
    MO = [n0]
    
    # In tiêu đề bảng
    print("| N | S | Child(S) | MO |")
    print("|---|---|---|---|")
    print(f"| 0 | $\\emptyset$ | $\\emptyset$ | {n0} |")
    
    N = 1
    while len(MO) > 0:
        S = MO.pop(0)
        
        children = graph_vidu1[S].get('children', [])
        child_str_list = []
        
        # Xử lý sinh con và định dạng chuỗi
        for c in children:
            if graph_vidu1[c]['type'] == 'leaf':
                if graph_vidu1[c]['status'] == 'gd':
                    child_str_list.append(f"{c}*") # Nút giải được
                else:
                    child_str_list.append(f"{c}_0") # Nút không giải được
            else:
                child_str_list.append(c)
                # Chỉ thêm vào MO các nút chưa xác định
                if nhan[c] == 'kxd' and c not in MO:
                    MO.append(c)
                    
        child_str = ", ".join(child_str_list) if child_str_list else "$\\emptyset$"
        
        # Kích hoạt lan truyền nhãn cho các nút con là lá vừa sinh ra
        for c in children:
            if graph_vidu1[c]['type'] == 'leaf':
                lan_truyen_nhan(c)
        
        # Cập nhật và lan truyền cho chính S
        cap_nhat_nhan_don(S)
        lan_truyen_nhan(S)
        
        # Kiểm tra điều kiện dừng
        if nhan[n0] == 'gd' or nhan[n0] == 'kgd':
            print(f"| {N} | {S} | {child_str} |  |") # Trống MO ở bước cuối
            break
        else:
            mo_str = ", ".join(MO)
            print(f"| {N} | {S} | {child_str} | {mo_str} |")
            
        N += 1

# Chạy chương trình
BFS_AND_OR_Table('A')