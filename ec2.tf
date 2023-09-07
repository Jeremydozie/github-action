provider "aws" {
    region = "us-east-1"
  
}

resource "aws_instance" "jay_ec2-test" {
    instance_type = "t2.micro"
    ami = "ami-053b0d53c279acc90"
    tags = {
      Name = "jay-instance"
    }
  
}


