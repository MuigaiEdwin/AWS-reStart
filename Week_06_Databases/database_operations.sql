
-- OBJECTIVES
-- ========================================================
-- 1. Use the CREATE statement to create databases and tables
-- 2. Use the SHOW statement to view databases and tables
-- 3. Use the ALTER statement to alter the structure of a table
-- 4. Use the DROP statement to delete databases and tables
-- ========================================================

-- --------------------------------------------------------
-- TASK 1: Connect to Database
-- --------------------------------------------------------
-- Terminal commands used (not SQL):
-- sudo su
-- cd /home/ec2-user/


-- --------------------------------------------------------
-- TASK 2: Create Database and Tables
-- --------------------------------------------------------

-- View existing databases
SHOW DATABASES;

-- Create a new database named 'world'
CREATE DATABASE world;

-- Verify database creation
SHOW DATABASES;

-- Create the 'country' table with schema
CREATE TABLE world.country (
  `Code` CHAR(3) NOT NULL DEFAULT '',
  `Name` CHAR(52) NOT NULL DEFAULT '',
  `Conitinent` ENUM('Asia','Europe','North America','Africa','Oceania','Antarctica','South America') NOT NULL DEFAULT 'Asia',
  `Region` CHAR(26) NOT NULL DEFAULT '',
  `SurfaceArea` FLOAT(10,2) NOT NULL DEFAULT '0.00',
  `IndepYear` SMALLINT(6) DEFAULT NULL,
  `Population` INT(11) NOT NULL DEFAULT '0',
  `LifeExpectancy` FLOAT(3,1) DEFAULT NULL,
  `GNP` FLOAT(10,2) DEFAULT NULL,
  `GNPOld` FLOAT(10,2) DEFAULT NULL,
  `LocalName` CHAR(45) NOT NULL DEFAULT '',
  `GovernmentForm` CHAR(45) NOT NULL DEFAULT '',
  `HeadOfState` CHAR(60) DEFAULT NULL,
  `Capital` INT(11) DEFAULT NULL,
  `Code2` CHAR(2) NOT NULL DEFAULT '',
  PRIMARY KEY (`Code`)
);

-- Switch to world database and view tables
USE world;
SHOW TABLES;

-- View all columns in the country table
SHOW COLUMNS FROM world.country;

-- Fix the misspelled column name 'Conitinent' to 'Continent'
ALTER TABLE world.country RENAME COLUMN Conitinent TO Continent;

-- Verify the column name correction
SHOW COLUMNS FROM world.country;

-- --------------------------------------------------------
-- CHALLENGE 1: Create City Table
-- --------------------------------------------------------
-- Create a table named 'city' with Name and Region columns

CREATE TABLE world.city (
  `Name` CHAR(50) NOT NULL,
  `Region` CHAR(50) NOT NULL
);

-- Verify city table creation
SHOW TABLES;

-- --------------------------------------------------------
-- TASK 3: Delete Database and Tables
-- --------------------------------------------------------

-- Drop the city table
DROP TABLE world.city;

-- --------------------------------------------------------
-- CHALLENGE 2: Drop Country Table
-- --------------------------------------------------------

DROP TABLE world.country;

-- Verify both tables have been dropped
SHOW TABLES;

-- Drop the world database
DROP DATABASE world;

-- Verify the database has been deleted
SHOW DATABASES;

-- ========================================================
-- LAB COMPLETED SUCCESSFULLY
-- ========================================================
-- Skills Demonstrated:
-- ✓ CREATE DATABASE and CREATE TABLE
-- ✓ SHOW DATABASES, SHOW TABLES, SHOW COLUMNS
-- ✓ ALTER TABLE for schema modifications
-- ✓ DROP TABLE and DROP DATABASE
-- ✓ Database schema design with various data types
-- ✓ PRIMARY KEY constraint implementation
-- ========================================================