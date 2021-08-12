## MFE for custom login and register 
This is a micro-frontend application responsible for the login, registration and password reset functionality.

https://github.com/edx/frontend-app-authn

End modified for Tutor Open edX. 
It works fine but, please test it before using in production !



### Installation:
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

Building process takes some time, please be patient :)

$ tutor local quickstart

visit http://authn.yourdomain.com/login.

or

visit https://authn.yourdomain.com/login


![](/src/authn.gif)