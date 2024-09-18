
class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val, freq):
        self.heap.append((val, freq))
        self.heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return root

    def peek(self):
        if len(self.heap) > 0:
            return self.heap[0]
        return None

    def heapify_up(self, index):
        parent_index = (index - 1) // 2
        if parent_index < 0 or self.heap[parent_index][1] <= self.heap[index][1]:
            return

        self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
        self.heapify_up(parent_index)

    def heapify_down(self, index):
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        smallest = index

        if (
            left_child < len(self.heap)
            and self.heap[left_child][1] < self.heap[smallest][1]
        ):
            smallest = left_child

        if (
            right_child < len(self.heap)
            and self.heap[right_child][1] < self.heap[smallest][1]
        ):
            smallest = right_child

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heapify_down(smallest)

    def __len__(self):
        return len(self.heap)

    def __repr__(self):
        return f'{self.heap}'

