# Terraform configuration for Google cloud

provider "google" {
    project = "zoomcamp-project-455614"
    region = "US"
}

resource "google_bigquery_dataset" "NYC_trips_dataset" {
    dataset_id = "NYC_trips_dataset"
}