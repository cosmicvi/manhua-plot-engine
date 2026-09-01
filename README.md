# Manhua Plot Engine (MCP Server)

[![Deploy MCP Server on Demand](https://github.com/cosmicvi/manhua-plot-engine/actions/workflows/deploy_mcp.yml/badge.svg)](https://github.com/cosmicvi/manhua-plot-engine/actions/workflows/deploy_mcp.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![MCP](https://img.shields.io/badge/MCP-2.x-green.svg)](https://modelcontextprotocol.io/)

A specialized **Model Context Protocol (MCP)** server and narrative architecture engine designed for web-novels, progression fantasy, and manhua-style narratives (**Cultivation, LitRPG, System, and Isekai**).

It provides AI models (Claude, Gemini, GPT-4, Cursor, Antigravity) with structured tool calling, world-bible continuity checks, strict power-scaling audits, and cinematic scene drafting capabilities.

---

## ⚡ Quick Start

### 1. Host On-Demand via GitHub Actions (Zero Setup / Remote)

You can launch a live, publicly accessible MCP server directly on GitHub Actions without installing anything locally:

1. Navigate to **Actions** $\rightarrow$ **Deploy MCP Server on Demand** in your repository.
2. Click **Run workflow** (select `transport: sse` and `tunnel: cloudflare`).
3. Once running, view the workflow summary for your live public URL:
   ```text
   📡 SSE Endpoint: https://xxxx.trycloudflare.com/sse
   ```
4. Add the endpoint to your MCP client:
   ```json
   {
     "mcpServers": {
       "manhua-plot-engine": {
         "url": "https://xxxx.trycloudflare.com/sse"
       }
     }
   }
   ```

---

### 2. Run Locally via STDIO (Claude Desktop / Cursor / Antigravity)

1. Clone and install dependencies:
   ```bash
   git clone https://github.com/cosmicvi/manhua-plot-engine.git
   cd manhua-plot-engine
   python -m venv .venv
   .\.venv\Scripts\activate   # Windows (or: source .venv/bin/activate on Unix)
   pip install -r requirements.txt
   ```

2. Add to your local MCP client configuration:
   ```json
   {
     "mcpServers": {
       "manhua-plot-engine": {
         "command": "python",
         "args": [
           "path/to/manhua-plot-engine/mcp_server.py",
           "--transport",
           "stdio"
         ]
       }
     }
   }
   ```

---

### 3. Run Locally as an SSE / HTTP Network Service

```bash
# Start Server-Sent Events (SSE) server on port 8080
python mcp_server.py --transport sse --host 0.0.0.0 --port 8080

# Or Streamable HTTP transport
python mcp_server.py --transport streamable-http --host 0.0.0.0 --port 8080
```

---

## 🛠️ MCP Tools & Capabilities

The server exposes 7 specialized tools designed around the core operational guidelines in [`skills/manhua-plot-engine/SKILL.md`](skills/manhua-plot-engine/SKILL.md):

| Tool | Mode | Description |
| :--- | :--- | :--- |
| `synthesize_outline` | **The Architect** | Converts fragmented notes into a 3-tier hierarchy (Macro-Plot, Arc-Plot, Chapter Beats) with escalation hooks. |
| `architect_scene` | **The Architect** | Expands a single plot beat into a 5-stage scene breakdown (Opening Hook, Tension Rise, The Turn, Climax, Cliffhanger). |
| `track_continuity_state` | **The Chronicler** | Audits text against realm ranks, faction statuses, debts/grudges, and flags lore inconsistencies. |
| `audit_power_scaling` | **The Chronicler** | Validates character feats against realm ceilings to prevent unearned power creep and broken battle logic. |
| `review_chapter` | **Developmental Review** | Multi-pass critique checking "The Turn", manhua pacing, show-vs-tell, AI cliché detection, and 3 actionable fixes. |
| `critique_dialogue` | **Dialogue Audit** | Audits spoken dialogue for subtext, swagger, character distinctness, and eliminates clunky exposition. |
| `improvise_scene` | **Analytical Co-Writing**| Provides cinematic framing and scene drafting directives matching the author's voice without generic AI tropes. |

---

## 📚 MCP Resources & Prompts

### Resources
- `resource://manhua-plot-engine/rules`: Full operational guidelines, rules of engagement, and anti-cliché directives.
- `resource://manhua-plot-engine/world-bible-template`: Standardized Markdown template for cultivation realms, economic scale, sects, and grudges.
- `resource://manhua-plot-engine/tropes-guide`: Best practices for executing high-engagement tropes (Hidden Master, Face-Slapping, Auction Arcs, Tribulations).

### Prompts
- `synthesize`: Outline generation prompt.
- `architect`: Granular scene expansion prompt.
- `review`: Comprehensive developmental critique prompt.

---

## 📂 Repository Structure

```text
├── .github/
│   └── workflows/
│       └── deploy_mcp.yml     # On-demand GitHub Actions deployment with Cloudflare tunnel
├── skills/
│   └── manhua-plot-engine/
│       └── SKILL.md           # Core rules, role definitions, and system guidelines
├── mcp_server.py              # Main MCP Server implementation (FastMCP / MCPServer)
├── requirements.txt           # Python dependencies (mcp, starlette, uvicorn, etc.)
├── LICENSE                    # MIT License
└── README.md                  # Documentation and quickstart guide
```

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.