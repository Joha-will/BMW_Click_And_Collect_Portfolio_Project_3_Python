# **BMW Click and Collect** 
![headimg](https://user-images.githubusercontent.com/98041941/185298467-6c1f21c8-86a8-4763-9eaf-26f5ed0fa02c.png)
- Live links to the project, Github and Heroku.
    - [https://github.com/Joha-will/Portfolio-Project-3-Python-Essentials-](https://github.com/Joha-will/Portfolio-Project-3-Python-Essentials-)
    - [https://bmw-click-and-collect.herokuapp.com/](https://bmw-click-and-collect.herokuapp.com/)
---
## **Table of Contents**
- [Introduction](https://github.com/Joha-will/Portfolio-Project-3-Python-Essentials-#introduction)
- [Technical Design](https://github.com/Joha-will/Portfolio-Project-3-Python-Essentials-#technical-design)
    - Flow Chart
- [How to use](https://github.com/Joha-will/Portfolio-Project-3-Python-Essentials-#how-to-use)
- [User Experience (UX)](https://github.com/Joha-will/Portfolio-Project-3-Python-Essentials-#user-experience-ux)
    - Target Audience
    - User Stories
    - Site owner goals
- [Features](https://github.com/Joha-will/Portfolio-Project-3-Python-Essentials-#features)
- [Technologies Used](https://github.com/Joha-will/Portfolio-Project-3-Python-Essentials-#technologies-used)
    - Frameworks and Tools
- [Testing](https://github.com/Joha-will/Portfolio-Project-3-Python-Essentials-#testing)
    - Bugs and Errors found
    - Solved Bugs
    - Remaining Bugs
    - Validator Testing
- [Deployment](https://github.com/Joha-will/Portfolio-Project-3-Python-Essentials-#deployment)
    - Using GitHub and GitPod
    - Forking the GitHub Repository
    - Deployment to Heroku
    - Creating a Heroku account
    - Configuring settings Heroku
    - Deploy section
- [Credits](https://github.com/Joha-will/Portfolio-Project-3-Python-Essentials-#credits)
    - Code
    - Content
    - Acknowledgments
---

## **Introduction**
Welcome to my third project, which is a command-line user interface application built mainly using python.

What inspired me to build this app was having the motivation to independently create an idea, put it 
together and make it work. This idea also came from the love and interest I have for BMW cars. At 
the planning phase of my third project I was unsure of what I was going to build which made very challenging as well as being a novice using python. However, I stayed motivated and focused and created this project which I learned a lot from and it has helped me to gain more experience and skills with the python language. 

In this README I will detail the steps I took to develop and create this project, with the use of  screen photos, images, links, charts and more.
This project is for education purposes only, this is not a product of BMW.

Thank you for viewing my project.

I hope you find the application useful!

---

## **Technical Design**

**Flow Chart**  

The aim of this flow chart which was created in the planning phase was to help with the development of the project. It assistted me several times with working out the logics and how each function would work when the application is being used.
![BMW_Click_and_collect (1)](https://user-images.githubusercontent.com/98041941/185299225-574d508a-b8b1-45c7-87f1-9804a2c645d9.jpeg)

---

## **How to use**
This BMW click and collect app, is used for making car orders and getting them prepared for collection at your nearest
store in your current town or city. To use this app, you need to follow the instructions on the screen and
fill out the input fields with the information needed in the correct format. The app will provide the list of cars available for you to choose from as well as, alerting you with messages if you enter invalid data in the input fields. Once you are happy with your choice of car and you have successfully completed your order. The app provides a detailed message on what you need to do for the collection process.

---

## **User Experience (UX)**


### **Target Audience**
- This application is targeted to people age 17 or older which is the legal age in the United Kingdom. 

- This application is not gender specific. 

- This application is targeted to people who want to buy a BMW car. 

- This application is targeted to people who are time restricted. 

- This application is targeted to the citizens of the United Kingdom. 

### **User Stories**
- As a user of the app, I want to have clear instructions on how to use the app.
- As a user of the app, I want to easily navigate around without difficulty.
- As a user of the app, I want to be made aware of any invalid data I input and how to rectify it.
- As a user of the app, I would like an easy way of ordering a car and get it prepared for collection.
- As a user of the app, I would like a reference to show as proof of order.
- As a user of the app, I would like to see the cars that's available for me to order.
- As a user of the app, I would like to get information or a description of the car I am ordering.

### **Site owner goals**
- As the site owner I would like an automated click and collect which enables the users to easily place an order and collect at the location nearest them. 
- As the site owner I would like an application to provide clear instructions for making an easy ordering process for the users. 
- As the site owner I would like an applcation to be able to perform the click and collect process successfully with little or no employee input to allow employees to focus on larger scaled jobs. 

---

## **Features**
- This BMW click and collect application has a title in font design 'ANSI shadow' which was created using [Patorjk](https://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=BMW%20CLICK%20AND%20COLLECT) and a BMW car logo which was created using [ASCII Art Generator](https://asciiart.club/). A link to the screenshot of the logo can be found below.
    - [Logo Screenshot](https://github.com/Joha-will/Portfolio-Project-3-Python-Essentials-/blob/main/assets/images/bmwlogo.png)
- This BMW click and collect application has functions that gives users warning messages when they have entered invalid data. The messages is displayed with a red background which make the warning more visiable. This background effect was implemented using [Colorama](https://pypi.org/project/colorama/). A link to the screenshot of the background colour effect can be found below.
    - [Background Colour Effect](https://github.com/Joha-will/Portfolio-Project-3-Python-Essentials-/blob/main/assets/images/bugfound1.png)
- This BMW click and collect application sends the users completed orders to the company's googlesheet via an API which is saved and used for the preparation of customers orders. A link to the screenshot of the company's googlesheet can be found below.
    - [Googlesheet Screenshot](https://github.com/Joha-will/Portfolio-Project-3-Python-Essentials-/blob/main/assets/images/googlesheet.png)
- This BMW click and collect application has a Typewriter effect which makes the app more captivating and user friendly.
- This BMW click and collect application has a list of cars that is shown to the users upon request. A link to the screenshot of the car list can be found below.
    - [Car list Screenshot](https://github.com/Joha-will/Portfolio-Project-3-Python-Essentials-/blob/main/assets/images/cartable.png)
- This BMW click and collect application supplies a reference number and more information about the car collection once they have completed their order. A link to the screenshot of the information can be found below.
    - [Information Screenshot](https://github.com/Joha-will/Portfolio-Project-3-Python-Essentials-/blob/main/assets/images/referencenumber.png)
- This BMW click and collect application provides users with the option of getting a description of the car. A link to the screenshot of the description can be found below.
    - [Description Screenshot](https://github.com/Joha-will/Portfolio-Project-3-Python-Essentials-/blob/main/assets/images/descriptionshot.png)

---

## **Technologies Used**

- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
    - This was the main tool used to build this project.

### **Frameworks and Tools**
- [Patorjk](https://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=BMW%20CLICK%20AND%20COLLECT)
    - This was used to create the logo for the application that is displayed to the users in the terminal.
- [ASCII Art Generator](https://asciiart.club/)
    - This was used to convert the image of a BMW car in text (ASCII art), which is displayed below the logo in the terminal.
- [Colorama](https://pypi.org/project/colorama/)
    - This was installed and imported to apply a red background to warning messages, when ever users enters invalid data into the input fields.
- [Lucidchart](https://www.lucidchart.com/pages/landing?utm_source=google&utm_medium=cpc&utm_campaign=_chart_en_tier1_mixed_search_brand_exact_&km_CPC_CampaignId=1490375427&km_CPC_AdGroupID=55688909257&km_CPC_Keyword=lucidchart&km_CPC_MatchType=e&km_CPC_ExtensionID=&km_CPC_Network=g&km_CPC_AdPosition=&km_CPC_Creative=442433236001&km_CPC_TargetID=kwd-33511936169&km_CPC_Country=9045685&km_CPC_Device=c&km_CPC_placement=&km_CPC_target=&gclid=Cj0KCQjwgO2XBhCaARIsANrW2X3bXE7BqWPDkzDIXS4AFQGgJwkcG8yWrLUkoUtT7-FWVojw5AIchkEaArzYEALw_wcB)
    - This was used in the planning phase of the project to create a web-base diagram, which explains how the application would work.
- [Python Tutor](https://pythontutor.com/)
    - This was used to help with the understanding of the python language, by visualizing code execution.
- [Google Sheets](https://www.google.com/sheets/about/)
    - This was used to store data sent from python via an application programming interface.
- [PEP8 Python Validator](http://pep8online.com/)
    - This was used to check the python code for any errors or warnings.
- [Heroku](https://heroku.com/)
    - This was used to deploy this application.
- [Gitpod](https://gitpod.io/)
    - This was the development environment used to build this project.
- [Git](https://git-scm.com/)
    - This is a version control system which I used to handle my project throughout the development stages, to save and push my work from gitpod to github.
- [Github](http://github.com/)
    - This was used to store my project after it was saved and pushed from gitpod.

---

## **Testing**
This project was tested manually by using the following methods:
- The PEP8 python validator was used to test the python code for this project and there are no errors, warnings or potential problems within the project.
    - [PEP8 Python Validator Results](https://github.com/Joha-will/Portfolio-Project-3-Python-Essentials-/blob/main/assets/images/Screenshot%202022-08-15%20at%2007.17.48.png)

- Tested all input fields by intentionally entering invalid data. For example:
    - Entering integers where strings are required and vice versa.
    - Entering special characters where only numbers and letters are required.
    - Entering data that's not specific to inputs fields that requests specific data.
    - Entering the same input numerous times.
- Tested in my local terminal as well as the Heroko terminal.

- I asked three family members to use the app to monitior if they would encounter any errors which was good for the testing.

### **Bugs and Errors found**

**Solved Bugs**
- By entering invalid data into the input fields I was able to test this project for errors. I encountered a problem with the validate_order function. I entered the
  invalid data several times and the function successfully notified the user with error messages, that the data being entered was invalid. I then entered the
  correct data which was accepted however, it kept repeating the invalid data message and was not running the next function. A link to the screenshot of the errors I encountered can be found below.
  - [Validate_order function(Errors)](https://github.com/Joha-will/Portfolio-Project-3-Python-Essentials-/blob/main/assets/images/bugfound1.png)

    1. However, this bug was successfully found and rectifed. The bug came from an error in the except ValueError statment because, I called the make_order function without a (return), so the function was not ending. A link to the screenshots of the validate_order function before and after the problem was rectified can be found below.
    - [Validate_order function(Before)](https://github.com/Joha-will/Portfolio-Project-3-Python-Essentials-/blob/main/assets/images/prefunction.png)
    - [Validate_order function(After)](https://github.com/Joha-will/Portfolio-Project-3-Python-Essentials-/blob/main/assets/images/postfunction.png)

- I found a ValueError in the validate_age function. I encountered this problem by trying to enter letters into the input field of the user_age function, which only accepted numbers
  and this lead the application to break. A link to the screenshot of the errors I encountered can be found below.
  - [Validate_age function(Errors)](https://github.com/Joha-will/Portfolio-Project-3-Python-Essentials-/blob/main/assets/images/valueerror.png)

    1. However, this ValueError was successfully found and rectifed. The ValueError came from the user_age function. I implemented the (int()) function which took the input() function as a argument, so this meant that the input function was only taking numbers as valid data. I rectified this by removing the (int()) function from the (input()) function and I implemented different methods and functions to the try except  statments to check if the data being entered by users met the age requirements. A link to the screenshots of both user_age function and the validate_age function before and after the problem was rectified, can be found below.
    - [User_age and Validate_age function(Before)](https://github.com/Joha-will/Portfolio-Project-3-Python-Essentials-/blob/main/assets/images/ageerror1.png)
    - [User_age and Validate_age function(After)](https://github.com/Joha-will/Portfolio-Project-3-Python-Essentials-/blob/main/assets/images/ageerror2.png)

**Remaining Bugs**
- No remaining bugs

**Validator Testing**
- PEP8
    -  When the PEP8 validator first checked the project's code, it found errors. The following three errors were discovered:
        1. line too long
        2. too many blank lines
        3. trailing whitespace
    - However, I rectified these by performing the following:
        1. To rectify the line too long error, I had to  use multiline comments and compress the project's code so that it did not exceed the allowed characters per line.
        2. To rectify the too many blank lines error, I thouroughly went through the project's code and deleted any unnecessary the blank lines.
        3. To rectify the trailing whitespace error, I thouroughly went through the project's code and removed the  trailing whitespaces. 
    -  A link to the screenshot of the errors I encountered can be found below.
        - [PEP8 Validator Errors](https://github.com/Joha-will/Portfolio-Project-3-Python-Essentials-/blob/main/assets/images/pep8results.png)

---

## **Deployment**

### **Using GitHub and GitPod**
The main branch of this repository has been used for the deployed version of this application.
As instructed by Code Institute, I used the Python Essentials Template that was provided.
- [Python Essentials Template](https://github.com/Code-Institute-Org/python-essentials-template)

The following steps were used to create a repository, setup a workspace and use Github and Gipod.
- Click the Use this Template button.
- Give your repository a name, and description is you wish.
- Click the Create repository from template button to create your repository.
- Click the Gitpod button to create a Gitpod workspace, this could take a few minutes.
- When working on the project using Gitpod, it is best to open the workspace from Gitpod as this will open your previous workspace instead of creating a new one.
    - You can commit your work using the following commands:
        1. git add . - adds all updated files to a staging area.
        2. git commit -m " Add short message explaining your commit" - commits all changes to a local repository.
        3. git push - pushes all your commmited changes to your Github repository.

### **Forking the GitHub Repository**
By forking a GitHub repository you can make a copy of the original repository to your own GitHub account to view and make changes without making any changes to the original repository.

1. Log in to GitHub and local the GitHub repository.
2. At the top right of the page, locate "fork button" which is just below the bell icon.
3. You should now have a copy of the original repository in your GitHub account.

### **Deployment to Heroku**

For the project to run on Heroku, there is a list of dependencies that needed to be installed before deploying the project.

The list of dependencies goes into the requirements.txt file by using the following:
-  pip3 freeze > requirements.text

**Creating a Heroku account**
- Go to [Heroku.com](https://heroku.com/) and create an account.
- From the Heroku dashboard click Create New App button.
- Enter a name for the project and select your region.
- Click the Create App button.

**Configuring settings Heroku**
- After creating app, click the Settings button on the horizontal nav bar at the top.
- Go to Config Vars and click the Reveal Config Vars button.
- In the field for KEY, enter CREDS in all capital letters.
- In the field for VALUE, go to your Gitpod workspace, click on creds.json file, copy the entire cred.json file, go back to Heroku and paste the cred.json data in the VALUE field.
- Click the Add button.
- Add another Config Var.
- In the field for KEY, enter PORT in all capital letters.
- In the field for VALUE, enter 8000.
- Then scroll down until you find buildpacks.
- Click Add buildpack button.
- Select Python from the list of languages.
- Click Save Changes button.
- Click Add buildpack button to add another buildpack.
- Select node.js from the list of languages.
- Click Save Changes button.
    - Note for this project the buildpacks had to be in the order of python first then node.js.

**Deploy section**
- On the same horizontal nav bar, click the Deploy button.
- Scroll to Deloyment methods and click the GitHub button.
- Go to Connect GitHub and search for your repository name in the search bar.
- Then click the Search button.
- When the repository pop's up below the search bar click the Connect button.
- Scroll down to Automatic and Manual deploys
- Click on the Deploy Branch button to deploy project, which would start building the project, and there is also the Automatic Deploys option which updates the project code everytime
  you push work to the GitHub repository.
- Click on the View button to view app and test to see if it works when the app is successfully deployed.

---

## **Credits**

**Code**

I wanted to learn how to implement colours and a typeWriter effect into my project as it was being developed. I carried out some research and found this website which helped me to achieve this typeWrite effect. I also found a youtube video that demonstrated how to implement colours into my project. Code was used from the the website and the video. A link to the website and the video can be found below. Code was used from [programiz](https://www.programiz.com/) to set current time and date.
- [www.101computing.net](https://www.101computing.net/python-typing-text-effect/)
- [Tech With Tim](https://www.youtube.com/watch?v=u51Zjlnui4Y&ab_channel=TechWithTim)

These online resources were really helpful when I needed to refamiliarize myself with a specific topic or syntax. They were really education as well.

- [Code Institute](https://codeinstitute.net/)
- [W3Schools](https://www.w3schools.com/default.asp)
- [programiz](https://www.programiz.com/)
- [PyPI](https://pypi.org/)
- [Digital Ocean](https://www.digitalocean.com/)

**Content**

- [BMW](https://www.bmw.co.uk/en/index.html)
    - Content was used from the offical BMW website to provide some of the car names.


### Acknowledgments

- Harry Dhillon - I want to say thank you to my mentor for his time and help throughout the developement of this project.
- Code Institute - I want to say thank you to Code Institute for the support and resources they have provided which facilitated me throughtout the development of this project.
- CI Slack Community - I want to say thank you to the Code Institute Slack community which had alot of supportive content about the modules and coding challenges.

I want to say thank you to my family and friend who have supported and helped me throughout the development of this project.

Finally, thank you for viewing this project and I hope you like it!

---




