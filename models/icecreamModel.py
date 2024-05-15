from database_config import dataBase

# Convert icecreaminventory record tuple to dict
def icecream_invetory_object(databaseResultTuple):
    icecream_invetory = {
        "id": databaseResultTuple[0],
        "brand_id": databaseResultTuple[1],
        "Flavor": databaseResultTuple[2],
        "Quantity": databaseResultTuple[3],
        "Status": databaseResultTuple[4],
        "Created Date": str(databaseResultTuple[5]),
        "Updated Date": str(databaseResultTuple[6])
    }
    return icecream_invetory


# Find icecreaminventory item by id
def find_icecream_invetor_by_id(id):
    cursorObject = dataBase.cursor()
    cursorObject.execute("SELECT * FROM icecreaminventory WHERE id = %s", (id,))
    data = cursorObject.fetchone()
    return data


# Find icecreambrand item by brand name
def find_icecream_brand(brand):
    cursorObject = dataBase.cursor()
    cursorObject.execute("SELECT id FROM icecreambrands WHERE Brand = %s", (brand,))
    data = cursorObject.fetchone()
    return data


# Check whether icecreaminvetory item already exist or not
def check_already_exist(brand_id,flavor):
    cursorObject = dataBase.cursor()
    cursorObject.execute("SELECT * FROM icecreaminventory WHERE Brand_id = %s and Flavor = %s", (brand_id,flavor))
    data = cursorObject.fetchone()
    if data!=None and len(data) == 0:
        raise Exception("Icecream Already Exists")


def create(data):
    cursorObject = dataBase.cursor()
    brand = data['Brand']
   
    # Check if the brand exists in the icecreambrand table
    myResult = find_icecream_brand(brand)

    brand_id = None

    if len(myResult) == 0:
        # If brand doesn't exist, insert it into icecreambrand table
        sql = "INSERT INTO icecreambrands (Brand) VALUES (%s)"
        val = (brand,)
        cursorObject.execute(sql, val)
        dataBase.commit()  # Commit the transaction

        # Get the newly inserted brand_id
        brand_id = cursorObject.lastrowid
    else:
        brand_id = myResult[0]

    try:
        check_already_exist(brand_id,data['Flavor'])
    except Exception as e:
        raise e

    # Insert data into icecreaminventory table
    sql = "INSERT INTO icecreaminventory (Brand_id, Flavor, Quantity, Status) VALUES (%s, %s, %s, %s)"
    val = (brand_id, data['Flavor'], data['Quantity'], data['Status'])
    cursorObject.execute(sql, val)
    dataBase.commit()  # Commit the transaction

    # Return the inserted data
    result = find_icecream_invetor_by_id(cursorObject.lastrowid)
    print(result)

    cursorObject.close()
    
    return icecream_invetory_object(result)

def update(data):

    cursorObject = dataBase.cursor()

    # Update the quantity
    sql = "UPDATE icecreaminventory SET Quantity = %s WHERE id = %s"
    val = (data['Quantity'], data['id'])
    cursorObject.execute(sql, val)

    dataBase.commit()

    # Retrieve the updated data
    updated_data = find_icecream_invetor_by_id(data['id'])
    
    cursorObject.close()  # Ensure cursor is closed

    return icecream_invetory_object(updated_data)
   

def delete(id):
    cursorObject = dataBase.cursor()

    #set item quantity as NULL
    sql = "UPDATE icecreaminventory SET Quantity = NULL WHERE id = %s"

    cursorObject.execute(sql, (id,))
    dataBase.commit()
    cursorObject.close()


def availability(data):
    cursorObject = dataBase.cursor()

    # Check availability based on brand and flavor
    sql = "SELECT *\
          FROM icecreaminventory \
          WHERE Brand_id = (SELECT id FROM icecreambrands WHERE Brand = %s) \
          AND Flavor = %s"
    
    val = (data['Brand'], data['Flavor'])

    cursorObject.execute(sql, val)
    result = cursorObject.fetchone()
    cursorObject.close()
    
    return icecream_invetory_object(result)