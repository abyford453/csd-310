import sys
import mysql.connector


def connect_database():
    return mysql.connector.connect(
        host="localhost",
        user="outland_user",
        password="Outland123!",
        database="outland_adventures"
    )


def print_table(headers, rows):
    rows_as_strings = [
        [str(value) for value in row]
        for row in rows
    ]

    widths = []

    for index, header in enumerate(headers):
        values = [len(str(header))]

        for row in rows_as_strings:
            values.append(len(row[index]))

        widths.append(max(values))

    header_line = " | ".join(
        str(header).ljust(widths[index])
        for index, header in enumerate(headers)
    )

    separator = "-+-".join(
        "-" * width
        for width in widths
    )

    print(header_line)
    print(separator)

    for row in rows_as_strings:
        print(
            " | ".join(
                row[index].ljust(widths[index])
                for index in range(len(headers))
            )
        )


def report_one(cursor):
    print()
    print("=" * 70)
    print("REPORT 1: EQUIPMENT PURCHASES VS. RENTALS")
    print("=" * 70)

    print(
        "Purpose: Compare customer equipment purchases and rentals to help "
        "determine whether Outland Adventures should continue equipment sales."
    )
    print()

    query = """
        SELECT
            TransactionType,
            COUNT(*) AS TotalTransactions
        FROM equipment_transaction
        GROUP BY TransactionType
        ORDER BY TransactionType;
    """

    cursor.execute(query)
    rows = cursor.fetchall()

    print_table(
        ["Transaction Type", "Total Transactions"],
        rows
    )


def report_two(cursor):
    print()
    print("=" * 70)
    print("REPORT 2: BOOKING TRENDS BY REGION")
    print("=" * 70)

    print(
        "Purpose: Compare monthly trip bookings in Africa, Asia, and "
        "Southern Europe to identify changes in booking activity over time."
    )
    print()

    query = """
        SELECT
            l.Region,
            DATE_FORMAT(b.BookingDate, '%Y-%m') AS BookingMonth,
            COUNT(*) AS TotalBookings
        FROM booking b
        INNER JOIN trip t
            ON b.TripID = t.TripID
        INNER JOIN location l
            ON t.LocationID = l.LocationID
        WHERE b.BookingDate >= '2025-11-01'
          AND b.BookingDate < '2026-02-01'
        GROUP BY
            l.Region,
            DATE_FORMAT(b.BookingDate, '%Y-%m')
        ORDER BY
            l.Region,
            BookingMonth;
    """

    cursor.execute(query)
    rows = cursor.fetchall()

    print_table(
        ["Region", "Month", "Total Bookings"],
        rows
    )


def report_three(cursor):
    print()
    print("=" * 70)
    print("REPORT 3: EQUIPMENT MORE THAN FIVE YEARS OLD")
    print("=" * 70)

    print(
        "Purpose: Identify aging inventory that may require inspection, "
        "replacement, or retirement."
    )
    print()

    query = """
        SELECT
            EquipmentID,
            EquipmentName,
            EquipmentType,
            PurchaseDate,
            TIMESTAMPDIFF(YEAR, PurchaseDate, CURDATE()) AS EquipmentAge
        FROM equipment
        WHERE PurchaseDate < DATE_SUB(CURDATE(), INTERVAL 5 YEAR)
        ORDER BY PurchaseDate;
    """

    cursor.execute(query)
    rows = cursor.fetchall()

    print_table(
        [
            "Equipment ID",
            "Equipment Name",
            "Type",
            "Purchase Date",
            "Age"
        ],
        rows
    )


def main():
    database = connect_database()
    cursor = database.cursor()

    try:
        if len(sys.argv) == 1:
            report_one(cursor)
            report_two(cursor)
            report_three(cursor)

        elif sys.argv[1] == "1":
            report_one(cursor)

        elif sys.argv[1] == "2":
            report_two(cursor)

        elif sys.argv[1] == "3":
            report_three(cursor)

        else:
            print("Usage:")
            print("python3 outland_reports.py")
            print("python3 outland_reports.py 1")
            print("python3 outland_reports.py 2")
            print("python3 outland_reports.py 3")

    finally:
        cursor.close()
        database.close()


if __name__ == "__main__":
    main()
