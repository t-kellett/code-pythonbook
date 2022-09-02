from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass(frozen=True)
class OrderLine:
    orderid: str
    sku: str
    qty: int

class Batch:
    def __init__(self, reference: str, sku: str, qty: int, eta: Optional[date]) -> None:
        self.reference = reference
        self.sku = sku
        self.available_quantity = qty
        self.eta = eta

    def allocate(self, line) -> int:
        self.available_quantity -= line.qty
