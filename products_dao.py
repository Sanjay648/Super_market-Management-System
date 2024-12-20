from sql_connection import get_sql_connection
def get_all_products(connection):
    cursor=connection.cursor()
    query='select products.product_id,products.product_name,products.uom_id,products.price_per_unit,uom.uom_name from products inner join uom on products.uom_id =uom.uom_id;;'
    cursor.execute(query)

    response=[]
    for (product_id,product_name,uom_id,price_per_unit,uom_name) in cursor:
        response.append(
            {
                'product_id':product_id,
                'product_name':product_name,
                'uom_id':uom_id,
                'price_per_unit':price_per_unit,
                'uom_name':uom_name
            }
        )

    #connection.close()
    connection.commit()
    return response

def insert_new_products(connection,product):
    cursor1=connection.cursor()
    query='insert into products(product_name,uom_id,price_per_unit) values(?,?,?);'
    data=(product["product_name"],product["uom_id"],product["price_per_unit"])
    cursor1.execute(query,data)
    connection.commit()

def delete_product(connection,product_id):
    cursor2=connection.cursor()
    query=('delete from products where product_id=' +str(product_id))
    cursor2.execute(query)
    connection.commit()

if __name__=='__main__':
    connection=get_sql_connection()
    print(delete_product(connection,20))