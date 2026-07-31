CREATE DATABASE IF NOT EXISTS calculator;


USE calculator;


CREATE TABLE IF NOT EXISTS history (

    id INT AUTO_INCREMENT PRIMARY KEY,

    num1 FLOAT NOT NULL,

    num2 FLOAT NOT NULL,

    operation VARCHAR(20) NOT NULL,

    result FLOAT NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);



INSERT INTO history
(num1,num2,operation,result)

VALUES

(10,5,'add',15),

(20,4,'mul',80);
