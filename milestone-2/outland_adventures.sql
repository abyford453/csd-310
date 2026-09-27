CREATE DATABASE IF NOT EXISTS outland_adventures;
USE outland_adventures;

DROP TABLE IF EXISTS equipment_transaction;
DROP TABLE IF EXISTS booking;
DROP TABLE IF EXISTS equipment;
DROP TABLE IF EXISTS trip;
DROP TABLE IF EXISTS customer;
DROP TABLE IF EXISTS location;

CREATE TABLE customer (
    CustomerID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Phone VARCHAR(20),
    Email VARCHAR(100)
);

CREATE TABLE location (
    LocationID INT PRIMARY KEY,
    LocationName VARCHAR(100),
    Region VARCHAR(100)
);

CREATE TABLE trip (
    TripID INT PRIMARY KEY,
    TripName VARCHAR(100),
    LocationID INT,
    StartDate DATE,
    EndDate DATE,
    TripPrice DECIMAL(10,2),
    FOREIGN KEY (LocationID) REFERENCES location(LocationID)
);

CREATE TABLE booking (
    BookingID INT PRIMARY KEY,
    CustomerID INT,
    TripID INT,
    BookingDate DATE,
    FOREIGN KEY (CustomerID) REFERENCES customer(CustomerID),
    FOREIGN KEY (TripID) REFERENCES trip(TripID)
);

CREATE TABLE equipment (
    EquipmentID INT PRIMARY KEY,
    EquipmentName VARCHAR(100),
    EquipmentType VARCHAR(50),
    PurchaseDate DATE,
    InventoryStatus VARCHAR(50)
);

CREATE TABLE equipment_transaction (
    TransactionID INT PRIMARY KEY,
    CustomerID INT,
    EquipmentID INT,
    TransactionDate DATE,
    TransactionType VARCHAR(50),
    FOREIGN KEY (CustomerID) REFERENCES customer(CustomerID),
    FOREIGN KEY (EquipmentID) REFERENCES equipment(EquipmentID)
);

INSERT INTO customer
(CustomerID, FirstName, LastName, Phone, Email)
VALUES
(1, 'John', 'Miller', '555-0101', 'john.miller@example.com'),
(2, 'Sarah', 'Davis', '555-0102', 'sarah.davis@example.com'),
(3, 'Michael', 'Brown', '555-0103', 'michael.brown@example.com'),
(4, 'Emily', 'Wilson', '555-0104', 'emily.wilson@example.com'),
(5, 'David', 'Taylor', '555-0105', 'david.taylor@example.com'),
(6, 'Jessica', 'Moore', '555-0106', 'jessica.moore@example.com');

INSERT INTO location
(LocationID, LocationName, Region)
VALUES
(1, 'Kenya', 'Africa'),
(2, 'Tanzania', 'Africa'),
(3, 'Nepal', 'Asia'),
(4, 'Japan', 'Asia'),
(5, 'Italy', 'Southern Europe'),
(6, 'Greece', 'Southern Europe');

INSERT INTO trip
(TripID, TripName, LocationID, StartDate, EndDate, TripPrice)
VALUES
(1, 'Kenya Safari Trek', 1, '2026-01-10', '2026-01-18', 3200.00),
(2, 'Tanzania Mountain Adventure', 2, '2026-02-05', '2026-02-14', 3500.00),
(3, 'Nepal Himalayan Trek', 3, '2026-03-12', '2026-03-22', 4100.00),
(4, 'Japan Mountain Trail', 4, '2026-04-08', '2026-04-15', 3000.00),
(5, 'Italian Alps Adventure', 5, '2026-05-03', '2026-05-11', 2900.00),
(6, 'Greek Mountain Trek', 6, '2026-06-14', '2026-06-21', 2700.00);

INSERT INTO booking
(BookingID, CustomerID, TripID, BookingDate)
VALUES
(1, 1, 1, '2025-10-01'),
(2, 2, 2, '2025-10-05'),
(3, 3, 3, '2025-10-10'),
(4, 4, 4, '2025-10-15'),
(5, 5, 5, '2025-10-20'),
(6, 6, 6, '2025-10-25');

INSERT INTO equipment
(EquipmentID, EquipmentName, EquipmentType, PurchaseDate, InventoryStatus)
VALUES
(1, 'Backpack', 'Camping', '2018-04-15', 'Available'),
(2, 'Tent', 'Camping', '2019-06-20', 'Available'),
(3, 'Sleeping Bag', 'Camping', '2020-08-10', 'Rented'),
(4, 'Hiking Boots', 'Hiking', '2022-03-05', 'Available'),
(5, 'Trekking Poles', 'Hiking', '2023-07-12', 'Available'),
(6, 'Portable Stove', 'Camping', '2024-01-18', 'Rented');

INSERT INTO equipment_transaction
(TransactionID, CustomerID, EquipmentID, TransactionDate, TransactionType)
VALUES
(1, 1, 1, '2026-01-02', 'Rental'),
(2, 2, 2, '2026-01-05', 'Purchase'),
(3, 3, 3, '2026-02-01', 'Rental'),
(4, 4, 4, '2026-02-10', 'Purchase'),
(5, 5, 5, '2026-03-01', 'Rental'),
(6, 6, 6, '2026-03-05', 'Purchase');

SELECT * FROM customer;
SELECT * FROM location;
SELECT * FROM trip;
SELECT * FROM booking;
SELECT * FROM equipment;
SELECT * FROM equipment_transaction;
