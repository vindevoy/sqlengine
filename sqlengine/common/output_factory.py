import pandas
from tabulate import tabulate

from sqlengine.common.base import Base


class OutputFactory:
    """
    The engine factory has only one purpose: pretty print records in a tabular format.

    :version: 1.0.0
    :date: 2024-06-04
    :author: Yves Vindevogel <yves@vindevogel.net>
    """

    @classmethod
    def pretty_print(cls, data: list[Base]):
        """
        Print the records in a tabular format, "id" first, without any index indication.

        :version: 1.0.0
        :date: 2024-06-04
        :author: Yves Vindevogel <yves@vindevogel.net>
        """

        if len(data) == 0:
            print("\nNo data")

        ###
        # re-order the columns so that "id" is always the first.  Due to the inheritance of the base class,
        # the "id" appears always as last column instead of the first.  That is not a problem in the class,
        # but it looks a bit awkward.  This solves it.
        columns = ["id"]
        columns.extend(key for key in data[0].__table__.columns.keys() if key != "id")
        ###

        ###
        # convert to a dataframe for this tabulate module.  However, when you take the __dict__,
        # it also contains the object state in the fields.  Fortunately, this field begins with an underscore.
        # We filter out the fields with an underscore.
        df = pandas.DataFrame([row.__dict__ for row in data])
        df = df.loc[:, ~df.columns.str.startswith('_')]
        ###

        ###
        # re-order the columns in the dataframe according to our column order
        df = df[columns]
        ###

        print("\n")  # This is for pytest.  If this is the first output, you need an extra line in pytest.
        print(tabulate(df, headers=columns, showindex="never", tablefmt="fancy_outline"))
