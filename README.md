# amazon-web-services

# CREATE EC2 INSTANCE USING BOTO3 LIBRARY

# Step1:
Install boto3 and awscli

pip install boto3

pip install awscli



# Step2: 
Go to IAM and create a new user and give programmatic access and also add the policy AmazonEC2FullAccess
    
# Step3: 
In the terminal, make changes in aws configure and add the following.
When you create a new  user you will get the AWS access key id and AWS secret access key.

AWS Access Key ID [None]: enter the access key id

AWS Secret Access Key [None]: Enter the secret access key id

Default region name [None]: region name you are in

Default output format [None]: json


# Step 4:
Code

Create instance

Describe instance

Stop instance

Start instance

Terminate instance:

You can parallelly check if the operations are running successfully.

