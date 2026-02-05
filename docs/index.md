# :material-home-automation: Welcome to the Kreier Homelab

![GitHub License](https://img.shields.io/github/license/kreier/homeserver)
![GitHub Release](https://img.shields.io/github/v/release/kreier/homeserver)

Documentation on my journey to a small but capable homelab. The setup currently consists of 

- :material-router: 2 routers,
- :material-switch: 1 managed switch,
- :material-server: 3 always-on servers, and
- :material-brain: one LLM server activated on demand.

!!! info "Current Status"
    The lab features a combined 22 GB of GDDR5/X VRAM for local LLM inference and a dedicated Proxmox node for high-availability services.

## :material-layers-outline: Infrastructure at a Glance

* **[:material-server-network: server.home](./machines/server-hardware.md)**: The LLM playground with triple NVIDIA GPUs.
* **[:material-microchip: 8500.home](./machines/8500-hardware.md)**: The energy-efficient HP EliteDesk mini (4W idle).
* **[:material-raspberry-pi: pi4.home](./machines/pi4.md)**: Network backbone for Home Assistant and DNS.
* **[:material-lan: pi3.home](./machines/pi3.md)**: Secondary network management.
