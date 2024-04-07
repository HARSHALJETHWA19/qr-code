Terraform Deployment of App on
AWS Serverless Services

● An API that processes images or videos an example of a QR Code Generator

Steps
1. Create a Serverless function.
2. Write the code for your function. Your function should handle incoming HTTP requests
and return a response.
3. Deploy your function to the cloud.
4. Create an API Gateway resource or HTTP trigger and configure it to trigger your
Serverless function.
5. Test your API by sending HTTP requests to the API Gateway resource.
6. Write IaC for your Serverless Function so that you can use code to deploy it. You can use
any one of the following: Terraform or Pulumi.
7. Set up a GitHub repository where you will push your serverless function code and IaC
code.
8. Set up a CICD pipeline to deploy your Function

QR Code Generator
I built an API using AWS Lambda that accepts POST requests with a URL field in the body and
generates a QR Code for the provided URL, saves the QR Code in the S3 bucket, and then sends
back the QR Code S3 Object with 200 OK responses.
