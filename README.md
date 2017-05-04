## A basic user sign up form using Flask and MySQL ##

This is a simple sign up form built with the Flask framework and MySQL. This was made following the tutorial at [envatotuts](https://code.tutsplus.com/tutorials/creating-a-web-app-from-scratch-using-python-flask-and-mysql--cms-22972?utm_source=ActiveCampaign&utm_medium=email&utm_content=Advanced+Beginner+Challenge%3A+Python+Day+19&utm_campaign=Python+Day+19). Most of the functionality is built into app.py, and the form takes a username, password, and email and saves it to the MySQL database.

For the purposes of this tutorial the password max length was kept short, as when the password is hashed it's easy to overshoot 255 characters in a VARCHAR-type variable. 

Cheers,
Wolf
