DROP TABLE IF EXISTS GoalReached;
DROP TABLE IF EXISTS Game;
DROP TABLE IF EXISTS Airport;
DROP TABLE IF EXISTS Goal;


CREATE TABLE Game (
  id varchar(40),
  co2_consumed int(8),
  co2_budget int(8),
  location varchar(10),
  screen_name varchar(40),
  PRIMARY KEY (id)
);


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

CREATE TABLE Goal (
	id INTEGER,
	name VARCHAR(40),
	description VARCHAR(200),
	icon VARCHAR(8),
	target VARCHAR(40),
	target_minvalue DECIMAL(8,2),
	target_maxvalue DECIMAL(8,2),
	target_text VARCHAR(40),
	PRIMARY KEY (id)
);

INSERT INTO Goal VALUES 
(1, "HOT", "Temperature over +25C", "01d", "TEMP", 25, 9999, NULL),
(2, "COLD", "Temperature under -20C", "13d", "TEMP", -9999, -20, NULL),
(3, "0DEG", "Temperature exactly 0C", "04d", "TEMP", -0.5, 0.5, NULL),
(4, "10DEG", "Temperature exactly +10C", "04d", "TEMP", 9.5, 10.5, NULL),
(5, "20DEG", "Temperature exactly +20C", "04d", "TEMP", 19.5, 20.5, NULL),
(6, "CLEAR", "Clear skies", "01d", "WEATHER", NULL, NULL, "Clear"),
(7, "CLOUDS", "Cloudy", "04d", "WEATHER", NULL, NULL, "Clouds"),
(8, "WINDY", "Wind blows more than 10 m/s", "04d", "WIND", 10.0, 9999, NULL)
;

CREATE TABLE GoalReached (
	gameid VARCHAR(40),
	goalid INTEGER,
	PRIMARY KEY (gameid, goalid),
	FOREIGN KEY (gameid) REFERENCES Game(id),
	FOREIGN KEY (goalid) REFERENCES Goal(id)
);
