import sys

import cx_Oracle


def test_oracle(url, username, password, p_name, p_value):
    connection = cx_Oracle.connect(username, password, url)
    print('Oracle DB version is {0}.'.format(connection.version))
    cursor = connection.cursor()
    cursor.execute("select param_name, param_value from SMRTTRG.config_param where param_name like '%url'")
    result_set = cursor.fetchall()
    for row in result_set:
        print('param_name = {0}, param_value = {1}'.format(row[0], row[1]))
    cursor.close()
    connection.close()
    print('Trying to insert param name "{0}" with param value "{1}".'.format(p_name, p_value))


if __name__ == '__main__':
    args = sys.argv
    if args is None or len(args) < 6:
        print(
            'Usage: python3 oracle_trial.py <ORACLE_DB_URL> <ORACLE_DB_USERNAME> <ORACLE_DB_PASSWORD> <PARAM_NAME> <PARAM_VALUE>')
    else:
        db_url = args[1]
        db_user = args[2]
        db_pass = args[3]
        param_name = args[4]
        param_value = args[5]
        test_oracle(db_url, db_user, db_pass, param_name, param_value)
