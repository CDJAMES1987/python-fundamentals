"""
Practice Problem 1: Transaction Risk Evaluation

You must implement three classes:

-User
    -Stores a history of past transactions
    -Exposes a method that returns the users average transaction amount
    -Exposes a method that returns all distinct merchant categories the user has transacted with

-Purchase
    -Contains an amount and a merchant category

-RiskEngine
    -Contains a method is_high_risk(user, purchase) that you must implement

Rules:
    -A purchase is considered high risk if either of the following is true:
        1. The purchase amount is more than 4 times the users average transaction amount
        2. The merchant category has never appeared in the users transaction history

Constraints:
    -Do not modify the input objects
    -Do not store state inside RiskEngine
    -Assume all helper methods on User are correct
    -Return a boolean only
"""


class Purchase:
    def __init__(self, user_id: int, amount: float, merchant_category: str) -> None:
        self.amount = amount
        self.merchant_category = merchant_category
        self.user_id = user_id


class User:
    def __init__(self, user_id: int, transactions: list[Purchase]) -> None:
        self.user_id = user_id
        self.transactions = transactions

    def average_transaction_amount(self) -> None:
        pass


transactions = [
    Purchase(user_id=1, amount=127.00, merchant_category='retail'),
    Purchase(user_id=2, amount=1.00, merchant_category='food'),
    Purchase(user_id=3, amount=3000.00, merchant_category='retail'),
    Purchase(user_id=1, amount=27.00, merchant_category='food'),
    Purchase(user_id=2, amount=40.00, merchant_category='gas'),
    Purchase(user_id=3, amount=30.00, merchant_category='gas'),
]

users = {}

for purchase in transactions:
    uid = purchase.user_id

    if uid not in users:
        users[uid] = User(user_id=uid, transactions=[])
    users[uid].transactions.append(purchase)
