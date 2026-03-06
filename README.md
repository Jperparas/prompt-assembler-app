# Prompt Designer

A web app that generates LLM prompts using the PARTS framework (Persona, Aim, Recipients, Theme, Structure).

🔗 [prompt.jeffdomain.com](https://prompt.jeffdomain.com)

## Tech Stack

| Technology | Purpose |
|---|---|
| **Streamlit** | Python framework that turns the script into a web app |
| **Groq API** | LLM inference service running Llama 3.3 70B for prompt generation |
| **EC2** | AWS virtual server hosting the app (free tier) |
| **Amazon Linux 2023** | Operating system on the EC2 instance |
| **Caddy** | Reverse proxy handling HTTPS and routing traffic to Streamlit |
| **Let's Encrypt** | Free SSL certificate authority (managed automatically by Caddy) |
| **Route 53** | AWS DNS service pointing the custom domain to the server |
| **Elastic IP** | Static IP address so the server's address never changes |
| **systemd** | Linux service manager that keeps Streamlit running and restarts on crashes |
