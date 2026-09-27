import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="outland_user",
    password="Outland123!",
    database="outland_adventures"
)

cursor = db.cursor()

tables = [
    "customer",
    "location",
    "trip",
    "booking",
    "equipment",
    "equipment_transaction"
]

for table in tables:
    print("\n" + "=" * 80)
    print(f"{table.upper()} TABLE")
    print("=" * 80)

    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

cursor.close()
db.close()
