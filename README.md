<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/OGWJ/express-flask-microservice-demo">
    <img src="https://ogwj-public-bucket.s3.eu-west-2.amazonaws.com/favicon.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Polyglot Micro-Service Development with Express, Flask and Docker</h3>

  <p align="center">
    In this example, we use an Express server to send an image across a local Docker network for classification by a neural net hosted on a Flask server.
    <br />
    <a href="https://github.com/OGWJ/express-flask-microservice-demo"><strong>View the Blog Post »</strong></a>
    <br />
    <br />
    <a href="https://github.com/OGWJ/express-flask-microservice-demo/issues">Report Bug</a>
    ·
    <a href="https://github.com/OGWJ/express-flask-microservice-demo/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#prerequisites">Installation</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

* You have docker installed. See https://docs.docker.com/get-docker/ for how to install Docker on your local system.

### Installation and Usage
1. Clone the repo
   ```sh
   git clone https://github.com/OGWJ/express-flask-microservice-demo.git
   ```
2. Check Docker engine is running\*
3. Start your micro-service application
    ```sh
    cd express-flask-microservice-demo && docker-compose up
    ```
4. Visit localhost:3000 to get predictions for your image.

5. Try swapping out the image.jpeg (for another named image.jpeg) in the express-requests directory.

6. Finished? Ctrl+C in your application terminal and clean up your system with
    ```sh
    docker-compose down --rmi all --volumes --remove-orphans
    ```
7. Stop Docker\*

8. Remove the local repository from your system
    ```sh
    cd .. && rm -rf express-flask-microservice-demo
    ```

* (\* this will depend on your OS- see documentation linked in Prerequisites)

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact

Owen Jenkins - [@LinkedIn](https://www.linkedin.com/in/owenglynwilliamjenkins/) - owenglynwilliamjenkins@gmail.com

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* The keras image classification code is inspired by a blog post on Keras' website by [Adrian Rosebrock](https://blog.keras.io/building-a-simple-keras-deep-learning-rest-api.html)