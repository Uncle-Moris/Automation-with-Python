output "repository_url" {
  description = "URL of the ECR repository"
  value       = aws_ecr_repository.react_flask_repo.repository_url
}