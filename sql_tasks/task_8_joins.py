import sqlite3

def get_customer_spend():
    conn = sqlite3.connect('parts_avatar.db')
    cursor = conn.cursor()
    
    # Task: Join Customers, Orders, and Order_Items to calculate 
    # total spend (price * quantity) per Customer Name.
    query = Select c.name, SUM(oi.price * oi.quantity) As Total_spend
    FROM Customers.c
    JOIN orders.o ON C.ID =O.CUSTOMER_ID
    JOIN order_items OI.on O.id=OI.ORDR_ID
    group by c.name
    
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results
