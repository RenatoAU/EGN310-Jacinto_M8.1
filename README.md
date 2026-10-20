# Help Desk Ticket Queue

EGN 310 Data Structures — Module 8, Assignment 8.1

Two implementations serve the lowest priority number first: 1 is emergency,
2 is intermediate, and 3 is routine. Both use `(priority, number, description)`.
The supplied CSV is preserved unchanged.

## Run

Python 3 is required. There are no external dependencies.
Extract the entire ZIP first, then open a terminal in `help_desk_ticket_queue`.

```sh
python ticket_queue.py
python sorted_version.py
python -m unittest -v
```

On systems where the command is `python3`, substitute it for `python`.
Both scripts find `tickets.csv` beside their source files, even when launched
from a different working directory. `output.txt` contains the captured heap
output, which is identical to the sorted-list output.

## Functions and assumptions

Both modules expose `add_ticket(queue, priority, number, description)`,
`next_ticket(queue)`, and `pending_count(queue)`. Start with an empty list.
The first function changes the queue in place. The second removes and returns
one tuple, or returns `None` when empty. Counting does not remove anything.
Invalid priorities raise `ValueError` naming the supplied value.

Ticket numbers must be unique and increase in arrival order. The supplied
CSV uses 101 through 112 in file order, so ticket-number order also means
arrival order. Uniqueness alone would not guarantee arrival order if arbitrary
ticket numbers were used. Number assignment is the caller's responsibility.
Do not interpret the heap's internal list as a fully sorted list; use
`next_ticket` to retrieve tickets in service order.

Expected ticket numbers:

```text
102, 104, 108, 111, 101, 105, 107, 110, 103, 106, 109, 112
```

## Verification

Six automated test methods cover both implementations: twelve-ticket service
order, arrival-order ties instead of alphabetical description order, empty
queues, rejected priority values, counts, urgent arrivals after service, and
printed output against `output.txt`. The two script outputs were also compared
byte for byte.


