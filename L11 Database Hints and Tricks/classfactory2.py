"""Here are your instructions:

Modify the classFactory.py source code so that the DataRow class returned by the build_row function has another method:

    retrieve(self, curs, condition=None)

self is (as usual) the instance whose method is being called, curs is a database cursor on an existing database
connection, and condition (if present) is a string of condition(s) which must be true of all received rows.

The retrieve method should be a generator, yielding successive rows of the result set until it is completely 
exhausted. Each row should be a next object of type DataRow."""

########################################################################################################################################################################

"""
classFactory: function to return tailored classes
"""

def build_row(table, cols):
    """Build a class that creates instances of specific rows"""
    class DataRow:
        """Generic data row class, specialized by surrounding function"""

        def __init__(self, data):
            """Uses data and column names to inject attributes"""
            assert len(data)==len(self.cols)
            for colname, dat in zip(self.cols, data):
                setattr(self, colname, dat)

        def __repr__(self):
            return "{0}_record({1})".format(self.table,
                     ", ".join(repr(getattr(self, c)) for c in self.cols))

        def retrieve(self, curs, condition=None):
            sWhere = ''
            if condition is not None:
                sWhere = ' WHERE ' + condition

            sqlCommand = 'SELECT {0} FROM {1}{2}'.format(', '.join(self.cols),
                                                         self.table,
                                                         sWhere)
            print (sqlCommand)  # printing the command

            #for row in curs.execute(sqlCommand): #TypeError: 'long' object is not iterable
            curs.execute(sqlCommand)
            for row in curs.fetchall():
                #print DataRow(row) # print check
                yield DataRow(row)

    DataRow.table = table
    DataRow.cols = cols.split()
    DataRow.__name__ += table   # append the table name to the class name
    return DataRow  # The CLASS is returned.

if __name__ == '__main__':
    import mysql.connector
    from database import login_info
    conn = mysql.connector.Connect(**login_info)
    curs = conn.cursor()
    ClassA = build_row('animal', 'id name family weight')
    a = ClassA(['id', 'myName', 'myFamily', 64]) # prints sample object
    print ('The object:', repr(a))
    for obj in a.retrieve(curs, 'weight > 300'):
        print (repr(obj))
