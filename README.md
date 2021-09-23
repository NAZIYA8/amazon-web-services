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

AWS Access Key ID [None]: AKIAQU44RNYXGZV5X7QV

AWS Secret Access Key [None]: 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

Default region name [None]: ap-south-1

Default output format [None]: json


# Step 4:
Code

Create instance

Describe instance

Stop instance

Start instance

Terminate instance:

You can parallelly check if the operations are running successfully.

