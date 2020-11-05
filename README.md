[![Contributors][contributors-shield]][https://github.com/tonykingnz/hugapi-acme-api/graphs/contributors]
[![Forks][forks-shield]][https://github.com/tonykingnz/hugapi-acme-api/network/members]
[![Issues][issues-shield]][https://github.com/tonykingnz/hugapi-acme-api/issues]


<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/tonykingnz/hugapi-acme-api/">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">ACME Company API</h3>

  <p align="center">
    An API designed to ACME company to create store, item, and make simple orders.
    <br />
    <a href="https://github.com/tonykingnz/hugapi-acme-api/"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/tonykingnz/hugapi-acme-api/">View Demo</a>
    ·
    <a href="https://github.com/tonykingnz/hugapi-acme-api/issues">Report Bug</a>
    ·
    <a href="https://github.com/tonykingnz/hugapi-acme-api/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

This projetc is designed to help the ACME Company have an API, that could manange they store, registring and creating with information like address. Also is possible to registre items for sale for each store an even procede with simple order (No payment).


### Built With

* [Hug - API](http://hug.rest/)
* [Postgress](https://www.postgresql.org)
* [OpenAPI 3.1](https://swagger.io)



<!-- GETTING STARTED -->
## Getting Started

Download a copy of this repo and run the following command inside *hugapi_src*:

> hug -f app.py

The server will be up in the port 8000 of the localhost

### Prerequisites

You must have the python lastest version installed, and run all the following commands:
* npm

> apt-get update
> apt upgrade

> apt install git
> apt install vim -y
> apt-get install postgresql -y

> pip install --upgrade pip

> pip3 install hug -U 
> pip install psycopg2
> pip install swagger-ui-bundle
> pip install openapi-spec-validator

Or you can simple run the docker image with docker-compose:

> docker-compose up -d

and the:

> docker exec -it **your_workspacename (***docker ps*** **and find the workspace name)**

## Usage

Check the Swagger documentation to know how to run the API:





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo.svg?style=flat-square
[contributors-url]: https://github.com/github_username/repo/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo.svg?style=flat-square
[forks-url]: https://github.com/github_username/repo/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo.svg?style=flat-square
[stars-url]: https://github.com/github_username/repo/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo.svg?style=flat-square
[issues-url]: https://github.com/github_username/repo/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo.svg?style=flat-square
[license-url]: https://github.com/github_username/repo/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/github_username
[product-screenshot]: images/screenshot.png
