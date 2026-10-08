write me a code for an application titled "Australian Aboriginal Language Explorer", which has a home page with options to navigate to "Explore Languages" and "Data". Under "explore languages", there should be a search bar which prompts "Search language, region, etc.", with a placeholder list below it that can be searched. Under "Data", there should be several headings, which show the number of languages (total), number of records by language status, the most represented regions by data, and distribution of languages across geographical area. This should count the number of languages in Australia, per state, how many are active in status or not, and how many languages are in each major region. Next to each line, include a # which describes what each line does.



Make a single-page home screen for a vocabulary-learning app. Its main action is "Practise now". Also show words learned this week, a dropdown to choose the language, a small progress chart, and a list of recent words. Use a clear visual hierarchy and keep the layout readable.



Write me code for a macbook application for exploring Australian Aboriginal languages. The home page should have a clear visual hierarchy, with buttons allowing to navigate to “Data” and “Language Search” pages. On the “data” page is a table with all available data on each language. There should also be graphs showing the abundance of languages per region. On the “language search” page is a search bar prompting to search for a language, region etc. There should be dropdown boxes to filter by region and by language status. The user can click on the language, which will take them to a small page with all the data for that one language. The layout should be modern and colourful.



can you add a readme file which explains installation, running, usage and testing.

where is the readme file? how does the user access it?

the readme should be accessible via the application. make it so that is possible. Under the "data" page there should be an option to click on "download README.md" which allows them to access the file.



I need you to help me build an application running via Streamlit called WA Aboriginal Language \& Country Explorer using the provided “pracset.csv” dataset. The application should help users explore publicly available Aboriginal language data through an easy-to-use interface. It must load the dataset from the CSV file and should include three main pages/views: Home, Explore Languages, and Data. The Explore Languages page should allow users to search and filter language records using a custom search/filter algorithm based on fields such as language name, state/territory and status, and display the matching records and relevant details. The Statistics \& Map page should perform meaningful analysis of the dataset, such as counting records by state/territory and status, calculating useful percentages, and displaying appropriate charts and a map using the available latitude/longitude data. The Home page should explain the purpose of the application and provide navigation. The application should handle missing data and invalid searches without crashing and include at least 8 automated tests covering the main functionality, search algorithm, analysis, data loading, invalid input and edge cases. Structure the code clearly, use functions for the main functionality, and include appropriate documentation, requirements, GitHub/deployment support, and an AI log. Use only verified information from the supplied dataset and recognised sources; do not generate Aboriginal cultural, language or historical content with AI. Before coding, inspect the actual dataset and use its real column names and values rather than assuming what the data contains.



make it so that the data file is imbedded within the application, so other users can access it without having to download the data themselves.

using pandas, create me a bar graph that shows the languages spoken per state (ie:, WA, NSW). Ensure it is colourful, has adequate headings and titles, and is easily readable. This should be on the "data" page.







This is my project manual as a pdf. Analyze it carefully. Below is the given proposal/idea me and my groupmates have created. Add onto it whatever new ideas/changes you think can score higher marks. Your priority should be adding on ideas, not changing. Remember, follow the rubric.



Idea:



Main idea: application that explores information, completes a task, answers questions or makes a decions 



Brief: language and country explorer – targets students and visitors, addresses lack of knowledge in students and tourists, users should be able to explore lots of Aboriginal language information, app needs to provide information on local languages and what certain words mean (large quantity of languages, a few examples words from each which are similar to others) 



Prepare data which includes a list of words from their respective languages.  



Present a usable interface which uses appropriate code and structuring, consistently uploaded to github, handles invalid cases, includes a README file which summarises the data presented and gives context to help others understand how its laid out 



Can compare the words side-by-side with other words, demonstrating similarities across languages 



How it analyses data: shows trends in language structure, showing how other languages may use similar words 



1\. Home screen (exploree languages, explore regions, compare data, take quiz), 2. page where they can search for data and find the details about each language (location, region, status), 3. calculates records in each region, analyses data for each place. 



Main algorithm: finds languages based on the main criteria searched by the user



I have attached the assignment instructions and brief as a text file. I have also attached the datasheet that will be used in this assessment. The data is from AIATSIS and provides Aboriginal and Torres Strait Islander languages and cultural collections, including AUSTLANG. I want you to completely analyze the documents, and understand exactly what is required from this assessment. Then you will carry out the tasks I give you.



This is the main idea for my part of the application:



&#x20;   Main idea: application that explores information, completes a task, answers questions or makes a decisons 



&#x20;   Brief: language and country explorer – targets students and visitors, addresses lack of knowledge in students and tourists, users should be able to explore lots of Aboriginal language information, app needs to provide information on local languages and what certain words mean (large quantity of languages, a few examples words from each which are similar to others) 



&#x20;   Can compare the words side-by-side with other words, demonstrating similarities across languages 



&#x20;   How it analyses data: shows trends in language structure, showing how other languages may use similar words 



&#x20;   Main algorithm: finds languages based on the main criteria searched by the user 



What I want you to do: get the data ready and make it smart.



Load the data into the app and clean it up (fix missing bits, keep only WA info)

Write the main algorithm: a function that compares words and works out how similar they are

Use that same function to make search smarter (still finds results even with typos)

Work out the stats: how many languages per region, language status breakdown

Make the charts/graphs that show this

Write tests for the algorithm and the data cleaning (about 4 tests)



While you write the code for the applications algorithms, explain exactly how I should be using GitHub throughout development, and if I have to do it multiple times, give me a step by step instruction list as to what to do with the code you have provided and how I should be using GitHub in relation to it.



Answer my questions:



1\) Should my csv file be in the same place as the other files? If so should I commit the csv data file to the github repository

2\) Why are all the code in different files? Explain why they are and if they shouldn't be in a single file, explain why they shouldn't be in one file

3\) I can't run all the files properly due to sloppy coding errors, I will provide them below, fix them or rewrite the code properly. I do not have time for errors. Remember, I am building an app.



Data loader:

PS C:\\Users\\mohit\\AppData\\Local\\Programs\\Microsoft VS Code> \& C:\\Users\\mohit\\AppData\\Local\\Python\\pythoncore-3.14-64\\python.exe "c:/Users/mohit/OneDrive - UWA/Documents/UWA/Units/Year 3/Sem 2/CITS1501/Project/data\_loader.py"

Traceback (most recent call last):

&#x20; File "c:\\Users\\mohit\\OneDrive - UWA\\Documents\\UWA\\Units\\Year 3\\Sem 2\\CITS1501\\Project\\data\_loader.py",line 109, in <module>

&#x20;   data = load\_austlang("austlang.csv")

&#x20; File "c:\\Users\\mohit\\OneDrive - UWA\\Documents\\UWA\\Units\\Year 3\\Sem 2\\CITS1501\\Project\\data\_loader.py",line 69, in load\_austlang

&#x20;   raise FileNotFoundError(f"AustLang data file not found: {filepath}")

FileNotFoundError: AustLang data file not found: austlang.csv

PS C:\\Users\\mohit\\AppData\\Local\\Programs\\Microsoft VS Code> 



Visualize:

The graphs are not visible, the code does not return any graph to me



The other files seem to run without any problems, but consider the fact that I am uploading this to github for others to see and use, and there should be no issue when they run the code.





