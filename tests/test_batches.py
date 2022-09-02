from datetime import date
from domain.model import OrderLine, Batch


def make_batch_and_line(sku: str, batch_qty: int, line_qty: int):
    return (
        Batch('batch-001', sku, batch_qty, eta=date.today()),
        OrderLine('order-123', sku, line_qty)
    )

def test_can_reduce_batch_quantity_by_orderline_quantity():
    batch, line = make_batch_and_line('WOODCHUCK-CHUCK', 20, 2)
    batch.allocate(line)

    assert batch.available_quantity == 18
def test_can_allocate_if_available_greater_than_or_equal_to_required():
    large_batch, small_line = make_batch_and_line('BIG-TABLE', 20, 2)

    assert large_batch.can_allocate(small_line)


def test_cannot_allocate_if_available_less_than_required():
    small_batch, large_line = make_batch_and_line('BIG-TABLE', 2, 10)

    assert small_batch.can_allocate(large_line) is False

def test_cannot_allocate_if_skus_do_not_match():
    batch = Batch('batch-002', 'YELLOW-LORRY', 2, eta=date.today())
    line = OrderLine('order-2', 'RED-LORRY', 2)

    assert batch.can_allocate(line) is False

def test_can_only_deallocate_allocated_lines():
    batch, unallocated_line = make_batch_and_line('LOVELY-LAMP', 10, 5)

    batch.deallocate(unallocated_line)

    assert batch.available_quantity == 10
