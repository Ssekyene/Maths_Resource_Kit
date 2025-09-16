<div align=center><img src=./static/images/icon.png width="150"></div>
<h1 align=center>Maths Resource Kit</h1>
<p align=center>Facilitating Effective Learning for New Lower Secondary Curriculum in Uganda</p>

[![Browse-pic](browse.PNG)](https://mrk.robkj.tech/concept_list)
<p align=center> Browse Math Concepts for a remarkable learning experience... 🚀</p>
<p align=center> Introduction | Recommended resources | Quiz questions | Activities of Integration | Conclusion
</p>

## Contents
* [About the Project](#about-the-project)
* [Setting up Project local deployment environment](#setting-up-project-local-deployment-environment)
    - [Install Project Requirements](#install-project-requirements)
    - [Setup the development Environment](#setup-the-development-environment)
    - [Run the main application and the api](#run-the-main-application-and-the-api)
* [Contribution](#contribution)
    - [How to Contribute](#how-to-contribute)
* [Related projects](#related-projects)
* [License](#license)
* [Author](#author)

## About the Project
[Maths Resource Kit](https://mrk.robkj.tech/) (MRK) is a web application platform that recommends curated `Mathematics resources` such as articles, blogs, videos and interactive tools from all over the internet to meet the need for understanding Mathematics concepts for a competence based learning strategy for `Lower Secondary Level`. Although the platform enlists concepts according to Uganda's curriculum, it is meant to support **every** Lower Secondary Level student/learner.

- Find more about MRK at this [blog](https://www.linkedin.com/posts/robertssekyene_maths-resource-kit-mrk-is-a-web-application-activity-7244402966227566592-2vaW?utm_source=share&utm_medium=member_desktop) at LinkedIn

## Setting up Project local deployment environment
The project was tested on Ubuntu 16.04 OS, if you dont use this OS, you may use a virtual Machine forexample you can use vagrant which and provision it with Ubuntu	16.04 OS (Vagrant requires a virtual Machine box. Oracle Virtual Box is preferrable for use).

Install git if you don't have it already with
```
sudo apt-get install git
```

Clone the repository to your local machine:
```
git clone https://github.com/Ssekyene/Maths_Resource_Kit.git
```
or with ssh
```
git clone git@github.com:Ssekyene/Maths_Resource_Kit.git
```

And follow the steps below:
1. [Install Project Requirements](#install-project-requirements)
2. [Setup the development Environment](#setup-the-development-environment)
3. [Run the main application and the api](#run-the-main-application-and-the-api)

### Install Project Requirements
- Install Python, version 3.8.16 and above
- Install Flask and all the dependencies
- Install MySQL and make sure you use the default settingS eg, the root user's password should be not changed
- Install MySQLdb module
- Install SQLAlchemy module

### Setup the development Environment
After installing all the above and the required dependencies, run the following:


```
cat setup_mysql_dev.sql | sudo mysql -uroot
```

``` 
cat 1-mrk_dump.sql | sudo mysql -uroot
```
```
source env-setup.sh
```


### Run the main application and the api
`In Terminal #0`: run the main application

```
python3 -m mrk
```

`In Terminal #1`: run the api

```
python3 -m api.app
```

> ⚠️ Make sure you're connected to the Internet for JQuery to load!

## Contribution
I welcome contributions to the development of this website! Whether you're a developer, designer, mathematician, sponsor or a student curious about Maths Resource Kit, your help is appreciated. 

### How to Contribute
For greater details, find me at:
- [Email](mailto:robertssekyene05@gmail.com) / [WhatsApp](https://wa.me/256755917055) / [x](https://x.com/robkj256)

Thanks!😊🤝 More awaits from you, for the progress of MRK

## Related projects
- [AirBnB_clone_v4](https://github.com/Ssekyene/AirBnB_clone_v4) (_A clone of [AirBnB](https://www.airbnb.com/) website developed at [ALX](https://www.alxafrica.com/) / [Holberton School](https://www.holbertonschool.com/)_)

## License
![MIT License](https://img.shields.io/badge/license-MIT-green)

## Author
- Ssekyene Robert - [LinkedIn](https://www.linkedin.com/in/robertssekyene/)
