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

import boto3
<<<<<<< HEAD
resource=ec2.boto3('ec2')
instances=ec2.create_instances(
        ImageId='ami-335dddfgs'
        InstanceType='t2.micro'
        MinCount='3'
        MaxCount='5'
        Security_group_Id='sg-4454sdfggs'
        SubnetId='sub-33sgd'
        KeyName='Linuxkeypair'
=======
ec2=boto2.resource('ec2')
instances=ec2.reboot_instances(
        InstanceId='i-ddfgdsd33434'
>>>>>>> master
        


aws ec2 run_instances --image_id="i-jjdkd3434" --instance_type="t2.micro" --min_count="3" --max_count="4" --key_name="linux key pair" --security_group_ids="sg-ssdjd422r5" --subnet_id="sub-3343dgdds"

aws s3 mb s3://rushimanikanta bucket1

aws s3 rb s3://rushimanikanta bucket1
