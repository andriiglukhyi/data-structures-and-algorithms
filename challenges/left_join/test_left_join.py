import pytest

from hash_table import HashTable
from left_join import left_join


@pytest.fixture
def empty_hash_table():
    """make empty table"""
    return HashTable()


@pytest.fixture
def table_one():
    """make small table"""
    small_table = HashTable(100)
    small_table.set('fond', 'enamored')
    small_table.set('wrath', 'anger')
    small_table.set('diligent', 'employed')
    small_table.set('guide', 'usher')
    return small_table


@pytest.fixture
def table_two():
    """make big table"""
    big_table = HashTable(100)
    big_table.set('fond', 'averse')
    big_table.set('wrath', 'deligth')
    big_table.set('diligent', 'idle')
    big_table.set('guide', 'follow')
    big_table.set('flow', 'jam')
    return big_table


def test_if_map_are_empty(table_one, empty_hash_table):
    """test if second hash map have some stuff in"""
    assert left_join(table_one, empty_hash_table) == [{'fond': 'enamored'}, {'guide': 'usher'}, {'diligent': 'employed'}, {'wrath': 'anger'}]


def test_if_two_tables(table_one, table_two):
    """test two non empty tables"""
    assert left_join(table_one, table_two) == [['fond', 'enamored', 'averse'], ['guide', 'usher', 'follow'], ['diligent', 'employed', 'idle'], ['wrath', 'anger', 'deligth']]


def test_when_first_array_is_empty(table_one, empty_hash_table):
    """test if first table hase no buckets"""
    assert left_join(empty_hash_table, table_one) == []
    