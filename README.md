## Inference Ops

> template for future django projects with web user auth + 2FA.

Aim of this project is to understand how user authentication and 2FA works with django and django-rest-framework and "maybe" include point 1.01

(old) To do List:
* first look into [account/ healthcheck github repo](https://github.com/healthchecks/healthchecks/tree/master/hc/accounts)
* implement your version of it. which includes 2FA
* after that check how same functions works in djano-rest-framework. for refernce checkout: https://github.com/pretix/pretix/blob/master/src/pretix/control/views/auth.py
* pretix has some complex 2FA implementation.

In the end we will have working model for 2fa which we can extend in our other projects.

1.01 After this is finished, we can make interal tool for an organization who want to give access to LLM models based on there role in the project. call it "inference".

##  UML (version 1.1)
![](https://github.com/karthikeyanrathore/inference-ops/blob/main/inference_ops/assets/inference-ops_version_1.1.png)
