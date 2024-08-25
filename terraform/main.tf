terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region  = "eu-central-1"
}

resource "aws_instance" "app_server" {
  ami           = "ami-00c6ce3be0974ed40"
  instance_type = "t2.micro"
  key_name       = "moris"
  tags = {
    Name = "Simple-Pipline-Instance"
  }
}

resource "aws_ecr_repository" "app_repository" {
  name                 = "simple-pipline-repo"
  image_tag_mutability = "MUTABLE"
  tags = {
    Name = "MyApplicationECRRepository"
  }
}
