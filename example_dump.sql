BEGIN TRANSACTION;
CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real);
INSERT INTO "stocks" VALUES('2022-02-07','buy','rhat',100.0,34.23);
INSERT INTO "stocks" VALUES('2021-11-23','buy','ibm',1000.0,45.0);
INSERT INTO "stocks" VALUES('1999-09-20','sell','msft',1000.0,72.0);
INSERT INTO "stocks" VALUES('2005-01-15','sell','ibm',500.0,53.0);
INSERT INTO "stocks" VALUES('2021-11-23','buy','ibm',1000.0,45.0);
INSERT INTO "stocks" VALUES('1999-09-20','sell','msft',1000.0,72.0);
INSERT INTO "stocks" VALUES('2005-01-15','sell','ibm',500.0,53.0);
COMMIT;
