-- Converts database `hbtn_0c_0` to UTF8.
-- Converts the `first_table` table to utf8mb4.
-- Converts the field `name` in `first_table` to utf8mb4.
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

ALTER TABLE hbtn_0c_0.first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

ALTER TABLE hbtn_0c_0.first_table MODIFY COLUMN name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
