terraform{
provider{
resource{
aws={
resource="hashicorp/aws"
version="~5"
}
}
resource=aws{
instances="create_instances""linux machine"{
ami="ami-3355addaf"
instance_type="t2.micro"
min_count="4"
max_count="6"
security_group_ids="sg-ee3334"
subnet_id="sub-333sghs"
}
}
}
}
