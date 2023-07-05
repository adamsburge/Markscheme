# Testing

## Responsive Testing
- Throughout the project:
    - The webapp has been manually tested for desktop on Google Chrome, Microsoft Edge, Firefox, Safari, Vivaldi and Arc. 
    - The webapp has been manually tested for mobile responsiveness on an iPhone 7, iPhone 8, and iPhone 14. The webapp has also been manually tested on an iPad 9th generation and an Onyx Boox NoteAir (1st generation). Additionally, Google devtools, [Am I Responsive?](https://ui.dev/amiresponsive) and [Screenfly](https://screenfly.org/) have been used to test the webapp on various other Apple and Android mobile phones and tablet devices from the iPhone 4 onward. 
    - The webapp looks good on all the major desktop web browsers and all the most popular tablet and mobile devices. I can confirm that the website looks good on all screensizes.

## Code Validator Testing

<details>
<summary>HTML:</summary>
The HTML for every webpage on this site has been checked for errors with the <a href="https://validator.w3.org/nu/">W3 NU HTML Checker</a> and cleared with no errors reported. Click below to see the validator testing scores.

<br>

<details>
<summary>Home Page</summary>
<img src="media/Readme-files/html-check-home.png">
</details>

<details>
<summary>About Page</summary>
<img src="media/Readme-files/html-check-about-png.png">
</details>

<details>
<summary>Staff Page</summary>
<img src="media/Readme-files/html-check-staff.png">
</details>

<details>
<summary>Product Pages</summary>

<details>
<summary>Workshops Page</summary>
<img src="media/Readme-files/html-check-workshops.png">
</details>

<details>
<summary>Add Workshop Page</summary>
<img src="media/Readme-files/html-check-add-workshop.png">
</details>

<details>
<summary>Workshop Detail Page</summary>
<img src="media/Readme-files/html-check-workshop-detail.png">
</details>

<details>
<summary>Digital Products Page</summary>
<img src="media/Readme-files/html-check-digital-products.png">
</details>

<details>
<summary>Add Digital Product Page</summary>
<img src="media/Readme-files/html-check-add-digital-product.png">
</details>

<details>
<summary>Digital Product Detail Page</summary>
<img src="media/Readme-files/html-check-digital-product-detail.png">
</details>

<details>
<summary>All Products Page</summary>
<img src="media/Readme-files/html-check-products.png">
</details>

<hr>
</details>

<details>
<summary>Checkout Pages</summary>

<details>
<summary>Bag Page</summary>
<img src="media/Readme-files/html-check-bag.png">
</details>

<details>
<summary>Checkout Form</summary>
<img src="media/Readme-files/html-check-checkout.png">
</details>

<details>
<summary>Checkout Success</summary>
<img src="media/Readme-files/html-check-order-history.png">
</details>

<hr>
</details>

<details>
<summary>Profile Pages</summary>

<details>
<summary>Normal User Profile</summary>
<img src="media/Readme-files/html-check-profile.png">
</details>

<details>
<summary>Superuser Profile</summary>
<img src="media/Readme-files/html-check-profile.png">
</details>

<hr>
</details>

<details>
<summary>Registration and Sign In Pages</summary>

<details>
<summary>Log In Page</summary>
<img src="media/Readme-files/html-check-log-in.png">
</details>

<details>
<summary>Sign Up Page</summary>
<img src="media/Readme-files/html-check-sign-up.png">
</details>

<hr>
</details>

<br>

</details>

<hr>

<details>
<summary>CSS:</summary>
The CSS for the site has been checked for errors with the <a href="https://jigsaw.w3.org/css-validator/">W3C CSS Validator</a> and passed with no errors found.

<br>

<img src="media/Readme-files/website-css-check.png">
</details>

<hr>

<details>
<summary>Javascript:</summary>
The Javascript for the site has been checked for errors with the <a href="https://jshint.com">JSHint Website</a> and no errors were found.

<br>

<details>
<summary>countryfield.js</summary>
<img src="media/Readme-files/js-check-countryfield.png">
</details>

<details>
<summary>stripe_elements.js</summary>
<img src="media/Readme-files/js-check-stripe_elements.png">
</details>

</details>

<br>

<hr>

<details>
<summary>Python:</summary>
The Python for this site has been linted by both the built-in linter in VSCode as well as the <a href="https://pep8ci.herokuapp.com/">Code Institute Pep8 linter</a>. No significant errors were found excepting four lines from the settings.py file which were indicated as being too long. These lines, however, are part of the code for Allauth and cannot be altered without affecting the efficacy of that app. See below the images of the code validation for each python file.

<br>
<br>

<details>
<summary>Markscheme Project Urls.py</summary>
<img src="media/Readme-files/markscheme.urls.png">
</details>

<details>
<summary>Bag App</summary>

<details>
<summary>contexts.py</summary>
<img src="media/Readme-files/bag.contexts.png">
</details>

<details>
<summary>views.py</summary>
<img src="media/Readme-files/bag.contexts.png">
</details>

<hr>
</details>

<details>
<summary>Checkout App</summary>

<details>
<summary>admin.py</summary>
<img src="media/Readme-files/checkout.admin.png">
</details>

<details>
<summary>apps.py</summary>
<img src="media/Readme-files/checkout.apps.png">
</details>

<details>
<summary>forms.py</summary>
<img src="media/Readme-files/checkout.forms.png">
</details>

<details>
<summary>models.py</summary>
<img src="media/Readme-files/checkout.models.png">
</details>

<details>
<summary>signals.py</summary>
<img src="media/Readme-files/checkout.signals.png">
</details>

<details>
<summary>urls.py</summary>
<img src="media/Readme-files/checkout.urls.png">
</details>

<details>
<summary>views.py</summary>
<img src="media/Readme-files/checkout.views.png">
</details>

<hr>

</details>

<details>
<summary>Home App</summary>

<details>
<summary>urls.py</summary>
<img src="media/Readme-files/home.urls.png">
</details>

<details>
<summary>views.py</summary>
<img src="media/Readme-files/home.views.png">
</details>

<hr>
</details>

<details>
<summary>Products App</summary>

<details>
<summary>admin.py</summary>
<img src="media/Readme-files/products.admin.png">
</details>

<details>
<summary>forms.py</summary>
<img src="media/Readme-files/products.forms.png">
</details>

<details>
<summary>models.py</summary>
<img src="media/Readme-files/products.models.png">
</details>

<details>
<summary>urls.py</summary>
<img src="media/Readme-files/products.urls.png">
</details>

<details>
<summary>views.py</summary>
<img src="media/Readme-files/products.views.png">
</details>

<hr>
</details>

<details>
<summary>Profiles App</summary>

<details>
<summary>forms.py</summary>
<img src="media/Readme-files/profiles.forms.png">
</details>

<details>
<summary>models.py</summary>
<img src="media/Readme-files/profiles.models.png">
</details>

<details>
<summary>urls.py</summary>
<img src="media/Readme-files/profiles.urls.png">
</details>

<details>
<summary>views.py</summary>
<img src="media/Readme-files/profiles.views.png">
</details>

<hr>
</details>

<hr>
</details>

</details>
<hr>
<br>

## Accessibility:
- I have checked the site for accessibility with Google's Lighthouse tool.
    - For Mobile: 
        ![Lighthouse Mobile](media/Readme-files/lighthouse-mobile.png)
        
        
    - For Desktop:
        ![Lighthouse Mobile](media/Readme-files/lighthouse-desktop.png)


## Bugs

### Solved
- Deployment to Heroku
    - When I initially attempted to deploy this project to Heroku (using AWS S3 for static files), I was unable to get my static files to load to AWS S3. I managed to solve this when I found that I had an unneccessary environment variable that was preventing me from uploading static files.
- Several purchases allowed:
  - Early on in the development of the app, users were allowed to repurchase an item that they already own. I managed to prevent this by checking if the using is in the list of product owners before displaying the 'Add to Bag' button. This also provided a convenient place to put the digital file download button as it now replaces the 'Add to Bag' button when the user already owns the digital product.

### Unsolved

- No names in attendance list
  - Currently, the workshop attendance list displayed to the superuser only includes the emails of the individuals signed up for the workshop. In the future, I could rework the sign up form provided by Allauth to make it require a first and last name in order for the user profiles to have this information. Alternatively, I could split the full name that is gathered upon checking out for a workshop purchase and then save that information to the user's profile. 
- No Messages:
  - In the interest of time, I did not add messages to this webapp. However, most of the functionality is place to display these messages. This is certainly something that could be done in the future.