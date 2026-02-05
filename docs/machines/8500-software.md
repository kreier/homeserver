# :material-order-bool-descending-variant: 8500.home - Software



| Level | Layer | Component | Function |
| :--- | :--- | :--- | :--- |
| **0** | **Physical** | :material-desktop-tower-monitor: HP EliteDesk 800 G4 | The "Bare Metal" hardware. |
| **1** | **Hypervisor** | :material-infinity: Proxmox VE | Type-1 Hypervisor. |
| **2** | **Virtual OS** | :material-linux: Ubuntu 24.04.3 LTS | The Guest VM. |
| **3** | **Container** | :material-docker: Docker & Compose | App isolation. |
| **4** | **Routing** | :material-traffic-light: Traefik | SSL and traffic handling. |
| **5** | **App** | :material-home-assistant: Home Assistant, Ollama | End-user services. |

!!! tip "GPU Passthrough"
    The UHD 630 GPU is passed through from Proxmox to Docker so Ollama can use it.
