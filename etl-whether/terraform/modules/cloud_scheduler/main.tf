# Create Pub/Sub topic
resource "google_pubsub_topic" "topic" {
  name = var.topic_name
}

# Create CloudScheduler
resource "google_cloud_scheduler_job" "job" {
  name        = var.job_name
  schedule    = "* 11 * * *"
  time_zone   = "Asia/Tokyo"

  pubsub_target {
    topic_name = google_pubsub_topic.topic.id
    data       = base64encode("{}")
  }
}