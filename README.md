


*Balance between Privacy and Utility of data for analysis* 
1) L-Anonymity 
1.1 Tasks:  
a. Defining the reasonable hierarchies for the 4 Quasi-identifiers [age, education, marital
status and race] 

➢ Age: When you look at the raw adult data, exact ages are mentioned, those ages are 
generalized into specific intervals.

![image](https://github.com/user-attachments/assets/1654e581-a7af-4243-ae33-3aec7392351f)

The current level generalization in the age hierarchy is 2. 
The maximum level generalization in the age hierarchy is 4. 

➢ Education: There was no need to generalize the education attribute in the quasi-identifier. 
To quantify the analysis of the dataset by keeping the attribute as it is.

![image](https://github.com/user-attachments/assets/79765115-aa3f-4e3a-a9c1-ba902e355805)

The current level of generalization in the education hierarchy is 0. 
The maximum level of generalization in the education hierarchy is 3.

➢ Marital-status: The Marital Status has been generalized by combining numerous married 
statuses into a single 'married' category and This represents a mid-level generalization in 
which specific categories such as 'Married-civ-spouse', 'Married-spouse-absent', and 
'Married-AF-spouse' are combined into 'Married'. The other statuses, such as 'divorced', 
'never-married','separated', and 'widowed', are unique based on the data presented. 
Generalization focused on simplifying the representation of marriage.

![image](https://github.com/user-attachments/assets/c1da58f8-6126-4b5c-8395-20ccfd18ad94)

The current level generalization in the marital-status hierarchy is 1. 
The maximum level generalization in the marital-status hierarchy is 3. 

➢ Race: There was no need to generalize the race category such as 'White', 'Black', 'Asian
Pac-Islander', 'Amer-Indian-Eskimo', and 'Other' into broader categories and there was 
some missing data for this attribute in the adult data as mentioned in the instructions filling 
missing data with “Unknown”. In this Quasi-identifer attribute the level of generalization 
would create broader categories and might significantly reduce the racial and ethnic 
identity. Again it might lead to higher privacy and lower data utilization.

![image](https://github.com/user-attachments/assets/70f3adef-489e-4bea-90d6-627bbcf81487)

The current level generalization in the race hierarchy is 0. 
The maximum level of generalization in the race hierarchy is 2.

b. Write a program for the heuristic algorithm, which generalizes/suppresses the data for (k1, k2)- 
anonymity while minimizing the utility loss. You can use any programming language, e.g., Java, 
Python, and C++. You can also extend the DataFly or µ-Argus Algorithm

![image](https://github.com/user-attachments/assets/ae6ade4a-c769-4565-9890-03320346942a)
![image](https://github.com/user-attachments/assets/5ca5094a-1876-42a7-a333-49446f46913e)

Output Console: 
![image](https://github.com/user-attachments/assets/35020298-45e7-456a-b630-21d96373ca19)

• There were total of 32561 records of adult data, after using generalization techniques and 
following all the requiring conditions which have been mentioned in the assignment, we 
anonymized data after applying (k1, k2) – anonymity and data for utilization we have is 30766. 
• And also we have created the anonymized dataset as a “get_anonymized_dataset” 
• We will attach all the source code files and anonymized datasets in a zip folder while submission. 





