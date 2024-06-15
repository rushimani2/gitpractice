import boto3
ec2=resource.boto3('ec2')
instances=ec2.create_instances(
        ImageId='ami-3343ddsd'
        InstanceType='t2.micro'
        MinCount='4'
        MaxCount='5'
        Security_groupIds='sg-ggskd44'
        SubnetId='sub-6343'
        KeyName='Linuxmanchine'
        )


import boto3
ec2=resource.boto3('ec2')
instances=ec2.stop_instances(
        InstanceId='i-dkddasd3434'
        )
