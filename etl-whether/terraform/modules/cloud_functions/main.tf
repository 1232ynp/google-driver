## Start CloudFunctions
# Archive src
data "archive_file" "src_archive" {
  type        = "zip"
  source_dir  = "../src"
  output_path = "../src.zip"
}

# Create deploy bucket
resource "google_storage_bucket" "bucket" {
  name          = var.buket_name
  location      = var.region
}

# Store archive src
resource "google_storage_bucket_object" "object" {
  name   = var.source_file_name
  bucket = google_storage_bucket.bucket.name
  source = "../src.zip"
}

# Create CloudFunctions
resource "google_cloudfunctions2_function" "function" {
  name        = var.function_name
  location    = var.region
  description = "a new function"

  build_config {
    runtime     = "python310"
    entry_point = "main"
    source {
      storage_source {
        bucket = google_storage_bucket.bucket.name
        object = google_storage_bucket_object.object.name
      }
    }
  }

  service_config {
    max_instance_count = 1
    available_memory   = "256M"
    timeout_seconds    = 60
  }

    event_trigger {
    trigger_region = var.region
    event_type = "google.cloud.pubsub.topic.v1.messagePublished"
    pubsub_topic = var.topic_id
  }
}
