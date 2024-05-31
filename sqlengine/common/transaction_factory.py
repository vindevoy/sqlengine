from sqlengine.common.transaction import Transaction


class TransactionFactory:
    """
    The transaction factory has only one purpose: to create a transaction (self defined class, no 3rd party).

    :version: 1.0.0
    :date: 2024-05-31
    :author: Yves Vindevogel <yves@vindevogel.net>
    """

    @classmethod
    def get_transaction(cls):
        """
        Create a transaction (self defined class, no 3rd party).

        :version: 1.0.0
        :date: 2024-05-31
        :author: Yves Vindevogel <yves@vindevogel.net>
        """

        return Transaction()
