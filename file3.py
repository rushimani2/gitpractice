import boto3
ec2=resource.boto3('ec2')
instances=ec2.create_instances(
        ImageId='ami-334dgsdgdg'
        InstanceType='t2.micro'
        MinCount='3'
        MaxCount='9'
        Security_groupIds='sg-fsd3342'
        SubnetId='sub-ffs3342'
        KeyName='Linux'
        )
