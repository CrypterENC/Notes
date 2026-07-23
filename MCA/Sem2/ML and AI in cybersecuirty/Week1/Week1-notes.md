## 1.4 How do Computers Learn? 
> **What is Learning** : The acquisition of knowledge or skills **through study, experience or being taught.**

### Deductive vs Inductive Learning

1. **Deductive Learning** : 
	- You give the **Algorithms 2 Things**:
		1. **~={red}Rules=~** (the logic/knowledge base — e.g., "IF port 22 AND failed_logins > 5 THEN alert").
		2. **~={red}Facts/Data=~** (the input — e.g., "port = 22, failed_logins = 10").
		
	- **The ~={cyan}algorithm applies the rules to the data**=~ and gives you a **~={green}conclusion/answer=~**

```markdown
Example 

|**Rule**     |"IF port == 22 AND failed_logins > 5 THEN ALERT"|
|**Data/Fact**|"port = 22, failed_logins = 10"|
|**Answer**   |"ALERT: SSH Brute Force"|
```

2. **Inductive Learning** : 
	-  You give the **Algorithms 2 Things**:
		1. **~={red}Data=~** (training samples — e.g., 10,000 network logs).
		2. **~={red}Labels/Outputs**=~ (the input — e.g., "port = 22, failed_logins = 10").
	- **The ~={cyan}algorithm studies the data and labels**=~, and **discovers/generates the rules itself** — without you telling it what rules to use.
	- **The ~={green}output is a MODEL**=~ (not a direct answer) — this model contains the learned patterns/rules

```markdown


|**You give:**        |50,000 PE files (executables), each labeled "malware" or "benign"|
|**Algorithm does:**  |Studies patterns — byte sequences, API calls, entropy, section names that correlate with malware|
|**You get:**         |A **trained model** (e.g., a Random Forest or Neural Network)|
|**Later:**           |You give the model a new, never-before-seen .exe file|
|**Model gives:**     |"This is MALWARE" (with 95% confidence)|


```

## Installing 

Download Miniconda from here -- https://anaconda.com/api/installers/Miniconda3-latest-Windows-x86_64.exe

- Then install libraries -- `conda install jupyter numpy pandas scikit-learn seaborn matplotlib jupyterlab`

- to run lab -- `jupyter lab` or `jupyter lab --no-browser`

## Testing if everything is working.

```python
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn import datasets
import matplotlib.pyplot as plt
```

## 1.6 Introduction to the Stack📜
In the next set of videos we will slowly work our way through the following notebook `0001_intro_software.ipynb.`

I will use this notebook as a base and demonstrate the basics of the libraries we will be using in this course. You should follow along on your computer.

## 1.7 Scikit-Learn and Jupyter🎦📜👩🏽‍💻

### NumPy🎦📜👩🏽‍💻
- Numerical Python
- The fundamental package for scientific computing
- it gives as **ndarray** (n-dimensional array)

#### Importing NumPy
```python
import numpy as np  # Standard convention
```

#### Core Concepts You MUST Know

##### 1. Creating Arrays
```python
# From a python list
arr = np.array([1,2,3,4,5])

#=============================================================
# Zeros, Ones, Identity
#=============================================================
zeros = np.zeros((3, 4))      # 3x4 matrix of zeros

	array([[0., 0., 0., 0.],
	       [0., 0., 0., 0.],
	       [0., 0., 0., 0.]])
	       
ones = np.ones((2, 3))        # 2x3 matrix of ones

	array([[1., 1., 1.],
	       [1., 1., 1.]])

eye = np.eye(3)               # 3x3 identity matrix

	array([[1., 0., 0.],
	       [0., 1., 0.],
	       [0., 0., 1.]])

#=============================================================
#Range of values
#=============================================================
range_arr = np.arange(0,10,2)  # from '0' to '10' with a step of '2'.

	array([0, 2, 4, 6, 8])

#=============================================================
#Random arrays (critical for ML!)
#=============================================================
rand = np.random.rand(3, 3)      # Uniform [0,1)

	array([[0.83469805, 0.12711334, 0.97709378],
	       [0.57115186, 0.91903702, 0.88583722],
	       [0.68845383, 0.84213991, 0.4950897 ]])

randn = np.random.randn(3, 3)    # Standard normal

	array([[ 1.05599473, -1.03353435,  1.86987715],
	       [-1.14992491, -0.62480301, -0.03767475],
	       [-1.97811994,  0.92250561,  0.01303398]])
	       
randint = np.random.randint(0, 100, (3, 3))  # Integers

	array([[14, 14, 15],
	       [77, 36, 67],
	       [23, 76, 22]], dtype=int32)
```

##### 2. Array Attributes

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])
```

| Key              | Description              |
| ---------------- | ------------------------ |
| **arr.shape**    | (2, 3) — rows, columns   |
| **arr.size**     | 6 — total elements       |
| **arr.ndim**     | 2 — number of dimensions |
| **arr.dtype**    | int64 — data type        |
| **arr.itemsize** | 8 — bytes per element    |
##### 3. Indexing and Slicing

```python
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])

# Access elements
arr[0, 2]          # 3 — row 0, column 2
arr[1, :]          # [5, 6, 7, 8] — entire row 1
arr[:, 1]          # [2, 6, 10] — entire column 1
arr[0:2, 1:3]      # [[2, 3], [6, 7]] — submatrix

#Here arr[0:2, 1:3] is arr[rows, columns].

                0   1  2  3

			0	[1, 2, 3, 4]
            1   [5, 6, 7, 8]
            2   [9, 10, 11, 12]
                
    0:2 ==> Rows    that is : [1, 2, 3, 4] and [5, 6, 7, 8] 
    1:3 ==> Columns that is : 2  and  3
                              6       7

# Boolean indexing (critical for filtering)
mask = arr > 5
arr[mask]          # [6, 7, 8, 9, 10, 11, 12]
```






```python
# Shape, Ndmin

np.random.seed(0)  # seed for reproducibility

x1 = np.random.randint(10, size=6)  # One-dimensional array
x2 = np.random.randint(10, size=(3, 4))  # Two-dimensional array
x3 = np.random.randint(10, size=(3, 4, 5))  # Three-dimensional array
```

```python
print(x1)
```

```python
array([5, 0, 3, 3, 7, 9], dtype=int32)
```

```python
print(x2)
```

```python
array([[3, 5, 2, 4],
       [7, 6, 8, 8],
       [1, 6, 7, 7]], dtype=int32)
```

```python
print(x3)
```

```python
array([[[8, 1, 5, 9, 8],
        [9, 4, 3, 0, 3],
        [5, 0, 2, 3, 8],
        [1, 3, 3, 3, 7]],

       [[0, 1, 9, 9, 0],
        [4, 7, 3, 2, 7],
        [2, 0, 0, 4, 5],
        [5, 6, 8, 4, 1]],

       [[4, 9, 8, 1, 1],
        [7, 9, 9, 3, 6],
        [7, 2, 0, 3, 5],
        [9, 4, 4, 6, 4]]], dtype=int32)
```

```python
print("x3 ndim: ", x3.ndim)  # ndim is n - dimensional
print("x3 shape:", x3.shape) 
print("x3 size: ", x3.size)
```

```python
x3 ndim:  3
x3 shape: (3, 4, 5)
x3 size:  60
```