-- Lists all records of the table `second_table`.
-- Rows without a name value are not listed.
SELECT * FROM second_table
    WHERE name IS NOT NULL AND name != ''
    ORDER BY score DESC;
