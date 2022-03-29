terraform {
  backend "s3" {
    bucket         = "elimimi0926"
    key            = "Talent-Academy/labs/ec2-lab-training/terraform.tfstates"
    dynamodb_table = "terraform-lock"
  }
}