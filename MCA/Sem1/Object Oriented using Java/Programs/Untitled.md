
```java

// Question 1: Employee Salary Management - SIMPLIFIED

class Employee {
    int empId;
    String name;

    Employee(int empId, String name) {
        this.empId = empId;
        this.name = name;
    }

    double calculateSalary() {
        return 0;
    }

    void display() {
        System.out.println("ID: " + empId + ", Name: " + name);
    }
}

class PermanentEmployee extends Employee {
    double basicPay, hra;

    PermanentEmployee(int empId, String name, double basicPay, double hra) {
        super(empId, name);
        this.basicPay = basicPay;
        this.hra = hra;
    }

    @Override
    double calculateSalary() {
        return basicPay + hra;
    }

    double calculateSalary(double bonus) {
        return basicPay + hra + bonus;
    }

    @Override
    void display() {
        super.display();
        System.out.println("Type: Permanent | Salary: " + calculateSalary());
    }
}

class ContractEmployee extends Employee {
    double hourlyRate;
    int hoursWorked;

    ContractEmployee(int empId, String name, double hourlyRate, int hoursWorked) {
        super(empId, name);
        this.hourlyRate = hourlyRate;
        this.hoursWorked = hoursWorked;
    }

    @Override
    double calculateSalary() {
        return hourlyRate * hoursWorked;
    }

    @Override
    void display() {
        super.display();
        System.out.println("Type: Contract | Salary: " + calculateSalary());
    }
}

public class Question1_Employee {
    public static void main(String[] args) {
        System.out.println("=== EMPLOYEE SALARY MANAGEMENT ===\n");

        PermanentEmployee emp1 = new PermanentEmployee(101, "John", 50000, 10000);
        emp1.display();
        System.out.println("With Bonus: " + emp1.calculateSalary(5000) + "\n");

        ContractEmployee emp2 = new ContractEmployee(102, "Jane", 500, 160);
        emp2.display();
    }
}

```


```java

// Question 2: Bank Account System - SIMPLIFIED

abstract class BankAccount {
    int accountNo;
    double balance;

    BankAccount(int accountNo, double balance) {
        this.accountNo = accountNo;
        this.balance = balance;
    }

    abstract void deposit(double amount);
    abstract void withdraw(double amount);

    void displayBalance() {
        System.out.println("Account: " + accountNo + " | Balance: " + balance);
    }
}

class SavingsAccount extends BankAccount {
    SavingsAccount(int accountNo, double balance) {
        super(accountNo, balance);
    }

    @Override
    void deposit(double amount) {
        balance += amount;
        System.out.println("Deposited: " + amount + " | New Balance: " + balance);
    }

    @Override
    void withdraw(double amount) {
        if (amount <= balance) {
            balance -= amount;
            System.out.println("Withdrawn: " + amount + " | New Balance: " + balance);
        } else {
            System.out.println("Insufficient balance!");
        }
    }
}

public class Question2_BankAccount {
    public static void main(String[] args) {
        System.out.println("=== BANK ACCOUNT SYSTEM ===\n");

        SavingsAccount acc = new SavingsAccount(1001, 50000);
        acc.displayBalance();
        
        System.out.println("\nDeposit:");
        acc.deposit(15000);
        
        System.out.println("\nWithdraw:");
        acc.withdraw(20000);
        
        System.out.println("\nFinal:");
        acc.displayBalance();
    }
}

```

```java

// Question 3: Student Management - SIMPLIFIED

class Person {
    String name;
    int age;

    Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    void displayPersonDetails() {
        System.out.println("Name: " + name + ", Age: " + age);
    }
}

class Student extends Person {
    int rollNo;
    String course;

    // Constructor 1
    Student(String name, int age, int rollNo, String course) {
        super(name, age);
        this.rollNo = rollNo;
        this.course = course;
    }

    // Constructor 2 (Overloading)
    Student(String name, int age, int rollNo) {
        super(name, age);
        this.rollNo = rollNo;
        this.course = "Not Declared";
    }

    @Override
    void displayPersonDetails() {
        super.displayPersonDetails();
        System.out.println("Roll No: " + rollNo + ", Course: " + course);
    }
}

public class Question3_StudentManagement {
    public static void main(String[] args) {
        System.out.println("=== STUDENT MANAGEMENT ===\n");

        Student s1 = new Student("Alice", 20, 1001, "Computer Science");
        System.out.println("Student 1:");
        s1.displayPersonDetails();

        System.out.println("\nStudent 2:");
        Student s2 = new Student("Bob", 21, 1002);
        s2.displayPersonDetails();

        System.out.println("\n--- Polymorphism Demo ---");
        Person[] students = { s1, s2 };
        for (Person p : students) {
            p.displayPersonDetails();
            System.out.println();
        }
    }
}

```

```java

// Question 4: Shape Drawing - SIMPLIFIED

interface Drawable {
    void draw();
}

abstract class Shape implements Drawable {
    String color;

    Shape(String color) {
        this.color = color;
    }

    abstract void calculateArea();
}

class Circle extends Shape {
    double radius;

    Circle(String color, double radius) {
        super(color);
        this.radius = radius;
    }

    @Override
    public void draw() {
        System.out.println("Drawing " + color + " Circle");
    }

    @Override
    void calculateArea() {
        double area = Math.PI * radius * radius;
        System.out.println("Circle Area = " + area);
    }
}

class Rectangle extends Shape {
    double length, breadth;

    Rectangle(String color, double length, double breadth) {
        super(color);
        this.length = length;
        this.breadth = breadth;
    }

    @Override
    public void draw() {
        System.out.println("Drawing " + color + " Rectangle");
    }

    @Override
    void calculateArea() {
        double area = length * breadth;
        System.out.println("Rectangle Area = " + area);
    }
}

public class Question4_ShapeDrawing {
    public static void main(String[] args) {
        System.out.println("=== SHAPE DRAWING ===\n");

        Circle circle = new Circle("Red", 5);
        System.out.println("Circle:");
        circle.draw();
        circle.calculateArea();

        System.out.println("\nRectangle:");
        Rectangle rectangle = new Rectangle("Blue", 10, 6);
        rectangle.draw();
        rectangle.calculateArea();

        System.out.println("\n--- Polymorphism with Drawable ---");
        Drawable[] shapes = { circle, rectangle };
        for (Drawable shape : shapes) {
            shape.draw();
        }

        System.out.println("\n--- Polymorphism with Shape ---");
        Shape[] shapeArray = { circle, rectangle };
        for (Shape shape : shapeArray) {
            shape.calculateArea();
        }
    }
}

```

```

abstract class Staff {

    int staffId;

    String name;

  

    Staff(int staffId, String name){

        this.name = name;

        this.staffId = staffId;

    }

  

    void displayDetials(){

        System.out.println("ID: "+staffId+"Staff Name: "+name);

    }

}

  

interface DigitalService{

    void accessPatientRecord();

    void processBilling(double amount);

  

}

  

class Doctor extends Staff implements DigitalService {

  

    Doctor(int staffid, String name, String Dep){

        super(staffId, name);    

    }

    @Override

    void performDuties() {

        System.out.println("Doctor "+name+" Diagonsing patients ");

    }

  

    @Override

    public void accessPatientRecord() {

        System.out.println("Doctor "+name+"Accessing patient records");

    }

  

    @Override

    public void processBilling(double amount) {

        System.out.println("Doctor "+name+"processed Bill"+amount);

    }

}

  

class Nurse extends Staff implements DigitalService {

  

    Nurse(int staffId, String name){

        super(staffId, name);

    }

  

    @Override

    void performDuties() {

        System.out.println("Nurse "+name+" Assiting with Treatments ");

    }

  

    @Override

    public void accessPatientRecord() {

        System.out.println("Nurse "+name+"Accessing patient records");

    }

  

    @Override

    public void processBilling(double amount) {

        System.out.println("Nurse "+name+"recorded Bill"+amount);

    }

}

  

public class HospitalManagmentSystem {

    public static void main(String[] args){

  

        System.out.println("");

  

        Doctor d = new Doctor(101, "De.Rajesh");

  

        Nurse n = new Nurse(201, "Anne");

  
  

        d.displayDetials();

        d.performDuties();

        d.accessPatientRecord();

        d.processBilling(1000);

  

        System.out.println();

  

        n.displayDetials();

        n.performDuties();

        n.accessPatientRecord();

        n.processBilling(600);

    }

}

```