from unittest.mock import patch, MagicMock

@patch('mypackage.mymodule.pymysql')
def test(self, mock_sql):
    self.assertIs(mypackage.mymodule.pymysql, mock_sql)

    conn = Mock()
    mock_sql.connect.return_value = conn

    cursor      = MagicMock()
    mock_result = MagicMock()

    cursor.__enter__.return_value = mock_result
    cursor.__exit___              = MagicMock()

    conn.cursor.return_value = cursor

    connectDB()

    mock_sql.connect.assert_called_with(host='localhost',
                                        user='user',
                                        password='passwd',
                                        db='db')

    mock_result.execute.assert_called_with("sql request", ("user", "pass"))
