CREATE TABLE facility (
    id           INTEGER PRIMARY KEY,
    company_id   INTEGER REFERENCES company (id),
    company_name TEXT    REFERENCES company (name),
    type         TEXT,
    service_area TEXT,
    product_id INTEGER REFERENCES product (id),
    address1     TEXT,
    address2     TEXT,
    city         TEXT,
    state        TEXT,
    postal       TEXT,
    country      TEXT,
    size         INTEGER
);
