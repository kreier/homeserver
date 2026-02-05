# :material-memory: server.home - Hardware :material-server:

This machine is a playground for local LLMs, utilizing 3 GPUs to achieve 22 GB of fast VRAM.

## :material-view-quilt: Physical Build

![Server Front](../assets/2025-01_server.jpg){ width="59.2%" } ![Server Internal](../assets/2025-01_server_display.jpg){ width="39.3%" }
*Left: The server enclosure. Right: Internal display showing system stats.*

<div class="grid cards" markdown>

-   ![Server Front](../assets/2025-01_server.jpg){ title="Server Enclosure Exterior" }
-   ![Server Internal](../assets/2025-01_server_display.jpg){ title="System Status Display" }

</div>

*Click any image to expand. You can use arrow keys to navigate the gallery.*

*Click any image above to expand it.*

## :material-cog-outline: Specifications

| Component | Detail |
| :--- | :--- |
| :material-cpu-64-bit: **CPU** | Intel i3-6100 (2C/4T @ 3.7 GHz Skylake) |
| :material-motherboard: **MB** | EVGA Z170 Classified 4-way |
| :material-memory: **RAM** | 16 GB DDR4 2400 (Reduced early 2026) |
| :material-harddisk: **Storage** | 256GB NVMe + 240GB SATA SSD for Ollama |

![EVGA Z170](../assets/2026-02-02z170classified.jpg)
*The EVGA Z170 Classified motherboard supporting 4-way GPU configurations.*


## :material-history: Historic Graphics Cluster (Early 2025)

Before the current optimization, the system ran a 4-GPU cluster to maximize VRAM availability.

| GPU Model | VRAM | Connection | Bandwidth |
| :--- | :--- | :--- | :--- |
| **RTX 3060 Ti** | 8 GB GDDR6 | PCIe 3.0 x16 | 448 GB/s |
| **P106-100** | 6 GB GDDR5 | PCIe 3.0 x8 | 192 GB/s |
| **P106-100** | 6 GB GDDR5 | PCIe 3.0 x4 | 192 GB/s |
| **GTX 1060** | 6 GB GDDR5 | **PCIe 1.0 x1** | 192 GB/s |

!!! warning "The PCIe 1.0 x1 Bottleneck"
    The fourth card (GTX 1060) was connected via a PCIe 1.0 x1 slot. While this provided an additional 6 GB of VRAM allowing larger models to load, the extremely narrow bus (0.25 GB/s) created significant latency when the model's KV Cache or weights needed to transit that specific card.

## :material-memory: Current Graphics Cluster (2026)

The current setup focuses on balancing thermal overhead and consistent VRAM speeds:

1.  **P104-100 (8GB GDDR5X)**: :material-speedometer: 314 GB/s
2.  **GTX 1070 (8GB GDDR5)**: :material-speedometer: 220 GB/s
3.  **P106-100 (6GB GDDR5)**: :material-speedometer: 176 GB/s

This rocks! All 47 layers in the GPUs, each with 1 GB space for local K-V values.

![nvtop output](../assets/2026-01-27nvtop.jpeg)