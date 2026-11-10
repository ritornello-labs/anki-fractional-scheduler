from __future__ import annotations

import sqlite3
import sys
import unittest
from datetime import datetime, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'addon'))
import schedule


class Collection:
    def __init__(self, decks):
        self._decks = decks
        self.db = self
        self.conf = {'rollover': 4}
        self.conn = sqlite3.connect(':memory:')
        self.conn.executescript('''
            create table cards (id integer primary key, did integer, odid integer,
                                type integer, queue integer);
            create table revlog (id integer primary key, cid integer, ease integer);
        ''')

    def all(self, sql, *args):
        return list(self.conn.execute(sql, args))


class AvailableDeckTests(unittest.TestCase):
    def setUp(self):
        self.plan = {'id': 'countries', 'type': 'every_n_days', 'm': 1, 'n': 2,
                     'fractional_strategy': 'balance_first'}
        self.decks = [schedule.DeckInfo(1, 'Tree::A'), schedule.DeckInfo(2, 'Tree::B')]
        self.front, self.other = schedule._stable_deck_order(self.plan, self.decks)
        self.col = Collection(self.decks)
        self.addCleanup(self.col.conn.close)

    def preview(self, day=10, days=2):
        return schedule._preview_balance_first_sequences_by_deck(
            self.col, self.plan, self.decks, '2026-01-01', day, days,
            all_decks=self.decks)

    def card(self, cid, did, card_type=0, queue=0, odid=0):
        self.col.conn.execute('insert into cards values (?, ?, ?, ?, ?)',
                              (cid, did, odid, card_type, queue))

    def test_exhausted_front_is_skipped_without_reducing_group_budget(self):
        self.card(1, self.front.deck_id, 2, 2)
        self.card(2, self.other.deck_id)
        result = self.preview()
        self.assertEqual(result[self.front.deck_id], [0, 0])
        self.assertEqual(result[self.other.deck_id], [1, 1])

    def test_no_available_cards_produces_no_release(self):
        self.card(1, self.front.deck_id, 0, -1)
        self.card(2, self.other.deck_id, 0, -2)
        self.assertTrue(all(not any(seq) for seq in self.preview().values()))

    def test_new_cards_in_filtered_deck_do_not_hold_rotation(self):
        self.card(1, self.front.deck_id, odid=self.front.deck_id)
        self.card(2, self.other.deck_id)
        self.assertEqual(self.preview()[self.other.deck_id], [1, 1])

    def test_finishing_deck_does_not_offer_another_country_same_day(self):
        self.card(1, self.front.deck_id, 2, 2)
        self.card(2, self.other.deck_id)
        stamp = datetime(2026, 1, 1, 4, 1).astimezone() + timedelta(days=10)
        self.col.conn.execute('insert into revlog values (?, 1, 3)',
                              (int(stamp.timestamp() * 1000),))
        result = self.preview()
        self.assertEqual(result[self.front.deck_id], [1, 0])
        self.assertEqual(result[self.other.deck_id], [0, 1])

    def test_available_front_keeps_place_after_missed_day(self):
        self.card(1, self.front.deck_id)
        self.card(2, self.other.deck_id)
        self.assertEqual(self.preview(day=11)[self.front.deck_id][0], 1)

    def test_parent_can_supply_cards_from_a_child(self):
        child = schedule.DeckInfo(3, self.front.name + '::Child')
        self.card(1, child.deck_id)
        result = schedule._preview_balance_first_sequences_by_deck(
            self.col, self.plan, self.decks, '2026-01-01', 10, 1,
            all_decks=self.decks + [child])
        self.assertEqual(result[self.front.deck_id], [1])
        self.assertEqual(result[self.other.deck_id], [0])

    def test_replenished_deck_rejoins_without_resetting_rotation(self):
        self.card(1, self.front.deck_id, 2, 2)
        self.card(2, self.other.deck_id)
        self.assertEqual(self.preview()[self.other.deck_id][0], 1)
        self.card(3, self.front.deck_id)
        self.assertEqual(self.preview()[self.front.deck_id][0], 1)


if __name__ == '__main__':
    unittest.main()
