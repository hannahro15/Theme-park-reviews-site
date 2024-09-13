# UK Rides Hub (A theme park database and reviews site)

For my Milestone 3 project I am creating a reviews site for theme parks on a database using Mongodb.

# UX

## Wireframes

### Home Page - Mobile
![image](wireframes/home-page-mobile.png)

### Home Page - Desktop
![image](wireframes/home-page-desktop.png)

### Rides Page - Mobile
![image](wireframes/rides-page-mobile.png)

### Rides Page - Desktop
![image](wireframes/rides-page-desktop.png)

### Registration Page - Mobile
![image](wireframes/registration-page-mobile.png)

### Registration Page - Desktop
![image](wireframes/registration-page-desktop.png)

### Login Page - Mobile
![image](wireframes/login-page-mobile.png)

### Login Page - Desktop
![image](wireframes/login-page-desktop.png)

### Ratings/Review Form (In the form of a Modal, similar for all screen sizes)
![image](wireframes/login-page-desktop.png)

## User Stories

* As a user I should be able to find out the purpose of the website and what it is about from the home page.
* As a user I should be able to see a list of rides and on the 'View all rides' page and search for them.
* As a user, I shouldn't be able to submit a review unless I am logged in.
* As a user I should be able to write a review on the 'Write a Review' Page and be able to submit it.
* As A user, I should be able to write a review via the ride modals and it should submit and post it to the reviews page.
* As a user on the 'Reviews' page, I should be able to add, edit or delete my own review/s.
* As a user on the 'Reviews' page, I shouldn't be able to edit reviews other than ones of my own.
* As a user, I should be able to read all the reviews on the reviews page.
* As a user I should be able to register an account.
* As a user I should be able to login to my account.
* As a user I expect the website to be responsive on a range of screen sizes so I am view it on different devices.


# Technologies Used
* HTML
* CSS
* Bootstrap Framework
* Python
* Flask Framework

# Features


## Future Features

- Admin page via website to add, edit, and delete rides.
- Add more rides and theme parks to the website.
- Make the profile page for users and admin when logged in more attractive.

# Credits and Acknowledgements

## Credits

### General

* [Canva](https://www.canva.com/) - or creating and designing the logo

* [Balsamiq](https://balsamiq.com/wireframes/) - for creating the wireframes

* [Gitpod](https://www.gitpod.io/) - For working/completing on my project

* [Github](https://github.com/) - To store my project online

* [MongoDB](https://www.mongodb.com/) - To store the database info on

* [Heroku](https://id.heroku.com/login) - For deploying the project and storing the env variables.

* [RandomKeyGen](https://randomkeygen.com/) - For generating secret key contained in the env file.

* [Rgb color code website](https://rgbcolorcode.com/) - For choosing colours

* [Readme Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#links) - For markdown documentation for the ReadMe

* [ChatGPT](https://openai.com/index/chatgpt/) - For general debugging and spotting basic errors.

• [Claude AI](https://claude.ai/new) - For general debugging and spotting basic errors.

### Images

* [Wikimedia Commons](https://commons.wikimedia.org/wiki/Category:Images) - For the home image and all the ride images

* [Font Awesome](https://fontawesome.com/icons) - For the icons used for the social links in the footer

### Content/Documentation

* For sorting out the whitespace under the footer issue I used some of the code on [this webpage](https://www.30secondsofcode.org/css/s/footer-at-the-bottom/). The website is called the 30 seconds of code website and the page is about the footer being on the bottom.

* [W3 schools](https://www.w3schools.com/) - For general documentation

* [Bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/) - For the relevant documentation

* [Hidden Input Fields ](https://www.w3schools.com/tags/att_input_type_hidden.asp) - Used for submitting the form when the rides and theme_park showed up as none in the review modal and said none on the reviews page.

* All content about the Theme Park rides on the website were written myself and from Google from my knowledge of visiting these theme parks in the past. 

## Acknowledgements

A big thanks to the support from my mentor at the Code Institute, my facilitator at the City of Bristol College, and the Code Institute Slack Community and Tutor Support for assistant on my Milestone 3 project.

# Deployment

Please find the steps below to deploy to Heroku.

Install the following in your terminal first in VS Code/Gitpod.
- pip3 freeze --local > requirements.txt
- echo web: python app.py > Procfile

You can check these have been added by looking at your files on the left hand side in VS Code/Gitpod.

 Go to Heroku.com and implement the following stepsin this order:
 - On the home page, click 'New' and in the dropdown, click on 'Create a new app'.
 - Add app name (This name must be unique, and have all lower case letters. Also use minus/dash signs instead of spaces.)
 - Select Region  (Select the most relevant region, mine is Europe)
 - Click the button that says 'Create App'.
 - Click on the Deploy tab near the top of the screen.
 - Where is says Deployment Method click on Github.
 - Below that, search for your repo name and add that.
 - Click connect to the app.

 Before clicking below on enable automatic deployment do the following:
 - Click on the settings tab
 - Click on reveal config vars.
 - Add in your variables from your env. files as key value pairs. (These are the IP, Port, Secret-Key, Mongo-URI (Won't  have connected to the Mongo-URI yet at this point), Mongo-DBName). Mongo-URI can be added at a later stage.
 - Go back and click on the Deploy tab. 
 
 Before we can connect it we need to push new files to the repository. Back in the terminal in your coding environment we need to add the following in the terminal:
 - git status
 - git add requirements.txt
 - git commit -m "Add requirements.txt file"
 - git add Procfile
 - git commit -m "Add Procfile"
 - git push

 Head back over to Heroku where the Deploy tab is.
 - Click 'Enable Automatic Deploys'
 - Click Deploy Branch. (Should be a main or master branch)
 - Heroku will receive code from Github and build app with the required packages. Hopefully once done the 'App has successfully been deployed message below' will appear.. 
 - Click 'View' to launch the new app.

Your app has been successfully deployed now at this point and should automatically update everytime we make changes to our code in GitHub. The deployed link to this project is https://theme-park-reviews-website-f1f235eaa19d.herokuapp.com/







 
