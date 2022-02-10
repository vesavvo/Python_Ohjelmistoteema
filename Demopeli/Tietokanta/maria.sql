DROP TABLE IF EXISTS Airport;

CREATE TABLE Airport(
id VARCHAR(40),
ident VARCHAR(40),
type VARCHAR(40),
name VARCHAR(200),
latitude_deg DECIMAL(20,14),
longitude_deg DECIMAL(20,14),
elevation_ft DECIMAL(8,2),
continent VARCHAR(40),
iso_country VARCHAR(40),
iso_region VARCHAR(40),
municipality VARCHAR(200),
scheduled_service VARCHAR(40),
gps_code VARCHAR(40),
iata_code VARCHAR(40),
local_code VARCHAR(40),
home_link VARCHAR(1000),
wikipedia_link VARCHAR(1000),
keywords VARCHAR(1000),
PRIMARY KEY (ident)
) CHARACTER SET 'utf8'; 


LOAD DATA LOCAL INFILE "C:\\Users\\olliv\\Documents\\airports\\airports.csv"
INTO TABLE Airport
CHARACTER SET 'utf8'
FIELDS TERMINATED BY "," ENCLOSED BY '"';
