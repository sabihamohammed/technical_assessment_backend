import sqlite3

def get_popular_skus():
    conn = sqlite3.connect('parts_avatar.db')
    cursor = conn.cursor()
    
    # Task: Return SKUs where the SUM of quantity across all orders is > 1.
    query = SELECT sku
    FROM  order_items
    GROUP by get_popular_skus
    HAVING SUM(quantity)>1
    
    cursor.execute(query)
    return cursor.fetchall()
