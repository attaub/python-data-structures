"""

python
Copy
Edit
A tree-based data structure with the heap property

Min-Heap: parent_val <= children_val.
Max-Heap: parent_val >= children_val.
Commonly used to implement priority queues.

A priority queue supports retrieving elements in order of their priority (lowest or highest).

Efficient Insertions, Deletions: O(log n) time

Use Cases:
Job Scheduling, Pathfinding Dynamic median finding

Python has a built-in library, heapq, supports min-heaps.
Implement a max-heap, by inverting values ( multiplying them by -1)

"""

# min heap operations
import heapq
min_heap = []
heapq.heappush(min_heap, 10)
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 20)
heapq.heappush(min_heap, 1)

print("Min-Heap:", min_heap)  # [1, 5, 20, 10]

# get the smallest element
smallest = heapq.heappop(min_heap)
smallest = min_heap[0]

#  max heap
max_heap = []
heapq.heappush(max_heap, -10)
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -20)
heapq.heappush(max_heap, -1)
max_heap  # [-20, -10, -5, -1]

largest = -heapq.heappop(max_heap)
print([-x for x in max_heap])  # [10, 1, 5]

# Convert a List into a Heap
numbers = [10, 5, 20, 1]
heapq.heapify(numbers)
numbers  # [1, 5, 20, 10]
heapq.heappop(numbers)  # 1


# Priority queue with (priority, value)
pq = []
heapq.heappush(pq, (2, "Task A"))
heapq.heappush(pq, (1, "Task B"))
heapq.heappush(pq, (3, "Task C"))

# Process tasks in priority order
while pq:
    priority, task = heapq.heappop(pq)
    print(f"Processing {task} with priority {priority}")


# find the k smallest/largest elements
numbers = [10, 5, 20, 1, 15, 25, 8]
print(heapq.nsmallest(3, numbers))  # [1, 5, 8]
print(heapq.nlargest(3, numbers))  # [25, 20, 15]

# Merge Sorted Lists
list1 = [1, 3, 5]
list2 = [2, 4, 6]
list3 = [0, 7, 8]
merged = heapq.merge(list1, list2, list3)
print(list(merged))  # [0, 1, 2, 3, 4, 5, 6, 7, 8]


# Implementing Dijkstra’s (shortest) Algorithm
import heapq

def dijkstra(graph, start):
    heap = [(0, start)]  # (distance, node)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    while heap:
        current_distance, current_node = heapq.heappop(heap)

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances

# Example graph as adjacency list
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)],
}

print("Shortest Distances:", dijkstra(graph, 'A'))
