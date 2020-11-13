# Series Review app

## Contents
- [Brief](#brief)
    - [Objective](#obj)
    - [Requirements](#reqs)
    - [Project Approach](#approach)
- [Architecture](#arch)
    - [Entity Relationship Diagrams](#erd)
    - [CI Pipeline](#ci)
- [Project Planning & User Stories](#use_case)
- [Risk Assessment](#risks)
    - [Explanation](#risk-exp)
- [Testing](#test_)
    - [Unit testing](#utest)
- [Deployment](#depl)
- [Technologies used](#tech)
- [Front end Design](#FE)
    - [Page: Home](#home)
    - [Page: Add Series name](#addSN)
    - [Page: Review Series](#revS)
    - [Page: View Review](#virev)
- [Future Improvements](#improve)

<a name="breif"></a>
## Breif

<a name="obj"></a>
### Objective
The objective of the DevOps Core Fundamental Project is to create a CRUD application with utilisation of supporting tools,
methodologies and technologies that encapsulate all core modules we have covered up until week 5 of the Training Academy.

Core concepts to involve:
- **Project Management**
- **Python Fundamentals**
- **Python Testing**
- **Git**
- **Basic Linux**
- **Python Web Development**
- **Continuous Integration**
- **Cloud Fundamentals**
- **Databases**

<a name="reqs"></a>
### Requirements 
- A Trello board (or equivalent Kanban board tech) with full expansion
on user stories, use cases and tasks needed to complete the project.
It could also provide a record of any issues or risks that you faced
creating your project.
- A relational database used to store data persistently for the
project, this database needs to have at least 2 tables in it, to
demonstrate your understanding, you are also required to model a
relationship.
- Clear Documentation from a design phase describing the architecture
you will use for you project as well as a detailed Risk Assessment.
- A functional CRUD application created in Python, following best
practices and design principles, that meets the requirements set on
your Kanban Board
- Fully designed test suites for the application you are creating, as
well as automated tests for validation of the application. You must
provide high test coverage in your backend and provide consistent
reports and evidence to support a TDD approach.
- A functioning front-end website and integrated API's, using Flask.
- Code fully integrated into a Version Control System using the
Feature-Branch model which will subsequently be built through a CI
server and deployed to a cloud-based virtual machine.

<a name="approach"></a>
### Project Approach
My project focuses on creating a website where you can review a list of series that you may have watched for others to read. 
This will consist of users being able to: 

- Create and add a series name
    -**Title** of the series
- Create and add a review to any listed series
    - **Description** of the series
    - **Rating** of the series 
- View and update series name 
- Delete series and reviews

<a name="arch"></a>
## Architecture
<a name="erd"></a>
### Entity Relationship Diagrams (ERD)
#### Plan

Below is shown ERD table for the project. My project will be connected to a GCP hosted MySQL server which will store the Series and Review 
details, allowing anyone to Create, Read, Update and Delete from the database. Relationship between tables is a one-to-many relationship as
1 series can have many reviews and 1 review cannot have many series attached to it. 


<img src="/Documentation/ERD.png" alt="ERD" width="100%" height="100%"/>


The inital plan for the ERD was consistent throughout the projects lifecycle and the project was delievered with the ERD shown below. No 
changes were needed to be made to the database as all functionalty requirements were met. 

<a name="ci"></a>
### CI Pipeline

A CI pipeline was involved in the development and deployment of the project, a mock-up of this can be seen below.

<img src="/Documentation/CI Pipeline.png" alt="CI" width="100%" height="100%"/>

<a name="use_case"></a>
## Project Planning & User Stories 

For the project a tool called Trello is being used as a planning tool to keep track of tasks and update what needed to be done or has been completed.
Trello is a free and easy to use platform that creates Kanban boards. Below is a screenshot of the Trello board and a link to the Trello board:

[Trello Board](https://trello.com/b/siBc2gmV/fundamental-qa-project)

<img src="/Documentation/Trello Board.png" alt="Trello" width="100%" height="100%"/>

### Use Case Overview

<img src="/Documentation/Use case Overview.png" alt="Usecase" width="100%" height="100%"/>


<a name=risks></a>
## Risk Assessment

I have thought of a number of risks that my project may face and have categorised them below to analyse the risk, its impact, likelihood and the appropriate response to that risk. The risks can be seen as a combination of technical risks associate with the development side of the project and general risks that will directly or indirectly impact the project

| Risks                            | Likelihood    | Impact       |    Explanation          |
| -------------------------------- |:-------------:| :-----------:| -----------------------:|
| Lack of clear planning           | Low           | High         | [1 Click here](#plan)
|  Automation not working and potentially causing issues     | Medium        |   high     | [2 Click here](#auto)
| Problems with the development of the project        | Medium        |  High        | [3 Click here](#dev)
| Have insufficient GCP Credit   | Very Low     |    High | [4 Click here](#gcp)
| Issues with the implementation of the tests        |  Medium     |    Medium       | [5 Click here](#test)
| Loss of data due to Server or VM being shutdown   | Low     |    Medium | [4 Click here](#vm)
| Potential release of data (eg account info, private IP addresses or environment variables) when uploading        |  Very Low     |    High       | [5 Click here](#data)

<a name="risk-exp"></a>
### Risk Explanation
<a name="plan"></a>
#### Lack of clear planning
Building of web app can get complex down the line as the code source increases.
##### High impact
- Lack of clear planning will result to the project failing overall
##### Low Likelihood
- Difficulty of structuring a project will still learning the fundamentals of programming and app development
##### Response 
- Use of Jira to identify aim and be able to plan and track project progression
##### Revisit
- 

<a name="auto"></a>
#### Automation not working and potentially causing issues
Automation can save a lot of time and hussle if done right, however if not done properly it can have a:
#### Lack of clear planning
Building of web app can get complex down the line as the code source increases.
##### High impact
- Automation if not done right can slow development time
##### Medium Likelihood
- Due to my lack of experience I may write scripts that have many bugs and therefore needed to be fixed
##### Response 
- Ensure automation learning through python is at a sufficient level to debug an issue I may face
##### Revisit
- 

<a name="dev"></a>
#### Problems with the development of the project
Development part of the project is the most critical stage, the risks of running into issue are:
##### High impact
- Development is what makes the project. Thus, any issues within development will hinder project progress
##### Medium Likelihood
- Due to my lack of experience in app development I may run into a few problems during the development phase
##### Response 
- Solving problems as and when they take place. Ensure that I follow project plan to make tracing back steps easier in the case of an issue 
##### Revisit
- 

<a name="gcp"></a>
#### Have insufficient GCP Credit 
Running out of GCP credit for this project is very unlikely, however if I do the risks are:
##### High impact
- Running out of GCP credit if I leave multiple instances/databases up and running without stopping or deleting themprogress
##### Very Low Likelihood
- I start with $300 in free credit. If I am careful when using compute resources, I can make the credit last
##### Response 
- I will ensure that all instances are stopped and only activated when needed to save compute resources
##### Revisit
- 

<a name="test"></a>
#### Issues with the implementation of the tests 
Risks of inadequate tests will result to:
##### Medium impact
- One of the most critical parts of the project. May lead to me overseeing any issues with the app. 
##### Medium Likelihood
- Issues may arise during the testing phase and when the tests are running alongside other services 
##### Response 
- Ensure Unit testing learning is at a sufficient level to solve any implementation issues that may arise
##### Revisit
- 

<a name="vm"></a>
#### Loss of data due to Server or VM being shutdown 
Risks of GCP server shutting down will result to:
##### Medium impact
- The server/VM when shut down may cause downtime for the app
##### Very Low Likelihood
- The cloud provider is responsible for the upkeep of the servers/VMs. Unlikely to run into any issues 
##### Response 
- Ensure that I push an changes made to the source code to GitHub, ensuring that my code is always backed up
##### Revisit
- 

<a name="data"></a>
#### Potential release of data (eg account info, private IP addresses or environment variables) when uploading 
It is likely that I will be working on different VM machines, hence there will be a public Git repo. Hence, it is very likely that I may upload some credentils by mistake the risks are:
##### High impact
- If I accidentally release/misplace data then anyone can use this to access and manipulate the application 
##### Very Low Likelihood
- Unlikely that this risk may occur as I will be responsible to ensure this does not happen. Low possibility that data will fall into the wrong hands
##### Response 
- Ensure that I do not make a sensitive information public on GitHub or elsewhere and always follow best practices
##### Revisit
-


<a name="test_"></a>
## Testing 
Testing has been done using pytest. The coverage report for the backend is __. 


<a name="depl"></a>
## Deployment


<a name="tech"></a>
### Technologies Used
* Database: GCP SQL Server
* Programming language: Python
* Framework: Flask
* Deployment: Gunicorn
* CI Server: Jenkins
* Test Reporting: Pytest, Selenium
* VCS: [Git](https://github.com/aaboungab)
* Project Tracking: [Trello](https://trello.com/b/siBc2gmV/fundamental-qa-project)
* Live Environment: GCP


<a name="FE"></a>
## Front End Design

<a name="home"></a>
### Home Page
Clear home page consists of an Add series button and home button to redirect back to the homepage. 
<img src="/Documentation/home.png" alt="Usecase" width="100%" height="100%"/>


<a name="addSN"></a>
### Add Series Name Page
Clicking on the Add a Series button you will be redirect to the Add series page. 
<img src="/Documentation/Add a Series.png" alt="Usecase" width="100%" height="100%"/>

#### Home page after Adding series name
<img src="/Documentation/home-AddedSeries.png" alt="Usecase" width="100%" height="100%"/>


<a name="revS"></a>
### Review Series Page
#### Add review
Add a review by clicking on the Add review button on the home page. That will then redirect you to the add review page:

<img src="/Documentation/Add a review.png" alt="Usecase" width="100%" height="100%"/>

After adding your review you will be automatically redirected to the Review page where you can view your review and other reviews on the specific series:

<img src="/Documentation/viewreviewpage.png" alt="Usecase" width="100%" height="100%"/>



<a name="virev"></a>
### View Review Page
You can veiw reviews of each series by clicing  the view review button on the homepage:

<img src="/Documentation/viewreview button.png" alt="Usecase" width="100%" height="100%"/>


<a name="improve"></a>
## Improvements for the Future
