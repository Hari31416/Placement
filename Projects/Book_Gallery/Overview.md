- [1. The Data Source](#1-the-data-source)
- [2. Aim of the Project](#2-aim-of-the-project)
- [3. The Front-End of the Project](#3-the-front-end-of-the-project)
- [4. The Back-End](#4-the-back-end)
- [5. Database](#5-database)
- [6. Deployment](#6-deployment)
- [7. Result](#7-result)
- [8. Question Section](#8-question-section)
  - [8.1. If you were to do something differently, what would that be?](#81-if-you-were-to-do-something-differently-what-would-that-be)
  - [8.2. What were the most challenging aspect of the project and how you overtook it?](#82-what-were-the-most-challenging-aspect-of-the-project-and-how-you-overtook-it)
  - [8.3. What did you learn from this project?](#83-what-did-you-learn-from-this-project)
  - [8.4. Some mistakes you made and how you fixed them?](#84-some-mistakes-you-made-and-how-you-fixed-them)
  - [8.5. What improvements can be made?](#85-what-improvements-can-be-made)
# 1. The Data Source
The data is scraped from multiple source. Two main sources are:
1. [Goodreads](https://www.goodreads.com/): Book related infomation
2. [Amazon](https://www.amazon.com/): Images of the books

# 2. Aim of the Project
The website is a kind of gallery of books. The website features hundreds of books organized by various authors and in many genre. The website provides some basic information about the books and also provides so images of the book.

The idea was to use the skills learned by me related to front end and back end to create a website. This will challenge me to do something new and learn new skills. The reason I chose a book gallery is because I love reading books and I wanted to create something that makes me feel satisfied and happy.
# 3. The Front-End of the Project
The website is written using express, ejs and nodejs. There are three main pages:
1. Home Page
2. Book Page
3. All Books Page
# 4. The Back-End
The app is written in express, ejs and nodejs. For database, I've used mongodb by using the library mongoose. The back-end is designed follwoing the Restful API design. There are three main routes:
1. `/`: Home Page
2. `/books`: All Books Page
3. `/books/:id`: Book Detail Page

Apart from these, on the `/books` route, I've used query parameters to filter the books which lets us filter books by author, genre as well as series.
# 5. Database
As database, I've used mongodb. Using the library mongoose makes using mongodb more easier.

# 6. Deployment
The website is deployed on [heroku](https://h31416-book-gallery.herokuapp.com/) as well as on microsoft [azure](https://hari31416-bookgallery.azurewebsites.net/). As heroku is closing its free tier, the app won't be available on heroku after November 28.

# 7. Result
The website can be accessed on [heroku](https://h31416-book-gallery.herokuapp.com/) as well as on microsoft [azure](https://hari31416-bookgallery.azurewebsites.net/). This contains over 400 books.
# 8. Question Section
## 8.1. If you were to do something differently, what would that be?
I would like to have some more routes, such as an author route and genre route. Also, the way I've scraped the data can be modified. I might use some sophisticated framework like scrapy for this.

## 8.2. What were the most challenging aspect of the project and how you overtook it?
Scraping the required data was quite a challenge. I needed a large number of attributes and multiple images to display. First, I tried using BS4. However, it turned out to be insufficient as some of the data were available only after interacting with the DOM element. Later, I used Selenium which gives you options to interact with the DOM elements. This was a good choice as it gave me the required data.

## 8.3. What did you learn from this project?
There are a number of skills which I learned from this project. Some of them are:
1. Scraping data using selenium
2. Using mongodb as database and mongoose as library
3. RESTful API design
4. Query parameters
5. Deploying on heroku and azure
   
... and many more

## 8.4. Some mistakes you made and how you fixed them?
One of the silly mistake which I made was this: My password of mongodb contained some special characters. While connecting with mongodb, I was passing them 'as is', without using url encoding. This caused the connection to fail. I fixed this by using url encoding.

## 8.5. What improvements can be made?
There are a number of improvements which can be made. Some of them are:
1. Adding more routes, especially author and genre routes
2. Adding more books
3. Adding more attributes to the books
4. Implementing a search bar
5. Adding CRUD operations