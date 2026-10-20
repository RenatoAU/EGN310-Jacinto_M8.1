"""Run with: python -m unittest -v"""

import contextlib
import io
from pathlib import Path
import unittest

import sorted_version
import ticket_queue


class TicketQueueTests(unittest.TestCase):
    def test_empty_queue(self):
        for implementation in (ticket_queue, sorted_version):
            with self.subTest(implementation=implementation.__name__):
                queue = []
                self.assertIsNone(implementation.next_ticket(queue))
                self.assertEqual(implementation.pending_count(queue), 0)

    def test_invalid_priorities_name_value_and_preserve_queue(self):
        for implementation in (ticket_queue, sorted_version):
            for priority in (0, 4, -1, 99, 1.5, "1", None, True):
                with self.subTest(implementation=implementation.__name__, priority=priority):
                    queue = [(2, 100, "Already waiting")]
                    before = queue.copy()
                    with self.assertRaises(ValueError) as error:
                        implementation.add_ticket(queue, priority, 101, "Rejected")
                    self.assertIn(repr(priority), str(error.exception))
                    self.assertEqual(queue, before)

    def test_priority_and_arrival_ties(self):
        arrivals = [
            (2, 101, "Routine printer"),
            (1, 102, "Z outage"),
            (3, 103, "Setup"),
            (1, 104, "A outage"),
        ]
        expected = [arrivals[1], arrivals[3], arrivals[0], arrivals[2]]
        for implementation in (ticket_queue, sorted_version):
            with self.subTest(implementation=implementation.__name__):
                queue = []
                for count, ticket in enumerate(arrivals, start=1):
                    implementation.add_ticket(queue, *ticket)
                    self.assertEqual(implementation.pending_count(queue), count)
                self.assertEqual([implementation.next_ticket(queue) for _ in arrivals], expected)
                self.assertIsNone(implementation.next_ticket(queue))

    def test_new_urgent_ticket_after_service(self):
        for implementation in (ticket_queue, sorted_version):
            with self.subTest(implementation=implementation.__name__):
                queue = []
                implementation.add_ticket(queue, 2, 101, "Printer")
                implementation.add_ticket(queue, 3, 102, "Monitor")
                self.assertEqual(implementation.next_ticket(queue)[1], 101)
                implementation.add_ticket(queue, 1, 103, "Server down")
                self.assertEqual(implementation.next_ticket(queue)[1], 103)
                self.assertEqual(implementation.next_ticket(queue)[1], 102)

    def test_all_twelve_csv_tickets(self):
        expected_numbers = [102, 104, 108, 111, 101, 105, 107, 110, 103, 106, 109, 112]
        for implementation in (ticket_queue, sorted_version):
            with self.subTest(implementation=implementation.__name__):
                queue = []
                ticket_queue.load_tickets(queue, implementation.add_ticket,
                                         Path(__file__).with_name("tickets.csv"))
                self.assertEqual(implementation.pending_count(queue), 12)
                result = [implementation.next_ticket(queue) for _ in range(12)]
                self.assertEqual([ticket[1] for ticket in result], expected_numbers)
                self.assertEqual([ticket[0] for ticket in result], [1]*4 + [2]*4 + [3]*4)
                self.assertIsNone(implementation.next_ticket(queue))

    def test_both_printed_outputs_match_saved_output(self):
        expected = Path(__file__).with_name("output.txt").read_text(encoding="utf-8")
        for implementation in (ticket_queue, sorted_version):
            with self.subTest(implementation=implementation.__name__):
                output = io.StringIO()
                with contextlib.redirect_stdout(output):
                    implementation.main()
                self.assertEqual(output.getvalue(), expected)


if __name__ == "__main__":
    unittest.main()
