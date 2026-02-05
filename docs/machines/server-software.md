# :material-auto-fix: server.home - Software

The system runs on **Ubuntu 24.04 LTS** with support (ESM) until 2034.

## :material-docker: Service Stack
* **Traefik**: Handles domain names and SSL for `*.server.home`.
* **Ollama**: Backbone for local LLMs accessed via Open WebUI and n8n.
* **WordPress**: Multiple test installations including `hofkoh.server.home`.

!!! success ":material-file-certificate: SSL Security"
    Once the root certificate is imported, all subdomains are trusted, and local traffic is fully encrypted.
