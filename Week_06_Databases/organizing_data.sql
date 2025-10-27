
-- ========================================================
-- OBJECTIVES
-- ========================================================
-- 1. Use GROUP BY clause with aggregate function SUM()
-- 2. Use OVER clause with RANK() window function
-- 3. Use OVER clause with SUM() and RANK() functions
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
-- Basic Query with ORDER BY
-- --------------------------------------------------------

-- List countries in Australia and New Zealand region
-- Ordered by population in descending order
SELECT Region, Name, Population 
FROM world.country 
WHERE Region = 'Australia and New Zealand' 
ORDER BY Population DESC;

-- --------------------------------------------------------
-- Using GROUP BY with Aggregate Functions
-- --------------------------------------------------------

-- Calculate total population for Australia and New Zealand region
-- GROUP BY groups records together for aggregation
SELECT 
    Region, 
    SUM(Population) AS "Total Population"
FROM world.country 
WHERE Region = 'Australia and New Zealand' 
GROUP BY Region 
ORDER BY SUM(Population) DESC;

-- --------------------------------------------------------
-- Window Functions: OVER Clause with SUM()
-- --------------------------------------------------------

-- Calculate running total of population
-- OVER() creates a window for calculations across rows
-- PARTITION BY divides results into groups
SELECT 
    Region, 
    Name, 
    Population, 
    SUM(Population) OVER(PARTITION BY Region ORDER BY Population) AS 'Running Total'
FROM world.country 
WHERE Region = 'Australia and New Zealand';

-- --------------------------------------------------------
-- Window Functions: OVER Clause with RANK()
-- --------------------------------------------------------

-- Add ranking to running total
-- RANK() assigns position numbers to rows
SELECT 
    Region, 
    Name, 
    Population, 
    SUM(Population) OVER(PARTITION BY Region ORDER BY Population) AS 'Running Total',
    RANK() OVER(PARTITION BY Region ORDER BY Population) AS 'Ranked'
FROM world.country 
WHERE Region = 'Australia and New Zealand';

-- --------------------------------------------------------
-- CHALLENGE: Rank Countries by Population in Each Region
-- --------------------------------------------------------

-- Rank all countries within their regions (largest to smallest)
SELECT 
    Region, 
    Name, 
    Population, 
    RANK() OVER(PARTITION BY Region ORDER BY Population DESC) AS 'Ranked'
FROM world.country 
ORDER BY Region, Ranked;

-- --------------------------------------------------------
-- ADDITIONAL PRACTICE QUERIES
-- --------------------------------------------------------

-- Total population by continent using GROUP BY
SELECT 
    Continent,
    COUNT(*) AS "Number of Countries",
    SUM(Population) AS "Total Population",
    AVG(Population) AS "Average Population"
FROM world.country
GROUP BY Continent
ORDER BY SUM(Population) DESC;

-- Rank countries globally by population
SELECT 
    Name,
    Continent,
    Population,
    RANK() OVER(ORDER BY Population DESC) AS 'Global Rank'
FROM world.country
ORDER BY Population DESC
LIMIT 20;

-- Rank countries within each continent by GNP
SELECT 
    Continent,
    Name,
    GNP,
    RANK() OVER(PARTITION BY Continent ORDER BY GNP DESC) AS 'GNP Rank'
FROM world.country
WHERE GNP IS NOT NULL
ORDER BY Continent, GNP DESC;

-- Running total of surface area by region
SELECT 
    Region,
    Name,
    SurfaceArea,
    SUM(SurfaceArea) OVER(PARTITION BY Region ORDER BY SurfaceArea) AS 'Running Total Area'
FROM world.country
ORDER BY Region, SurfaceArea;

-- Top 3 most populous countries per continent
SELECT 
    Continent,
    Name,
    Population,
    RANK() OVER(PARTITION BY Continent ORDER BY Population DESC) AS 'Rank'
FROM world.country
WHERE RANK() OVER(PARTITION BY Continent ORDER BY Population DESC) <= 3
ORDER BY Continent, Population DESC;

-- Average life expectancy by region with country count
SELECT 
    Region,
    COUNT(*) AS "Countries",
    AVG(LifeExpectancy) AS "Avg Life Expectancy",
    MIN(LifeExpectancy) AS "Min Life Expectancy",
    MAX(LifeExpectancy) AS "Max Life Expectancy"
FROM world.country
WHERE LifeExpectancy IS NOT NULL
GROUP BY Region
ORDER BY AVG(LifeExpectancy) DESC;

-- Percentage of continent population by country
SELECT 
    Continent,
    Name,
    Population,
    SUM(Population) OVER(PARTITION BY Continent) AS 'Continent Total',
    ROUND(Population * 100.0 / SUM(Population) OVER(PARTITION BY Continent), 2) AS 'Percentage'
FROM world.country
ORDER BY Continent, Population DESC;

-- Dense rank vs regular rank (handles ties differently)
SELECT 
    Region,
    Name,
    Population,
    RANK() OVER(PARTITION BY Region ORDER BY Population DESC) AS 'Rank',
    DENSE_RANK() OVER(PARTITION BY Region ORDER BY Population DESC) AS 'Dense Rank'
FROM world.country
WHERE Region = 'Southern Europe'
ORDER BY Population DESC;

-- Row number for each country within continent
SELECT 
    Continent,
    Name,
    Population,
    ROW_NUMBER() OVER(PARTITION BY Continent ORDER BY Population DESC) AS 'Row Number'
FROM world.country
ORDER BY Continent, Population DESC;

-- Compare country population to regional average
SELECT 
    Region,
    Name,
    Population,
    AVG(Population) OVER(PARTITION BY Region) AS 'Regional Avg',
    Population - AVG(Population) OVER(PARTITION BY Region) AS 'Difference from Avg'
FROM world.country
ORDER BY Region, Population DESC;

-- ========================================================
-- LAB COMPLETED SUCCESSFULLY
-- ========================================================
-- Skills Demonstrated:
-- ✓ GROUP BY clause for aggregating data
-- ✓ OVER clause for window functions
-- ✓ PARTITION BY for dividing data into groups
-- ✓ SUM() as aggregate and window function
-- ✓ RANK() window function for ordering
-- ✓ DENSE_RANK() for handling ties
-- ✓ ROW_NUMBER() for sequential numbering
-- ✓ Running totals and cumulative calculations
-- ✓ Percentage calculations within partitions
-- ========================================================

-- ========================================================
-- KEY CONCEPTS
-- ========================================================
-- GROUP BY:
--   - Collapses rows into groups
--   - Used with aggregate functions (SUM, AVG, COUNT, etc.)
--   - Produces one row per group
--   - Example: Total population per continent
--
-- OVER Clause (Window Functions):
--   - Performs calculations across rows
--   - Does NOT collapse rows like GROUP BY
--   - Each row maintains its identity
--   - PARTITION BY divides data into windows
--   - ORDER BY determines calculation order
--
-- Window Functions:
--   RANK(): Assigns rank with gaps for ties (1,2,2,4)
--   DENSE_RANK(): Assigns rank without gaps (1,2,2,3)
--   ROW_NUMBER(): Unique sequential number (1,2,3,4)
--   SUM() OVER(): Running/cumulative totals
--   AVG() OVER(): Moving averages
--
-- When to Use:
--   - Use GROUP BY when you want summary rows
--   - Use OVER when you need detail rows with calculations
-- ========================================================