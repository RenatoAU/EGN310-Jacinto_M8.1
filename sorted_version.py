"""Equivalent help desk queue using append, sort, and pop(0)."""

from pathlib import Path

from ticket_queue import load_tickets


def add_ticket(queue, priority, number, description):
    """Append a ticket and re-sort; numbers increase in arrival order."""
    if type(priority) is not int or priority not in (1, 2, 3):
        raise ValueError(f"Priority must be an integer from 1 to 3; received {priority!r}")
    queue.append((priority, number, description))
    queue.sort()


def next_ticket(queue):
    """Take the first ticket, shifting the remaining items to the left."""
    if not queue:
        return None
    return queue.pop(0)


def pending_count(queue):
    """Return the number of waiting tickets."""
    return len(queue)


def main():
    queue = []
    load_tickets(queue, add_ticket, Path(__file__).with_name("tickets.csv"))
    while pending_count(queue):
        priority, number, description = next_ticket(queue)
        print(priority, number, description)


if __name__ == "__main__":
    main()
