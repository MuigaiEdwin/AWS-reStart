
-- ========================================================
-- OBJECTIVES
-- ========================================================
-- 1. Use aggregate functions: SUM(), MIN(), MAX(), AVG()
-- 2. Use SUBSTRING_INDEX() to split strings
-- 3. Use LENGTH() and TRIM() for string length
-- 4. Use DISTINCT() to filter duplicates
-- 5. Use functions in SELECT and WHERE clauses
-- ========================================================

-- --------------------------------------------------------
-- Connection Setup (Terminal Commands - Not SQL)
-- --------------------------------------------------------
-- sudo su
-- cd /home/ec2-user/
-- mysql -u root -p

-- --------------------------------------------------------
-- TASK 2: Query the World Database
-- --------------------------------------------------------

-- Show existing databases
SHOW DATABASES;

-- Review table schema and data
SELECT * FROM world.country;

-- --------------------------------------------------------
-- Aggregate Functions
-- --------------------------------------------------------

-- Use SUM(), AVG(), MAX(), MIN(), COUNT() to summarize population data
SELECT 
    SUM(Population) AS "Total Population",
    AVG(Population) AS "Average Population",
    MAX(Population) AS "Maximum Population",
    MIN(Population) AS "Minimum Population",
    COUNT(Population) AS "Count of Countries"
FROM world.country;

-- --------------------------------------------------------
-- String Manipulation: SUBSTRING_INDEX()
-- --------------------------------------------------------

-- Split region name at first space
-- SUBSTRING_INDEX(string, delimiter, position)
SELECT Region, SUBSTRING_INDEX(Region, " ", 1) AS "First Word"
FROM world.country;

-- Use SUBSTRING_INDEX() in WHERE clause
-- Find countries in regions starting with "Southern"
SELECT Name, Region 
FROM world.country 
WHERE SUBSTRING_INDEX(Region, " ", 1) = "Southern";

-- --------------------------------------------------------
-- String Length: LENGTH() and TRIM()
-- --------------------------------------------------------

-- Find regions with fewer than 10 characters
-- TRIM() removes leading/trailing spaces
-- LENGTH() counts remaining characters
SELECT Region 
FROM world.country 
WHERE LENGTH(TRIM(Region)) < 10;

-- --------------------------------------------------------
-- Removing Duplicates: DISTINCT()
-- --------------------------------------------------------

-- Same query as above but without duplicate regions
SELECT DISTINCT(Region) 
FROM world.country 
WHERE LENGTH(TRIM(Region)) < 10;

-- --------------------------------------------------------
-- CHALLENGE: Split Micronesian/Caribbean Region
-- --------------------------------------------------------

-- Split region name into two columns at "/" delimiter
SELECT 
    Name, 
    SUBSTRING_INDEX(Region, "/", 1) AS "Region Name 1",
    SUBSTRING_INDEX(Region, "/", -1) AS "Region Name 2" 
FROM world.country 
WHERE Region = "Micronesia/Caribbean";

-- --------------------------------------------------------
-- ADDITIONAL PRACTICE QUERIES
-- --------------------------------------------------------

-- Find country with longest name
SELECT Name, LENGTH(Name) AS "Name Length"
FROM world.country
ORDER BY LENGTH(Name) DESC
LIMIT 1;

-- Count distinct continents
SELECT COUNT(DISTINCT(Continent)) AS "Number of Continents"
FROM world.country;

-- Average surface area by continent
SELECT 
    Continent,
    AVG(SurfaceArea) AS "Avg Surface Area",
    COUNT(*) AS "Number of Countries"
FROM world.country
GROUP BY Continent
ORDER BY AVG(SurfaceArea) DESC;

-- Find countries with single-word names
SELECT Name, Region
FROM world.country
WHERE Name NOT LIKE "% %"
ORDER BY Name;

-- Countries with names containing exactly 5 characters
SELECT Name, Region
FROM world.country
WHERE LENGTH(Name) = 5
ORDER BY Name;

-- Total GNP by continent (excluding NULL values)
SELECT 
    Continent,
    SUM(GNP) AS "Total GNP",
    AVG(GNP) AS "Average GNP",
    MAX(GNP) AS "Highest GNP",
    MIN(GNP) AS "Lowest GNP"
FROM world.country
WHERE GNP IS NOT NULL
GROUP BY Continent
ORDER BY SUM(GNP) DESC;

-- Extract government form before comma
SELECT 
    Name,
    GovernmentForm,
    SUBSTRING_INDEX(GovernmentForm, ",", 1) AS "Gov Type"
FROM world.country
WHERE GovernmentForm LIKE "%,%"
LIMIT 10;

-- Count countries by first letter of name
SELECT 
    SUBSTRING(Name, 1, 1) AS "First Letter",
    COUNT(*) AS "Number of Countries"
FROM world.country
GROUP BY SUBSTRING(Name, 1, 1)
ORDER BY COUNT(*) DESC;

-- Find regions with longest names
SELECT DISTINCT(Region), LENGTH(Region) AS "Region Name Length"
FROM world.country
ORDER BY LENGTH(Region) DESC
LIMIT 10;

-- Population density (Population / SurfaceArea)
SELECT 
    Name,
    Population,
    SurfaceArea,
    ROUND(Population / SurfaceArea, 2) AS "Population Density"
FROM world.country
WHERE SurfaceArea > 0
ORDER BY (Population / SurfaceArea) DESC
LIMIT 10;


-- ========================================================
-- KEY FUNCTIONS SUMMARY
-- ========================================================
-- AGGREGATE FUNCTIONS:
--   SUM(): Calculates total of numeric values
--   AVG(): Calculates average of numeric values
--   MAX(): Finds maximum value
--   MIN(): Finds minimum value
--   COUNT(): Counts number of rows
--
-- STRING FUNCTIONS:
--   SUBSTRING_INDEX(str, delim, count): Splits string
--     Positive count: returns substring before delimiter
--     Negative count: returns substring after delimiter
--   LENGTH(str): Returns character count
--   TRIM(str): Removes leading/trailing spaces
--   SUBSTRING(str, start, length): Extracts substring
--   UPPER(str): Converts to uppercase
--   LOWER(str): Converts to lowercase
--
-- OTHER FUNCTIONS:
--   DISTINCT(): Removes duplicate rows
--   ROUND(number, decimals): Rounds numeric value
--   CONCAT(str1, str2, ...): Combines strings
-- ========================================================