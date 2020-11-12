# Series Review app

## contents
- [Brief](#brief)
    - [Objective](#objective)
    - [Requirements](#requirements)
    - [Project Approach](#project-approach)
- [Architecture](#architecture)
    - [Entity Relationship Diagrams](#entity relationship diagrams)
- [Project Planning & User Stories](#project planning & user stories )


## Breif

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

## Architecture
### Entity Relationship Diagrams (ERD)
#### Plan

Below is shown ERD table for the project. My project will be connected to a GCP hosted MySQL server which will store the Series and Review 
details, allowing anyone to Create, Read, Update and Delete from the database. Relationship between tables is a one-to-many relationship as
1 series can have many reviews and 1 review cannot have many series attached to it. 

The inital plan for the ERD was consistent throughout the projects lifecycle and the project was delievered with the ERD shown below. No 
changes were needed to be made to the database as all functionalty requirements were met. 

## Project Planning & User Stories 

For the project a tool called Trello is being used as a planning tool to keep track of tasks and update what needed to be done or has been completed.
Trello is a free and easy to use platform that creates Kanban boards. Below is a screenshot of the Trello board and a link to the Trello board:


