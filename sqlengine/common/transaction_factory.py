from sqlengine.common.transaction import Transaction


class TransactionFactory:
    @classmethod
    def get_transaction(cls):
        return Transaction()
