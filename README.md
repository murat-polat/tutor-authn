## MFE for custom login an register
This is a micro-frontend application responsible for the login, registration and password reset functionality. End modified for Tutor Open edX. This is an example plugin for to implement a micro-frontend application to Tutor Open edX.  Please test it before using in production !

Cloning and configuring Frontend-app-logistration
Step 1: Fork this repository from edx https://github.com/edx/frontend-app-authn to your GitHub account


Installation:
If using virtualenv: (optional)

$ python3 -m venv ~/tutor

$ source ~/tutor/bin/activate

### Cloning and installing plugin

$ git clone https://github.com/murat-polat/tutor-authn 

$ pip3 install -e tutor-authn

$ tutor plugins list

$ tutor plugins enable authn

$ tutor config save

Building new Docker services for Tutor

$ tutor images build authn

$ tutor local quickstart

visit http://yourdomain.com:1999/login.

Django Admin site redirection(login and register pages)
By default Open edX login page is " LMS_HOST/login ". But on Logistration is " LMS_HOST:1999/login ". So we must redirect login and register pages to the new login pages . There are different ways available for redirections. But the most easiest way, to do that on the Django Admin side.

To add new site go to the http://yourdomain.com/admin/sites/site/ and add new site for Logistration service: (LMS_HOST:1999)

After adding new page go to the http://yourdomain.com/admin/redirects/redirect/ and add new redirection for login page
