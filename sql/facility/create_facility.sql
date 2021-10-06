CREATE TABLE facility (
    id INTEGER PRIMARY KEY,
    company_id   INTEGER REFERENCES company (id) ,
    company_name TEXT,
    primary_use TEXT,
    year_opened INTEGER,
    HQ TEXT,
    facility_name TEXT,
    size_sq_ft INTEGER,
    size_acres INTEGER,
    city TEXT,
    state TEXT,
    address1 TEXT,
    address2 TEXT,
    address3 TEXT,
    postal TEXT,
    country TEXT
);