variable "aws_region" {
  description = "The AWS region to deploy resources in"
  type        = string
  default     = "us-east-1"
}

variable "cluster_name" {
  description = "The name of the EKS cluster"
  type        = string
  default     = "ai-travel-planner-cluster"
}

variable "node_group_name" {
  description = "Name for the EKS node group"
  type        = string
  default     = "ai-travel-planner-nodes"
}

variable "instance_types" {
  description = "Instance types for the EKS node group"
  type        = list(string)
  default     = ["t3.medium"]
}
