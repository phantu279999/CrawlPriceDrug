CREATE TABLE Drug(
    drug_id INT PRIMARY KEY AUTO_INCREMENT,
    declaration_date DATETIME NULL,
    status VARCHAR(255) NULL,
    petition VARCHAR(255) NULL,
    name VARCHAR(255) NOT NULL UNIQUE,
    hc_name VARCHAR(255) NULL,
    nd_hl VARCHAR(255) NULL,
    gplh_gpnk VARCHAR(255) NULL,
    dosage_form VARCHAR(255) NULL,
    packaging_specifications VARCHAR(255) NULL,
    DVT VARCHAR(50) NULL,
    price VARCHAR(20) NULL,
    url VARCHAR(200) NULL,
    INDEX idx_drug_name (name)
);
