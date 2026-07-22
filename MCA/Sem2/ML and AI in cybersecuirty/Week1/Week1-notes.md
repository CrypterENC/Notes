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