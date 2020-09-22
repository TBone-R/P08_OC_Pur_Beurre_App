# Application web Pur Beurre.

A python web application using the Open Food Fact resources to find substitutes
 to daily products.

## Fat, yes, but of quality!
_(fictive context)_ Remy and Colette, owner of the restaurant are concerned 
about their client's diet at home. In the hope that will help people to make
 healthier choices Remy and Colette wish to create a website that can help 
 to find substitutes in a few click.

## An academic project.
This repository one of the deliverable for the 8th project from the
Openclassrooms’s paths
 [“Développeur d'application - Python”](https://openclassrooms.com/fr/paths/68/projects/159/assignment)
.
#####Evaluated skill : 
* Create a web application respecting the load specifications given by the
client.
* Make use of integration tests, unit testing and create a test report.

## Setup.
This project uses a django framework.

After installing the requirements using pip install -r requirements.txt or by
author means, you can use the manage.py migrate then the manage.py
build_sample command before the runserver command to set up the website. 

If you wish to test the code you can do it using manage.py test followed by
the name of the app you want to test. The functional_tests contains the
functional test and only works on local wive a Edge web browser.

### Site model.

[Some sketches are given by the client](https://drive.google.com/file/d/0B43oBMW7-CwzVG82R1JfMDBiQms/view).

"home" /
>This page is the homepage and must contain 2 forms for search of a product in the database. It corresponds to the sketch 1.

"detail"	/\<int:id>/
>This contains the detailed view of a product. It corresponds to the sketch 3.

"result"	/result/
>This contains the result for the database search from the homepage’s forms.

"substitute"	/\<int:id>/substitute/
>This contains the result for the substitute search in the database. It corresponds to the sketch 2

"register"	/register/
"login"	/login/
"logout"	/logout/
>Are the basic views for an user

"save" 	/save/
>This is the views that save a product.

"myproduct"	/myproduct/
>This contains the saved product.

"myaccount"	/myaccount/
>This is the detailed view of a user.

"legal"	/legal/
>This contains all the legal mention.
