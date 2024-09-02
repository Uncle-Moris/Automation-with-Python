variable "aws_region" {
    description = "AWS REgion for resources"
    type = string
    default = "eu-central-1"
}

variable "ecr_repository_name" {
     description = "ECR Repo name"
    type        = string
    default     = "flask-react-simple-app"
}