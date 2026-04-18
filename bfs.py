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
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, {}):
                if neighbor not in visited:
                    queue.append(path + [neighbor])
                    
    return None
# Donald Sam

if __name__ == "__main__":
    result = blind_search_bfs('HN', 'V')
    print("Đường đi BFS:", " -> ".join(result) if result else "Không tìm thấy")