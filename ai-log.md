Team Members and Github Link 

The group members involved in the production of this application are Mohit Srungurapu and Luke Ogden. Our Github link is provided here. We have utilised Github collaboratively to save versions of our assignment and track the contributions of each member throughout the project. 

 

The Application and Target Audience 

The Aboriginal Language and Country Explorer is an interactive application designed to allow users to publicly explore information about Aboriginal languages in Australia. The application is intended primarily for students, visitors, and other users who want to explore language records through a simple and interactive interface. The application uses the supplied austlang.csv dataset and allows users to search and filter language records, explore information associated with individual records, and explore patterns in the dataset through statistics and visualisations. The application consists of three main views: Home, Explore Languages, and Data. The Home page introduces the purpose of the application and provides navigation. The Explore Languages page allows users to search and filter the dataset. The Data page provides analysis of the dataset and visual representations of geographical and categorical information. All Aboriginal cultural, language, and historical information presented by the application originates from information available via fair use on AITSIS website, allowing select criteria of data to be downloaded. 

 

Architecture and Data Flow 

The application follows a simple structure in which the user interacts with a Streamlit interface, which uses Python functions to process the dataset and perform various calculations including the creation of a graph. The main data flow is:  

User --> Streamlit Interface --> Python Functions --> Dataset --> Processed Results --> User Interface.  

The CSV dataset is stored separately from the main application code. When the application starts, Python reads austlang.csv using the Pandas library. The resulting data is then used by the different application pages. The Explore Languages page sends the user's search and filter selections to the relevant processing functions. These functions examine the dataset and return matching records. The Data page uses the same dataset to calculate counts, percentages and other summaries before presenting the results as a line graph. This structure separates the raw data from the application’s logic and allows the dataset to be updated without manually rewriting the program. 

 

Algorithms and Technical Decisions 

A major computational component of the application is the language search and filtering algorithm. Instead of relying entirely on a pre-built search function, the application processes the user's input and compares it against relevant fields in the dataset. The search algorithm checks whether the user's search term occurs within the language name, while additional filters can be applied to fields such as state or territory and status. Records that satisfy the selected conditions are returned to the user. The basic process is: 

Receive the user's search term and filter selections. 

Convert text to a consistent format so searches are not affected by capitalisation. 

Examine each relevant dataset record. 

Check whether the record satisfies the search and filter conditions. 

Add matching records to the results. 

Display the results to the user. 

The application also includes algorithms for analysing the dataset. For example, records can be grouped by state or territory and counted to identify how many records belong to each category. The program also accounts for missing data by showing edge cases where no information is available on a language, or where certain caterogies of information are unavailable. These decisions make the application more reliable and demonstrate processing beyond just simply displaying the raw dataset. 

 

Data Source and Preparation 

The application uses the supplied austlang.csv dataset. The dataset contains 1,183 records, exceeding the project requirement of at least 200 records, making a large database available to browse. 

The dataset contains the following fields: 

austlang_code 

primary_name 

Lat 

Lon 

state_territory 

Status 

The primary_name field is used for language searches, while state_territory and status provide opportunities for filtering and statistical analysis. Initial inspection identified missing values in some fields. In particular, some records are missing state or territory information. These values are not automatically treated as incorrect; instead, the application handles missing information appropriately depending on the feature being used. For example, records that are missing certain fields may be omitted from the data page, due to unreliability. The original source and licensing conditions of the dataset are available below: 

Original source: https://aiatsis.gov.au/research/languages/austlang 

Licence/usage conditions: Free usage 

This verification is particularly important because Aboriginal and Torres Strait Islander material must come from an appropriate recognised source and that copyright, licensing, access restrictions and cultural protocols must be considered. 

 

Analysis and Visualisation 

The application performs analysis to provide information that is more useful than simply displaying individual records. One analysis groups records according to state or territory and calculates the number of records in each category. This allows users to see how the records in the dataset are distributed geographically. The application can also analyse records according to their status, allowing users to see the distribution of different status categories. The results are presented using suitable visualisations such as line graphs. The line graphs provide a clear comparison between categories. The visualisations are intended to help users identify patterns in the dataset that may be less obvious when looking at individual rows of the CSV file. 

 

Interface and User Experience 

The application has three main views designed to provide a simple progression from introduction to exploration and analysis. The Home page introduces the purpose of the application and explains what users can do. Navigation is provided so that users can move between the different sections. The explore languages page provides the main interactive search functionality. Users can enter a language name and apply filters to narrow the results. Matching records are displayed in a list, allowing users to explore the available information. The data page presents calculations and visualisations derived from the dataset. Users can view statistical summaries, charts and geographical information. The interface overall is designed to avoid unnecessary complexity. User input is handled through interactive controls such as search boxes and selection menus, while feedback is provided through the displayed results. Missing information is handled without causing the application to crash. 

 

Testing and Limitations 

As required, we have prepared 8 tests. They are as follows: 

Correct loading of the CSV dataset. 

Confirmation that the dataset contains the expected minimum number of records. 

Successful search for an existing language. 

Search returning no results for an unavailable term. 

Correct filtering by state or territory. 

Correct application of multiple filters. 

Correct calculation of statistical results. 

Appropriate handling of missing or invalid data. 

The application however has several limitations. The quality and completeness of the results depend on the supplied dataset. Some records may be missing certain information, which can be confusing to some users. The application is also limited to the information contained within the selected dataset and verified supporting sources, and as such it should not be interpreted as a complete representation of all Aboriginal languages, cultures or Countries. 

 

Security and Privacy 

The application does not require users to provide sensitive personal information. The dataset is used for informational and educational purposes and does not require user accounts or passwords. User input, particularly search terms and filter selections, is processed by the application rather than being directly incorporated into the code that is executed. This reduces the risk associated with unexpected inputs. No passwords, API keys or other confidential credentials should be stored in the GitHub repository. The project also considers cultural and ethical data-use requirements. Aboriginal and Torres Strait Islander cultural, language and historical information should only be used when the source, permission and usage conditions are clear. The application does not generate cultural or historical information using AI, in accordance with the project requirements. 

 

Deployment 

The completed application is intended to be deployed so that it can be accessed outside the development environment. The application is built using Streamlit and can therefore be hosted as a web application. The deployed application will include the Python source code, dataset and required dependencies so that the application functions correctly outside the local development environment.  

Deployment platform: Local session in browser 

Application URL: http://127.0.0.1:63061/ 

Before final deployment, the application should be tested in the deployed environment to ensure that the CSV file is loaded correctly and that all pages, searches, visualisations and other functionality operate as expected. 

 

11. Team Contributions 

The project was developed collaboratively, with both team members contributing to the design, development, testing and documentation of the application. 

Luke Ogden: 

Basic application design, architecture and layout of the three pages 

Search algorithm 

Creation of line graphs 

Mohit Srungurapu: 

Data gathering + compiling 

Creation of pie chart, line graph of distribution by state, and distribution plot 

Made automated tests 

Both: 

This final report, each section worked on by the respective member who completed the certain aspect/s 

README.md file 

 

GitHub was used throughout development to record individual contributions and manage changes to the project. Both team members also developed an understanding of the complete application so that we could explain the design, algorithms, dataset, testing and technical decisions during the demonstration and Q&A.  

Overall, the combined efforts of both group members contributed to the synthesis of a well-functioning application which enables audiences to securely access information regarding Aboriginal languages, and can utilise an application that works successfully each time. 
