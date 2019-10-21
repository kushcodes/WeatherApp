# WeatherApp

Website: [kushp.me](http://kushp.me)

This is a highly available Flask weather app that I built to learn more about Python, AWS, and CI/CD tools. I am using the OpenWeather API to get current weather data. You can select a city from the dropdown menu and get the current temperature and a corresponding weather icon. The static content is hosted in a S3 bucket. 

I have deployed this web app with Docker, GitLab, and AWS. I have an infrastructure pipeline that creates 2 CloudFormation Stacks. This creates all the resources necessary to deploy containers onto EC2 instances using ECS. 

The application pipeline builds and tags the Docker image and then pushes it to the ECR repository. The deploy stage of this pipeline creates a new container definition with the latest Docker image and updates the task definition. New EC2 instances will use the updated task definition with the latest Docker image. 
