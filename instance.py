import boto3
resource=ec2.boto3('ec2')
instances=ec2.create_instances(
        ImageId="ami-33ami8888"
        InstanceType="t2.micro"
        MinCount="3"
        MaxCount="6"
        Security_Group_Ids="sg-sggs3535"
        SubnetId="445dsgug"
        
    )

import boto3
resource=ec2.boto3('ec2')
instances=ec2.stop_instances(
        Instance_Id="i-eeettccxd353"
        )
