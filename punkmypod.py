#!/usr/bin/env python3.11

import argparse
import random
import subprocess
import yaml
import os
import logging

def setup_logging():
    logs_dir = "logs"
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)
    logging.basicConfig(filename=os.path.join(logs_dir, "punkmypod.log"), level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

def get_helm_releases():
    try:
        # Get list of Helm releases
        result = subprocess.run(['helm', 'list', '--output', 'json'], capture_output=True, check=True)
        releases = yaml.safe_load(result.stdout)

        return [release['name'] for release in releases]
    except Exception as e:
        logging.error("Error retrieving Helm releases:", exc_info=True)
        return []

def delete_helm_release(release_name):
    try:
        # Delete Helm release
        subprocess.run(['helm', 'uninstall', release_name], check=True)

        logging.info(f"Helm release '{release_name}' deleted successfully")
        return True
    except Exception as e:
        logging.error(f"Error deleting Helm release '{release_name}':", exc_info=True)
        return False

def main():
    setup_logging()

    parser = argparse.ArgumentParser(description="Punk My Pod - Delete a random Helm chart and associated resources")
    args = parser.parse_args()

    # Get list of Helm releases
    releases = get_helm_releases()

    if releases:
        # Select a random Helm release
        release_to_delete = random.choice(releases)

        # Delete the selected Helm release
        if delete_helm_release(release_to_delete):
            # Remove associated resources from Kubernetes cluster
            subprocess.run(['kubectl', 'delete', 'all', '--selector', f"release={release_to_delete}"], check=True)
    else:
        logging.info("No active Helm releases found")

if __name__ == "__main__":
    main()
