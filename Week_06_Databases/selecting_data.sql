-- ========================================================
-- Week 6 Lab 3: Selecting Data from a Database
-- AWS re/Start Program
-- Student: Edwin Muigai
-- Date: October 2025
-- ========================================================

-- ========================================================
-- OBJECTIVES
-- ========================================================
-- 1. Use the SELECT statement to query a database
-- 2. Use the COUNT() function
-- 3. Use operators: <, >, =, WHERE, ORDER BY, AND
-- ========================================================

-- --------------------------------------------------------
-- TASK 1: Connect to Database
-- --------------------------------------------------------
-- Terminal commands used (not SQL):
-- sudo su
-- cd /home/ec2-user/
-- put the password ***********

-- --------------------------------------------------------
-- TASK 2: Query the World Database
-- --------------------------------------------------------

-- Show existing databases
SHOW DATABASES;

-- List all rows and columns in the country table
SELECT * FROM world.country;

-- Count the number of rows in the country table
SELECT COUNT(*) FROM world.country;

-- List all columns in the country table to understand schema
SHOW COLUMNS FROM world.country;

-- Query specific columns from the country table
SELECT Name, Capital, Region, SurfaceArea, Population 
FROM world.country;

-- Use AS to create user-friendly column names
SELECT Name, Capital, Region, SurfaceArea AS "Surface Area", Population 
FROM world.country;

-- Order results by Population (ascending order)
SELECT Name, Capital, Region, SurfaceArea AS "Surface Area", Population 
FROM world.country 
ORDER BY Population;

-- Order results by Population in descending order
SELECT Name, Capital, Region, SurfaceArea AS "Surface Area", Population 
FROM world.country 
ORDER BY Population DESC;

-- Use WHERE clause to filter results (Population > 50,000,000)
SELECT Name, Capital, Region, SurfaceArea AS "Surface Area", Population 
FROM world.country 
WHERE Population > 50000000 
ORDER BY Population DESC;

-- Use multiple conditions with AND operator
-- Countries with population between 50,000,000 and 100,000,000
SELECT Name, Capital, Region, SurfaceArea AS "Surface Area", Population 
FROM world.country 
WHERE Population > 50000000 AND Population < 100000000 
ORDER BY Population DESC;

-- --------------------------------------------------------
-- CHALLENGE: Southern Europe Query
-- --------------------------------------------------------
-- Question: Which country in Southern Europe has a population greater than 50,000,000?

SELECT Name, Capital, Region, SurfaceArea AS "Surface Area", Population 
FROM world.country 
WHERE Population > 50000000 AND Region = "Southern Europe";

-- --------------------------------------------------------
-- ADDITIONAL PRACTICE QUERIES
-- --------------------------------------------------------

-- Count countries by region
SELECT Region, COUNT(*) AS "Number of Countries"
FROM world.country
GROUP BY Region
ORDER BY COUNT(*) DESC;

-- Find countries with smallest surface area
SELECT Name, SurfaceArea AS "Surface Area"
FROM world.country
ORDER BY SurfaceArea
LIMIT 10;

-- Find countries with highest life expectancy
SELECT Name, LifeExpectancy
FROM world.country
WHERE LifeExpectancy IS NOT NULL
ORDER BY LifeExpectancy DESC
LIMIT 10;

-- Query countries in specific continent
SELECT Name, Region, Population
FROM world.country
WHERE Continent = 'Africa'
ORDER BY Population DESC
LIMIT 10;

-- Find countries with population less than 1 million
SELECT Name, Population
FROM world.country
WHERE Population < 1000000
ORDER BY Population DESC;

-- Query countries that gained independence after 1990
SELECT Name, IndepYear, Region
FROM world.country
WHERE IndepYear > 1990
ORDER BY IndepYear DESC;


