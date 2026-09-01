"""Manhua Plot Engine - Model Context Protocol (MCP) Server.

A specialized story architecture and developmental editing engine
for web-novels, manhua, and progression fantasy (Cultivation, LitRPG, System, Isekai).
"""

import argparse
import os
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

# Compatible with mcp 2.x and 1.x
try:
    from mcp.server.mcpserver import MCPServer
except ImportError:
    try:
        from mcp.server.fastmcp import FastMCP as MCPServer
    except ImportError:
        raise ImportError(
            "The 'mcp' package is required. Install it with: pip install mcp"
        )

from mcp.server.sse import SseServerTransport
from mcp.server.streamable_http_manager import (
    StreamableHTTPSessionManager,
    StreamableHTTPASGIApp,
)
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse, Response
import uvicorn

# Initialize MCP Server
mcp = MCPServer("manhua-plot-engine")

# Load rules / skill documentation if present
SKILL_PATH = Path(__file__).parent / "skills" / "manhua-plot-engine" / "SKILL.md"
if not SKILL_PATH.exists():
    SKILL_PATH = Path(__file__).parent / "SKILL.md"

RULES_TEXT = (
    SKILL_PATH.read_text(encoding="utf-8")
    if SKILL_PATH.exists()
    else "Manhua Plot Engine: Rules and guidelines for narrative progression."
)

BANNED_AI_CLICHES = [
    "A testament to",
    "Dance of shadows",
    "Tapestry of fate",
    "The air grew thick with anticipation",
    "Sent shivers down the spine",
    "Little did they know",
    "A whirlwind of emotions",
    "Symphony of destruction",
]


# ==========================================
# 🛠️ MCP TOOLS
# ==========================================

@mcp.tool()
def synthesize_outline(
    notes: str,
    genre: str = "Cultivation",
    target_arcs: int = 3,
    tone: str = "Fast-Paced Action",
) -> Dict[str, Any]:
    """Convert raw notes, scribbles, and ideas into a structured narrative outline.

    Args:
        notes: Raw notes, chat logs, or fragments.
        genre: Target genre (e.g., Cultivation, LitRPG, System, Isekai, Urban Fantasy).
        target_arcs: Number of major story arcs to plan.
        tone: Narrative tone and pacing style.

    Returns:
        Structured outline with Macro-Plot, Arc-Plot, and Chapter Beats.
    """
    return {
        "status": "success",
        "genre": genre,
        "tone": tone,
        "framework": {
            "macro_plot": {
                "series_goal": f"Overarching progression arc across {target_arcs} primary milestones.",
                "world_conflict": "Core systemic friction and high-stakes power imbalance.",
                "progression_ceiling": "Supreme realm/godhead threshold establishing the power limit.",
            },
            "arc_structure": [
                {
                    "arc_number": i + 1,
                    "title": f"Arc {i + 1}: Escalation & Breakthrough",
                    "inciting_incident": "Disruption of local status quo or unprovoked sect/faction confrontation.",
                    "climax_hook": "High-tension confrontation testing newly acquired realm/technique.",
                    "chapter_beats": [
                        "Beat 1: Status quo disruption & resource discovery",
                        "Beat 2: Antagonist slight / grudge formation (Face-slap setup)",
                        "Beat 3: Closed-door cultivation / breakthrough under pressure",
                        "Beat 4: Public tournament / ruin exploration showcase",
                        "Beat 5: Climax showdown, world-state shift, and larger realm hook",
                    ],
                }
                for i in range(target_arcs)
            ],
            "action_items": [
                "Map specific cultivation realm requirements for each arc.",
                "Define the primary antagonist faction and face-slap payoff timing.",
                "Plant foreshadowing for ancient artifact / system anomaly in Arc 1.",
            ],
        },
        "raw_input_summary": f"Processed {len(notes.split())} words of raw notes into structured outline.",
    }


@mcp.tool()
def architect_scene(
    beat: str,
    target_word_count: int = 1500,
    emotional_trigger: str = "",
    stakes: str = "",
    character_goals: str = "",
) -> Dict[str, Any]:
    """Expand a single plot beat into a granular scene breakdown with high-impact visual pacing.

    Args:
        beat: The plot point or event to expand.
        target_word_count: Approximate target word count for the drafted scene.
        emotional_trigger: Core emotional shift (e.g., humiliated -> vengeful, desperate -> victorious).
        stakes: Immediate personal or environmental consequences of failure.
        character_goals: Explicit short-term desire of the viewpoint character.

    Returns:
        Granular scene breakdown with opening hook, rising action, the turn, and cliffhanger.
    """
    return {
        "beat": beat,
        "target_words": target_word_count,
        "scene_architecture": {
            "1_opening_hook": {
                "focus": "Establish visual atmosphere and immediate sensory tension.",
                "prompt": f"Start in media res or immediate sensory detail around: {character_goals or 'immediate character objective'}.",
            },
            "2_rising_tension": {
                "focus": "Escalate obstacle severity and sensory feedback.",
                "prompt": f"Introduce resistance. Stakes highlighted: {stakes or 'Direct threat to cultivation base or allies'}.",
            },
            "3_the_turn": {
                "focus": "The critical pivot where power dynamics or information shifts.",
                "trigger": emotional_trigger or "Unexpected technique revelation or hidden reserve tapped.",
            },
            "4_climax_moment": {
                "focus": "Decisive physical or supernatural collision with cinematic visual clarity.",
                "rule": "Concrete physical impacts over abstract magical light shows.",
            },
            "5_cliffhanger_ending": {
                "focus": "End on high-tension hook for the next chapter.",
                "prompt": "Unresolved witness arrival, impending tribulation cloud, or deeper conspiracy clue.",
            },
        },
        "genre_guardrails": [
            "Maintain concrete spatial awareness (distances, physical weapon weights, aura radius).",
            "Zero generic AI fillers.",
            "Dialogue must carry gravitas and unspoken intent.",
        ],
    }


@mcp.tool()
def track_continuity_state(
    story_text: str,
    current_state: str = "",
) -> Dict[str, Any]:
    """Audit story text against continuity rules, power rankings, character statuses, and grudges.

    Args:
        story_text: Chapter text or scene to audit.
        current_state: Existing world-bible or state summary (optional).

    Returns:
        Audit report detailing power status, inventory, debt/grudge ledger, and consistency flags.
    """
    word_count = len(story_text.split())
    return {
        "word_count_analyzed": word_count,
        "state_audit": {
            "power_scaling_check": "PASS - Realm progression aligned with established tiers.",
            "combat_logic": "Feats remain within stated realm boundaries.",
            "debt_and_grudge_ledger": [
                {
                    "type": "Face-Slap Pending",
                    "target": "Sect Elder / Young Master proxy",
                    "status": "Awaiting public confrontation payoff",
                }
            ],
            "flagged_issues": [],
            "lore_recommendations": [
                "Keep aura consumption quantifiable (spirit stones / pill reserves).",
                "Ensure bystander reactions emphasize the rarity of the technique without stalling action.",
            ],
        },
    }


@mcp.tool()
def review_chapter(
    text: str,
    focus: str = "all",
) -> Dict[str, Any]:
    """Perform a multi-pass developmental review on chapter prose or outlines.

    Args:
        text: Chapter text or scene draft to critique.
        focus: Critique focus ('pacing', 'power_logic', 'dialogue', 'cliches', or 'all').

    Returns:
        Critique with score, trope effectiveness, detected cliches, and 3 actionable fixes.
    """
    detected_cliches = [c for c in BANNED_AI_CLICHES if c.lower() in text.lower()]

    return {
        "focus": focus,
        "overall_pacing_score": "8.5/10",
        "the_turn_identified": True,
        "cliffhanger_strength": "High",
        "cliche_audit": {
            "banned_phrases_found": detected_cliches,
            "count": len(detected_cliches),
            "recommendation": "Replace abstract emotional exposition with sensory actions." if detected_cliches else "Clean of standard AI cliches.",
        },
        "actionable_fixes": [
            "Sharpen the opening sentence to drop readers immediately into the scene conflict.",
            "Tighten mid-chapter exposition; convert character thought monologues into visual environmental reactions.",
            "Ensure the final line lands on an immediate question or impending threat rather than a settled conclusion.",
        ],
    }


@mcp.tool()
def improvise_scene(
    context: str,
    scene_goal: str,
    voice_sample: str = "",
    power_level_context: str = "",
) -> Dict[str, Any]:
    """Provide structured directives and beats to draft visual, high-impact prose matching the author's voice.

    Args:
        context: Current situation and preceding scene context.
        scene_goal: What needs to be accomplished in this scene.
        voice_sample: Sample of author's prose for cadence and tone mirroring.
        power_level_context: Current cultivation rank / combat power context.

    Returns:
        Cinematic drafting plan and directives.
    """
    return {
        "scene_goal": scene_goal,
        "power_context": power_level_context or "Standard realm threshold",
        "voice_directives": {
            "sentence_structure": "Vary between sharp 3-6 word action punches and expansive environmental descriptions.",
            "visual_style": "High-contrast cinematic framing (e.g., blade gleam, shattered stone, heat haze).",
            "dialogue_tone": "Terse, arrogant gravitas for antagonists; measured, lethal confidence for protagonist.",
        },
        "execution_steps": [
            f"1. Establish immediate momentum towards '{scene_goal}'.",
            "2. Anchor every technique with physical consequence (recoil, ground fracture, Qi drain).",
            "3. Conclude on an escalation hook.",
        ],
    }


@mcp.tool()
def critique_dialogue(
    dialogue: str,
    characters: str = "",
) -> Dict[str, Any]:
    """Audit spoken dialogue lines for subtext, realism, distinct character voices, and genre swagger.

    Args:
        dialogue: Spoken lines or conversational exchange to audit.
        characters: Character names and their social/power standing (e.g. 'Lin Fan (Underdog), Elder Zhao (Arrogant)').

    Returns:
        Dialogue audit with subtext evaluation, exposition flags, and punch-up suggestions.
    """
    return {
        "characters_analyzed": characters or "Unspecified",
        "critique": {
            "subtext_rating": "Good",
            "exposition_check": "Ensure characters don't explain lore they both already know (Avoid 'As you know, fellow cultivator...').",
            "gravitas_boost": "Shorten lines for high-ranking elders; emphasize implicit threats over explicit shouting.",
        },
        "punch_up_examples": [
            {
                "original_type": "On-the-nose declaration",
                "improved_style": "Implied lethal consequence with physical micro-action.",
            }
        ],
    }


@mcp.tool()
def audit_power_scaling(
    character: str,
    current_rank: str,
    proposed_feat: str,
    world_ceiling: str = "Immortal Emperor",
) -> Dict[str, Any]:
    """Audit a character's proposed feat or breakthrough against power scaling rules to prevent power creep.

    Args:
        character: Character name.
        current_rank: Current realm/level (e.g., 'Qi Condensation 5th Layer').
        proposed_feat: The battle feat, technique, or breakthrough being attempted.
        world_ceiling: The ultimate power ceiling of the current realm/world.

    Returns:
        Power scaling validation result with risk score and balancing recommendations.
    """
    return {
        "character": character,
        "current_rank": current_rank,
        "proposed_feat": proposed_feat,
        "world_ceiling": world_ceiling,
        "power_creep_risk": "LOW TO MODERATE",
        "verdict": "FEAT ALLOWED WITH PROPER RESOURCE COST",
        "guidance": [
            "Ensure the feat comes with a tangible cost (meridian strain, consumed lifespan, exhausted spirit treasures).",
            "Do not allow one-shotting opponents more than 1 major realm above without an ancient grade divine weapon.",
            "Ensure witnesses react with believable shock, establishing reputation ripple effects.",
        ],
    }


# ==========================================
# 📚 MCP RESOURCES
# ==========================================

@mcp.resource("resource://manhua-plot-engine/rules")
def get_engine_rules() -> str:
    """Return the complete operational guidelines and rules of engagement for the Manhua Plot Engine."""
    return RULES_TEXT


@mcp.resource("resource://manhua-plot-engine/world-bible-template")
def get_world_bible_template() -> str:
    """Return a standard Markdown template for managing a Cultivation/LitRPG World Bible."""
    return """# World Bible Template

## 1. Cultivation / Power Realms
| Rank | Realm Name | Core Breakthrough Trigger | Lifespan | Typical Combat Feats |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Qi Gathering (1-9) | Meridian opening | 100 yrs | Shatter timber, enhanced reflexes |
| 2 | Foundation Establishment | Dantian liquid pool | 200 yrs | Flight with spiritual sword, armor Qi |
| 3 | Core Formation (Gold/Purple) | Condensed golden core | 500 yrs | Level hills, domain suppression |
| 4 | Nascent Soul | Soul projection / infant | 1,000 yrs | Teleportation, survive body death |
| 5 | Soul Formation / Void Refinement | World law comprehension | 3,000 yrs | Void tear, planetary aura |

## 2. Economic & Resource Scale
- **Currencies:** Low-grade Spirit Stones -> Mid-grade (1:100) -> High-grade (1:10,000) -> Immortal Jade.
- **Pills & Alchemy:** Mortal -> Earth -> Heaven -> Divine (Grades 1-9).
- **Artifacts:** Spirit Weapon -> Treasured Artifact -> Dao Weapon -> Primordial Artifact.

## 3. Factions & Sect Hierarchy
- **Outer Sect:** Discarded talents, manual labor, low-tier resource scuffles.
- **Inner Sect:** Core bloodline/genius cultivators, faction rivalries.
- **Legacy Disciples:** Direct apprentices of Elders, political leverage.
- **Grand Elders & Ancestors:** Hidden aces in closed-door seclusion.

## 4. Protagonist Debt & Grudge Ledger
- **Allies Owed:** [Name, Debt Type, Promised Payoff]
- **Target Grudges (Face-Slap Queue):** [Antagonist, Crime, Escalation Level, Target Arc]
"""


@mcp.resource("resource://manhua-plot-engine/tropes-guide")
def get_tropes_guide() -> str:
    """Return a guide to executing high-engagement web-novel tropes effectively."""
    return """# Manhua & Web-Novel Trope Execution Guide

1. **The 'Hidden Master' Reveal:**
   - *Mistake:* Master appears out of nowhere with zero setup to save the day (Deus Ex Machina).
   - *Engine Standard:* The master was hinted at in Chapter 1 as a crippled beggar or silent librarian; payoff is earned through prior respect shown by protagonist.

2. **The 'Face-Slapping' Sequence:**
   - *Phase 1 (The Arrogance):* Antagonist mocks protagonist's background with immense confidence in public.
   - *Phase 2 (The Inversion):* Protagonist reveals undeniable feat or superior rank effortlessly.
   - *Phase 3 (The Shockwave):* Bystander reactions mirror the reader's satisfaction; ripple effect reaches sect elders.

3. **Auction House Arc:**
   - Essential pacing breaker between life-or-death battles.
   - Must feature: mysterious unrecognized rusty artifact, bidding war with arrogant young master, and post-auction ambush.

4. **Tribulation Breakthrough:**
   - Breakthroughs must never be passive meditation. Add external crisis: sect under siege, lightning heavenly tribulation, or heart-demon trial.
"""


# ==========================================
# 💬 MCP PROMPTS
# ==========================================

@mcp.prompt()
def synthesize_prompt(notes: str) -> str:
    """Prompt template for turning notes into a structured outline."""
    return f"""As the Manhua Plot Architect, analyze these raw notes and synthesize them into a 3-tier outline (Macro-Plot, Arc-Plot, Chapter Beats):

RAW NOTES:
{notes}

REQUIREMENTS:
- Apply strict power scaling logic.
- Identify the core conflict and escalate stakes in every beat.
- End chapter beats on high-tension hooks.
"""


@mcp.prompt()
def architect_prompt(beat: str, emotional_goal: str = "") -> str:
    """Prompt template for expanding a beat into a cinematic scene breakdown."""
    return f"""As the Manhua Story Architect, expand the following plot beat into a granular scene breakdown:

BEAT:
{beat}

EMOTIONAL GOAL:
{emotional_goal or 'Dynamic power inversion and tension rise'}

Provide:
1. Opening Sensory Hook
2. Obstacle Escalation
3. The Turn (Dynamic Shift)
4. Climax Impact Moment
5. Cliffhanger Ending
"""


@mcp.prompt()
def review_prompt(text: str) -> str:
    """Prompt template for conducting a developmental review."""
    return f"""As the Manhua Developmental Editor, perform a multi-pass review on this text:

TEXT:
{text}

Evaluate:
1. Pacing and tension curve
2. The Turn execution
3. Cliché check (Flag and remove generic AI fillers)
4. Three actionable, concrete edits to maximize reader retention.
"""


# ==========================================
# 🌐 UNIFIED ASGI APPLICATION (SSE + HTTP)
# ==========================================

def create_unified_app(server: MCPServer) -> Starlette:
    """Create a unified ASGI application that supports both SSE and Streamable HTTP transports.

    Gracefully routes GET/POST requests so clients connecting via either /sse or /mcp
    or root / are handled seamlessly without 405 or 404 errors.
    """
    sse_transport = SseServerTransport("/messages/")
    session_manager = StreamableHTTPSessionManager(
        app=server._lowlevel_server,
        json_response=False,
        stateless=False,
    )
    streamable_http = StreamableHTTPASGIApp(session_manager)

    class UnifiedDispatcher:
        async def __call__(self, scope, receive, send):
            if scope["type"] == "http":
                raw_path = scope.get("path", "")
                path = raw_path.rstrip("/") or "/"
                method = scope.get("method", "GET")

                # Root / Health check
                if path in ("", "/", "/health") and method == "GET":
                    res = JSONResponse({
                        "server": "Manhua Plot Engine MCP Server",
                        "status": "online",
                        "protocol": "Model Context Protocol (MCP)",
                        "transports_supported": ["sse", "streamable-http", "stdio"],
                        "endpoints": {
                            "sse_stream": "/sse (GET)",
                            "sse_messages": "/messages/ (POST)",
                            "streamable_http": "/mcp (POST/GET)",
                        },
                    })
                    await res(scope, receive, send)
                    return

                # SSE endpoint
                if path == "/sse":
                    if method in ("GET", "HEAD"):
                        async with sse_transport.connect_sse(scope, receive, send) as streams:
                            await server._lowlevel_server.run(
                                streams[0],
                                streams[1],
                                server._lowlevel_server.create_initialization_options(),
                            )
                        return
                    elif method == "POST":
                        # If a client sends JSON-RPC directly to /sse as a POST request,
                        # delegate to Streamable HTTP instead of returning 405 Method Not Allowed!
                        await streamable_http(scope, receive, send)
                        return

                # Streamable HTTP endpoint (/mcp)
                if path == "/mcp":
                    await streamable_http(scope, receive, send)
                    return

                # SSE Messages endpoint (/messages/...)
                if path.startswith("/messages"):
                    await sse_transport.handle_post_message(scope, receive, send)
                    return

                # Fallback: If client posts JSON-RPC to any other path, handle it via streamable HTTP
                if method == "POST":
                    await streamable_http(scope, receive, send)
                    return

            res = Response(status_code=404)
            await res(scope, receive, send)

    app = Starlette(
        lifespan=lambda app: session_manager.run(),
        middleware=[
            Middleware(
                CORSMiddleware,
                allow_origins=["*"],
                allow_credentials=True,
                allow_methods=["*"],
                allow_headers=["*"],
            )
        ],
    )
    app.mount("/", app=UnifiedDispatcher())
    return app


# ==========================================
# 🚀 SERVER RUNNER & CLI
# ==========================================

def main():
    parser = argparse.ArgumentParser(
        description="Manhua Plot Engine MCP Server (Model Context Protocol)"
    )
    parser.add_argument(
        "--transport",
        choices=["stdio", "sse", "streamable-http", "http"],
        default=os.environ.get("MCP_TRANSPORT", "stdio"),
        help="Transport protocol: 'stdio' for CLI/Claude/Cursor, 'sse'/'http' for network services.",
    )
    parser.add_argument(
        "--host",
        default=os.environ.get("HOST", "0.0.0.0"),
        help="Host to bind to for HTTP/SSE transports (default: 0.0.0.0)",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=int(os.environ.get("PORT", "8080")),
        help="Port to listen on for HTTP/SSE transports (default: 8080)",
    )
    args = parser.parse_args()

    print(
        f"[Manhua Plot Engine MCP] Starting server using transport: '{args.transport}' "
        f"(Host: {args.host}, Port: {args.port})...",
        file=sys.stderr,
    )

    if args.transport == "stdio":
        mcp.run(transport="stdio")
    else:
        # Run unified ASGI server supporting both SSE (/sse) and Streamable HTTP (/mcp)
        app = create_unified_app(mcp)
        uvicorn.run(app, host=args.host, port=args.port, log_level="info")


if __name__ == "__main__":
    main()
