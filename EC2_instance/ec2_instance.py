'''
@Author: Naziya
@Date: 2021-09-23
@Last Modified by: Naziya
@Last Modified : 2021-09-23
@Title : Program Aim is to create an ec2 instance using boto3 library.
'''

from LoggerFormat import logger
import boto3

def create_ec2_instance():
    """
    Description:
    This method is used to create ec2 instance.
       
    """
    try:
        logger.info("Creating EC2 instance")
        
        ec2_resource = boto3.client("ec2")
        ec2_resource.run_instances(
            ImageId="ami-0c1a7f89451184c8b",
            MinCount=1,
            MaxCount=1,
            InstanceType="t2.micro",
            KeyName="naziya",
            
        )
    except Exception as err:
        logger.error(err)


def describe_ec2_instance():
    """
    Description:
    This method is used to describe ec2 instance and fetch the instance id.
       
    """
    try:
        logger.info("Describing EC2 instance")
        resource_ec2 = boto3.client("ec2")
        logger.info(resource_ec2.describe_instances()["Reservations"][0]["Instances"][0]["InstanceId"])
        return str(resource_ec2.describe_instances()["Reservations"][0]["Instances"][0]["InstanceId"])
    except Exception as err:
        logger.error(err)



def stop_ec2_instance():
    """
    Description:
    This method is used for stopping instance
       
    """
    try:
        logger.info("Stopping EC2 instance")
        instance_id = describe_ec2_instance()
        resource_ec2 = boto3.client("ec2")
        logger.info(resource_ec2.stop_instances(InstanceIds=[instance_id]))
    except Exception as err:
        logger.error(err)


def start_ec2_instance():
    """

    Description:
    This method is used to start ec2 instance.
       
    """
    try:
        logger.info("Start EC2 instance")
        instance_id = describe_ec2_instance()
        resource_ec2 = boto3.client("ec2")
        logger.info(resource_ec2.start_instances(InstanceIds=[instance_id]))
    except Exception as err:
        logger.error(err)


def terminate_ec2_instance():
    """
    Description:
        This method is used for deleting instance
       
    """
    try:
        logger.info("Terminate EC2 instance")
        instance_id = describe_ec2_instance()
        resource_ec2 = boto3.client("ec2")
        logger.info(resource_ec2.terminate_instances(InstanceIds=[instance_id]))
    except Exception as err:
        logger.error(err)

if __name__ == "__main__":

    create_ec2_instance()
    #describe_ec2_instance()
    #stop_ec2_instance()
    #start_ec2_instance()
    #terminate_ec2_instance()

