"""
Prerequisites:
  libmyodbc
  unixodbc-bin
  unixodbc-dev

  sudo apt-get install libmyodbc unixodbc-bin unixodbc-dev
"""

import pyodbc
import logging
import time


logger = logging.getLogger('dbtools')
retry_timeout = 30


class DatabaseConnection(object):
    """
    Context manager for odbc database connections.

    Usage:
        with DatabaseConnection('DSN=example_dsn;') as cursor:
            try:
                cursor.execute(query)
            except:
                raise
            else:
                cursor.commit()
    """

    def __init__(self, connection_string, autocommit=False, ansi=False, timeout=0, **kwargs):
        self.database = pyodbc.connect(connection_string, autocommit=autocommit, ansi=ansi, timeout=timeout, **kwargs)
        self.cursor = self.database.cursor()

    def close(self):
        self.cursor.close()
        self.database.close()

    def __enter__(self):
        """
        :rtype: pyodbc.Cursor
        :return:
        """
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        return not bool(exc_type)


def retry_on_lock(f):
    """
    Continue to retry transaction while "lock" is in the error message.

    This should include deadlocks and lock wait timeouts.

    Usage:

        @retry_on_lock
        def insert_data(data_tuple):
            query = "INSERT INTO example VALUES (?, ?, ?);"
            with DatabaseConnection('DSN=example_dsn;') as cursor:
                cursor.execute(query, data_tuple)
                cursor.commit()

    :param f: function to wrap
    :return:
    """
    def inner(*args, **kwargs):
        for i in range(5):
            try:
                return f(*args, **kwargs)
            except pyodbc.Error as e1:
                logger.error(e1)
                if 'lock' in e1.args[1].lower():
                    time.sleep(retry_timeout)
                    continue
                raise
        else:
            raise Exception('max retries exceeded when attempting to write to database.')
    return inner
