# AI Assistance Log

## Assignment 8.1 — Help desk ticket queue

Date: October 20, 2026

Tool: OpenAI ChatGPT / Codex

### Request and material provided

The student provided the assignment instructions and the original
`tickets.csv` containing twelve help desk tickets. The task was to explain, review
and sorted-list priority queues, record output, and explain insertion costs.

### Assistance provided in this session

- AI generated CSV loading, comments, and this
  documentation.
- AI drafted the comparison, including why Python's adaptive sort can exploit
  a sorted prefix rather than always taking O(n log n) on these insertions.
- AI generated and executed automated checks for ordering, tie handling,
  empty queues, invalid priorities, counts, and matching printed output.

### Results observed by AI

Both scripts printed the same twelve lines. Six unittest methods passed,
including subtests for both implementations. Invalid priorities raised
`ValueError` containing the rejected value and left the queue unchanged.
No remote repository was configured and no GitHub push was performed.
