
-- ========================================================
-- OBJECTIVES
-- ========================================================
-- 1. Insert rows into a table
-- 2. Update rows in a table
-- 3. Delete rows from a table
-- 4. Import rows from a database backup file
-- ========================================================

-- --------------------------------------------------------
-- TASK 1: Connect to Database
-- --------------------------------------------------------
-- Terminal commands used (not SQL):
-- sudo su
-- cd /home/ec2-user/


-- View existing databases
SHOW DATABASES;

-- --------------------------------------------------------
-- TASK 2: Insert Data into Table
-- --------------------------------------------------------

-- Verify that the country table exists and view its contents
SELECT * FROM world.country;

-- Insert Ireland record
INSERT INTO world.country VALUES (
  'IRL',
  'Ireland',
  'Europe',
  'British Islands',
  70273.00,
  1921,
  3775100,
  76.8,
  75921.00,
  73132.00,
  'Ireland/Éire',
  'Republic',
  1447,
  'IE'
);

-- Insert Australia record
INSERT INTO world.country VALUES (
  'AUS',
  'Australia',
  'Oceania',
  'Australia and New Zealand',
  7741220.00,
  1901,
  18886000,
  79.8,
  351182.00,
  392911.00,
  'Australia',
  'Constitutional Monarchy, Federation',
  135,
  'AU'
);

-- Verify successful insertion of both records
SELECT * FROM world.country WHERE Code IN ('IRL', 'AUS');

-- --------------------------------------------------------
-- TASK 3: Update Rows in Table
-- --------------------------------------------------------

-- Update Population to 0 for all rows (no WHERE clause = all rows affected)
UPDATE world.country SET Population = 0;

-- Verify the Population column update
SELECT * FROM world.country;

-- Update multiple columns (Population and SurfaceArea) for all rows
UPDATE world.country SET Population = 100, SurfaceArea = 100;

-- Verify both columns were updated
SELECT * FROM world.country;

-- --------------------------------------------------------
-- TASK 4: Delete Rows from Table
-- --------------------------------------------------------

-- Disable foreign key checks to allow deletion
SET FOREIGN_KEY_CHECKS = 0;

-- Delete ALL rows from country table (no WHERE clause = all rows deleted)
DELETE FROM world.country;

-- Verify all rows have been deleted
SELECT * FROM world.country;

-- --------------------------------------------------------
-- TASK 5: Import Data Using SQL File
-- --------------------------------------------------------

-- Exit MySQL terminal
QUIT;

-- Terminal commands used (not SQL):
-- ls /home/ec2-user/world.sql


-- Reconnect to database after import


-- Switch to world database
USE world;

-- Verify all tables were created from the import
SHOW TABLES;

-- Verify data was loaded into country table
SELECT * FROM country;

-- Query other tables to verify successful import
SELECT * FROM city LIMIT 10;
SELECT * FROM countrylanguage LIMIT 10;

-- ========================================================
-- LAB COMPLETED SUCCESSFULLY
-- ========================================================
-- Skills Demonstrated:
-- ✓ INSERT statement for adding rows
-- ✓ UPDATE statement for modifying existing data
-- ✓ DELETE statement for removing rows
-- ✓ SELECT statement for querying data
-- ✓ WHERE clause for filtering results
-- ✓ Setting system variables (FOREIGN_KEY_CHECKS)
-- ✓ Importing data from SQL backup files
-- ✓ Working with multiple related tables
-- ========================================================

-- ========================================================
-- IMPORTANT NOTES
-- ========================================================
-- ⚠️ UPDATE without WHERE clause affects ALL rows
-- ⚠️ DELETE without WHERE clause removes ALL rows
-- ⚠️ These operations may not be reversible - always backup!
-- ⚠️ Use WHERE clauses carefully to target specific rows
-- ========================================================