-- Creates database `htbn_0d_2` and user `user_0d_2`,
-- if they do not exists.
-- Grants `SELECT` privilege to `user_0d_2` in `hbtn_0d_2`.
CREATE DATABASE
    IF NOT EXISTS htbn_0d_2;
CREATE USER
    IF NOT EXISTS 'user_0d_2'@'localhost'
    IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT
    ON htbn_0d_2.*
    TO 'user_0d_2'@'localhost';
