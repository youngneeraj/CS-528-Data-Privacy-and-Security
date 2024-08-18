


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

c. Calculate the distortion and precision of the output (k1 = 10, k2 = 5) based on your designed 
hierarchies and algorithm 

![image](https://github.com/user-attachments/assets/55188bd6-9df5-425a-b372-5c0d755beb24)

![image](https://github.com/user-attachments/assets/e78ce4f7-3ce7-41c1-a5a0-cb85b491ac67)

Output Console: 

• This code calculates the distortion and precision, and also we did manual calculations for better 
understanding according to the formulas provided in the pdfs.

Manual Calculation of Distortion and Precision: 

![image](https://github.com/user-attachments/assets/56769d87-e3d7-4e3b-ab8a-852a7681da17)

![image](https://github.com/user-attachments/assets/c2f2fc68-f849-4e39-9313-837f8a6c3bb5)

![image](https://github.com/user-attachments/assets/44f9de18-f166-425e-a4db-f5a6b385b306)

![image](https://github.com/user-attachments/assets/649a92da-018f-485a-a23e-bba572cabf30)


2 L-Diversity 
 
VGHs 
Education 

Level 0: Preschool, 1st-4th, 5th-6th, 7th-8th, 9th, 10th, 11th, 12th (without diploma), HS-grad, 
Some-college (no degree), Assoc-voc, Assoc-acdm, Bachelors, Masters, Prof-school, Doctorate. 

Level 1: Elementary: Preschool, 1st-4th, 5th-6th 
Intermediate: 7th-8th, 9th, 10th 
Secondary: 11th, 12th, HS-grad 

Level 2: Non-degree Postsecondary: Some-college, Assoc-voc, Assoc-acdm 
Undergraduate: Bachelors 
Graduate: Masters, Prof-school, Doctorate 

Level 3: * 
 
        Age 
        Level 0: exact ages(11,16,24, 46, 59 etc…) 
        Level 1: 11-20, 21-30, 31-40, 41-50, 51-60. 
        Level 2: 20-40, 40-60 
        Level 3: <40, <60 
        Level 4: * 
         
 
 Marital-status 

Level 0: Current Specific Levels: Married-civ-spouse, Divorced, Never-married, Separated, Widowed,              
Married-spouse-absent, Married-AF-spouse. 

Level 1: Married: Combining all married statuses (Married-civ-spouse, Married-spouse-absent, Married
AF-spouse) into a single 'Married' category, Divorced, Never-married, separated, widowed 

Level 2: Married, single , previously married 

Level 3: * 
         
Race 

Level 0: Specific Levels (Current): White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black. 

Level 1: Caucasian: This could include 'White' and possibly other groups classified under 'Other' that     
predominantly identify with Caucasian ancestry. 

African Descent: Combining 'Black' and potentially some individuals from 'Other' who identify with 
African ancestry. 

Asian/Pacific Islander: Keeping 'Asian-Pac-Islander' as a broad category that covers a wide range of 
ethnic groups from Asia and the Pacific Islands. 

Indigenous Peoples: This could potentially include 'Amer-Indian-Eskimo' and others who identify with 
indigenous groups from various regions. 

Other/Unknown: A catch-all category for those who do not fit into the above categories or whose race 
data is missing or unspecified. 

Level 2: *


2.1 Tasks: 

a. Write a program for the heuristic algorithm (which generalizes/suppresses the data for “Entropy `l - diversity” while minimizing the utility loss). You can use any programming language, e.g., 
Java,Python, and C++.

![image](https://github.com/user-attachments/assets/53ea9562-6a81-42ec-bd40-a917db68978d)

![image](https://github.com/user-attachments/assets/6d195342-1c8b-4f2b-b12d-6d6dd9d5c946)

![image](https://github.com/user-attachments/assets/917b9b48-5faf-4dd8-a05f-b1c11041f78a)

• In this program, we took the database that has been created by k – anonymity which is 
“get_anonymized_dataset” . 

• Implemented a code to obtain the Entropy l – diversity. The goal of Entropy l – diversity is nothing 
but as  it is a privacy model that enhances the k – anonymity. 

• Entropy is a measure of uncertainity and unpredictability that means higher entropy, higher 
unpredictability in the sensitive attribute  column in each equivalence class. 

• ENTROPY L DIVERSITY should be atleast log(l) 

• After Implementation of that code we have created the “generalized_dataset_l_diversity”  

• Ofcourse our dataset is huge,not all the equivalence classes will satisfy Entropy L Diversity 

• We will attach all the source code files and anonymized datasets in a zip folder while submission. 


Note:{For our own Educational Purposes} We have also implemented a code to calculate the 
Entropy for equivalence classes which are non diverse from our “generalized_datatset_l_diversity” 
for just reference how Entropy is calculated and also will provide manual calculation of one 
equivalence class.

![image](https://github.com/user-attachments/assets/504bd928-b80a-47a7-a042-6a436cf84a76)
![image](https://github.com/user-attachments/assets/4a7c3369-3876-4ac5-b477-c96b5d802436)















