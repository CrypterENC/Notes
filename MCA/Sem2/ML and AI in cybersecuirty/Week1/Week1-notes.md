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

## NumPy🎦📜👩🏽‍💻
- Numerical Python
- The fundamental package for scientific computing
- it gives as **ndarray** (n-dimensional array)

### Importing NumPy
```python
import numpy as np  # Standard convention
```

### Core Concepts You MUST Know

#### 1. Creating Arrays
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

#### 2. Array Attributes
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
#### 3. Indexing and Slicing
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

#### 4. Vectorized Operations (WHY NumPy is FAST)
```python
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Element-wise operations (NO LOOPS!)
arr1 + arr2        # [5, 7, 9]
arr1 * arr2        # [4, 10, 18]
arr1 ** 2          # [1, 4, 9]
np.sqrt(arr1)      # [1, 1.41, 1.73]

# Broadcasting — apply operation to entire array
arr = np.array([1, 2, 3, 4])
arr + 10           # [11, 12, 13, 14]
arr * 2            # [2, 4, 6, 8]
```

#### 5. Reshaping and Transposing
```python
arr = np.array([1, 2, 3, 4, 5, 6])

# Reshape
arr.reshape(2, 3)    # [[1, 2, 3], [4, 5, 6]]
arr.reshape(3, 2)    # [[1, 2], [3, 4], [5, 6]]

# Transpose
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
arr2.T               # [[1, 4], [2, 5], [3, 6]]

# Flatten
arr2.flatten()       # [1, 2, 3, 4, 5, 6]
```

## 1.9 Matplotlib🎦📜👩🏽‍💻
### Import Matplotlib
```python
import matplotlib.pyplot as plt  # Standard alias
```

### Core Concepts You MUST Know
#### 1. Basic Line Plot
```python
import matplotlib.pyplot as plt
import numpy as np

#Data
x = np.array([1,2,3,4,5])
y = np.array([2,4,6,8,10])

#Create plot
plt.plot(x,y);
plt.title('First Line Plot using Matplotlib')
plt.xlabel('X-zxis')
plt.ylabel('Y-zxis')
```

#### 2. Figure and Axes (The OOP Way)
```python
# Create figure and axes explicitly (RECOMMENDED for complex plots)
import matplotlib.pyplot as plt
import numpy as np

#Data
x = np.array([1,2,3,4,5])
y = np.array([2,4,6,8,10])

fig, ax = plt.subplots()

ax.plot(x,y);
ax.set_xlabel('X-axis');
ax.set_ylabel('Y-axis');
ax.set_title('Line Plot');
```

#### 3. Multiple Plots on Same Figure

```python
x = np.linspace(0,10,100)
y1 = np.sin(x)    # Sine of each element in x
y2 = np.cos(x)    # Cosine of each element in x
y3 = x**2         # Square of each element in x (element-wise)

# Single Figure with multiple lines
plt.plot(x, y1, label='sin(x)', color='blue', linestyle='-')
plt.plot(x, y2, label='cos(x)', color='red', linestyle='--')
plt.plot(x, y3, label='x2', color='green', linestyle=':')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Multiple Lines')
plt.legend()
plt.grid(True, alpha=0.3)
```

![[Anatomy of Matplotlib figure.png]]

## 1.10 Pandas🎦📜👩🏽‍💻

## What is Pandas?

| **Aspect**                           | **Details**                                                                                               |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------- |
| **What it is**                       | The **#1 data manipulation library** in Python                                                            |
| **Core data structures**             | **Series** (1D) and **DataFrame** (2D — like a spreadsheet)                                               |
| **Why it matters for ML/AI**         | Data cleaning, preprocessing, feature engineering, exploratory data analysis (EDA)                        |
| **Why it matters for Cybersecurity** | Parsing logs, analyzing network traffic, processing threat intelligence feeds, handling security datasets |
| **Analogy**                          | Pandas = **Excel on steroids** with code                                                                  |

### Importing the Lib
```python
import pandas as pd  # Standard alias
import numpy as np   # Pandas builds on NumPy
```

### Core Data Structures
#### Series (1D)
```python
import pandas as pd

# Create a Series from a list
s = pd.Series([10, 20, 30, 40, 50])
print(s)

	# Output:
	# 0    10
	# 1    20
	# 2    30
	# 3    40
	# 4    50
	# dtype: int64

# Series with custom index
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(s)
	# a    10
	# b    20
	# c    30
	# dtype: int64
```

#### DataFrame (2D — Most Important!)
```python
# Create a DataFrame from dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, 30, 35, 28],
    'City': ['New York', 'London', 'Paris', 'Tokyo']
}
df = pd.DataFrame(data)
print(df)

# Output:
	#       Name  Age      City
	# 0    Alice   25  New York
	# 1      Bob   30    London
	# 2  Charlie   35     Paris
	# 3    Diana   28     Tokyo
```

### Reading Data
```python
# Read CSV file (most common)
df = pd.read_csv('network_logs.csv')

# Read Excel file
df = pd.read_excel('threat_intelligence.xlsx')

# Read JSON (API responses)
df = pd.read_json('alerts.json')

# Read from URL (threat feeds)
df = pd.read_csv('https://raw.githubusercontent.com/.../malware_data.csv')
```