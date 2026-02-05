# :material-gpu: server.home - Hardware

This machine is a playground for local LLMs, utilizing 3 GPUs to achieve 22 GB of fast VRAM.

## :material-cog-outline: Specifications

| Component | Detail |
| :--- | :--- |
| :material-cpu-64-bit: **CPU** | Intel i3-6100 (2C/4T @ 3.7 GHz Skylake) |
| :material-motherboard: **MB** | EVGA Z170 Classified 4-way |
| :material-memory: **RAM** | 16 GB DDR4 2400 (Reduced early 2026) |
| :material-harddisk: **Storage** | 256GB NVMe + 240GB SATA SSD for Ollama |

## :material-memory: Graphics Cluster

1.  **P104-100 (8GB GDDR5X)**: :material-speedometer: 314 GB/s
2.  **GTX 1070 (8GB GDDR5)**: :material-speedometer: 220 GB/s
3.  **P106-100 (6GB GDDR5)**: :material-speedometer: 176 GB/s

!!! warning "PCIe Lane Bottlenecks"
    The last GPU is connected via PCIe 1.0 x1, limiting transfer speeds to 0.25 GB/s compared to the 16 GB/s of 3.0 x16 slots.
