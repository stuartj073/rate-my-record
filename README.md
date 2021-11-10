# Rate My Record

In line with the criteria for the third milestone project I have chosen to adopt the first route in developing my own idea and bringing it to life. The idea chosen meets all CRUD criteria in making the dynamic website function and allows visitors to sign up/sign in at any given point of their own choosing.
The idea is quite simple. The website is a review sharing site which allows users to comment on specific albums/records/singles as well as record stores themselves. On their own profile page, user’s can view the reviews they’ve made in the past as well as editing them. They can also add reviews from other users to their own page using the ‘add to wishlist’ button displayed on reviews made from others on the landing page. Going with these features is the ability a user has to remove their own review as well as those from their wish list. 
The purpose of the website is to give user’s the chance to acquire and learn about new music/record stores they would’ve been unfamiliar with. The database is utilised in such a way as to prompt users into discovering new things and potentially providing some knowledge of their own musical taste. 
Going forward with this project, I would ideally like to allow user’s to interact with one another and to facilitate an online marketplace for the buying and selling of vinyl records. 

## User Stories 

- As a user I want to access a website that allows me to review a record and/or a record store.
- As a user I want to input my own reviews in a seamlessly easy fasion.
- As a user I want the site to make perfect sense upon my initial point of entry to it.
- As a user I want to be able to update my reviews on the website.
- As a user I want to be able to read other user's reviews.
- As a user I want to be able to search the website for any particular review of my choosing.
- As a user I want to be able to remove a review made by myself.
- As a user I want to have a neat, accessible and organised website that has a very clear outline from the moment I enter it.
- As a user I would like to be able to contact the site owner(s) over any issues/improvements that I see fit to further my experience on the website.
- As admin, I would like to mediate over all user's actions.
- As admin I would like to be able to communicate with user's and have their issues and improvement suggestions listened and seen to.
- As admin I want to ensure that user's are enjoying their experience as much as possible and ensure the website is as responsive to a mobile user as it is to a desktop user.
- As admin I want to ensure that all information supplied by the users is fair and just.


## UX/UI

### Scope

For this particularly project to flourish, it was vital that the correct steps and frameworks were utilised in order to provide the users a fluid manner in which to perform CRUD operations at will. 
The functional requirements utilised to achieve the project criteria were as follows:
- Materialise 
- Flask
- Python
- Flash 
- MongoDB

The features of the website were drafted up to suit the project criteria whilst also making sense for a potential user of the site itself. Being an online review page for music, I felt the following features were more than necessary for the website:

#### Current Features

- Landing page (with all reviews)
- Search bar (for all reviews)
- Log in page
- Register page
- About page
- Add a record review page
- Add a record store review page
- Edit a record review page
- Edit a record store review page
- Profile page (displays a user's reviews & wishlist)
- Delete button (for reviews)
- Add to wishlist button
- Remove from wishlist button
- Manage reviews page (for admin)
- Manage user's page (admin)
- Contact page
- Social links
- Site banner with core message

#### Features left to implement
- Direct Messaging: Allow user's to contact one another, which will promote the essence of the website in a more intimate matter as they discuss an album or store together.
- Marketplace: Eventually, I would like to push the website into the realm of e-commerce, allowing user's to advertise what they have got for sale and what they would like to purchase. Allowing them to search through the site will help users locate records they would like to buy and in tandem with direct messaging they will be able to set up a payment with the seller of said record.

### Structure

- The landing page (home page) will be home to every review made from all user's to the website. If it is a first time visitor to the site, the page will only work as to be read from. On the site banner above the image at the top of the page, the unregistered/not logged on user will have two links available to them. One for registering (which will bring a user to the registration page) and the other for loggin in. If the user is logged in then each review will have the following buttons below the review description: Add to wishlist (if the user didn't create the review), Edit & Delete (if they did create the review).

- The edit button will take the user to the edit review page/ edit store review page. Here they will be able to update all current information on the review to date.

- The delete button will permanently delete whatever review is chosen by the user. Admin has access to this button on every review on the site.

- The about page will give a brief background into what the website is all about. It will also have links for first time visitors to register or for current users to report something that is amiss.

- Log in/ Log out. In the navbar, these two options will be available to visitors to the website depending on whether they are currently logged in (log out displays) and vice-versa.

- The add a review link works as a dropdown and allows user's to decide on writing up a review on either a record or on a record store. 

- For the admin two additional pages will be available: Manage Reviews & Manage Users. Each page allows admin full control over the content of the site and who is able to contribute.

- Profile page has all of a user's reviews along with the reviews they have added to their own wishlist. The user can click into any review to view it and can remove any review from either their own review list or from their wishlist if they want.

- Each review will have it's own designated review page. This page provides full information on the review and if the user has created it they will have access to the edit and delete buttons.

### Skeleton

The site was first sketched on paper with a pen by myself before I attempted to make a more concrete blueprint using [Balsamiq](https://balsamiq.com/).

### Surface

In order to mitigate the effects of colour overload, I kept this in mind whilst debating which colours to use for the website.

- Colours
For the main body of the site I decided to utilise a background color of '#d7ccc8' and for the font color of all elements in the body element I used the hex color of '#212121'. For all headings on the site I used the 'jungle' font-family along with a background colour of '#a1887f'. All in all, I felt the background colours worked to project the core colours of the body elements very well. When I look at the site (across all pages) I feel that all sections are distinct and visible and this is more or less down to the combination of colours I conciously decided on at the onset of the project. 

- Typography
The font-families that were utilised throughout the project were: 'Zilla & Slab', 'Gabriel' & 'Jungle'. I didn't want to choose anymore than three as I felt that would work to distract the overall experience for a visitor to the website. 

- Images
The images used for the cover of the landing page was obtained through [unsplash] (https://unsplash.com/) as was the default image for the record store reviews. The default image for the record reviews was obtained through [google] (www.google.com).


### Landing Page

As stated in the above user stories, I want the main message of the site to become known to the user upon entering the website. When a user clicks on to the site, they will be greeted by a large cover photo with a backgdrop image of vinyl records. The banner presiding over the image reads: "Rate My Record.. A place for like-minded music lovers to contribute". Below it are two options allowing a first time visitor the option to register or a current user the chance to log back in. Below this (if a user is logged in) section is a search bar allowing user's to look for anything they are interested in. Following underneath the search bar are the various record and record store reviews left by user's registered on the website. Each part is accompanied with headings and each review is given it's own 'review-card'.

As to ensure the banner is as clear as possible over the site cover image I decided to make it right in the middle of the image, with a white background in order to facilitate an easy to read black color for the content of the page banner. The headings for the page are exactly 50% in width and have a '#a1887f'/brownish sort color along with a '#e0e0e0' border. Review cards are shown in rows of two on large screens and one by one on smaller devices. Again, the coloring is quite straightforward as to not produce color overload to the user(s) with a white background and black color for the content. Images for the reviews are shown as either the image provided by the user or else the default image as seen in the if statement for the image section in profile.html.

The background color to the website was chosen as '#d7ccc8'. I chose it as I felt that it allowed all corresponding elements and their colors to mix well with one another and it proved to project the main message of the website easily, accessibly and neatly.

### Profile

The profile page is split into two halves. On the left side are all the reviews the user has left on the website and on the right are the reviews that have been added to the user's wishlist. 

The reviews here are styled similiarly to the reviews as seen on the landing page but with a slight difference. The image element has no padding around it and instead takes up the top half of the review. On the bottom half of the review we are left with the review name which is either the album name or the record store name. Clicking on the review will lead the user to each individual review page which in turn provides full information on the review in question. 

### Manage Reviews

This page is only visible for the admin of the website. 



