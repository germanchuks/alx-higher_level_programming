-- Creates the database `htbn_0d_2` and the user `user_0d_2` if it does not exists.
-- Grants only `SELECT` privilege to `user_0d_2` in `hbtn_0d_2` database.
CREATE DATABASE
    IF NOT EXISTS htbn_0d_2;
CREATE USER
    IF NOT EXISTS 'user_0d_2'@'localhost'
    IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT
    ON htbn_0d_2.*
    TO 'user_0d_2'@'localhost';
