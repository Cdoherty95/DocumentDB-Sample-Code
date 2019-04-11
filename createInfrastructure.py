import boto3
import urllib


# This function will add your public IP Address to the security group allowing all traffic
def add_ip_to_security_group():

    # Get our Public Ip address and decode it to be a string
    our_public_ip = urllib.request.urlopen('http://ip.42.pl/raw').read().decode("utf-8")

    # Create our client object referencing boto3 access to the ec2 service
    client = boto3.client('ec2')

    # We are describing the security group to get the ID and name of the group
    response = client.describe_security_groups()

    # We are setting the group ID and name received from the response to individual variables
    security_group_id = response['SecurityGroups'][0].get('GroupId')
    security_group_name = response['SecurityGroups'][0].get('GroupName')

    # Creating a variable object referencing the resources part of the SDK
    ec2 = boto3.resource('ec2')

    # Creating our security group client and passing the group Id so it know what we want to work with
    security_group_client = ec2.SecurityGroup(security_group_id)

    # Formatting out public IP Address to be in cider notation
    cidr_ip = str(our_public_ip + "/32")

    try:
        # Call to function to add your public IP address to the security Group
        security_group_client.authorize_ingress(
            GroupName=security_group_name,
            IpPermissions=[
                {
                    # -1 is used to allow all traffic
                    'FromPort': -1,
                    'IpProtocol': "-1",
                    'IpRanges': [
                        {
                            'CidrIp': cidr_ip,
                            'Description': 'Our Public IP Address'
                        },
                    ],
                    'ToPort': -1
                },
            ],
        )
    except Exception as e:
        error = str(e)
        if "already" in error:
            print("Your Ip address is already allowed in the security group")
        else:
            print(e)

    # End of add_ip_to_security_group
    return


# This function will launch an EC2 instance
def create_ec2_instance():

    # Create our client object referencing boto3 access to the ec2 service
    client = boto3.client('ec2')

    # We are describing the security group to get the ID and name of the group
    security_group_id = client.describe_security_groups()['SecurityGroups'][0].get('GroupId')

    # Calling the method to launch our ect instance
    client.run_instances(
        ImageId='ami-0830de8c36a487d4a',
        InstanceType='t2.micro',
        KeyName='documentdbKey',
        MaxCount=1,
        MinCount=1,
        Placement={
            'AvailabilityZone': 'us-east-1a',
        },
        SecurityGroupIds=[
            security_group_id
        ],
        IamInstanceProfile={
            'Name': 'EC2RoleForDocumentDBTutorial'
        },
    )

    # End of create_ec2_instance function
    return


# This function will create the DocumentDB cluster and instances
def create_document_db():

    # Create our client object referencing boto3 access to the DocumentDB service
    docDBclient = boto3.client('docdb')

    # Create our ec2 client referencing boto3 access to the ec2 service
    ec2client = boto3.client('ec2')

    # We are describing the security group to get the ID and name of the group
    security_group_id = ec2client.describe_security_groups()['SecurityGroups'][0].get('GroupId')

    # Setting the DocumentDB Cluster Identifier to a variable to be referenced multiple times
    documentdb_id = 'documentdb-cluster-id'

    docDBclient.create_db_cluster(
        AvailabilityZones=[
            'us-east-1a',
        ],
        BackupRetentionPeriod=1,
        DBClusterIdentifier=documentdb_id,
        VpcSecurityGroupIds=[
            security_group_id,
        ],
        Engine='docdb',
        Port=27017,
        MasterUsername='documentdbUser',
        MasterUserPassword='documentdbPassword'
    )

    docdbInstId = ['documentdb-instance1']
    # docdbInstId = ['documentdb-instance1-1', 'documentdb-instance2-1']

    for instanceID in docdbInstId:
        docDBclient.create_db_instance(
            DBInstanceIdentifier=instanceID,
            DBInstanceClass='db.r4.large',
            Engine='docdb',
            AvailabilityZone='us-east-1a',
            DBClusterIdentifier=documentdb_id,
        )

    # This is the end of create_document_db function
    return


# add_ip_to_security_group()
# create_ec2_instance()
create_document_db()
