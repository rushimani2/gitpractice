import boto3()
ec2.boto3= instances
ec2.instances={ run_instances
	image_id="ami-34rmahnas33"
	instance_type="t2.micro"
        count="3"
        key_name="linuxkeypair"
        security_group="sg-1222jdgdd88"
        subnet="sub-233jdgsss"
}	
