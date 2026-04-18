import heapq
from collections import deque

graph = {
    'LC': {'ST': 20, 'V': 100},
    'LS': {'HB': 17},
    'ST': {'LC': 20, 'HN': 5},
    'HN': {'ST': 5, 'HB': 7, 'TB': 15, 'NĐ': 10},
    'HB': {'LS': 17, 'HN': 7, 'QN': 90, 'HP': 30},
    'NĐ': {'HN': 10, 'TB': 10, 'NB': 15},
    'TB': {'HN': 15, 'NĐ': 10, 'NB': 15, 'HP': 10},
    'HP': {'HB': 30, 'TB': 10, 'QN': 15},
    'NB': {'NĐ': 15, 'TB': 15, 'TH': 25},
    'TH': {'NB': 25, 'V': 15},
    'QN': {'HB': 90, 'HP': 15, 'V': 90},
    'V':  {'LC': 100, 'TH': 15, 'QN': 90}
}

h = {
    'HN': 50, 'ST': 60, 'LC': 75, 'HB': 65,
    'LS': 70, 'HP': 80, 'QN': 80, 'TB': 55,
    'NĐ': 45, 'NB': 20, 'TH': 15, 'V': 0
}


def blind_search_bfs(start, goal):
    print("=== Kết quả tìm kiếm mù (BFS) ===")
    
    # Queue lưu trữ đường đi (path)
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        current = path[-1]

        if current == goal:
            print("Đường đi tìm thấy: " + " -> ".join(path))
            print()
            return

        if current not in visited:
            visited.add(current)
            # Lấy các đỉnh kề của đỉnh hiện tại
            for neighbor in graph.get(current, {}):
                if neighbor not in visited:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)
                    
    print("Không tìm thấy đường đi!\n")
# Donald Sam

if __name__ == "__main__":
    blind_search_bfs('TB', 'QN')
