# UK Rides Review Hub (A theme park database and reviews site)

For my Milestone 3 project I am creating a reviews site for theme parks on a database using MongoDB.

The project is a website where users can submit theme park ride reviews to the website using CRUD functionality. There is an all rides page where users can search for rides, and there are also individual theme park pages where it shows just the rides for that particular theme park, this is all via a "Theme Parks" dropdown tab in the navbar. There is also a write a review page, and a view all reviews page via a "Reviews" dropdown tab. As well as writing a review for a ride via the write a review page, you can also write a review via each indivdual ride modal on the theme park pages. 

Live Link:
https://theme-park-reviews-website-f1f235eaa19d.herokuapp.com/

# UX

## Wireframes

<details>
<summary>Home Page - Mobile</summary>
<img src="wireframes/home-page-mobile.png" alt="Home Page - Mobile">
</details>

<details>
<summary>Home Page - Desktop</summary>
<img src="wireframes/home-page-desktop.png" alt="Home Page - Desktop">
</details>

<details>
<summary>Rides Page - Mobile</summary>
<img src="wireframes/rides-page-mobile.png" alt="Rides Page - Mobile">
</details>

<details>
<summary>Rides Page - Desktop</summary>
<img src="wireframes/rides-page-desktop.png" alt="Rides Page - Desktop">
</details>

<details>
<summary>Registration Page - Mobile</summary>
<img src="wireframes/registration-page-mobile.png" alt="Registration Page - Mobile">
</details>

<details>
<summary>Registration Page - Desktop</summary>
<img src="wireframes/registration-page-desktop.png" alt="Registration Page - Desktop">
</details>

<details>
<summary>Login Page - Mobile</summary>
<img src="wireframes/login-page-mobile.png" alt="Login Page - Mobile">
</details>

<details>
<summary>Login Page - Desktop</summary>
<img src="wireframes/login-page-desktop.png" alt="Login Page - Desktop">
</details>

<details>
<summary>Ratings/Review Form (Via a modal in each ride container, similar for all screen sizes)</summary>
<img src="wireframes/ride-review-modal-form.png" alt="Ride Modal Review Form">
</details>

<details>
<summary>Write a Review Page - Mobile</summary>
<img src="wireframes/write-a-review-page-mobile.png" alt="Write a Review Page - Mobile">
</details>

<details>
<summary>Write a Review  Page - Desktop</summary>
<img src="wireframes/write-a-review-page-desktop.png" alt="Write a Review Page - Desktop">
</details>

<details>
<summary>Reviews Page - Mobile</summary>
<img src="wireframes/reviews-page-mobile.png" alt="Reviews Page - Mobile">
</details>

<details>
<summary>Reviews Page - Desktop</summary>
<img src="wireframes/reviews-page-desktop.png" alt="Reviews Page - Desktop">
</details>

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

- Add more rides and theme parks to the website.
- As more rides and theme parks are added in to the website, then I could add in search functionality for each theme park.
- A pop-up asking if confirm if you want to delete a review, or edit a review before actually doing it.
- Add in pagination for if there a large number of rides on a page.
- Admin page via website to add, edit, and delete rides rather than directly on MongoDB database.
- Make the profile page for users and admin when logged in more attractive.
- Show users own reviews to their profile page.

# Testing

## Bugs 
### Fixed Bugs
- When submitting a review via the ride modals to begin with, the ride and theme park names didn't show up/transfer over to the reviews page, and said none. I tried doing an inner for loop with Jinja for reviews within the relevant parts in the forms, but then the ride and theme park names didn't show up in the modal review forms, I also tried slightly amending other bits of Jinja to 'reviews.ride_name' rather than 'rides.ride_name' in the forms but that didn't solve the problem either.  After debugging it and finding out the issue with ChatGPT, it mentioned about adding in hidden input form fields for everything affected so I added that in. I looked up the official documentation afterwards of hidden input form fields to clarify my understanding of it.
- The other small issue affected by the above was I had to decided to amend a key, which I altered in the app.py file, from ride to ride_name so it was consistent for both reviews, and the rides collections. I also had to change this manually on the MongoDB website, and in the relevant template files as well.
- When submitting the form it went to the 'Write a Review' page instead of the page where all the reviews were shown. I fixed this issue by amending the route name next the 'POST' method in the action bit in the relevant templates files to 'get_reviews' instead of add_review. This solved the issue, and it made it a better user experience.
- Problem where other users submitting reviews didn't submit to the reviews page. I first discovered this via a Peer Code Review channel on Slack. It was fixed by checking and amending odd variable names, making sure it matched in the app.py files and also amending routes in odd files in the templates folder. I also created a second user account for myself to check this bug was fixed.

### Unfixed Bugs
- When first entering the website, the images can take a few seconds to show on the ride pages. This may be because of it being a url for images which I used on the MongoDB website. 

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

* [Hidden Input Fields ](https://www.w3schools.com/tags/att_input_type_hidden.asp) - Used for submitting the form when the rides and theme_park didn't show up in the review modal and then said none on the reviews page when submitting.

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

The app has been successfully deployed now and it should automatically update any changes made to our code in GitHub. The deployed link to this project is https://theme-park-reviews-website-f1f235eaa19d.herokuapp.com/







 
