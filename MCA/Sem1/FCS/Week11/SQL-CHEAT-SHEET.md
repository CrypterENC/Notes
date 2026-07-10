### **1. DDL Commands (Data Definition Language)**

**DDL commands** are used for defining and modifying database structures like tables, indexes, and schemas.

|**Command**|**Description**|**Example**|
|---|---|---|
|**CREATE**|Used to create a new table, database, or other database objects.|`CREATE TABLE employees (id INT, name VARCHAR(50));`|
|**ALTER**|Modifies an existing database object (e.g., table structure).|`ALTER TABLE employees ADD COLUMN age INT;`|
|**DROP**|Deletes an entire table or database.|`DROP TABLE employees;`|
|**TRUNCATE**|Removes all records from a table but retains the table structure.|`TRUNCATE TABLE employees;`|
|**RENAME**|Renames a table or database object.|`ALTER TABLE employees RENAME TO staff;`|

---

### **2. DML Commands (Data Manipulation Language)**

**DML commands** are used for adding, updating, or deleting data in tables.

|**Command**|**Description**|**Example**|
|---|---|---|
|**INSERT**|Adds new rows of data into a table.|`INSERT INTO employees (id, name, age) VALUES (1, 'John', 30);`|
|**UPDATE**|Modifies existing data in a table.|`UPDATE employees SET age = 35 WHERE id = 1;`|
|**DELETE**|Removes specific rows of data from a table.|`DELETE FROM employees WHERE age < 25;`|

---

### **3. TCL Commands (Transaction Control Language)**

**TCL commands** manage transactions in SQL, helping to ensure data integrity.

|**Command**|**Description**|**Example**|
|---|---|---|
|**COMMIT**|Saves the current transaction permanently.|`COMMIT;`|
|**ROLLBACK**|Reverts the database to the last saved state.|`ROLLBACK;`|
|**SAVEPOINT**|Sets a savepoint to mark a specific point in a transaction.|`SAVEPOINT sp1;`|
|**SET TRANSACTION**|Defines the isolation level for transactions.|`SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;`|

---

### **4. DQL Commands (Data Query Language)**

**DQL commands** are used to query and retrieve data from a database.

| **Command** | **Description**                         | **Example**                               |
| ----------- | --------------------------------------- | ----------------------------------------- |
| **SELECT**  | Retrieves data from one or more tables. | `SELECT * FROM employees WHERE age > 30;` |