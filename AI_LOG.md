# AI Assistance Log

## Assignment 8.1 — Help desk ticket queue

Date: October 20, 2026

Tool: OpenAI ChatGPT / Codex

### Request and material provided

The student provided the full assignment instructions and the original
`tickets.csv` containing twelve help desk tickets. The task was to implement
heap and sorted-list priority queues, record output, and explain insertion costs.

### Assistance provided in this session

- AI generated both Python implementations, CSV loading, comments, and this
  documentation.
- AI drafted the comparison, including why Python's adaptive sort can exploit
  a sorted prefix rather than always taking O(n log n) on these insertions.
- AI generated and executed automated checks for ordering, tie handling,
  empty queues, invalid priorities, counts, and matching printed output.
- AI created four local commits in implementation stages. These commits were
  created during this session under the environment's Codex identity; they
  do not represent earlier independent student development.

### Results observed by AI

Both scripts printed the same twelve lines. Six unittest methods passed,
including subtests for both implementations. Invalid priorities raised
`ValueError` containing the rejected value and left the queue unchanged.
No remote repository was configured and no GitHub push was performed.

### Student review still required

The student should run the programs locally, review the generated code and
comparison, and practice explaining or modifying the queue operations. This
log does not claim that the student has already completed that review.
