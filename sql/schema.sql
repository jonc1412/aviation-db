CREATE TABLE fact_passenger_flight (
    usg_apt_id INT,
    fg_apt_id INT,
    airline_id INT,
    type VARCHAR(25),
    scheduled INT,
    charter INT,
    total INT,
    data_date DATE
);

CREATE TABLE dim_airport (
    airport_key INT IDENTITY(1,1) PRIMARY KEY,
    
)