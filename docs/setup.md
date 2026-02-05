# :material-hammer-wrench: Setup Guide

This guide covers the core operations for managing the containerized services across the homelab.

## :material-folder-network: Project Structure
Organize your services by creating a dedicated subfolder for each container within a central directory:
* **Directory**: `~/docker/`
* **Example**: `~/docker/wordpress/docker-compose.yml`

## :material-docker: Docker Workflow
Use these standard commands to manage your service stacks:

| Action | Command |
| :--- | :--- |
| **Start Services** | `docker compose up -d` |
| **Stop Services** | `docker compose down` |
| **Restart a Container** | `docker restart <container_name>` |
| **Interactive Shell** | `docker exec -it <container_name> bash` |
| **Run LLM Model** | `docker exec -it ollama ollama run mistral --verbose` |

## :material-lan-connect: Networking
Before starting your containers, ensure the shared internal network is created so services can communicate:

```sh
# Create the network
docker network create my_network

# List existing networks
docker network ls
