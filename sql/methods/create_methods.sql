
CREATE TABLE methods (
    id           INTEGER PRIMARY KEY,
    type         TEXT,
    method       TEXT,
    medium       TEXT,
    detail1      TEXT,
    cea          BOOLEAN,
    area         INTEGER,
    product_item TEXT    REFERENCES product (item) 
);
