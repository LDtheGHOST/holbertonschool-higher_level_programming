-- a script creates the user and gives privileges --
CREATE USER IF NOT EXISTS "user_0d_1" @ "localhost" IDENTIFIED BY "user_0d_1_pwd";
GRANT ALL PRIVILEGES ON *.* TO "user_0d_1" @ "locahost" WITH GRANT OPTION;
FLUSH PRIVILEGES;

-- creates user user_0d_1
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;