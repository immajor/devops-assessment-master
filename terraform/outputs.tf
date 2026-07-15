output "namespace_name" {
  description = "The name of the Kubernetes namespace created"
  value       = kubernetes_namespace.homework.metadata[0].name
}

output "helm_release_status" {
  description = "The status of the Helm release"
  value       = helm_release.homework.status
}