# Chinese to Begin

###### Code Institute / Full Stack Frameworks With Django

ChiBegin is a Chinese institute website built by using Pythons Django framework and hosted by using Heroku.

This is a language learning institute website that promote their Chinese teaching to the language learner. The interested one can register the course by purchasing the course at the website. They can view their order history at their own profile page. They can also contacting the website admin to have more queries on the course or the institute itself.

The deployed website can be found at here: **[CHIBegin](https://chinese-to-begin.herokuapp.com/)**

## UX
This website can be split into 2 sections:
1. The normal user section - They can navigate to normal user section only, such as to view the information at the website, to register a course, to manage their own profile, to view their order history, and to contact the website admin.
2. The super user section - They can navigate beyond than a normal user, such as to manage the store, add, update and delete the course.

The design of the website is more on simplistic yet appeared to be eye catchy and easy to be navigated. The navigation bar is sticked on top so that the user could easily navigate despite of the scroll location. Scroll to top button also provided to ease the user back to the top of certain page. The used of colors are random but suit to the theme of the website.

### User Stories

<img src="media/user_stories/user-stories.JPG" align=top width=1000>

### Design

#### Application Framework
Django framework is used in the website.

#### Database
The sqlite3 database was used during the development. The PostgreSQL database was used when the website deployed to Heroku.

Besides the normal e-commerce website models, such as the model of Store, UserProfile, Order and OrderLineItem, I have added 2 more models, that are Condition and Contact for future features. Condition model was added to indicate the existing or archive courses in the store so we can only show the existing courses to the user. While the Contact model was added to let the user to contact the website admin for any enquiry on the courses.

<img src="media/models/models.png" align=top width=800>

#### CSS Framework
Bootstrap v4.5 framwork was used in the website.

#### Icon
Font Awesome 5 was used throughout the project, across all the pages.

#### Typography
Only 1 type of font is used throughout the website: **[Merriweather](https://fonts.google.com/specimen/Merriweather?query=Merriweather)**

### Wireframes
The wireframes were created at the beginning of the project by using **[balsamiq](https://balsamiq.com/)**. The final website are similar to the created wireframes, yet do differ as adding some functionalities and designs to all the pages.

#### Desktop & Tablet View
##### [Home] | [Tips of Learning] | [Store] | [About] | [My Account]
<img src="media/wireframe/index_d_t.png" align=top width=200>&nbsp;
<img src="media/wireframe/tips_of_learning_d_t.png" align=top width=200>&nbsp;
<img src="media/wireframe/store_d_t.png" align=top width=200>&nbsp;
<img src="media/wireframe/about_d_t.png" align=top width=200>&nbsp;
<img src="media/wireframe/signin_d_t.png" align=top width=200>

#### Mobile View
##### [Home] | [Tips of Learning] | [Store] | [About] | [My Account]
<img src="media/wireframe/index_m.png" align=top width=200>&nbsp;
<img src="media/wireframe/tips_of_learning_m.png" align=top width=200>&nbsp;
<img src="media/wireframe/store_m.png" align=top width=200>&nbsp;
<img src="media/wireframe/about_m.png" align=top width=200>&nbsp;
<img src="media/wireframe/signin_m.png" align=top width=200>

## Features

### Current features
#### Home
#### Tips of Learning
#### Store
#### About
#### User Registration
#### User Login

### Future features