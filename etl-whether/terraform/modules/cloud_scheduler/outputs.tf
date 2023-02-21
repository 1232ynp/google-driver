# Use cloud_functions module
output "topic_id" {
  value = google_pubsub_topic.topic.id
}