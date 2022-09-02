from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass(frozen=True)
class OrderLine:
    orderid: str
    sku: str
    qty: int

class Batch:
    def __init__(self, reference: str, sku: str, qty: int, eta: Optional[date]
                 ) -> None:
        self.reference = reference
        self.sku = sku
        self.purchased_quantity = qty
        self.eta = eta
        self._allocated_lines = set()

    def can_allocate(self, line) -> int:
        return self.available_quantity >= line.qty and self.sku == line.sku

    def allocate(self, line):
        if self.can_allocate(line):
            self._allocated_lines.add(line)

    def deallocate(self, line):
        if line in self._allocated_lines:
            self._allocated_lines.remove(line)

    @property
    def allocated_quantity(self):
        return sum(line.qty for line in self._allocated_lines)

    @property
    def available_quantity(self):
        return self.purchased_quantity - self.allocated_quantity
