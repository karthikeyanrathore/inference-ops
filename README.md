## Access Policy Plugin

> template for future django projects with UI web user auth + 2FA.

Aim of this project is to understand how user authentication and 2FA works with django and django-rest-framework.

To do List:
* first look into [account/ healthcheck github repo](https://github.com/healthchecks/healthchecks/tree/master/hc/accounts)
* implement your version of it. which includes 2FA
* after that check how same functions works in djano-rest-framework. for refernce checkout: https://github.com/pretix/pretix/blob/master/src/pretix/control/views/auth.py
* pretix has some complex 2FA implementation.

In the end we will have working model for 2fa which we can extend in our other projects.

