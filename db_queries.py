import mysql.connector as mysql


def check_order_in_db():
    db_orders = mysql.connect(
        host="localhost",
        user="root",
        passwd="",
        database='litecart'
    )
    cursor = db_orders.cursor()

    query = "SELECT * FROM `lc_orders`"
    cursor.execute(query)
    db_orders.close()
    if len(query) > 0:
        return True
    else:
        return False


def check_changed_first_name():
    db_orders = mysql.connect(
        host="localhost",
        user="root",
        passwd="",
        database='litecart'
    )
    cursor = db_orders.cursor()

    query = "SELECT firstname FROM `lc_customers` WHERE ID=4"
    cursor.execute(query)
    list_first_name = cursor.fetchall()
    db_orders.close()
    for item in list_first_name:
        first_name = item[0]
        if first_name == 'Gomer':
            return True
        else:
            return False
