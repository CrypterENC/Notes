# Java Abstract Classes, Interfaces & Packages - One Shot Exam Notes 📝

---

# PART 1: ABSTRACT CLASSES

## 1. What is an Abstract Class?

A class declared with `abstract` keyword that **cannot be instantiated** (can't create objects).

java

abstract class Animal {
    abstract void sound();  // abstract method (no body)
    
    void sleep() {          // concrete method (with body)
        System.out.println("Sleeping");
    }
}

## 2. Key Rules

|Rule|Explanation|
|---|---|
|✅ Can have abstract & concrete methods|Both types allowed|
|✅ Can have constructors|Called when subclass object created|
|✅ Can have instance variables|Normal variables allowed|
|✅ Can have main method|Abstract class can have main()|
|❌ Cannot create object|`new Animal()` ❌ not allowed|
|❌ Cannot be final|`final abstract` ❌ not allowed|

## 3. Abstract Method Rules

java

abstract void display();     // ✅ No body, ends with semicolon
abstract void show() { }     // ❌ Cannot have body

- Must be implemented by **first concrete subclass**
    
- Cannot be **private** (wouldn't be accessible)
    
- Cannot be **final** (can't override)
    
- Cannot be **static**
    

## 4. Complete Example

java

abstract class Shape {
    String color;
    
    Shape(String color) {
        this.color = color;
    }
    
    abstract double area();      // abstract method
    abstract double perimeter(); // abstract method
    
    void displayColor() {        // concrete method
        System.out.println("Color: " + color);
    }
}
class Circle extends Shape {
    double radius;
    
    Circle(String color, double radius) {
        super(color);
        this.radius = radius;
    }
    
    double area() {
        return 3.14 * radius * radius;
    }
    
    double perimeter() {
        return 2 * 3.14 * radius;
    }
}
public class Test {
    public static void main(String[] args) {
        // Shape s = new Shape(); ❌ Cannot instantiate
        Circle c = new Circle("Red", 5.0);
        System.out.println("Area: " + c.area());
        c.displayColor();
    }
}

---

# PART 2: INTERFACES

## 1. What is an Interface?

A **blueprint** of a class that contains only abstract methods (until Java 7). It achieves **100% abstraction** and **multiple inheritance**.

java

interface Drawable {
    void draw();  // abstract method (public abstract by default)
}

## 2. Interface Rules

|Rule|Explanation|
|---|---|
|✅ Multiple inheritance|Class can implement multiple interfaces|
|✅ Variables are `public static final`|Constants by default|
|✅ Methods are `public abstract`|(Java 7 and earlier)|
|✅ Java 8+|Default & static methods allowed|
|✅ Java 9+|Private methods allowed|
|❌ Cannot have constructors|No object creation|
|❌ Cannot have instance variables|Only constants|

## 3. Interface Evolution

java

interface MyInterface {
    // Before Java 7
    int MAX = 100;           // public static final
    void method1();          // public abstract
    
    // Java 8
    default void method2() { // default method
        System.out.println("Default method");
    }
    
    static void method3() {  // static method
        System.out.println("Static method");
    }
    
    // Java 9
    private void method4() { // private method
        System.out.println("Private method");
    }
}

## 4. Complete Example

java

interface Printable {
    void print();
}
interface Showable {
    void show();
    
    default void display() {  // default method
        System.out.println("Default display");
    }
}
// Multiple inheritance
class Document implements Printable, Showable {
    public void print() {
        System.out.println("Printing...");
    }
    
    public void show() {
        System.out.println("Showing...");
    }
}
public class Test {
    public static void main(String[] args) {
        Document d = new Document();
        d.print();
        d.show();
        d.display();  // default method
    }
}

---

# PART 3: ABSTRACT CLASS vs INTERFACE

|Feature|Abstract Class|Interface|
|---|---|---|
|Keyword|`abstract`|`interface`|
|Multiple Inheritance|❌ No|✅ Yes|
|Variables|Non-final, non-static|`public static final`|
|Constructors|✅ Yes|❌ No|
|Method Types|Abstract & Concrete|Abstract (Java 7), Default/Static (Java 8+)|
|Access Modifiers|All|`public` (methods), `public static final` (variables)|
|When to Use|Common base with state|Contract/capability|

## When to Use?

java

// Use Abstract Class when:
// - You have common code to share
// - You need instance variables
// - You need constructors
abstract class Vehicle {
    String brand;
    Vehicle(String brand) { this.brand = brand; }
    abstract void start();
}
// Use Interface when:
// - You need multiple inheritance
// - You're defining a capability/callback
// - You want loose coupling
interface Flyable {
    void fly();
}
interface Swimmable {
    void swim();
}

---

# PART 4: PACKAGES

## 1. What is a Package?

A **namespace** that groups related classes and interfaces.

## 2. Types of Packages

|Type|Description|
|---|---|
|**Built-in**|Java API packages (java.lang, java.util, [java.io](https://java.io/))|
|**User-defined**|Packages created by programmer|

## 3. Common Built-in Packages

|Package|Purpose|
|---|---|
|`java.lang`|Default, automatically imported (String, System, Object)|
|`java.util`|Collections, Scanner, Date|
|`java.io`|Input/Output operations|
|`java.awt`|GUI components|
|`java.net`|Networking|
|`java.sql`|Database connectivity|

## 4. Creating a Package

java

// File: com/mypackage/MyClass.java
package com.mypackage;
public class MyClass {
    public void display() {
        System.out.println("Hello from package");
    }
}

## 5. Importing Packages

java

// Import specific class
import java.util.Scanner;
// Import all classes from package
import java.util.*;
// Import static members (Java 5+)
import static java.lang.System.out;
public class Test {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        out.println("Hello");  // instead of System.out.println
    }
}

## 6. Package Naming Convention

text

Reverse domain name: com.companyname.projectname
Examples:
- com.google.android
- java.util
- org.springframework.boot

## 7. Access Specifiers with Packages

|Modifier|Same Class|Same Package|Subclass (diff pkg)|Anywhere|
|---|---|---|---|---|
|`public`|✅|✅|✅|✅|
|`protected`|✅|✅|✅|❌|
|`default` (no modifier)|✅|✅|❌|❌|
|`private`|✅|❌|❌|❌|

## 8. Compiling and Running with Packages

bash

# Directory structure
src/com/mypackage/MyClass.java
# Compile
javac -d . src/com/mypackage/MyClass.java
# Run
java com.mypackage.MyClass
# Create JAR
jar -cf myapp.jar com/

---

# Quick Comparison Table

|Concept|Abstract Class|Interface|Package|
|---|---|---|---|
|Keyword|`abstract`|`interface`|`package`|
|Purpose|Partial abstraction|Full abstraction (till Java 7)|Organize classes|
|Instantiation|❌ No|❌ No|N/A|
|Inheritance|Single|Multiple|N/A|

---

# Sample Exam Questions

## Q1: What is output?

java

abstract class A {
    A() { System.out.print("A"); }
    abstract void show();
}
class B extends A {
    B() { System.out.print("B"); }
    void show() { System.out.print("C"); }
}
public class Test {
    public static void main(String[] args) {
        A obj = new B();
        obj.show();
    }
}
// Output: ABC

## Q2: Which is correct?

java

interface I {
    int x = 10;  // What is x?
}
// Answer: public static final int x = 10;

## Q3: Package statement must be?

java

// Answer: First line in file (before imports)
package com.test;
import java.util.*;