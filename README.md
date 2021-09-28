# amazon-web-services

# Step 1:
Create an Amazon SageMaker Notebook Instance.

An Amazon SageMaker notebook instance is a fully managed machine learning (ML) Amazon Elastic Compute Cloud (Amazon EC2) compute instance that runs the Jupyter Notebook App. You use the notebook instance to create and manage Jupyter notebooks for preprocessing data and to train and deploy machine learning models. 

Open the Amazon SageMaker console at https://console.aws.amazon.com/sagemaker/. 
Choose Notebook instances, and then choose Create notebook instance.

On the Create notebook instance page, provide the following information (if a field is not mentioned, leave the default values):
For Notebook instance name, type a name for your notebook instance.

For Instance type, choose ml.t2.medium. This is the least expensive instance type that notebook instances support, and it suffices for this exercise. If a ml.t2.medium instance type isn't available in your current AWS Region, choose ml.t3.medium.


For the IAM role, choose Create a new role, and then choose Create role. This IAM role automatically gets permissions to access any S3 bucket that has sagemaker in the name. It gets these permissions through the AmazonSageMakerFullAccess policy, which SageMaker attaches to the role.
Choose Create notebook instance.
In a few minutes, SageMaker launches an ML compute instance—in this case, a notebook instance—and attaches a 5 GB of Amazon EBS storage volume to it. The notebook instance has a preconfigured Jupyter notebook server, SageMaker and AWS SDK libraries, and a set of Anaconda libraries.

# Step 2:
Create a Jupyter Notebook

Open the notebook instance as follows:
Sign in to the SageMaker console at https://console.aws.amazon.com/sagemaker/
On the Notebook instances page, open your notebook instance by choosing either Open JupyterLab for the JupyterLab interface or Open Jupyter for the classic Jupyter view.

Create a notebook as follows:

If you opened the notebook in the JupyterLab view, on the File menu, choose New, and then choose Notebook. For Select Kernel, choose conda_python3. This preinstalled environment includes the default Anaconda installation and Python 3.

If you opened the notebook in the classic Jupyter view, on the Files tab, choose New, and then choose conda_python3. This preinstalled environment includes the default Anaconda installation and Python 3.

Save the notebooks as follows:

In the Jupyter classic view, choose File, choose Save as..., and then rename the notebook.

# Step3: 
Creating s3 bucket and setting the output path
You can check if the bucket is created 
    
    
# Step4: 
Downloading the dataset and storing it in s3 bucket.

Train test split.

Saving train data into bucket.

Saving test data into bucket.
    
# Step5: 
Building Models Xgboost- Inbuilt Algorithm

Look for the XGBoost image URI and builds an XGBoost container.

Initialize the hyperparameters.

Construct a sagemaker estimator that calls xgboost container.

# Step6: 
Fit the model

# Step7: 
Deploy Machine learning model as Endpoints

Prediction of test data

Confusion matrix

# Step8: Deleting the endpoints.
