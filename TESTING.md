## Testing (Post Development)

**Validation**

[HTML](https://validator.w3.org/nu/?doc=https%3A%2F%2Femerald-isle-jewelry-af11dcd57db0.herokuapp.com)

No HTML errors found 


[CSS](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Femerald-isle-jewelry-af11dcd57db0.herokuapp.com&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)

No CSS errors found.

**Python - PEP8 - using pycodestyle**

I utilized the "pycodestyle" tool to assess my Python code. "pycodestyle" is a command-line utility obtainable through pip installation. I executed the command "pycodestyle --first <-appname->," modifying it based on the documentation's recommendation. This command scans through all files within both the main and subdirectories of the app and promptly reports the initial encountered error.

I did work through all reported errors but there are a handful of E501 errors in various files I decided not to shorten.
For example the `AUTH_PASSWORD_VALIDATORS` settings in my settings.py file. It is not advisible to shorten those. 

## Lighthouse Scores 

**Home**

![](/media/Lh_home.png)

**Product Page**

![](/media/Lh_products.png)

**Checkout Page**

![](/media/Lh_checkout.png)

**Testimonials**

![](/media/testimonials_lh.png)

**Contact Form**

![](/media/contact_lh.png)

**Profile Page**

![](/media/profile_lh.png)

## Manual Testing

For the following, I will skip the type of user, i.e. "As a shopper, I can…” and only list the latter part of the story as a heading

**Set up and deployment**

 *Site accessibility*

  * Result Passed : Access the site via the deployed URL on the desktop
  * Result Passed : Access the site via the deployed URL on the tablet
  * Result Passed : Access the site via the deployed URL on the mobile

 *Viewing & Navigation*

  * Result Passed : Site has a clear purpose and it is easy to navigate
  * Result Passed : All navigational links take user to correct page
  * Result Passed : Can view products
  * Result Passed : All products render a description , price and rating
  * Result Passed : Can view total of purchases at any time

 *Registration and User Accounts*

  * Result Passed : Guest can create account
  * Result Passed : User can login and logout of account
  * Result Passed : Recover password if lost
  * Result Passed : Receive email after registering
  * Result Passed : View personal order history, shipping information
  * Result Passed : Be able to update shipping information

 *Sorting & Searching*

  * Result Passed : Products can be easily sorted by price, name, rating & alphabetically
  * Result Passed : Products can be viewed by category
  * Result Passed : Products can be found via the search bar when searching by name or description

 *Purchasing & Checkout*

  * Result Passed : Easily select size and quantity
  * Result Passed : View Items in bag
  * Result Passed : Be able to link back to products from shopping bag
  * Result Passed : Be able to link back to bag from checkout page
  * Result Passed : View order summary in checkout page
  * Result Passed : Ability to save items for later and have that information stored on users profile
  * Result Passed : Prompt user with how much extra they need to spend to gain free shipping
  * Result Passed : Charge shipping for orders which do not meet the $100 limit
  * Result Passed : Do not process orders unless all required fields are filled out
  * Result Passed : Do not process orders which use incorrect credit card information
  * Result Passed : Ability to enter payment information and ensure it works and processes orders
  * Result Passed : Order information been passed onto stripe
  * Result Passed : Process order if payment hits stripe and page crashes
  * Result Passed : View order confirmation after purchase
  * Result Passed : Receive confirmation email after purchase
  * Result Passed : Ability to add testimonial after purchase which saves to the database

 *Store Owners*

  * Result Passed : Add product to store when logged in as the store owner
  * Result Passed : Ensure required fields must be complete before adding/editing product
  * Result Passed : Edit/update product to store when logged in as the store owner
  * Result Passed : Delete product from store when logged in as the store owner   

 *SEO*

  * Done : Robots.txt
  * Done : Sitemap
  * Done : Descriptive meta tags in the HTML

 *Other*

  * Result Passed : View testimonials from recent purchases
  * Result Passed : Dont allow testimonial complete unless all fields are filled out
  * Result Passed : Dont allow testimonial complete unless a number between 1-5 is entered in the rating box
  * Result Passed : Ability to contact store via the contact form and ensure that information saves to the database
  * Result Passed : Prompt user to fill our required fields on contact form if they do not do so
  * Result Passed : Prompt user with a success message once contact form has completed
  * Result Passed : Allow users to subscribe to newsletter and pass that information onto the mailchimp account
  * Result Passed : Facebook link in footer redirects to Facebook page
  * Result Passed : Custom 404 page

[Back to README](https://github.com/oconnorian3/emerald-isle-jewelry/blob/main/README.md)