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

#### 📍DataFrame (2D — Most Important!)
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

### DataFrame Data Inspection
```python
# Quick overview
df.head()           # First 5 rows
df.tail()           # Last 5 rows
df.sample(10)       # Random 10 rows

# Information about dataset
df.info()           # Column names, data types, non-null counts
df.shape            # (rows, columns)
df.columns          # List of column names
df.dtypes           # Data types of each column

# Statistical summary
df.describe()       # Count, mean, std, min, 25%, 50%, 75%, max (only numeric)
df.describe(include='object')  # For categorical columns
```

## 1. Data Loading & Export Functions

|Function|What it does|Cybersecurity Use Case|
|---|---|---|
|`pd.read_csv()`|Load CSV file|Import network logs, IDS alerts, malware datasets|
|`pd.read_excel()`|Load Excel file|Read threat intelligence reports, compliance data|
|`pd.read_json()`|Load JSON file|Parse API responses from threat feeds (VirusTotal, Shodan)|
|`pd.read_html()`|Parse HTML tables|Scrape security advisories, CVE databases|
|`pd.read_sql()`|Query SQL database|Extract logs from SIEM databases|
|`df.to_csv()`|Save to CSV|Export processed datasets, share with team|
|`df.to_excel()`|Save to Excel|Create reports for management|
|`df.to_json()`|Save to JSON|Export for API integration|
|`df.to_sql()`|Write to SQL|Store processed data in database|

---

## 2. Data Inspection Functions

|Function|What it does|Cybersecurity Use Case|
|---|---|---|
|`df.head()`|First 5 rows|Quick glance at new dataset|
|`df.tail()`|Last 5 rows|Check end of dataset|
|`df.sample()`|Random rows|Randomly inspect data (audit)|
|`df.info()`|Column info, dtypes, non-nulls|Understand data structure|
|`df.shape`|(rows, columns)|Dataset size for capacity planning|
|`df.columns`|List of column names|Feature engineering reference|
|`df.dtypes`|Data types of each column|Ensure correct types (int vs object)|
|`df.describe()`|Statistical summary|Distribution analysis of traffic metrics|
|`df.describe(include='object')`|Stats for categorical data|Analyze attack types, protocols|
|`df.value_counts()`|Count unique values|Class distribution (benign vs malicious)|
|`df.nunique()`|Number of unique values|Unique IPs, ports, attack types|
|`df.memory_usage()`|Memory usage|Optimize for large datasets|

---

## 3. Data Selection Functions (CRITICAL!)

|Function|What it does|Cybersecurity Use Case|
|---|---|---|
|`df['col']`|Select single column|Access traffic_bytes, label|
|`df[['col1','col2']]`|Select multiple columns|Feature matrix creation|
|`df.loc[row_label]`|Select by **label** (inclusive)|Access specific connection|
|`df.loc['a':'c']`|Label range (INCLUSIVE)|Select connection ID range|
|`df.loc[:, 'col']`|Column by label|Access port column by name|
|`df.loc[:, ['col1','col2']]`|Multiple columns by label|Extract features by name|
|`df.loc['a':'c', 'col1':'col3']`|Row & column by label|Subset by connection ID and feature|
|`df.loc[df['col'] > value]`|Conditional filtering|Find high-traffic connections|
|`df.loc[condition, 'col'] = value`|Conditional assignment|Label malicious traffic|
|`df.iloc[row_position]`|Select by **integer position**|Quick access to nth row|
|`df.iloc[0:3]`|Position range (EXCLUSIVE)|First 3 rows for testing|
|`df.iloc[:, 0]`|Column by position|Access first column|
|`df.iloc[:, [0,2]]`|Multiple columns by position|Extract features by index|
|`df.iloc[1:4, 0:2]`|Row & column by position|Subset by position|
|`df.iloc[(df['col'] > value).values]`|Conditional with positions|Position-based filtering|
|`df.filter()`|Filter columns by name|Pattern-based column selection|
|`df.query()`|Query using string expression|Complex filters (e.g., "protocol == 'TCP' and bytes > 10000")|
|`df.sample()`|Random rows|Random auditing of traffic|
|`df.nlargest()`|Top N rows by column|Top bytes sent (potential exfil)|
|`df.nsmallest()`|Bottom N rows by column|Smallest traffic (potential scanning)|

---

## 4. Data Cleaning Functions

|Function|What it does|Cybersecurity Use Case|
|---|---|---|
|`df.isnull()`|Check null values|Find missing data in logs|
|`df.isnull().sum()`|Count null per column|Missing data assessment|
|`df.dropna()`|Drop rows with nulls|Remove incomplete logs|
|`df.dropna(axis=1)`|Drop columns with nulls|Remove unusable features|
|`df.fillna(value)`|Fill nulls with value|Impute missing data|
|`df.fillna(df['col'].mean())`|Fill with mean|Impute average bytes|
|`df.fillna(df['col'].median())`|Fill with median|Impute robust central value|
|`df.fillna(method='ffill')`|Forward fill|Fill time series gaps|
|`df.duplicated()`|Check duplicates|Find duplicate logs|
|`df.drop_duplicates()`|Remove duplicates|Deduplicate connections|
|`df.drop_duplicates(subset=['col'])`|Remove duplicates on specific columns|Deduplicate by IP pairs|
|`df.rename(columns={})`|Rename columns|Standardize column names|
|`df.replace()`|Replace values|Replace malicious codes|
|`df.astype()`|Change data type|Convert to category/float|

---

## 5. Data Manipulation & Feature Engineering Functions

|Function|What it does|Cybersecurity Use Case|
|---|---|---|
|`df['new_col'] = expr`|Create new column|Feature creation (e.g., bytes_per_second)|
|`df.assign()`|Create multiple columns|Bulk feature creation|
|`df.apply(func)`|Apply function to rows/cols|Custom feature transformation|
|`df.apply(lambda x: ...)`|Apply lambda function|Quick transformations|
|`df.groupby('col')`|Group by column|Aggregation by attack type|
|`df.groupby('col').agg(['mean','sum'])`|Aggregations|Summary statistics by label|
|`df.groupby('col').agg({'col1':'mean','col2':'sum'})`|Multiple aggregations|Complex summaries|
|`df.pivot_table()`|Pivot table|Cross-tabulation of features|
|`df.merge()`|SQL-style join|Combine threat intelligence|
|`df.merge(df2, on='col')`|Inner join|Enrich logs with threat data|
|`df.merge(df2, how='left')`|Left join|Add threat scores without losing data|
|`df.concat([df1, df2])`|Concatenate|Combine multiple log files|
|`df.sort_values()`|Sort by column|Sort by time or bytes|
|`df.sort_index()`|Sort by index|Sort by connection ID|
|`df.set_index()`|Set index|Make connection_id index|
|`df.reset_index()`|Reset index|Convert index to column|
|`df.pipe()`|Chain functions|Pipeline transformations|

---

## 6. Time Series Functions (Critical for Security Logs!)

|Function|What it does|Cybersecurity Use Case|
|---|---|---|
|`pd.to_datetime()`|Convert to datetime|Parse timestamp columns|
|`df['col'].dt.hour`|Extract hour|Hour of attack analysis|
|`df['col'].dt.dayofweek`|Extract day of week|Day patterns of attacks|
|`df['col'].dt.is_month_end`|Month end|Monthly attack trends|
|`df.resample('H')`|Resample by hour|Aggregate per hour|
|`df.resample('D').sum()`|Daily aggregation|Daily traffic summaries|
|`df.rolling(window=10)`|Rolling window|Smoothing traffic patterns|
|`df.shift(1)`|Shift data|Lag features for prediction|
|`df.diff()`|Difference|Rate of change analysis|

---

## 7. String Operations (Text Analysis)

|Function|What it does|Cybersecurity Use Case|
|---|---|---|
|`df['col'].str.contains()`|Contains pattern|Find suspicious URLs|
|`df['col'].str.startswith()`|Starts with|Check URL prefix|
|`df['col'].str.endswith()`|Ends with|Check file extensions|
|`df['col'].str.split()`|Split string|Extract domain from email|
|`df['col'].str.extract()`|Extract pattern|Regex extraction|
|`df['col'].str.len()`|String length|URL length analysis|
|`df['col'].str.lower()`|Lowercase|Normalize text|
|`df['col'].str.replace()`|Replace|Clean logs|

---

## 8. Statistical & Aggregation Functions

|Function|What it does|Cybersecurity Use Case|
|---|---|---|
|`df['col'].sum()`|Sum|Total bytes transferred|
|`df['col'].mean()`|Mean|Average packet size|
|`df['col'].median()`|Median|Median traffic volume|
|`df['col'].std()`|Standard deviation|Traffic variability|
|`df['col'].var()`|Variance|Traffic volatility|
|`df['col'].min()`|Minimum|Smallest connection|
|`df['col'].max()`|Maximum|Largest connection|
|`df['col'].count()`|Count|Number of connections|
|`df['col'].nunique()`|Unique count|Unique IPs, ports|
|`df['col'].mode()`|Mode|Most common value|
|`df['col'].quantile()`|Quantile|Percentile analysis|
|`df['col'].corr()`|Correlation|Feature correlation|
|`df['col'].cov()`|Covariance|Covariance between features|
|`df.agg(['mean','std'])`|Multiple aggs|Comprehensive stats|
|`df.cumsum()`|Cumulative sum|Running total bytes|
|`df.cummax()`|Cumulative max|Peak traffic|

---

## 9. Handling Categorical Data

|Function|What it does|Cybersecurity Use Case|
|---|---|---|
|`df['col'].astype('category')`|Convert to category|Save memory for protocols|
|`df['col'].cat.codes`|Numeric codes|Encode for ML|
|`pd.get_dummies()`|One-hot encode|Create binary features|
|`df['col'].value_counts()`|Count values|Distribution of attacks|

---

## 10. Index Operations

|Function|What it does|Cybersecurity Use Case|
|---|---|---|
|`df.set_index('col')`|Set index|Make timestamp index|
|`df.reset_index()`|Reset index|Convert index to column|
|`df.index`|Access index|View current index|
|`df.rename_index()`|Rename index|Custom index names|
|`df.sort_index()`|Sort by index|Sort by connection ID|

---

## 11. MultiIndex (Hierarchical Indexing)

|Function|What it does|Cybersecurity Use Case|
|---|---|---|
|`df.set_index(['col1','col2'])`|Multi-level index|Index by (src_ip, dst_ip)|
|`df.xs('value', level='col')`|Cross-section|Select by level|
|`df.loc[(val1, val2)]`|Loc with MultiIndex|Access multi-index|
|`df.unstack()`|Unstack levels|Pivot data|

---

## 12. Memory & Performance Functions

|Function|What it does|Cybersecurity Use Case|
|---|---|---|
|`df.memory_usage()`|Memory usage|Optimize large datasets|
|`df.info(memory_usage='deep')`|Detailed info|Memory profiling|
|`pd.read_csv(chunksize=)`|Chunk reading|Process huge log files|
|`df.astype('category')`|Category memory|Reduce memory for strings|
|`df.select_dtypes()`|Select by dtype|Separate numeric/categorical|

---

## 13. Visualization Integration (Pandas + Matplotlib)

|Function|What it does|Cybersecurity Use Case|
|---|---|---|
|`df.plot()`|Plot lines|Traffic over time|
|`df.hist()`|Histogram|Distribution of bytes|
|`df.boxplot()`|Box plot|Outlier detection|
|`df['col'].value_counts().plot(kind='bar')`|Bar chart|Attack counts|
|`df.corr()`|Correlation matrix|Feature correlation|
|`df.plot.scatter()`|Scatter plot|Feature relationships|