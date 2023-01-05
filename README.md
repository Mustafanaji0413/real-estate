<h1> Portfolio Project 4 - Full-Stack Toolkit </h1>

<h2>  MN Real Estate - Property Searching Just Got So Easy </h2>

Find the right broker for your housing deal!

<h3>  This is how easy it works!</h3>

1: Simply filter our listings to fit your needs. <br>
2: Find the perfect home that fits you. <br>
3: Send an inquiry and we will get in touch!

<img>

<h3>Live Site

</h3>


<h3>Repository

</h3>


<section>
<h2>Catalouge</h2>

- Target group 
- User Experience Design 
- - Storytelling 
- - Wireframe 
- User Stories
- - Nav Bar
- - Home Page
- - About Page
- - Listings Page
- - Register Page
- - Login Page
- - Dashboard Page
- - Edit Listing Page
- - Create Listing Page
- - Delete Listing 
- Testing 
- Deployment 
- Credits
- Technologies Used

</section>
<br>

## Target Group 
MN Real Estate has mainly two target groups, customers seeking a new home and customers wanting to sell their home. We are confident that our reputation and marketing strategies will lead to more customers wanting to partner with us when hearing about what we have accomplished. 

### Buying Customers
The real estate market is one of the safest and most profitable markets out there. With turnovers of trillions of dollars each year it is a lucrative market to jump into. MN Real Estate is here to help first-time buyers and veterans in the field. We are here to help buyers have a great experience selling their homes and get the most value for it!


### Selling Customers
Together with our reputation and our marketing strategy, using major social media platforms and their algorithms to target home-interested buyers. We are confident that MN real estate and our modern marketing strategy will attract new customers and make current customers stay. 


#  User Experience Design

To better understand the customer journey I have written an example of what it could look like. 

## The story of the Andersson

The Andersons have for a long time been looking to buy a new home and sell their current house. But with the large jungle of different real estate companies and promises they all make, it has been difficult to make the decisions of what real estate company the Andersons should partner with. 

While scrolling online the Andersson came across an ad about MN Realestate. By partnering with some of the biggest social media platforms MN Realestate has been able to use its algorithm to target individuals that have shown interest in real estate reels and posts. 

The Andersson clicked on the ad shown and started to read more about MN Realestate and the approach they are taking to sell their listings and comfort customers. Along with reviews and recommendations, the Andersons decided to browse our website to possibly find a home matching their needs.

After some research and consideration, Andersson found a home that was perfect for them. After reading more about the listing, they could easily contact the realtor responsible by filling out a simple form. 

The Realtor got back in contact with them and the process of buying a new home is well on its way. 


<img FLOWCHART>


## User Stories 
- As a User, I can register an account so that I can log in and view listings.
- As a User, I can see all my requests in an overview so that I have control and know the status of the requests.
- As a User, I can make an inquiry about a listing to a realtor so that I can get to see more of that listing 
- As a User, I can filter all of the listings so that I can better find the house for my needs.
- As a User, I can read more about MN real estate and the team behind them. 
- As a User, I can read more about each listing to get a better understanding of it.
- As a User, I can browse the listing images to get a visual understanding of it. 
- As an Admin I can add listings.
- As an Admin I can edit listings.
- As an Admin I can delete listings.


## The surface Plane

### Base

To make the application as dynamic as possible, I want the navbar and footer to be the same in all of the applications. Therefore, Django dynamic pages are used so the user always recognizes the default layout they're on.

#### Navbar
<img>

#### Footer
<img>

### Home page

    A major key for us is to not distract the user away from the purpose of them visiting the website. We do not want to make it difficult for them to find what they need and scare them off. That's why we have chosen to make the search bar and filtering options the first thing the user sees. 

 <img>

 When the user scrolls down we present them with the latest listings that have been posted to keep them engaged. On each listing, there is a call to action button to read more about the listing as well.

 <img>

 Further down on the home page, we have chosen to display three main focuses we at MN real estate focus on. We have opted to do so to keep the user intrigued with the capabilities of our company. 

 <img>

 ### About Page

 When you first visit the about page, the first thing you are greeted with is more about us at MN Real Estate. You get to read more about our accomplishments and what services we provide along with further information about customer reviews. On the left side of the about page, we also show the realtor of the month to further interest the user and encourage our staff.  

 <img>

 Further down on the about page, we have also added a quote that says "We Work For You!" in an attempt to get them to browse our listings. In that section is a call to action button that takes them directly to our featured listings page so the user doesn´t have to scroll up to go there. 

 <img>

 At the bottom of our about page, users can find our qualified team and more information about them. This is in an attempt to get a visual understanding of the realtors to better build a bond instead of them possibly only seeing a name. 

 <img>

 ### Featured Listings Page
 
 On our featured listings page the user gets to see all of our listings if the user decides not to filter them. Here the user can jump between pages and read more about each listing that catches their interest. 

 <img>

  ### Register Page
  On the navbar, the user has the option to register to keep track of what listings they have shown interest in. To sign up, the user needs to fill out a couple of basic details. 

  <img>

 ### Login Page
 It is easy to log in for returning users. Just fill in your username and password and you get logged in.

 <img>


  ### Dashboard Page
 On the dashboard page, a logged-in user sees what listings they have shown interest in and sent an inquiry. This makes it easier to keep track of interesting listings and makes for a better user experience. 

 <img>

 ### Make An Inquiry page
  
  On the Make An Inquiry page the user can make an Inquiry and get in touch with the correct realtor for the listing to get more info and proceed in the process of buying a home. 

  <img>

  ### Add a listing. 
  As an admin, you can choose to create a brand new listing. To do this you need to fill out the listing information and other valid details to be able to post it. 

  <img>

  ### Edit Listing 
  Admin users can also choose to edit listings if for example, new information has occurred or if the admin has received new images. 

  <img>


  ### Delete Listing

  Furthermore, the admin can also choose to delete a listing if it has for example been sold or if the seller has chosen to take it on the market. 

 <img>

     

## Testing
I have manually tested this project by doing the following:

Passed the code through a PEP8 linter and confirmed there are no major issues.


- Click the "Use This Template" button.
- Give your repository a name, and description if you wish.
- Click the Create Repository from Template to create your repository.
- Click the Gitpod button to create a gitpod workspace, this can take a few minutes.
- When working on a project using Gitpod, please open the workspace from Gitpod, this will open your previous workspace rather than creating a new one.
- Use the following commands to commit your work, git add. - adds all modified files to a staging area.

git commit -m "A short message explaining your commit" - commits all changes to a local repository.

git push - pushes all your committed changes to your GitHub repository.

- Before making the first commit: PLEASE MAKE SURE NEVER TO PUBLISH SECRET KEYS, ADD THE env.py TO A .gitignore TO AVOID PUSHING KEYS TO GITHUB.

### Heroku Deployment

1. Log into Heroku
2. Create a new app, choose a location closest to you
3. Search for Heroku Postgres from the resources tab and add it to your project
4. Make sure to have dj_database_url and psycopg2 installed.

pip3 install dj_database_url pip3 install psycopg2

5. log in to the Heroku CLI - Heroku login -i
6. Run migrations on Heroku Postgres - Heroku run python manage.py migrate
7. Create a superuser - python manage.py createsuperuser
8. Instal gunicorn - pip3 install gunicorn
9. Create a requirements.txt file - pip3 freeze > requirements.txt
10. Create a Procfile (note the capital P), and add the following,

web: gunicorn realestate.wsgi

11. Disable Heroku from collecting static files

heroku config:set Remove the Collect static from config vars. 

12. Add the hostname to the project settings.py file
ALLOWED_HOSTS = ['real-estate0413.herokuapp.com', 'localhost']

13. Connect Heroku to your Github, by selecting Github as the deployment method and searching for the GitHub repository and pressing


14. In Heroku, within settings, under config vars select

Reveal config vars

15. Add the following

DATABASE_URL = URL to the database CLOUDINARY_URL = URL to cloudinary SECRET_KEY = The secret key

16. Commit and push in your CLI

git add. git commit -m "Initial commit" git push

17. Go back to the Deploy tab and press
Deploy Branch

18. Your deployed site can be launched by clicking Open App from its page within Heroku.

- <a href=""> HTML</a>
- <a href="">CSS </a>
- <a href=""> Javascript</a>
- <a href=""> Python</a>
- <a href=""> Django</a>
- <a href=""> ElephantSQL</a>
- <a href=""> Bootstrap</a>
- <a href=""> Heroku</a>
- <a href=""> Cloudinary</a>
- <a href=""> Github</a>
- <a href=""> Gitpod</a>
- <a href=""> </a>
- <a href=""> </a>
- <a href=""> </a>
- <a href=""> </a>
- <a href=""> </a>


## Credits 

#### Code 

#### Bootstrap


#### Django

Issues with code
- Most of my problems were solved with the help of Tutor Support, W3Schools, Stack Overflow, and my Mentor Harry. 