resource "aws_ecr_repository" "react-flask-repo" {
    name = var.ecr_repository_name
    image_tag_mutability = "MUTABLE"
    image_scanning_configuration {
      scan_on_push = true
  }    
}