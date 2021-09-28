
CREATE TABLE product (
    id            INTEGER PRIMARY KEY,
    facility_id   INTEGER REFERENCES facility (id),
    category      TEXT,
    subcategory   TEXT,
    item          TEXT,
    item_detail   TEXT,
    customer_type TEXT    REFERENCES customer (type) 
);
