CREATE TABLE fact_passenger_flight (
    flight_date DATE,
    usg_apt_iata VARCHAR(10) NOT NULL,
    fg_apt_iata VARCHAR(10) NOT NULL,
    flight_type VARCHAR(20),
    scheduled INT,
    charter INT,
    total INT
)
SORTKEY (flight_date, usg_apt_iata, fg_apt_iata);

CREATE TABLE dim_airport (
    iata VARCHAR(3) UNIQUE NOT NULL,
    airport_name VARCHAR(255),
    country_code VARCHAR(3),
    region_name VARCHAR(255),
    latitude DECIMAL(9,6),
    longitude DECIMAL(9,6)
)
DISTKEY (airport_key)
SORTKEY (country_code, iata);