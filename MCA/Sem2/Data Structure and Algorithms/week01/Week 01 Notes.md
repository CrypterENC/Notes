### Data Structures

> A **data structure** is a way of organizing, storing, and managing data so that it can be accessed and modified efficiently.

**Example:** Arrays, Linked Lists, Stacks, Queues, Trees, Graphs, Hash Tables.

### Algorithm

>An algorithm is a **definite sequence of unambiguous steps** to solve a computational problem. It **takes an input**, **apply finites number of computations** on it and give back the result as output. 

> An **algorithm** is a **~={red}finite=~** sequence of well-defined steps to solve a specific problem.

- Algorithm must be both **definite and finite**
	-  That is :
		1. **Definite** -- Each step must be clear, unambiguous, and precisely defined.
		2. **Finite**     -- The algorithm must terminate after a finite number of steps 

	-   Example: A recipe is a good analogy:
		  - It has definite steps ("add salt" is clear, not "add some salt maybe")
		  - It has finite steps (it doesn't go on forever)
		  - When you follow it correctly, you get a result

**Example:**
- Binary search algorithm to find an element in a sorted array.
- Bubble sort algorithm to sort numbers.

### Abstract Data Types (ADT)
An **Abstract Data Type (ADT)** is a **mathematical model** for data types, defined by:

- **The values** it can hold (data)
    
- **The operations** that can be performed on it

> An **ADT** defines _what_ operations can be performed on data, but _not how_ they are implemented. It focuses on behavior, not implementation details.

### Array 

#### 1D Array

A **1D array**  is a **collection of elements** of the **same data type**, stored in **contiguous memory locations**, and accessed using a **single index**.

##### 🔹Definition of an 1D Array (in C/Java style):
```
int arr[5];              // C
int num[] = new int[5];  // Java --> Defines an array named num, of size 5 in Java language.                                      num is a reference to the array object.

NOTE: if num[5] is accessed then it throws an error "throws arrayindexoutofbound exeception"
```
##### 🔹 Declaration, Assignment, Initialization:
```
int arr1[];   // array declaration, no memory is allocated to store array, arr1 is a                          reference which is null.

arr1 = new int[10]; // arr1 refers to an array of 10 integers.

int arr2[] = new int[10];   //  defines an array of 10 integers.

int arr2[5] = {10, 20, 30, 40, 50}; // creates and initialises an array


for(int j=0;j<arr2.length;j++)
	System.out.println(arr2[j]);


```

#### 2D Array (array of arrays)
A **2D array** is a collection of elements arranged in **rows and columns**.  
It can be visualized as a **table** with **m rows** and **n columns**.

##### Syntax
```java
int[][] matrix = new int[3][4];   // 3 rows, 4 columns
```

##### Accessing
- An element of 2 D array is accessed using two indices, **row index** and **column index**.
	-  If array name is A, 1st element is accessed using `A[0][0]`.

##### 📍 Row-Major vs Column-Major Order -- This is **very important** for address calculation

| Order            | Storage Pattern                               | Formula for `A[i][j]`             |
| ---------------- | --------------------------------------------- | --------------------------------- |
| **Row-Major**    | Row 0, then Row 1, then Row 2..               | Base + ((i * numCols) + j) * size |
| **Column-Major** | Column 0, then Column 1, then Column 2....... | Base + ((j * numRows) + i) * size |
##### Example Problem for Address Calculation  
**Given a 2 D array, B with No of rows = 4, No. of columns = 5 . Size of each item in the array is 1 byte. Base address of the array is 5000.** 

Find the address of the location `B[4][3]` in `4 x 5 array`
- Row-major Representation Address of `B[4][3]`       = `5000 + ((4 * 5) + 3) * 1 = 5023`
- Column-major Representation Address of `B[4][3]`  = `5000 + ((3 * 4) + 4) * 1 = 5016`

#####  Jagged Array -- **ragged array**
A **jagged array** is an **array of arrays** where each row (inner array) can have a **different length**.

- Example

```java
int[][] jagged = new int[3][];   // 3 rows, but columns not yet defined

jagged[0] = new int[2];   // Row 0 has 2 columns
jagged[1] = new int[4];   // Row 1 has 4 columns
jagged[2] = new int[1];   // Row 2 has 1 column
```
