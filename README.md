# **BMW Click and Collect** 














## **Table of Contents**









## **Introduction**
Welcome to my third project, which is a command-line user interface application built mainly using python.

What inspired me to build this app was having the ability to independtly coming up with an idea, putting it 
together and actully making it work. This idea also come from the love and interest I have for BMW cars. At 
the planning phase of my third project it was difficult as I was unsure of what I was going to build and I
was also new to python. But I stayed motivated and came up with this project which I learned alot from and
it has helped me to gain more experience with the python language as well as improving my 


## **User Experience**


### **Target Audience**
- This is for people preferably


### **User Stories**
- As a user of the app, I want to have clear instructions on how to use the app.
- As a user of the app, I want to easily navigate around without difficulty.
- As a user of the app, I want to be made aware of any invalid data I input and how to rectify it.
- As a user of the app, I would like an easy way of ordering a car and get it prepared for collection.
- As a user of the app, I would like a reference to show as proof of order.
- As a user of the app, I would like to see the cars that's available for me to order.
- As a user of the app, I would like to get information or a description of the car I am ordering.

### **Site owner goals**




### **How to use**
This BMW click and collect app is used for making car orders and getting them prepared for collection at your nearest
store in your current town or city. This app might be similar to a click and collect app you have used before which
would make it even easier to use. To use this app, all you need to do is follow the instructions provided by the app and
fill out the input fields with the required information, in the required format. The app will provide all the information
required such as the showing the list of cars available for you to choose from, as well as alerting you with messages if
you enter invalid data in the input fields. Once you are happy with your choice of car and you have successfully completed
your order. The app provides a detailed message on what you need to do for collection process.

## **Introduction**

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