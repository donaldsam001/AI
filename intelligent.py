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


def informed_search_astar(start, goal):
    print("=== Kết quả tìm kiếm thông minh (A*) ===")
    
    # Hàng đợi ưu tiên (Priority Queue) sử dụng heapq
    # f_score, g_score, current_node, path
    pq = [(h[start], 0, start, [start])]
    
    # Dictionary lưu trữ chi phí g nhỏ nhất đã biết để đến 1 node
    min_g = {}

    while pq:
        current_f, current_g, current, path = heapq.heappop(pq)

        if current == goal:
            print("Đường đi tìm thấy: " + " -> ".join(path))
            print(f"Tổng chi phí thực tế (g): {current_g}")
            print()
            return

        if current not in min_g or current_g <= min_g[current]:
            min_g[current] = current_g

            for neighbor, cost in graph.get(current, {}).items():
                new_g = current_g + cost
                new_f = new_g + h[neighbor]
                
                new_path = list(path)
                new_path.append(neighbor)
                
                heapq.heappush(pq, (new_f, new_g, neighbor, new_path))
                
    print("Không tìm thấy đường đi!\n")
# Donald Sam


if __name__ == "__main__":
    start_node = 'HN'
    goal_node = 'V'


    informed_search_astar(start_node, goal_node)