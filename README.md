# My Personal Library app

### About the Project:
---
My project is designed to be a personal library app in where I can store, edit and delete data in regards to my book collection.    
I wanted it to be an easily accessible, no particular bells and whistles approach, for simplicity, but also locked behind a login function.

- [Live Preview](https://personal-library-mongodb.herokuapp.com/)
- [Github Repository](https://github.com/digimori/PersonalLibraryApp)

***

[AmIResponsive](https://ui.dev/amiresponsive?url=https://personal-library-mongodb.herokuapp.com/)
![Image for AmIResponsive](/readmeimages/Amiresponsivelibraryapp.png)   



### Table of Contents  
- [About The Project](#about-the-project)  
- [Technologies Used](#technologies-used)   
- [Developer Goals](#developer-goals)
- [User Stories](#user-stories)
- [Design Choices](#design-choices-fonts-colours-and-images-cards-and-hamburger-menus)
- [Wireframes](#wireframes)
- [Database Schema](#database-schema)
- [Features](#features-and-navigation)
- [Navigation](#navigation)
- [Testing And Validation](#testing-and-validation)
- [Deployment](#deployment-github-and-heroku)
- [Credits](#credits)


***

### Technologies used:
---
- HTML (Flask Frameworks)
- CSS (Materialize library)
- JavaScript (jQuery)
- Python3 (Back-end application)
- MongoDB (Non-Relational Database)

### Developer Goals:
---
As a developer, I wanted to build an app that could store data for a user in regards to their reading list. 
I want them to have a profile page which can be accessed via a login landing page and make it easy to navigate their way around adding, editing and deleting books to their reading list to keep track of books that they want to read and have read.
I also want the lists themselves to be displayed alphabetically in order to make it easier to find titles. 
I want the database to be searcheable to find the book the user wants by title, author or by whether or not it has been read and to display the results to the user.


### User Stories:
---

| As a ... | I want to ... |
| ----------- | ----------- |
| User: |  I want to be able to log in from the landing page into a profile where my reading list will be stored. |
| User: | I want to be able to seperate my books into "Read" and "To Read" categories for easy browsing, and be able to search by Author or Title. |
| User: | I want to be able to easily add books to my list |
| User: | I want to be able to edit books in my reading list in case I input incorrect information |
| User: | I want to be able to delete books from my Reading List profile |
| User: | I want to  be in control of which categories the books are listed in to determine what as been read and what has not |
| User: | I want to be able to add an image of the book cover to easily identify the books by visuals | 

### Design Choices (Fonts, Colours and images, cards and hamburger menus):
---
#### Font and Colours:
- For the fonts, I chose and mix of "Libre Baskerville" and "Special Elite". The choices for these were ease of use for reading as I originally wanted to use something more cursive because they represent the styles put on antique books and type-writers. This was to match up with the overall theme of a library and to match the login/registration cover image of antique style library books.  
I eventually opted to disregard the cursive fonts as they are very difficult for those with dyxlexia to read and I wanted to maintain accessibility.

- For the colours, I wanted to keep it muted, partly due to personal preferences and because it is easier to read. I wanted to limit eye strain and so avoided using pure whites and blacks and opted for greys, neutral beiges and browns instead.     
I also chose to use a cold colour for the "Unread books" cards over warm, as I realised, with browns and reds together, this is not going to be user friendly to people with colour-blindness, so opted for blue to distinguish from the red.

- The home page login and registration pages are backed with [this image](https://unsplash.com/photos/_YzGQvASeMk) from Unsplash, I chose it as it fit the library theme without being too busy or distracting. 

- For the Book entries, I chose to use cards through Materialize CSS. This provided a convenient, easily scalable and responsive method to display the information about each book entry to the user and customize it with edit and delete buttons. 

- The Navigation bar collapses into a hamburger menu on smaller screen sizes in order to not take up too much space. 

- At a later point, I removed the Footer as there was little need for it to be there. It cluttered the page more than anything else and had no real practical use.

### Wireframes
---

<details>
  <summary>Wireframes (Adobe Photoshop):</summary>

 ####  Desktop, Tablet, Mobile

- Index page (Not Logged in and Registration page are laid out the same):
![Index - Not logged in/Registration](/readmeimages/Wireframesprelogin.jpg)

- Profile Page (Once Logged in, cannot be accessed prior to login):
![Profile - Logged in](/readmeimages/Profilepagewireframe.jpg)

- Add-Book page (User must be logged in):
![Add Book](/readmeimages/addbookpage.jpg)
</details>

---

### Database Schema
---
| Database schema (Books to Read): | Database Schema (Books that have been Read): |
| ----------- | ----------- |
| • Title | • Title |
| • Author| • Author |
| • Genre | • Genre |
| • Rating (Hidden) | • Rating |
| • Release Date | • Release Date
| • Publisher | • Publisher |
| • ISBN-13 | • ISBN-13 |
| • Page Count | • Page Count |
| • Synopsis | • Synopsis |
| • Book Image URL | • Book Image URL |



I have ensured that the "Rating" input field, though part of both forms, is not required, so that when adding an un-read book, you do not need to add the star-rating to it straight away and can be added later.   
The categories are separated into "To_read" and "Read" to indicate whether or not the books have been read whilst maintaining a collated database on the back-end through MongoDB. 


### Features and Navigation
---

#### Login/Logout/Register

The login and registration pages are almost the same in an attempt to keep consistency across the app.
I chose to provide a welcome message, a login form and a navigation beneath the form depending on if you are signing up or registering. 

Once logged in, the navigation bar at the top will appear to provide the user with ways to add books and view their profile. 
There is also a "Logout" button, which will end the user session and log them out of the app, returning to the index page login screen.

<details>
<summary>Logged In Index and Registration - Navbar shown</summary>

![Logged in Nav-bar - Index](/readmeimages/indexlogindesktop.png) 
![Registration Page](/readmeimages/registrationpagedesktop.png)

</details>

<details>
<summary>Logout page</summary>

![Logout](/readmeimages/logoutscreen.png)

</details>

#### Profile

The profile page is designed to show both the books read and unread to the user. It also incorporates a search function that allows the user to find their books by Author or Title.  
The book entries display a placeholder image if no book cover is uploaded.  
The Search bar will display a "Results not found" message if the book entry does not exist. 


<details>
<summary>Profile Page</summary>

![Full Profile Page](/readmeimages/profilepagewholeview.png)
</details>

<details>
<summary>Instructions</summary>

![Instructions](/readmeimages/howtouselibrary.png)
</details>

<details>
<summary>Search Bar</summary>

The search bar is implemented near the top of the page and the user is able to search by book Title or by Author as stated in the instructions. 
The assigned book entry, if there is a match, will appear beneath the search bar, else, it will display the message of "No Results Found" 
The user is also able to reset the field by pushing the reset button, which will re-reveal their book entries.  

![Search Bar](/readmeimages/searchbar.png)
![No Results](/readmeimages/noresults.png)

</details>

<details>
<summary>Book Entry cards</summary>

The book entry cards themselves contain all of the information uploaded by the user from filling out the "Add Book" form. 
Second to this, there are edit and delete buttons at the bottom, giving the user the options to edit their entries without having to completely submit a new form from scratch, or otherwise delete the entry if they no longer wish to have it in their collection.  

![Book Entry Cards](/readmeimages/cardsforbooks.png)
</details>


### Adding books
- To add books, I implemented a form, asking for the user to input data, that will then be stored and pushed onto cards that they will be able to see on the profile page.
<details>
<summary>Whole page view</summary>

![Add Books Page](/readmeimages/addbookpagedesktop.png) 
</details>

<details>
<summary>Collapsible instructions</summary>

I chose to have the instructions as a collapsible just to make the page a little cleaner. 

![Instructions](/readmeimages/addbookcollapsible.png) 
</details>

<details>
<summary>Book Form - Used to add books to the database</summary>

The user inputs the information for their books into the fields and selects the category that they wish to upload it to.  
Following this, they can then tap the "Add Book" button to add their book entry to their profile page. 

![Form for Books](/readmeimages/addbookform.png)
</details>


### Editing books
- For the Editing books, I choose to implement a modal, so that there is no need to navigate back and fourth between separate pages. 
- The modal can be cancelled by tapping the cancel button, or by tapping anywhere outside of the modal.
- The editing also allows the user to change the category of the book from "Books to Read" to "Books Read" once they have been completed. 

<details>
<summary>Edit Form, Modal and Buttons</summary>

The edit form modal has two options. The user is able to cancel their edits via either tapping outside of the form, or by tapping the cancel button at the bottom of the form itself.
The form pre-populates with what has already been written in the entry previous, so that the form does not need to be repeatedly entered on each edit. 

![Edit form, buttons and modal](/readmeimages/editbookmodal.png)

</details>


#### Deleting Books
- I chose to implement a modal for deleting of book entries to implement defensive programming. This ensures that the user is aware that this is an action that cannot be reverse and making sure that they are happy to proceed with the deletion.

<details>
<summary>Book Deletion modal</summary>

The user, once prompted, can either proceed with deleting the entry, or cancel the deletion process by pressing the cancel button. 

![Delete Book Modal](/readmeimages/contentdeletemodal.png)
</details>

### Testing and Validation:
--- 

###  Validation (HTML, CSS, Python PEP8)
---
<details>
<summary>HTML</summary>

- [Index/Logout](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpersonal-library-mongodb.herokuapp.com%2Findex) 
- [Login - Incorrect User/Password](/readmeimages/wrongpassvalidation.png) 
- [Registration](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpersonal-library-mongodb.herokuapp.com%2Fregister)  

- Profile/AddBook - Needs direct input

</details>

<details>
<summary>CSS, jQuery and Python PEP8</summary>

[CSS Validation using Jigsaw](https://validator.w3.org/)
![CSS Validation](/readmeimages/cssvalidation.png)

[PEP8 Validation using CI's Linter](https://pep8ci.herokuapp.com/)
![Python PEP8](/readmeimages/lintercheck.png)

[jQuery Validation using JSHint](https://jshint.com/)
![jQuery](/readmeimages/jshintmetricsforpythonproject.png)
</details>


#### Manual Testing - User Testing

| Test | Expectation | Pass/Fail |
| ----------- | ----------- | ----------- |
| Login Form | I expect the form to recognize my login credentials and create a session to login to my profile | Pass |
| Registration Form | I expect the form to register a new user to the database, whilst checking if the username is taken or not. | Pass |
| Add Book Form| I expect to be able to fill the details of books for my database onto a form, that will then submit the data and allow it to be pulled onto cards that are set out on the profile page. | Pass |
| Edit Book Button | When clicked, I want the edit book button to open a modal containing a form for editing the entry. I then want this form to directly edit the entry and submit and save the data to the database. | Pass |
| Delete Book | When clicked, I expect a modal to open, confirming if I want the entry to be deleted and not directly delete on press. | Pass |
| Delete Modal | I want the delete modal to open when the Delete button is pressed, giving the user the option to delete the entry, or cancel the operation | Pass |
| Logout | When the logout button is pressed, I want the session cookie to be removed from the user in order to log the user out. | Pass |
| Search | To be able to search by book title, or by author in order to find an entry | Pass |
| Reset Search | When the reset button is pressed, to return to the profile page with all of the entries intact | Pass |
| Edit Searched Book | I want the user to be able to edit the book once it has been searched for by opening the "Edit book" modal | Pass |
| Delete Searched Book | I expect the Delete button to still trigger the modal for defensive programming, even after being searched | Pass |
| Force add_book page | I expect there to be defensive programming in place, redirecting me to the login page if I try to force my way into the add_book page without being logged in | Pass |
| Test Logs from Heroku | Running the log alongside manual testing on Heroku - Can be found under personal-library-mongodb-logs.txt file in Git/Workspace | Pass |


### Media Queries

I used the Chrome Dev tools to implement changes in real time before performing a final commit on the code itself.  
This was also used to test the responsiveness as I could change the breakpoints as I edited each line of code.


### Bugs and Fixes
---
| Bug/Issue | Explanation | Fix Implemented |
| ----------- | ----------- | ----------- |
| Modal Bug | When editing forms or deleting an entry through the modal, it would only delete the first entry | Put unique id tags on the divs that opened and connected the modals so that it could identify what was being specifically edited or deleted |
| Unable to select Category on Edit form | When selected, the edit form would not show the categories available for selection | Redefined the reading_list in the render_template method so that it linked to the category function |
| Books not displaying | I originally had books read and unread in separate collections, which made it harder to manage the data from a front-end point | Consolidated the books to one collection, separated instead by category_name to make them easier to loop through |
| Forcing Access to pages | I was able to brute force my way into the add_book page and edit/delete functions without logging in which is a security issue | Added defensive programming that redirects the user to the login page if they try to force their way in through the address bar | 
| Delete Bug | Delete function attached to modal was redirecting to an internal server error. This is due to me essentially doing a copy-paste from the edit book view without removing the username filter as Cursor objects cannot target it | Removed the Cursor that was causing the issue. Maintained security by having if 'user' in session as a method to stop brute forcing |
| Edit Bug | Editing the book would throw an error with the cursor object | Removed the Cursor causing the issue. It was the same bug as the Delete issue above | 

### Deployment (Github and Heroku):
---

#### Github into Gitpod/Local Code Editor/IDE:

#### To deploy and run locally via an IDE:

- Use the Chrome browser
- Create a Gitpod account at [this link](https://www.gitpod.io/)
- Download and install the Gitpod browser extension for Google Chrome.
- Restart browser after installation has completed.
- Log into Gitpod using your Github username and password. If you don't already have a GitHub account, [create one here](https://github.com/signup?source=login)
- Navigate into your desired Gitpod repository 
- This project's repository can be found both at the top of this README, [and here](https://github.com/digimori/PersonalLibraryApp)
- Click the green "Gitpod" button on the top right of the repository file section.
[image goes here]

- This will open the project into a Gitpod workspace and can then be worked on in a local setting, such as VSCode.

#### Clone and Fork:

-Follow [This link](https://github.com/digimori/PersonalLibraryApp) back to the Github project respository.
- Select the menu item above the repository files labelled "Code".
- To clone: Select the appropriate url or open to Git Desktop.
- To view on a web IDE: Click the dropdown labelled "Open in Web IDE" on the top right of the repository, and choose the appropriate IDE.
- This dropdown can also be used to clone the code into VSCode IDE.
- To clone into the Local IDE - in the terminal, type 'git clone' followed by the URL that can be copied from the aforementioned Code URL.
- To fork - Follow the instructions as outlined in the Github Docs here.


#### To deploy to Heroku:

Create an account with [Heroku](https://id.heroku.com/login)
Login with username/password (This requires multi-factor authentication through an external device such as the [Salesforce app](https://www.salesforce.com/solutions/mobile/app-suite/security/))
- Click on "New" > "Create App"
- Use "Europe" as the host
- Implement a distinct name for the app
- Click "Create App"
- Click on the app's name to open the settings and deployment section

- Open the Settings tab and find the section "Config Vars"
- Click "Reveal Config Vars"
- Input the following Key-Value Pairs (This is an example sample set and can be found under 'example.py' in this repository, you will need to configure it with your own settings placed inside the angle brackets - Remove the angle brackets once the information is placed inside them): 

| Key | Value | Explanation |
| ----------- | ----------- | ----------- |
| IP | 0.0.0.0 | Local IP |
| PORT | 5000 | This is the port for Flask |
| SECRET_KEY | Any secret key | A password for access |
| MONGO_URI | mongodb+srv://<user_name>:<pass_word>@<cluster_name>.ixpv5wd.mongodb.net/<database_name>?retryWrites=true&w=majority | Connection to Database |
| MONGO_DBNAME | <database_name> | Database name |
| DEVELOPMENT | FALSE | Turns the workspace off of the development state |
| DEBUG | FALSE | Turns the Debugger off for the workspace |


- Once those are saved, navigate to the Deploy tab
- On Deployment method", click "Github"
- Search the Repo (In this case, for this particular project, type in 'PersonalLibraryApp' and select the repo.)
- Enable Automatic deploys
- on Manual Deploy, select the Main branch and click "Deploy Branch"


### Credits
--- 
#### Code and libraries
- I kept a fair few bits of code from the mini project surrounding the login/register functionality to maintain security measures and validation.
- [Unsplash image for background](https://unsplash.com/photos/_YzGQvASeMk)
- Materialize(CSS) for the main bulk of the layout.
