BEGIN;
--
-- Create model Person
--
CREATE TABLE "person" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar NOT NULL, "email" varchar NOT NULL);
--
-- Create model NaturalPerson
--
CREATE TABLE "natural_person" ("person_ptr_id" bigint NOT NULL PRIMARY KEY REFERENCES "person" ("id") DEFERRABLE INITIALLY DEFERRED, "birthday" date NOT NULL, "salary" decimal NOT NULL, "gender" varchar NOT NULL, "picture" varchar(100) NOT NULL);
--
-- Create constraint unq_person_email on model person
--
CREATE TABLE "new__person" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar NOT NULL, "email" varchar NOT NULL, CONSTRAINT "unq_person_email" UNIQUE ("email"));     
INSERT INTO "new__person" ("id", "name", "email") SELECT "id", "name", "email" FROM "person";
DROP TABLE "person";
ALTER TABLE "new__person" RENAME TO "person";
--
-- Create constraint chk_natural_person_salary on model naturalperson
--
CREATE TABLE "new__natural_person" ("person_ptr_id" bigint NOT NULL PRIMARY KEY REFERENCES "person" ("id") DEFERRABLE INITIALLY DEFERRED, "birthday" date NOT NULL, "salary" decimal 
NOT NULL, "gender" varchar NOT NULL, "picture" varchar(100) NOT NULL, CONSTRAINT "chk_natural_person_salary" CHECK ("salary" >= '0'));
INSERT INTO "new__natural_person" ("person_ptr_id", "birthday", "salary", "gender", "picture") SELECT "person_ptr_id", "birthday", "salary", "gender", "picture" FROM "natural_person";
DROP TABLE "natural_person";
ALTER TABLE "new__natural_person" RENAME TO "natural_person";
--
-- Create constraint chk_natural_person_gender on model naturalperson
--
CREATE TABLE "new__natural_person" ("person_ptr_id" bigint NOT NULL PRIMARY KEY REFERENCES "person" ("id") DEFERRABLE INITIALLY DEFERRED, "birthday" date NOT NULL, "salary" decimal 
NOT NULL, "gender" varchar NOT NULL, "picture" varchar(100) NOT NULL, CONSTRAINT "chk_natural_person_salary" CHECK ("salary" >= '0'), CONSTRAINT "chk_natural_person_gender" CHECK ("gender" IN ('M', 'F', 'O')));
INSERT INTO "new__natural_person" ("person_ptr_id", "birthday", "salary", "gender", "picture") SELECT "person_ptr_id", "birthday", "salary", "gender", "picture" FROM "natural_person";
DROP TABLE "natural_person";
ALTER TABLE "new__natural_person" RENAME TO "natural_person";
COMMIT;