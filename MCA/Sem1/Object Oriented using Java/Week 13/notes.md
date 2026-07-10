# JDBC - One Shot Exam Notes 📝

---

## 1. What is JDBC?

**JDBC (Java Database Connectivity)** is a Java API that allows Java programs to interact with databases. It provides methods to query and update data in a database.

---

## 2. JDBC Architecture

text

Java Application
        ↓
    JDBC API
        ↓
JDBC Driver Manager
        ↓
    JDBC Driver
        ↓
    Database

---

## 3. JDBC Components

|Component|Description|
|---|---|
|**DriverManager**|Manages database drivers|
|**Connection**|Represents database connection|
|**Statement**|Executes SQL queries|
|**PreparedStatement**|Precompiled SQL statements (prevents SQL injection)|
|**CallableStatement**|Executes stored procedures|
|**ResultSet**|Stores query results|
|**SQLException**|Handles database errors|

---

## 4. Types of JDBC Drivers

|Type|Description|Example|
|---|---|---|
|**Type 1**|JDBC-ODBC Bridge (deprecated)|Uses ODBC driver|
|**Type 2**|Native-API Driver|Uses database client library|
|**Type 3**|Network Protocol Driver|Middleware server|
|**Type 4**|Thin Driver (Pure Java)|Direct database connection (most common)|

---

## 5. JDBC Steps (5 Steps to Connect)

java

// Step 1: Register/load the driver
Class.forName("com.mysql.cj.jdbc.Driver");
// Step 2: Create connection
Connection con = DriverManager.getConnection(
    "jdbc:mysql://localhost:3306/mydb",
    "username",
    "password"
);
// Step 3: Create statement
Statement stmt = con.createStatement();
// Step 4: Execute query
ResultSet rs = stmt.executeQuery("SELECT * FROM employees");
// Step 5: Process results
while (rs.next()) {
    System.out.println(rs.getInt(1) + " " + rs.getString(2));
}
// Step 6: Close connection (cleanup)
rs.close();
stmt.close();
con.close();

---

## 6. Complete JDBC Example

java

import java.sql.*;
public class JDBCDemo {
    public static void main(String[] args) {
        try {
            // 1. Load driver
            Class.forName("com.mysql.cj.jdbc.Driver");
            
            // 2. Create connection
            Connection con = DriverManager.getConnection(
                "jdbc:mysql://localhost:3306/college",
                "root",
                "password"
            );
            
            // 3. Create statement
            Statement stmt = con.createStatement();
            
            // 4. Execute query (INSERT)
            int rows = stmt.executeUpdate(
                "INSERT INTO students VALUES (101, 'John', 85)"
            );
            System.out.println(rows + " row(s) inserted");
            
            // 5. Execute query (SELECT)
            ResultSet rs = stmt.executeQuery("SELECT * FROM students");
            
            // 6. Process results
            while (rs.next()) {
                int id = rs.getInt("id");
                String name = rs.getString("name");
                int marks = rs.getInt("marks");
                System.out.println(id + " | " + name + " | " + marks);
            }
            
            // 7. Close resources
            rs.close();
            stmt.close();
            con.close();
            
        } catch (ClassNotFoundException e) {
            System.out.println("Driver not found: " + e);
        } catch (SQLException e) {
            System.out.println("Database error: " + e);
        }
    }
}

---

## 7. Statement vs PreparedStatement

|Feature|Statement|PreparedStatement|
|---|---|---|
|**SQL Injection**|Vulnerable|Safe|
|**Performance**|Slower (compiles each time)|Faster (precompiled)|
|**Parameters**|No|Yes (using ?)|
|**When to use**|Static queries|Dynamic queries|

### Statement Example:

java

// Vulnerable to SQL injection
String id = request.getParameter("id");
Statement stmt = con.createStatement();
ResultSet rs = stmt.executeQuery(
    "SELECT * FROM users WHERE id = " + id
);

### PreparedStatement Example:

java

// Safe from SQL injection
String name = "John";
PreparedStatement pstmt = con.prepareStatement(
    "INSERT INTO students VALUES (?, ?, ?)"
);
pstmt.setInt(1, 101);      // parameter 1
pstmt.setString(2, name);  // parameter 2
pstmt.setInt(3, 85);       // parameter 3
pstmt.executeUpdate();

---

## 8. ResultSet Methods

java

ResultSet rs = stmt.executeQuery("SELECT * FROM employees");
// Navigation methods
rs.next();      // Move to next row
rs.previous();  // Move to previous row
rs.first();     // Move to first row
rs.last();      // Move to last row
rs.absolute(5); // Move to row 5
rs.beforeFirst(); // Before first row
rs.afterLast();   // After last row
// Get data by column index (starts at 1)
String name = rs.getString(2);
int age = rs.getInt(3);
// Get data by column name
String name = rs.getString("name");
int age = rs.getInt("age");
// Data types
rs.getInt(1);      // Integer
rs.getString(2);   // String
rs.getDouble(3);   // Double
rs.getDate(4);     // Date
rs.getBoolean(5);  // Boolean

---

## 9. Types of ResultSet

java

// Forward only (default)
Statement stmt = con.createStatement();
ResultSet rs = stmt.executeQuery("SELECT * FROM emp");
// Scrollable ResultSet
Statement stmt = con.createStatement(
    ResultSet.TYPE_SCROLL_INSENSITIVE,
    ResultSet.CONCUR_READ_ONLY
);
ResultSet rs = stmt.executeQuery("SELECT * FROM emp");
rs.last();  // Can navigate backwards

|Type|Description|
|---|---|
|`TYPE_FORWARD_ONLY`|Can only move forward|
|`TYPE_SCROLL_INSENSITIVE`|Can scroll, not affected by DB changes|
|`TYPE_SCROLL_SENSITIVE`|Can scroll, reflects DB changes|

---

## 10. Batch Processing

java

// Execute multiple queries at once
Statement stmt = con.createStatement();
stmt.addBatch("INSERT INTO emp VALUES (1, 'John')");
stmt.addBatch("INSERT INTO emp VALUES (2, 'Jane')");
stmt.addBatch("UPDATE emp SET salary = 50000");
int[] results = stmt.executeBatch();
// With PreparedStatement
PreparedStatement pstmt = con.prepareStatement(
    "INSERT INTO emp VALUES (?, ?)"
);
for (int i = 1; i <= 100; i++) {
    pstmt.setInt(1, i);
    pstmt.setString(2, "Employee" + i);
    pstmt.addBatch();
}
pstmt.executeBatch();

---

## 11. Transaction Management

java

try {
    // Disable auto-commit
    con.setAutoCommit(false);
    
    // Execute queries
    stmt.executeUpdate("UPDATE accounts SET balance = balance - 500 WHERE id = 1");
    stmt.executeUpdate("UPDATE accounts SET balance = balance + 500 WHERE id = 2");
    
    // Commit if successful
    con.commit();
    System.out.println("Transaction successful");
    
} catch (SQLException e) {
    // Rollback if error
    con.rollback();
    System.out.println("Transaction failed - Rolled back");
}

|Method|Purpose|
|---|---|
|`setAutoCommit(false)`|Start transaction|
|`commit()`|Save changes permanently|
|`rollback()`|Undo changes|
|`setSavepoint()`|Create savepoint|
|`releaseSavepoint()`|Remove savepoint|

---

## 12. Database Metadata

java

DatabaseMetaData dbmd = con.getMetaData();
System.out.println("Database: " + dbmd.getDatabaseProductName());
System.out.println("Version: " + dbmd.getDatabaseProductVersion());
System.out.println("Driver: " + dbmd.getDriverName());
// Get all tables
ResultSet tables = dbmd.getTables(null, null, "%", null);
while (tables.next()) {
    System.out.println(tables.getString("TABLE_NAME"));
}

---

## 13. Common JDBC URLs

|Database|URL Format|
|---|---|
|**MySQL**|`jdbc:mysql://host:port/database`|
|**Oracle**|`jdbc:oracle:thin:@host:port:SID`|
|**PostgreSQL**|`jdbc:postgresql://host:port/database`|
|**SQL Server**|`jdbc:sqlserver://host:port;databaseName=db`|

---

## 14. Common SQLExceptions

|Exception|Cause|
|---|---|
|`SQLException`|General database error|
|`SQLIntegrityConstraintViolationException`|Duplicate key, foreign key violation|
|`SQLSyntaxErrorException`|SQL syntax error|
|`SQLTimeoutException`|Query timeout|

---

## 15. JDBC 4.0+ Features (Java 6+)

java

// No need for Class.forName() (auto-loading)
Connection con = DriverManager.getConnection(
    "jdbc:mysql://localhost:3306/mydb", "root", "password"
);
// try-with-resources (auto-closes resources)
try (Connection con = DriverManager.getConnection(url, user, pass);
     Statement stmt = con.createStatement();
     ResultSet rs = stmt.executeQuery("SELECT * FROM emp")) {
    
    while (rs.next()) {
        System.out.println(rs.getString(1));
    }
} catch (SQLException e) {
    e.printStackTrace();
}
// Resources automatically closed

---

## 16. JDBC vs Hibernate (Quick Comparison)

|Feature|JDBC|Hibernate|
|---|---|---|
|**Abstraction**|Low level|High level (ORM)|
|**SQL**|Write manually|Auto-generated|
|**Portability**|Database dependent|Database independent|
|**Performance**|Better for simple queries|Better for complex relationships|
|**Learning curve**|Steep|Moderate|

---

## Sample Exam Questions

### Q1: Write JDBC code to insert data

java

Connection con = DriverManager.getConnection(url, user, pass);
PreparedStatement pstmt = con.prepareStatement(
    "INSERT INTO emp VALUES (?, ?, ?)"
);
pstmt.setInt(1, 101);
pstmt.setString(2, "John");
pstmt.setDouble(3, 50000);
pstmt.executeUpdate();

### Q2: What is difference between Statement and PreparedStatement?

- Statement: No parameters, SQL injection risk, compiled each time
    
- PreparedStatement: Has parameters, SQL injection safe, precompiled
    

### Q3: What is ResultSet?

- Object that stores query results
    
- Provides navigation methods (next, previous, first, last)
    

### Q4: How to handle transactions in JDBC?

java

con.setAutoCommit(false);
// execute queries
con.commit();  // or con.rollback();