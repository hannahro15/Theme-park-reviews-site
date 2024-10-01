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
* As a user I should be able to see rides on the individual theme park pages. 
* As a user, I shouldn't be able to submit a review unless I am logged in.
* As a user I should be able to write a review on the 'Write a Review' Page and be able to submit it.
* As A user, I should be able to write a review via the ride modals and it should submit and post it to the reviews page.
* As a user on the 'Reviews' page, I should be able to add, edit or delete my own review/s.
* As a user on the 'Reviews' page, I shouldn't be able to edit reviews other than ones of my own.
* As a user, I should be able to read all the reviews on the reviews page.
* As a user I should be able to register an account.
* As a user I should be able to login to my account.
* As a user I expect the website to be responsive on a range of screen sizes so I am view it on different devices.
* As a user all social links work in the footer.

##  Database Schema

Please see below the Database Schema screenshot for my project. I used MongoDB Database to build my project with.

![screenshot](documentation/schema.png)

As you can see some fields are related to each other. Some have the same fields, such as ride names and theme parks and are in both the Reviews and Rides collections. Users are also connected to reviews as users write a review. Rides are connected to reviews as it contains some of the same fields and values. 

One field in two different collections have different field names but actually have the same values. It was 'created_by' in the Reviews collection and 'username' in the Users collection. They both contain the same username as a value but it made more sense on the Reviews page on the webesite to show 'created_by', and 'username' on the Register and Login pages.

# Technologies Used
* HTML
* CSS
* Bootstrap Framework
* Python
* Flask Framework


# Features

## Home Page

![screenshot]()

This page is an home page which has an image of Blackpool Pleasure Beach with a beach in the background and introduces what the website is about.

## Registration Page

![screenshot]()

This is a page where users can register for creating an account with.

## Login Page

![screenshot]()

This is a page where users can login to their account. There is an option from this page to link to the register page if you aren't already registered.

## Profile Page

![screenshot]()

A profile page that shows when the user is logged in to the website.

## View all Rides page

![screenshot]()

This page features all the rides on. There is a search bar that you can use to search for rides which makes it easier for the user to filter down to the ride they want to see and review. The page used Bootstrap card elements in a grid format and features a pop-up modal where you can fill out a review for that particular ride and then it gets submitted to the reviews page. It can only be submitted if a user is logged in. In the future if more rides are added to the website then pagination could be used to enhance the user experience.

## Individual Rides pages for the individual theme parks.

![Alton Towers]()

![Blackpool Pleasure Beach]()

![Thorpe Park]()

Works similar to the 'View all Rides page" mentioned above but doesn't have a search bar there. These individual pages are for each theme park. If more rides got added to these pages then a search bar could be added at a later stage. They also feature a pop-up modal for a review for each ride.

## Write a Review page

![screenshot]()

This page is a page for users to write a review. This is separate from the ride modal pop-up review form. If a user enters a website I thought it was a good idea to have a separate review page as well as the review from via the pop-up modals in the ride containers. Users cannot submit a review unless they are logged but they can fill out a form. If a user fills out a form and submits it if not logged it re-directs the user to the Login Page.

## Pop up modal for a ride review page (within each ride page)

![screenshot]()

Similar to the above.

##  View all Reviews Page

![screenshot]()

The reviews page is a page where all the reviews are shown that users submit. There is an option on there to edit and delete reviews. If you click on the edit button it takes you back to the write a review page and you can re-fill out the review form and it automatically edits on the review page. Only users who are logged in can edit or delete their own reviews. 

## Edit Review Page

This is where you go to from the View all Reviews Page to edit your own review.

![screenshot]()

## Navbar

![screenshot]()

This is the navbar which has the links to the relevant pages on the website. 

## Footer

![screenshot]()

This is the footer that contains the logo and the social links.

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
- Small bug when filling out a form is that you have to manually select a theme park after writing down the ride in the previous field. This means unless you know the ride and the theme park it is from you just you could just make up any ride, and any theme park that goes along with it. To improve the user experience I decided to put a note on the write a review page to say if you don't know the ride and theme park to go to the rides pages to fill out the review forms from there. This prevents this sort of error. Also one would assume you would already know the rides and the theme parks they are in if you are writing reviews on them!

## Validation
I have used the HTML, CSS and Python validators to validate my code.

HTML Validation Checks Below:

| Page      | Checked with HTML Validator with no errors (Yes or No)  |
| ------    | ------- |
| base.html | Yes |
| index.html | Yes |
| profile.html | Yes |
| register.html | Yes |
| login.html | Yes |
| rides.html | Yes |
| alton_towers.html | Yes |
| pleasure_beach.html | Yes |
| thorpe_park.html | Yes |
| add_review.html  | Yes |
| edit_review.html | Yes |
| reviews.html | Yes |
| 404.html | Yes |

![screenshot](documentation/html-validation.png)

CSS Validation: 

I can confirm that I have checked the code with the CSS Validator and that there are no errors.

![screenshot](documentation/css-validation.png)

Python Validation:

I can confirm that I have checked the code with the PEP8 validator and that there are no errors.

I haven't used Javascript in this project so there is no need for validation for that on this project.

## Lighthouse Testing

I have screenshots of my final lighthouse scores after editing things that have come up throughout the testing with Lighthouse. I used Google Lighthouse in a new browser window in 'Incognito Mode' to test this.

### Home Page - Mobile

![screenshot](documentation/lighthouse-home-mobile.png)

### Home Page - Desktop

![screenshot](documentation/lighthouse-home-desktop.png)

### Registration Page - Mobile

![screenshot](documentation/lighthouse-reg-mobile.png)

### Registration Page - Desktop

![screenshot](documentation/lighthouse-reg-desktop.png)

### Login Page - Mobile

![screenshot](documentation/lighthouse-login-mobile.png)

### Login Page - Desktop

![screenshot](documentation/lighthouse-login-desktop.png)

### Profile Page - Mobile

![screenshot](documentation/lighthouse-profile-mobile.png)

### Profile Page - Desktop

![screenshot](documentation/lighthouse-profile-desktop.png)

### View All Ride/Theme Parks Page - Mobile

![screenshot](documentation/lighthouse-rides-mobile.png)

### View All Ride/Theme Parks Page - Desktop

![screenshot](documentation/lighthouse-reg-desktop.png)

### Alton Towers Rides Page - Mobile

![Alton Towers](documentation/lighthouse-alton-towers-mobile.png)

### Alton Towers Rides Page - Desktop

![Alton Towers](documentation/lighthouse-alton-towers-desktop.png)

### Blackpool Pleasure Beach Rides Page - Mobile

![Blackpool Pleasure Beach](documentation/lighthouse-pleasure-beach-mobile.png)

### Blackpool Pleasure Beach Rides Page - Desktop

![Blackpool Pleasure Beach](documentation/lighthouse-pleasure-beach-desktop.png)

### Thorpe Park Rides Page - Mobile

![Thorpe Park](documentation/lighthouse-thorpe-park-mobile.png)

### Thorpe Park Rides Page - Desktop

![Thorpe Park](documentation/lighthouse-thorpe-park-desktop.png)

### View all Reviews Page - Mobile

![screenshot](documentation/lighthouse-all-reviews-mobile.png)

### View all Reviews Page - Desktop

![screenshot](documentation/lighthouse-all-reviews-desktop.png)

### Write a Review Page - Mobile

![screenshot](documentation/lighthouse-write-review-mobile.png)

### Write a Review Page - Desktop

![screenshot](documentation/lighthouse-write-review-desktop.png)

### Edit Review Page - Mobile

![screenshot](documentation/lighthouse-edit-review-mobile.png)

### Edit Review Page - Desktop

![screenshot](documentation/lighthouse-edit-review-desktop.png)

## Manual Testing

| User Story | Tested and everything is ok |
| ------ | ------- |
| As a user I should be able to find out the purpose of the website and what it is about from the home page.  | Yes |
| As a user I should be able to see a list of rides and on the 'View all rides' page and search for them. | Yes |
| As a user I should be able to see rides on the individual theme park pages. | Yes |
| As a user, I shouldn't be able to submit a review unless I am logged in. | Yes |
| As a user I should be able to write a review on the 'Write a Review' Page and be able to submit it. | Yes |
| As A user, I should be able to write a review via the ride modals and it should submit and post it to the reviews page.| Yes |
| As a user on the 'Reviews' page, I should be able to add, edit or delete my own review/s. | Yes |
| As a user on the 'Reviews' page, I shouldn't be able to edit reviews other than ones of my own.  | Yes |
| As a user, I should be able to read all the reviews on the reviews page. | Yes |
| As a user I should be able to register an account. | Yes |
| As a user I should be able to login to my account. | Yes |
| As a user I expect the website to be responsive on a range of screen sizes so I am view it on different devices. | Yes |
| As a user all social links work in the footer. | Yes |

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

* [Claude AI](https://claude.ai/new) - For general debugging and spotting basic errors.

### Images

* [Wikimedia Commons](https://commons.wikimedia.org/wiki/Category:Images) - For the home image and all the ride images

* [Font Awesome](https://fontawesome.com/icons) - For the icons used for the social links in the footer

### Validators

* [HTML Validator]() - HTML Validator

* [CSS Validator]() - CSS Validator

* [PEP8 Python Validator]() - Python Validator

### Content/Documentation

* For sorting out the whitespace under the footer issue I used some of the code on [this webpage](https://www.30secondsofcode.org/css/s/footer-at-the-bottom/). The website is called the 30 seconds of code website and the page is about the footer being on the bottom.

* [W3 schools](https://www.w3schools.com/) - For general documentation

* [Bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/) - For the relevant documentation

* [Hidden Input Fields ](https://www.w3schools.com/tags/att_input_type_hidden.asp) - When submitting the form and some of the fields didn't transfer over to the reviews page, advised by ChatGPT.

* All content about the Theme Park rides on the website were written myself and from Google from my knowledge of visiting these theme parks in the past. 

## Acknowledgements

A big thanks to the support from my mentor at the Code Institute, my facilitator at the City of Bristol College, and the Code Institute Slack Community and Tutor Support for assistant on my Milestone 3 project.

# Deployment

Please find the steps below to deploy to Heroku.

Install the following in your terminal first in VS Code/Gitpod.
- pip3 freeze --local > requirements.txt
- echo web: python app.py > Procfile

You can check these have been added by looking at your files on the left hand side in VS Code/Gitpod.

 Go to Heroku.com and implement the following steps in this order:
 1. On the home page, click 'New' and in the dropdown, click on 'Create a new app'.
 2. Add app name (This name must be unique, and have all lower case letters. Also use minus/dash signs instead of spaces.)
 3. Select Region  (Select the most relevant region, mine is Europe)
 4. Click the button that says 'Create App'.
 5. Click on the Deploy tab near the top of the screen.
 6. Where is says Deployment Method click on Github.
 7. Below that, search for your repo name and add that.
 8. Click connect to the app.

 Before clicking below on enable automatic deployment do the following:
 1. Click on the settings tab
 2. Click on reveal config vars.
 3. Add in your variables from your env. files as key value pairs. (These are the IP, Port, Secret-Key, Mongo-URI (Won't  have connected to the Mongo-URI yet at this point), Mongo-DBName). Mongo-URI can be added at a later stage.
 4. Go back and click on the Deploy tab. 
 
 Before the app can be connected, push the following new files below to the repository. Go back in the terminal in your coding environment and add the following:
 1. git status
 2. git add requirements.txt
 3. git commit -m "Add requirements.txt file"
 4. git add Procfile
 5. git commit -m "Add Procfile"
 6. git push

 Head back over to Heroku where the Deploy tab is.
 1. Click 'Enable Automatic Deploys'
 2. Click Deploy Branch. (Should be a main or master branch)
 3. Heroku will receive code from Github and build app with the required packages. Hopefully once done the 'App has successfully been deployed message below' will appear.. 
 4. Click 'View' to launch the new app.

The app has been successfully deployed now and it should automatically update any changes made to our code in GitHub. The deployed link to this project is https://theme-park-reviews-website-f1f235eaa19d.herokuapp.com/







 
