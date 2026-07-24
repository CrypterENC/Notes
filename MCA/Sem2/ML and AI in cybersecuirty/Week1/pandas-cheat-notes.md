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