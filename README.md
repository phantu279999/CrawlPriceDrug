# Crawl Price Drug
### Dự án đơn giản lấy dữ liệu giá của các loại thuốc của các trang


⚡ Cài đặt và chạy dự án

```shell
# Clone repository  
git clone https://github.com/phantu279999/CrawlPriceDrug.git
cd CrawlPriceDrug  

# Tạo và kích hoạt virtual environment  
python -m venv venv  
source venv/bin/activate  # Windows: venv\Scripts\activate  

# Cài đặt dependencies  
pip install -r requirements.txt  

# Chạy migration  
python main.py  

```

Cấu hình lấy dự liệu các trang ở file: config.json


####  Cấu trúc dữ liệu trong MySQL
```mysql
CREATE TABLE Drug(
    drug_id INT PRIMARY KEY AUTO_INCREMENT,
    declaration_date DATETIME NULL,
    status VARCHAR(255) NULL,
    petition VARCHAR(255) NULL,
    name VARCHAR(255) NOT NULL UNIQUE,
    hc_name VARCHAR(255) NULL, # Tên hoạt chất
    nd_hl VARCHAR(255) NULL,  
    gplh_gpnk VARCHAR(255) NULL,
    dosage_form VARCHAR(255) NULL,
    packaging_specifications VARCHAR(255) NULL,
    DVT VARCHAR(50) NULL,
    price VARCHAR(20) NULL,
    url VARCHAR(200) NULL,
    INDEX idx_drug_name (name)
);

```

Example
![](https://raw.githubusercontent.com/phantu279999/CrawlPriceDrug/refs/heads/master/example/example_data_sql.png)



#### Cấu trúc dữ liệu trong Redis

##### String Key
key = "drug name"
value = "string json"

##### Hash Key
Drug
field = "drug name"
value = "string json"

Example
![](https://raw.githubusercontent.com/phantu279999/CrawlPriceDrug/refs/heads/master/example/example_data.png)


### Cấu trúc luồng dữ liệu của dự án: Data pipeline

```
[Extract data] -> [Transform data] -> [Load data]
```