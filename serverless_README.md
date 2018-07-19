# Serverless in Baidu's Machine Translation API #

### How it Works: ### 

The serverless framework is combined with the AWS cloud provider to put the powerpoint translation service on a server. First, the user's selected powerpoint gets uploaded to a S3 bucket, in this case mine. Then, the submitter function takes the powerpoint and sends an URL to the serverside's translate function, where the file is stored in the user's /tmp directory and downloaded before getting translated by Baidu's Machine Translation API and sent back to the S3 bucket. Finally, the translated powerpoint is opened in a browser.  

****************************************************************************************************
### Setup: ###

Sign up for AWS S3 [here](https://aws.amazon.com/s3/)

Create a S3 Bucket [here](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html)

Create a new identity pool [here](https://docs.aws.amazon.com/cognito/latest/developerguide/identity-pools.html)

Update IAM roles in Cognito [here](https://docs.aws.amazon.com/cognito/latest/developerguide/iam-roles.html)

CloudWatch Logs
* Used for keeping track of requests. Learn more about them [here](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) 

****************************************************************************************************
### Feedback ###

Please make an issue, and we'll get back to you as soon as possible. 
