

-- ========================================================
-- OBJECTIVES
-- ========================================================
-- 1. Write search conditions using WHERE clause
-- 2. Use the BETWEEN operator
-- 3. Use the LIKE operator with wildcard characters
-- 4. Use the AS operator for column aliases
-- 5. Use functions in SELECT and WHERE clauses
-- ========================================================

-- --------------------------------------------------------
-- Connection Setup (Terminal Commands - Not SQL)
-- --------------------------------------------------------
-- sudo su
-- cd /home/ec2-user/
-- mysql -u root -p "password name"

-- --------------------------------------------------------
-- TASK 2: Query the World Database
-- --------------------------------------------------------

-- Show existing databases
SHOW DATABASES;

-- Review table schema and data
SELECT * FROM world.country;

-- --------------------------------------------------------
-- Using WHERE with AND Operator
-- --------------------------------------------------------

-- Query countries with population between 50M and 100M
-- Using >= and <= operators
SELECT Name, Capital, Region, SurfaceArea, Population 
FROM world.country 
WHERE Population >= 50000000 AND Population <= 100000000;

-- --------------------------------------------------------
-- Using BETWEEN Operator
-- --------------------------------------------------------

-- Same query as above, but using BETWEEN (more readable)
-- BETWEEN is inclusive (includes start and end values)
SELECT Name, Capital, Region, SurfaceArea, Population 
FROM world.country 
WHERE Population BETWEEN 50000000 AND 100000000;

-- --------------------------------------------------------
-- Using LIKE with Wildcard Characters
-- --------------------------------------------------------

-- Sum population of all European countries
-- % is a wildcard representing any number of characters
SELECT SUM(Population) 
FROM world.country 
WHERE Region LIKE "%Europe%";

-- --------------------------------------------------------
-- Using AS for Column Aliases
-- --------------------------------------------------------

-- Same query with user-friendly column alias
SELECT SUM(Population) AS "Europe Population Total" 
FROM world.country 
WHERE Region LIKE "%Europe%";

-- --------------------------------------------------------
-- Using Functions in WHERE Clause
-- --------------------------------------------------------

-- Case-insensitive search using LOWER function
-- Converts Region to lowercase before comparison
SELECT Name, Capital, Region, SurfaceArea, Population 
FROM world.country 
WHERE LOWER(Region) LIKE "%central%";

-- --------------------------------------------------------
-- CHALLENGE: North America Statistics
-- --------------------------------------------------------

-- Calculate sum of surface area and population for North America
SELECT 
    SUM(SurfaceArea) AS "N. America Surface Area", 
    SUM(Population) AS "N. America Population" 
FROM world.country 
WHERE Region = "North America";

-- --------------------------------------------------------
-- ADDITIONAL PRACTICE QUERIES
-- --------------------------------------------------------

-- Find countries with names starting with 'A'
SELECT Name, Region, Population 
FROM world.country 
WHERE Name LIKE "A%"
ORDER BY Name;

-- Find countries with names ending with 'land'
SELECT Name, Region, Population 
FROM world.country 
WHERE Name LIKE "%land"
ORDER BY Name;

-- Find countries with 'United' in the name
SELECT Name, Region, Population 
FROM world.country 
WHERE Name LIKE "%United%";

-- Count countries in each region containing 'Asia'
SELECT Region, COUNT(*) AS "Number of Countries"
FROM world.country
WHERE Region LIKE "%Asia%"
GROUP BY Region;

-- Average life expectancy in regions containing 'America'
SELECT Region, AVG(LifeExpectancy) AS "Avg Life Expectancy"
FROM world.country
WHERE Region LIKE "%America%" AND LifeExpectancy IS NOT NULL
GROUP BY Region;

-- Countries with independence year between 1900 and 1950
SELECT Name, IndepYear, Region
FROM world.country
WHERE IndepYear BETWEEN 1900 AND 1950
ORDER BY IndepYear;

-- Countries with population between 5M and 10M
SELECT Name, Population, Region
FROM world.country
WHERE Population BETWEEN 5000000 AND 10000000
ORDER BY Population DESC;

-- Sum of GNP for countries in regions containing 'Europe'
SELECT 
    SUM(GNP) AS "Total GNP",
    COUNT(*) AS "Number of Countries"
FROM world.country
WHERE Region LIKE "%Europe%" AND GNP IS NOT NULL;

-- ========================================================

-- ========================================================
-- KEY OPERATORS & FUNCTIONS
-- ========================================================
-- WHERE: Filters rows based on conditions
-- BETWEEN: Range operator (inclusive)
-- LIKE: Pattern matching with wildcards
--   %: Matches any number of characters
--   _: Matches exactly one character
-- AS: Creates column aliases
-- AND: Combines conditions (all must be true)
-- OR: Combines conditions (at least one must be true)
-- LOWER(): Converts string to lowercase
-- UPPER(): Converts string to uppercase
-- SUM(): Calculates total
-- AVG(): Calculates average
-- COUNT(): Counts rows
-- ========================================================