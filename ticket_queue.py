"""Help desk priority queue using heapq (Python standard library only)."""

import csv
import heapq
from pathlib import Path


def add_ticket(queue, priority, number, description):
    """Add a ticket; numbers must be unique and increase in arrival order."""
    if type(priority) is not int or priority not in (1, 2, 3):
        raise ValueError(f"Priority must be an integer from 1 to 3; received {priority!r}")
    # The number breaks priority ties without comparing descriptions.
    heapq.heappush(queue, (priority, number, description))


def next_ticket(queue):
    """Remove the most urgent ticket, or return None when empty."""
    if not queue:
        return None
    return heapq.heappop(queue)


def pending_count(queue):
    """Return the number of waiting tickets without changing the queue."""
    return len(queue)


def load_tickets(queue, add_function, csv_path):
    """Read records in file order using the selected queue implementation."""
    with open(csv_path, newline="", encoding="utf-8-sig") as source:
        for row in csv.DictReader(source):
            add_function(
                queue, int(row["priority"]), int(row["number"]), row["description"]
            )


def main():
    queue = []
    load_tickets(queue, add_ticket, Path(__file__).with_name("tickets.csv"))
    while pending_count(queue):
        priority, number, description = next_ticket(queue)
        print(priority, number, description)


if __name__ == "__main__":
    main()
