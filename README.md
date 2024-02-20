
# Punk My Pod

Punk My Pod is a powerful chaos engineering tool designed to introduce controlled disruptions into Kubernetes clusters. Developed for DevOps and SRE teams, Punk My Pod adds an element of unpredictability to Kubernetes environments, allowing users to test the resilience and fault tolerance of their applications and infrastructure.

### Features:

- **Random Helm Chart Deletion**: Punk My Pod randomly selects a Helm chart from actively running releases and deletes it, triggering the removal of all associated resources from the Kubernetes cluster.
  
- **Chaos Engineering**: With Punk My Pod, users can simulate real-world failures and incidents in their Kubernetes environments, helping them identify weaknesses and improve system reliability.

- **Debug Logging**: Punk My Pod logs all actions and errors to provide visibility into the chaos engineering process. Debug logging ensures that users can analyze and troubleshoot any issues that arise during testing.

### Installation:

To install Punk My Pod, follow these steps:

1. **Ensure Dependencies**: Make sure you have Helm and `kubectl` installed and configured properly on your system.

2. **Download Script**: Download the Punk My Pod script from the repository.

3. **Make Executable**: Make the script executable using the following command:

    ```bash
    chmod +x punkmypod.py
    ```

4. **Run Punk My Pod**: Run Punk My Pod script to initiate chaos engineering in your Kubernetes cluster.

### Usage:

The Punk My Pod script accepts the following command-line options:

```bash
#!/usr/bin/env python3.11

usage: punkmypod.py [-h]

Punk My Pod - Delete a random Helm chart and associated resources

optional arguments:
  -h, --help  show this help message and exit
```

Simply run the script without any arguments to initiate chaos engineering in your Kubernetes cluster.

---

Punk My Pod is a valuable tool for organizations looking to build more resilient and fault-tolerant Kubernetes deployments. By embracing chaos engineering principles, teams can proactively identify and address vulnerabilities, ultimately leading to more robust and reliable systems.