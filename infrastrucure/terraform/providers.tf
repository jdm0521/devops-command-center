terraform {
  required_version = ">= 1.5"

  backend "azurerm" {
    resource_group_name  = "devops-command-center"
    storage_account_name = "tfstatedevopscc"
    container_name       = "tfstate"
    key                  = "aks.tfstate"
  }

  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 4.0"
    }
  }
}

provider "azurerm" {
  features {}
}