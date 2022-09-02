class OrderLine:
    def __init__(self, reference:str, sku: str, qty: int):
        self.reference = reference
        self.sku = sku
        self.qty = qty