# DevOps Core Practical Project
As part of my training to become a DevOps engineer at QA, I was asked to create an application that generates "Objects" upon a set of predefined rules. This application must be based on a service-orientated architecture, composed of four services.

These four services all rely on each other to function. Service one handles the front-end of the program while communicating with all the other services to produce an output to the user, while storing them in an SQL database. Service 2 and 3 produce the randomly generated objects that are then used to create the final output for the user in service 4.

The complexity of the program itself is rather simple, since an emphasis was placed instead on ensuring the correct technologies were implemented and functioning properly. These technologies include but are not limited to: 
 - Containerisation of modules via **Docker**, orchestrated by **Docker Swarm**
 - Server provision and task automation via **Ansible**
 - Load balancing via **NGINX**, allowing for the use of an reverse proxy
 - Automated testing and deployment via **Jenkins**, executed by GitHub **Webhooks**

# Contents

To be added at the end

# Software Design

This section will explore the varies methods used to plan the development of this project.

## Planning

Before any development commenced, a Kanban board was created on Trello. The board holds information on what's currently in development, who is working on it and where something is in the process. It also stores project resources, User stories and Minimum viable product (MVP) requirements.

![TrelloBoard](images/TrelloBoard.png)

## Database

As this program only makes use of one table, an entity-relation diagram cannot be created, and so an entity diagram below is shown instead.

![EntityDiagram](images/EntityDiagram.png)

The table has three attributes:
- id : Uniquely represents each entity and is the primary key of the table
- Numberplate : Stores the numberplate of the car
- Color : Stores the color of the car 

## Risk Assessment

A risk assessment was also carried out as a tool for identifying and preventing potential project risks. However, unanticipated risks are expected as in any project, and so risks as added while the program is in development. The two images below show the risks before and after development:

Before development:

![FirstRA](images/FirstRA.png)

After development:

![SecondRA](images/SecondRA.png)


## Test plans

Test plans were also designed to ensure all aspects of the program were tested. The table below explains how each service is expected to be tested.

![TestPlan](images/TestPlan.png)
