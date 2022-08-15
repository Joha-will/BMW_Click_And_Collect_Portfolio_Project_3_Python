# **BMW Click and Collect** 














## **Table of Contents**









## **Introduction**
Welcome to my third project, which is a command-line user interface application built mainly using python.

What inspired me to build this app was having the motivation to independently create an idea, put it 
together and make it work. This idea also came from the love and interest I have for BMW cars. At 
the planning phase of my third project I was unsure of what I was going to build which made very challenging as well as being a novice using python. However, I stayed motivated and focused and created this project which I learned a lot from and it has helped me to gain more experience and skills with the python language. 

In this README I will detail the steps I took to develop and create this project, with the use of  screen photos, images, links, charts and more.

Thank you for viewing my project.

I hope you find the application useful!



## **User Experience**


### **Target Audience**
- This application is targeted to people above the age of 17 and older which is the legal age in the United Kingdom. 

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


### **How to use**
This BMW click and collect app, is used for making car orders and getting them prepared for collection at your nearest
store in your current town or city. To use this app, you need to follow the instructions on the screen and
fill out the input fields with the information needed in the correct format. The app will provide the list of cars available for you to choose from as well as, alerting you with messages if you enter invalid data in the input fields. Once you are happy with your choice of car and you have successfully completed your order. The app provides a detailed message on what you need to do for the collection process.


## **Features**
- This BMW click and collect application has a title in font design 'ANSI shadow' and BMW car logo.
- Type writer
- Colours
- Username - Input fields 

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!