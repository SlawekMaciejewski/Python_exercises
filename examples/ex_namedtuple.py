from collections import namedtuple
from dataclasses import dataclass
from datetime import datetime

Order = namedtuple('Order', ['product_name', 'category', 'custom_id', 'due_date', 'model'])

# lub
@dataclass
class OrderCls:
    product_name: str
    category: str
    custom_id: int
    Due_date: datetime
    model: str

if __name__ == '__main__':
    order1 = Order('tv sony', 'tv', 2, datetime.today(), 'KLD34')
    print(order1)
    print(order1.model)
    print(order1.due_date)
    order2 = OrderCls('radio sony', 3, 'radio', datetime.today(), 'RT12')
    print(order2)
    print(order2.model)
    print(order2.custom_id)