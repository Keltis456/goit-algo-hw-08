import heapq


def min_cost_to_connect_cables(cables: list[int]) -> int:
    if not cables:
        return 0
    if len(cables) == 1:
        return 0

    heap = cables.copy()
    heapq.heapify(heap)

    total_cost = 0

    while len(heap) > 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)

        connection_cost = first + second
        total_cost += connection_cost

        heapq.heappush(heap, connection_cost)

    return total_cost


if __name__ == "__main__":
    cables = [4, 3, 2, 6]
    result = min_cost_to_connect_cables(cables)
    print(f"Cables: {cables}")
    print(f"Minimum total cost: {result}")

    cables2 = [1, 2, 3, 4, 5]
    result2 = min_cost_to_connect_cables(cables2)
    print(f"\nCables: {cables2}")
    print(f"Minimum total cost: {result2}")

    cables3 = [8, 4, 6, 12]
    result3 = min_cost_to_connect_cables(cables3)
    print(f"\nCables: {cables3}")
    print(f"Minimum total cost: {result3}")

