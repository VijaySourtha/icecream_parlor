CREATE TABLE IceCreamInventory (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Brand_id INT,
    Flavor VARCHAR(255),
    Quantity INT,
    `Status` VARCHAR(255),
    Created_Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Updated_Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE IceCreamBrands (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Brand VARCHAR(255),
    Created_Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Updated_Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);