from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class Product:
    """商品对象"""

    name: str
    price: float
    description: str = ""
    category: str = ""
    stock: int = 0
    sku: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.now)

    @property
    def is_in_stock(self) -> bool:
        """判断是否有库存"""
        return self.stock > 0

    def apply_discount(self, percentage: float) -> float:
        """应用折扣，返回折后价格"""
        if not 0 <= percentage <= 100:
            raise ValueError("Discount percentage must be between 0 and 100")
        return self.price * (1 - percentage / 100)

    def __str__(self) -> str:
        return f"{self.name} - ¥{self.price:.2f} (库存: {self.stock})"


if __name__ == "__main__":
    # 示例用法
    product = Product(
        name="iPhone 16",
        price=6999.00,
        description="Apple iPhone 16 128GB",
        category="电子产品",
        stock=100,
        sku="APPLE-IP16-128",
    )

    print(product)
    print(f"是否有库存: {product.is_in_stock}")
    print(f"trigger test1111: {product.is_in_stock}")
    print(f"8折价格: ¥{product.apply_discount(20):.2f}")
