from hash_table import HashTable
from linked_list import LinkedList as lin
import pytest


@pytest.fixture
def empty_hash_table():
    """make empty table"""
    return HashTable()


@pytest.fixture
def small_table():
    """make small table"""
    small_table = HashTable(10)
    small_table.set('John', 1234)
    small_table.set('anna', 123456)
    small_table.set('john', '123')
    small_table.set('John', 'sdf')
    return small_table


@pytest.fixture
def big_table():
    """make big table"""
    big_table = HashTable()
    big_table.set('John', 1234)
    big_table.set('anna', 123456)
    big_table.set('john', '123')
    big_table.set('Skcot', 'sdf')
    big_table.set('Arina', 123456)
    big_table.set('Arina', '123')
    big_table.set('Arina', 'sdf')
    return small_table


def test_init_function():
    """test init function"""
    instance = HashTable()
    assert len(instance.buckets) == 1024
    assert instance.buckets[0] is None
    assert instance.max_size == 1024


def test_init_fucntion_dif_size():
    """test init function"""
    instance = HashTable(3)
    assert len(instance.buckets) == 3
    assert instance.buckets[0] is None
    assert instance.max_size == 3


def test_has_function():
    """test hashe finction"""
    instance = HashTable(10)
    assert instance.hash_key(1) is False
    assert instance.hash_key('John') == 9


def test_hashe_function_const():
    """test if hashe function return the smae value all the time"""
    instance = HashTable(10)
    
    assert instance.hash_key('abcd') != instance.hash_key('John')
    assert instance.hash_key('abc') == instance.hash_key('abc')


def test_set_function(empty_hash_table):
    """test set function"""
    assert empty_hash_table.buckets[0] is None
    empty_hash_table.set('John', 12314)
    assert empty_hash_table.buckets[399]
    assert empty_hash_table.buckets.count(None) == 1023
    assert type(empty_hash_table.buckets[399]) == dict
    assert empty_hash_table.buckets[399]['John'] == 12314


def test_set_fucntion_multiply(empty_hash_table):
    """test a couple set"""
    empty_hash_table.set('John', 12314)
    empty_hash_table.set('A', 12314)
    assert empty_hash_table.buckets.count(None) == 1022
    assert empty_hash_table.buckets[65]['A'] == 12314
    assert empty_hash_table.buckets[399]['John'] == 12314
    assert empty_hash_table.set(123, 123) is False


def test_collision(small_table):
    """test collision handling"""
    assert small_table.buckets[9].head
    # assert small_table.buckets[399]['John'] == 1234
    small_table.set('John', 'string')
    # assert small_table.buckets[399].head


