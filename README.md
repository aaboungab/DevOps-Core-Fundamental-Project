# Series Review app
# Author
## Anas Aboungab

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


<img src="/Documentation/ERD-db.png" alt="ERD" width="100%" height="100%"/>


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

### Use Stories Overview
Below are entailed a series of user stories according to the planned uses for the application and their level of requirement according to a MoSCoW (Must, Shoud, Could, Would) scale

|  | User Stories and their MoSCoW |
| ------ | ------ |
| MUST | As a user, I want to be able to access the app online |
| MUST | As a user, I want to be able to create reviews on the app |
| SHOULD | As a user, I want to be able to read reviews on the app |
| SHOULD | As a user I want to be able to update my reviews on the app |
| SHOULD | As a user I want to delete my reviews on the app |
| COULD | As a user, I want to access the web on a mobile devices|


<a name=risks></a>
## Risk Assessment

I have thought of a number of risks that my project may face and have categorised them below to analyse the risk, its impact, likelihood and the appropriate response to that risk. The risks can be seen as a combination of technical risks associate with the development side of the project and general risks that will directly or indirectly impact the project

[Excel version](https://docs.google.com/spreadsheets/d/1PkbGO7We7VWNwiyrE6rUQE0_KDZOs-1CUOdsQAjmLcc/edit#gid=0)
<img src="/Documentation/Risk Table.png" alt="CI" width="100%" height="100%"/>


<a name="test_"></a>
## Testing (Unit Testing)
Testing of my web app has been done by using Pytest and Selenium. The pytest had a test coverage report of 85%. With Pytest I was able to test most functions of my web app



<a name="depl"></a>
## Deployment
INCOMPLETE

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
Future improvements for the project would mostly be focused on the development stage. As the source code grew for my application it became more difficult to navigate around and due to my lack of knowledge and experince it was hard to keep up. In the future I can: 

- Seperate my routes.py file. Each route can be subdivided in their own category where Add review can be in its own file
- The current state of the app is fairly simple, in the future I would hope to add more functionalities or more complex services to the ones already in place. I would also improve general layout/design of the .html pages by using CSS or Bootstrap
- Use of integrated testing in the future as some of the services cannot currently be tested or must be tested when run as a Flask app (without Docker/Jenkins) as this would make the app more stable.
- Make my web app Mobile friendly, since most websites today are accessed over mobile



