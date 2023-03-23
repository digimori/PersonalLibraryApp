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
- [Wireframes](#wireframes-adobe-photoshop)
- [Database Schema](#database-schema)
- [Features](#features)
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
- As a user of this app, I want to be able to log in from the landing page into a profile where my reading list will be stored.
- I want to be able to seperate my books into "Read" and "To Read" categories for easy browsing, and be able to search by Author or Title.
- I want to be able to easily add, edit and delete books from my Reading List profile and be in control of which categories they are listed in.


### Design Choices (Fonts, Colours and images, cards and hamburger menus):
---
#### Font and Colours:
- For the fonts, I chose and mix of "Libre Baskerville" and "Special Elite". The choices for these were ease of use for reading as I originally wanted to use something more cursive because they represent the styles put on antique books and type-writers. This was to match up with the overall theme of a library and to match the login/registration cover image of antique style library books.  
I eventually opted to disregard the cursive fonts as they are very difficult for those with dyxlexia to read and I wanted to maintain accessibility.

- For the colours, I wanted to keep it muted, partly due to personal preferences and because it is easier to read. I wanted to limit eye strain and so avoided using pure whites and blacks and opted for greys, neutral beiges and browns instead.     
I also chose to use a cold colour for the "Unread books" cards over warm, as I realised, with browns and reds together, this is not going to be user friendly to people with colour-blindness, so opted for blue to distinguish from the red.

- The home page login and registration pages are backed with [this image]() from Unsplash, I chose it as it fit the library theme without being too busy or distracting. 

- For the Book entries, I chose to use cards through Materialize CSS. This provided a convenient, easily scalable and responsive method to display the information about each book entry to the user and customize it with edit and delete buttons. 

- The Navigation bar collapses into a hamburger menu on smaller screen sizes in order to not take up too much space. 

<details>
  <summary>Wireframes (Adobe Photoshop):</summary>
---
####  Desktop, Tablet, Mobile

- Index page (Not Logged in and Registration page are laid out the same):
![Index - Not logged in/Registration](/readmeimages/Wireframesprelogin.jpg)

- Profile Page (Once Logged in, cannot be accessed prior to login):
![Profile - Logged in](/readmeimages/Profilepagewireframe.jpg)

- Add-Book page (User must be logged in):
![Add Book](/readmeimages/addbookpage.jpg)
</details>
***

### Database Schema:-
---

Database schema (Books to Read):
- Title
- Author
- Genre
- Release Date
- Publisher
- ISBN-13
- Page Count
- Synopsis (TextArea)

Database Schema (Books that have been Read):
- Title
- Author
- Genre
- Rating 
- Release Date
- Publisher
- ISBN-13
- Page Count
- Synopsis (TextArea)


I have ensured that the "Rating" input field, though part of both forms, is not required, so that when adding an un-read book, you do not need to add the star-rating to it straight away and can be added later.   
The categories are separated into "To_read" and "Read" to indicate whether or not the books have been read whilst maintaining a collated database on the back-end through MongoDB. 


### Features
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

![Logout]()

</details>

#### Profile

Pages post-login:
- Profile
    - Display reading (to-read) list


- Add, Edit pages for each category
- Delete is a backend function
    - Defensive program this with a Javascript modal


#### Adding books
- To add books, I implemented a form, asking for the user to input data, that will then be stored and pushed onto cards that they will be able to see on the profile page.
<details>
<summary>Form for adding books</summary>

![Form for Books]()

</details>

#### Editing books
- For the Editing books, I choose to implement a modal, so that there is no need to navigate back and fourth between separate pages. 
- The modal can be cancelled by tapping the cancel button, or by tapping anywhere outside of the modal.
- The editing also allows the user to change the category of the book from "Books to Read" to "Books Read" once they have been completed. 

<details>
<summary>Edit Form, Modal and Buttons</summary>

![Edit form, buttons and modal]()

</details>


#### Deleting Books
- I chose to implement a modal for deleting of book entries to implement defensive programming. This ensures that the user is aware that this is an action that cannot be reverse and making sure that they are happy to proceed with the deletion.

<details>
<summary>Book Deletion modal</summary>

![Delete Book Modal]()
</details>

### Navigation

Profile - 
Add Book - 
Logout - 

Index - Login and Registration


### Testing and Validation:
--- 

### Validation (HTML, CSS, JSHint, Python PEP8)
#### Manual (Tables, Test-Pass)

| Test | Expectation | Pass/Fail |
| ----------- | ----------- | ----------- |
| Login Form | I expect the form to recognize my login credentials and create a session to login to my profile | Pass |
| Registration Form | I expect the form to register a new user to the database, whilst checking if the username is taken or not. | Pass |
| Add Book Form| I expect to be able to fill the details of books for my database onto a form, that will then submit the data and allow it to be pulled onto cards that are set out on the profile page. | Pass |
| Edit Book Button | When clicked, I want the edit book button to open a modal containing a form for editing the entry.   I then want this form to directly edit the entry and submit the data to the database.  | Pass |
| Delete Book | When clicked, I expect a modal to open, confirming if I want the entry to be deleted and not directly delete on press. | Pass |
| Delete Modal | I want the delete modal to open when the Delete button is pressed, giving the user the option to delete the entry, or cancel the operation | Pass |
| Logout | When the logout button is pressed, I want the session cookie to be removed from the user in order to log the user out. | Pass |
| Search | To be able to search by book title, or by author in order to find an entry | Pass |
| Reset Search | When the reset button is pressed, to return to the profile page with all of the entries intact | Pass |
| Edit Searched Book | I want the user to be able to edit the book once it has been searched for by opening the "Edit book" modal | Pass |
| Delete Searched Book | I expect the Delete button to still trigger the modal for defensive programming, even after being searched | Pass |


### Media Queries

I used the Chrome Dev tools to implement changes in real time before performing a final commit on the code itself.  
This was also used to test the responsiveness as I could change the breakpoints as I edited each line of code.


### Bugs and Fixes
---
| Bug/Issue | Fix Implemented |
| ----------- | ----------- |
| Login Form | I expect the form to recognize my login credentials and create a session to login to my profile |
- Modal bug
- unable to select category - fixed with redefining reader_list in both functions
- Overriding CSS Materialize - went to use !imporant but realised this is bad juju so specificity
- originally had books read and unread in separate collections, consolidated them to make them easier to loop through

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

Create an account with [Heroku]
Login with username/password (This requires multi-factor authentication through an external device such as the Salesforce app - download link)
Click on "New" > "Create App"
- Use "Europe" as the host
- Implement a distinct name for the app
- Click "Create App"

- Click on the app to open
[image]

- Open the Settings tab and find the section "Config Vars" (This should be the second section down - image)
- Click "Reveal Config Vars"
- Input the following Key-Value Pairs:
(CHECK THIS WITH MENTOR BECAUSE I THOUGHT YOU CAN'T DO THIS????? HENCE ENV.PY AND GITIGNORE???)

- Once those are saved, navigate to the Deploy tab
- On Deployment method", click "Github"
- Search the Repo (In this case, for this particular project, type in 'PersonalLibraryApp' and select the repo.)
- Enable Automatic deploys
- on Manual Deploy, select the Main branch and click "Deploy Branch"


### Credits
---     

#### Code and libraries
    - I kept a fair few bits of code from the mini project surrounding the login/register functionality to maintain securite measures and validation.
    - Unsplash image for background (find the link)
    - Materialize(CSS)
