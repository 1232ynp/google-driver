locals {
  currentDate = timestamp()
}


module "cloud_scheduler" {
  source = "./modules/cloud_scheduler/"
  topic_name = "${var.env}-${var.name}"
  job_name = "${var.env}-${var.name}"
}

module "cloud_functions" {
  source = "./modules/cloud_functions/"
  region = var.region
  env = var.env
  buket_name = "gcf-deploy-bucket-${var.env}-${var.name}"
  source_file_name = "${local.currentDate}.zip"
  function_name = "${var.env}-${var.name}"
  topic_id = module.cloud_scheduler.topic_id
}