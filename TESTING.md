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

</details>

<hr>

<details>
<summary>Python:</summary>
The Python for this site has been linted by both the built-in linter in VSCode as well as the <a href="https://pep8ci.herokuapp.com/">Code Institute Pep8 linter</a>. No significant errors were found other than indications that some lines were too long and warnings where I preferred to use tabs instead of spaces.



</details>
<hr>




## Accessibility:
- I have checked the site for accessibility with Google's Lighthouse tool.
    - For Mobile: 
        ![Home Page Wireframe](media/lighthousemobile.png)
        
        
    - For Desktop:
        ![Home Page Wireframe](media/lighthouse.png)


## Bugs

### Solved
- Deployment to Heroku
    - When I initially attempted to deploy this project to Heroku (using AWS S3 for static files), I was unable to get my static files to load to AWS S3. I managed to solve this when I found that I had an unneccessary environment variable that was preventing me from uploading static files.

### Unsolved
- Subscription form:
  - As I ran out of time, I was unable to place the subscription form in a better place. In the future 
- Several purchases allowed:
  - At the moment, users are allowed to repurchase an item that they already own. In the future, I could prevent this and redirect them to the page where they could download the file.
- No Messages:
  - In the interest of time, I did not add messages to this webapp. However, most of the functionality is place to display these messages. This is certainly something that could be done in the future.