USE outland_adventures;

-- Additional sample booking records for Milestone #3 reporting.
-- These records provide multiple months of booking activity so
-- regional booking trends can be analyzed.

INSERT IGNORE INTO booking
(BookingID, CustomerID, TripID, BookingDate)
VALUES

-- November 2025
-- Africa: 6 bookings
(7, 1, 1, '2025-11-02'),
(8, 2, 2, '2025-11-05'),
(9, 3, 1, '2025-11-09'),
(10, 4, 2, '2025-11-12'),
(11, 5, 1, '2025-11-18'),
(12, 6, 2, '2025-11-24'),

-- Asia: 3 bookings
(13, 1, 3, '2025-11-04'),
(14, 2, 4, '2025-11-14'),
(15, 3, 3, '2025-11-22'),

-- Southern Europe: 2 bookings
(16, 4, 5, '2025-11-08'),
(17, 5, 6, '2025-11-20'),

-- December 2025
-- Africa: 4 bookings
(18, 1, 1, '2025-12-03'),
(19, 2, 2, '2025-12-08'),
(20, 3, 1, '2025-12-15'),
(21, 4, 2, '2025-12-21'),

-- Asia: 4 bookings
(22, 1, 3, '2025-12-05'),
(23, 2, 4, '2025-12-11'),
(24, 3, 3, '2025-12-17'),
(25, 4, 4, '2025-12-26'),

-- Southern Europe: 3 bookings
(26, 5, 5, '2025-12-06'),
(27, 6, 6, '2025-12-16'),
(28, 1, 5, '2025-12-28'),

-- January 2026
-- Africa: 2 bookings
(29, 2, 1, '2026-01-04'),
(30, 3, 2, '2026-01-19'),

-- Asia: 5 bookings
(31, 1, 3, '2026-01-03'),
(32, 2, 4, '2026-01-08'),
(33, 3, 3, '2026-01-13'),
(34, 4, 4, '2026-01-20'),
(35, 5, 3, '2026-01-27'),

-- Southern Europe: 4 bookings
(36, 1, 5, '2026-01-06'),
(37, 2, 6, '2026-01-12'),
(38, 3, 5, '2026-01-21'),
(39, 4, 6, '2026-01-29');
