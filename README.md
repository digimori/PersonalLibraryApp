# My Personal Library app
- [Live Preview](https://personal-library-mongodb.herokuapp.com/)
- [Github Repository](https://github.com/digimori/PersonalLibraryApp)

ADD A TABLE OF CONTENTS HERE

### Developer Goals:
As a developer, I wanted to build an app that could store data for a user in regards to their reading list. 
I want them to have a profile page which can be accessed via a login landing page and make it easy to navigate their way around adding, editing and deleting books to their reading list to keep track of books that they want to read and have read.
I also want the lists themselves to be displayed alphabetically in order to make it easier to find titles. 
I want the database to be searcheable to find the book the user wants by title, author or by whether or not it has been read.


### User Stories:
- As a user of this app, I want to be able to log in from the landing page into a profile where my reading list will be stored.
- I want to be able to seperate my books into "Read" and "To Read" categories for easy browsing, and be able to search by Author or Title.
- I want to be able to easily add, edit and delete books from my Reading List profile and be in control of which categories they are listed in.


### Design Choices (Fonts, Colours and images, collapsibles, cards and hamburger menus):

#### Font and Colours:

#### Wireframes:
- Wireframes (FIGMA) - Desktop, Tablet, Mobile

### Database Schema:-

 Database schema (To Read):
    - Title
    - Author
    - Genre
    - Release Date
    - Publisher
    - ISBN-13
    - Page Count
    - Synopsis (TextArea)

- Database Schema (Read):
    - Title
    - Author
    - Genre
    - Rating 
    - Release Date
    - Publisher
    - ISBN-13
    - Page Count
    - Synopsis (TextArea)


### Features
Pages post-login:
- Profile
    - Display reading (to-read) list

- Reading list (dropdown menu in nav-bar)
    - (Get/View) To read
    - (Get/View) Read




- Add, Edit pages for each category
- Delete is a backend function
    - Defensive program this with a Javascript modal



#### Login/Logout/Register

#### Profile
    
#### Adding books

#### Editing books

#### Deleting



### Navigation



### Testing and Validation:

#### Validation (HTML, CSS, JSHint, Python PEP8)
#### Manual (Tables, Test-Pass)
#### Amiresponsive
#### Media Queries
#### Bugs and Fixes

### Deployment (Github and Heroku):

#### Github into Gitpod/Local Code Editor/IDE:

To deploy and run locally via an IDE:

Use the Chrome browser
Create a Gitpod account at this link
Download and install the Gitpod browser extension for Google Chrome.
Restart browser after installation has completed.
Log into Gitpod using your Github username and password. (If you don't already have a GitHub account, create one here
Navigate into your desired Gitpod repository (This project's repository can be found both at the top of this README, and here
Click the green "Gitpod" button on the top right of the repository file section.
This will open the project into a Gitpod workspace and can then be worked on in a local setting, such as VSCode.

Clone and Fork:

Follow This link back to the Github project respository.
Select the menu item above the repository files labelled "Code".
To clone: Select the appropriate url or open to Git Desktop.
To view on a web IDE: Click the dropdown labelled "Open in Web IDE" on the top right of the repository, and choose the appropriate IDE.
This dropdown can also be used to clone the code into VSCode IDE.
To clone into the Local IDE - in the terminal, type 'git clone' followed by the URL that can be copied from the aforementioned Code URL.
To fork - Follow the instructions as outlined in the Github Docs here.
To Deploy the respoitory to Github pages:

Open the Github repository here
Click the 'Settings' tab above the repository.
In the side bar to the left, click on "Pages".
Under "Build and Deployment", select the "Deploy from branch" under the "Source" tab.
In the "Branch" drop-down below, select the '/main' branch and click save.
This should create an accessible page once it has refreshed.
Follow steps 1-3 again to find the deployed page, which will now be above the "Build and Deployment" section.

#### Heroku


### Credits
#### Code bases and libraries
    - I kept a fair few bits of code from the mini project surrounding the login/register functionality to maintain securite measures and validation
    - Unsplash image for background (find the link)
