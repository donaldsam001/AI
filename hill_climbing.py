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

def hill_climbing(start, goal):
    current = start
    path = [current]

    while current != goal:
        neighbors = graph.get(current, {})
        if not neighbors:
            print("Kẹt tại ngõ cụt!")
            return None
            
        # Tìm đỉnh kề có h(n) nhỏ nhất
        best_neighbor = min(neighbors, key=lambda n: h[n])
        
        # Nếu đỉnh kề tốt nhất vẫn tệ hơn đỉnh hiện tại -> Bị kẹt ở cực tiểu địa phương
        if h[best_neighbor] >= h[current]:
            print(f"Bị kẹt tại cực tiểu địa phương ({current})")
            return path
            
        current = best_neighbor
        path.append(current)

    return path
# Donald Sam
if __name__ == "__main__":
    result = hill_climbing('HN', 'V')
    print("Đường đi Leo Đồi:", " -> ".join(result) if result else "Thất bại")