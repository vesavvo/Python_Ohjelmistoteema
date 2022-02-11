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


DROP TABLE IF EXISTS Goal;

CREATE TABLE Goal (
	id INTEGER,
	name VARCHAR(40),
	description VARCHAR(200),
	target VARCHAR(40),
	target_minvalue DECIMAL(8,2),
	target_maxvalue DECIMAL(8,2),
	target_text VARCHAR(40),
	PRIMARY KEY (id)
);

INSERT INTO Goal VALUES 
(1, "HOT", "Temperature over +25C", "TEMP", 25, 9999, NULL),
(2, "COLD", "Temperature under -25C", "TEMP", -9999, -25, NULL),
(3, "0DEG", "Temperature exactly 0C", "TEMP", -0.5, 0.5, NULL),
(4, "10DEG", "Temperature exactly +10C", "TEMP", 9.5, 10.5, NULL),
(5, "20DEG", "Temperature exactly +20C", "TEMP", 19.5, 20.5, NULL),
(6, "SUNNY", "Sunny weather", "WEATHER", NULL, NULL, "Sunny"),
(7, "CLOUDS", "Cloudy weather", "WEATHER", NULL, NULL, "Clouds"),
(8, "WINDY", "Wind blows more than 10 m/s", "WIND", 10.0, 9999, NULL)
;


CREATE TABLE GoalReached (
	gameid VARCHAR(40),
	goalid INTEGER,
	PRIMARY KEY (gameid, goalid),
	FOREIGN KEY (gameid) REFERENCES Game(id),
	FOREIGN KEY (goalid) REFERENCES Goal(id)
);
