# Heap queue versus sorted list

When ticket thirteen arrives, the heap version calls `heapq.heappush`. It
appends the tuple and sifts it upward, comparing it with parent nodes until
the heap property is restored. It follows one path through the heap rather
than sorting every ticket. Insertion costs O(log n) in the worst case.

The sorted version calls `list.append`, then `list.sort` on the entire list.
The expensive difference is re-sorting after every arrival. General sorting
has an O(n log n) worst-case bound. However, Python's adaptive Timsort can
exploit the already sorted prefix here, making this particular pattern O(n).
It still scans the list rather than following a logarithmic heap path.

Removal also differs: `heapq.heappop` costs O(log n), while `list.pop(0)` costs
O(n) because remaining references shift left. Counting costs O(1) in both.
Both versions produced identical output for all twelve CSV tickets, including
arrival-order ties because their unique ticket numbers increase with arrival.
