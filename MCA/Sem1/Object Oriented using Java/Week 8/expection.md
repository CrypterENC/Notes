# Java Exceptions - Complete Notes

## 1. What is an Exception?

An **exception** is an abnormal event that occurs during program execution that disrupts the normal flow of instructions.

## 2. Exception Hierarchy

text

Object
  └── Throwable
       ├── Error (unchecked, can't handle)
       │    ├── OutOfMemoryError
       │    ├── StackOverflowError
       │    └── VirtualMachineError
       │
       └── Exception (checked, can handle)
            ├── IOException
            ├── SQLException
            ├── ClassNotFoundException

make me notes for Exceptions in java, one shot for tomorrows exam

# Java Exceptions - One Shot Exam Notes 📝

## 1. What is Exception?

**Abnormal event** that disrupts normal program flow during execution.

---

## 2. Exception Hierarchy

text

Throwable (superclass)
    ├── Error (can't handle - JVM errors)
    │   ├── OutOfMemoryError
    │   ├── StackOverflowError
    │   └── VirtualMachineError
    │
    └── Exception (can handle)
        ├── Checked Exceptions (compile-time)
        │   ├── IOException
        │   ├── SQLException
        │   ├── FileNotFoundException
        │   └── ClassNotFoundException
        │
        └── Unchecked Exceptions (runtime)
            ├── ArithmeticException
            ├── NullPointerException
            ├── ArrayIndexOutOfBoundsException
            └── NumberFormatException

---

## 3. Types of Exceptions

|Type|Checked/Unchecked|When|Examples|
|---|---|---|---|
|**Checked**|Checked at compile-time|Must handle or declare|IOException, SQLException|
|**Unchecked**|Checked at runtime|May or may not handle|ArithmeticException, NullPointerException|
|**Error**|Unchecked|Cannot handle|OutOfMemoryError|

---

## 4. Exception Handling Keywords

|Keyword|Purpose|
|---|---|
|**try**|Block where exception may occur|
|**catch**|Handles the exception|
|**finally**|Always executes (cleanup code)|
|**throw**|Manually throw exception|
|**throws**|Declares exception in method signature|

---

## 5. Basic Syntax

java

// try-catch
try {
    // risky code
    int result = 10 / 0;
} catch (ArithmeticException e) {
    System.out.println("Cannot divide by zero");
}
// try-catch-finally
try {
    FileReader file = new FileReader("test.txt");
} catch (FileNotFoundException e) {
    System.out.println("File not found");
} finally {
    System.out.println("This always executes");
}
// try-with-resources (Java 7+)
try (FileReader fr = new FileReader("file.txt")) {
    // auto closes resources
} catch (IOException e) {
    e.printStackTrace();
}

---

## 6. Multiple Catch Blocks

java

try {
    int[] arr = new int[5];
    arr[10] = 50 / 0;
} catch (ArithmeticException e) {
    System.out.println("Arithmetic error");
} catch (ArrayIndexOutOfBoundsException e) {
    System.out.println("Array index error");
} catch (Exception e) {
    System.out.println("Generic exception");
}
// Order: Child → Parent (specific to general)

---

## 7. throw vs throws

|throw|throws|
|---|---|
|Used to **explicitly throw** exception|Used to **declare** exception in method|
|Inside method body|In method signature|
|Can throw only one exception|Can declare multiple exceptions|
|`throw new ArithmeticException();`|`void method() throws IOException`|

java

// throw example
void validateAge(int age) {
    if (age < 18) {
        throw new ArithmeticException("Not eligible");
    }
}
// throws example
void readFile() throws IOException, SQLException {
    // method body
}

---

## 8. Custom Exceptions

java

// Create custom exception
class InvalidAgeException extends Exception {
    InvalidAgeException(String message) {
        super(message);
    }
}
// Using custom exception
void validate(int age) throws InvalidAgeException {
    if (age < 18) {
        throw new InvalidAgeException("Age not valid");
    }
}
public static void main(String[] args) {
    try {
        validate(15);
    } catch (InvalidAgeException e) {
        System.out.println(e.getMessage());
    }
}

---

## 9. Common Exceptions & Causes

|Exception|Cause|
|---|---|
|`ArithmeticException`|Division by zero|
|`NullPointerException`|Accessing null object|
|`ArrayIndexOutOfBoundsException`|Invalid array index|
|`NumberFormatException`|Invalid number conversion|
|`FileNotFoundException`|File doesn't exist|
|`ClassNotFoundException`|Class not found|
|`IOException`|Input/output operation failed|