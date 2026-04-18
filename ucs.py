import heapq
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

def uniform_cost_search(graph, start, goal):

    priority_queue = [(0, start, [start])]
    
    visited = set()

    while priority_queue:
        current_cost, current_node, path = heapq.heappop(priority_queue)

        if current_node == goal:
            return path, current_cost

        if current_node not in visited:
            visited.add(current_node)

            for neighbor, weight in graph.get(current_node, {}).items():
                if neighbor not in visited:
                    new_cost = current_cost + weight
                    new_path = path + [neighbor]
                    heapq.heappush(priority_queue, (new_cost, neighbor, new_path))
                    
    return None, 0 
# Donald Sam

if __name__ == "__main__":
    start_node = 'HN'
    goal_node = 'V'
    
    path, cost = uniform_cost_search(graph, start_node, goal_node)
    
    if path:
        print(f"Đường đi UCS : {' -> '.join(path)}")
        print(f"Tổng chi phí : {cost}")
    else:
        print(f"Không tìm thấy đường đi từ {start_node} đến {goal_node}!")