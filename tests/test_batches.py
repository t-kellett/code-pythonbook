import pytest

from datetime import date
from orderline import OrderLine
from batch import Batch


def test_allocating_a_batch_reduces_available_quantity():
    batch = Batch("batch-001", "SMALL-TABLE", qty=20, eta=date.today())
    line = OrderLine("order-ref", "SMALL-TABLE", 2)

    batch.allocate(line)

    assert batch.available_quantity == 18
