import ll_merge as merge
import pytest
from linked_list import LinkedList as ll
from node import Node as nd

@pytest.fixture
def empty_ll():
    return ll()


@pytest.fixture
def small_ll():
    return ll([1, 2])

test
merge.merge_lists()