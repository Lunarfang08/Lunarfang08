<!-- SPIDER-MAN THEMED README — ARSAL ADNAN -->

<div align="center">

<svg width="900" height="160" viewBox="0 0 900 160" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      .web-line { stroke: #cc0000; stroke-width: 0.8; opacity: 0.4; fill: none; }
      .web-line-bright { stroke: #ff2222; stroke-width: 1.2; opacity: 0.7; fill: none; }
      @keyframes swing {
        0%   { transform: translateX(-120px) translateY(0px) rotate(-15deg); }
        25%  { transform: translateX(200px) translateY(40px) rotate(5deg); }
        50%  { transform: translateX(500px) translateY(10px) rotate(-10deg); }
        75%  { transform: translateX(780px) translateY(35px) rotate(8deg); }
        100% { transform: translateX(980px) translateY(0px) rotate(-5deg); }
      }
      @keyframes webDraw {
        0%   { stroke-dashoffset: 600; opacity: 0; }
        30%  { opacity: 0.7; }
        100% { stroke-dashoffset: 0; opacity: 0.3; }
      }
      @keyframes pulse {
        0%, 100% { opacity: 0.2; }
        50% { opacity: 0.8; }
      }
      @keyframes flicker {
        0%,100%{opacity:1}45%{opacity:1}50%{opacity:0.4}55%{opacity:1}90%{opacity:1}92%{opacity:0.6}94%{opacity:1}
      }
      .spidey { animation: swing 4s ease-in-out infinite alternate; }
      .web-strand { stroke-dasharray: 600; animation: webDraw 3s ease-out infinite; }
      .pulse-web { animation: pulse 2s ease-in-out infinite; }
      .title-text { font-family: 'Courier New', monospace; font-weight: 900; fill: #cc0000; font-size: 42px; letter-spacing: 6px; animation: flicker 5s infinite; }
      .sub-text { font-family: 'Courier New', monospace; fill: #ff4444; font-size: 13px; letter-spacing: 8px; }
    </style>
    <filter id="redglow">
      <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
      <feMerge><feMergeNode in="coloredBlur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="webglow">
      <feGaussianBlur stdDeviation="1.5" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <rect width="900" height="160" fill="#050505"/>
  <g class="pulse-web" filter="url(#webglow)">
    <line class="web-line" x1="0" y1="0" x2="120" y2="80"/>
    <line class="web-line" x1="0" y1="0" x2="80" y2="100"/>
    <line class="web-line" x1="0" y1="0" x2="150" y2="50"/>
    <line class="web-line" x1="0" y1="0" x2="60" y2="120"/>
    <path class="web-line" d="M 20,0 Q 60,30 40,60"/>
    <path class="web-line" d="M 40,0 Q 80,40 70,80"/>
    <path class="web-line" d="M 70,0 Q 95,35 95,70"/>
    <path class="web-line" d="M 0,20 Q 40,45 60,40"/>
    <path class="web-line" d="M 0,50 Q 55,65 90,60"/>
    <path class="web-line" d="M 0,80 Q 60,88 100,80"/>
  </g>
  <g class="pulse-web" filter="url(#webglow)" style="animation-delay:1s">
    <line class="web-line" x1="900" y1="0" x2="780" y2="80"/>
    <line class="web-line" x1="900" y1="0" x2="820" y2="100"/>
    <line class="web-line" x1="900" y1="0" x2="750" y2="50"/>
    <line class="web-line" x1="900" y1="0" x2="840" y2="120"/>
    <path class="web-line" d="M 880,0 Q 840,30 860,60"/>
    <path class="web-line" d="M 860,0 Q 820,40 830,80"/>
    <path class="web-line" d="M 830,0 Q 805,35 805,70"/>
    <path class="web-line" d="M 900,20 Q 860,45 840,40"/>
    <path class="web-line" d="M 900,50 Q 845,65 810,60"/>
    <path class="web-line" d="M 900,80 Q 840,88 800,80"/>
  </g>
  <path class="web-line-bright web-strand" d="M 80,0 Q 300,60 500,20 Q 700,60 900,10" filter="url(#webglow)" style="animation-delay:0.5s"/>
  <path class="web-line-bright web-strand" d="M 0,30 Q 250,90 500,50 Q 750,90 900,40" filter="url(#webglow)" style="animation-delay:1s; opacity:0.4;"/>
  <g class="spidey" style="transform-origin: 50px 20px;">
    <line x1="50" y1="20" x2="50" y2="-30" stroke="#cc0000" stroke-width="1" opacity="0.8"/>
    <ellipse cx="50" cy="35" rx="12" ry="16" fill="#cc0000"/>
    <ellipse cx="50" cy="17" rx="10" ry="11" fill="#cc0000"/>
    <ellipse cx="46" cy="15" rx="4" ry="5" fill="white" opacity="0.9"/>
    <ellipse cx="54" cy="15" rx="4" ry="5" fill="white" opacity="0.9"/>
    <ellipse cx="46" cy="15" rx="4" ry="5" fill="none" stroke="#1a0000" stroke-width="1"/>
    <ellipse cx="54" cy="15" rx="4" ry="5" fill="none" stroke="#1a0000" stroke-width="1"/>
    <line x1="50" y1="22" x2="50" y2="50" stroke="#1a0000" stroke-width="0.8"/>
    <line x1="38" y1="28" x2="62" y2="28" stroke="#1a0000" stroke-width="0.6"/>
    <line x1="39" y1="36" x2="61" y2="36" stroke="#1a0000" stroke-width="0.6"/>
    <line x1="41" y1="44" x2="59" y2="44" stroke="#1a0000" stroke-width="0.6"/>
    <line x1="38" y1="28" x2="22" y2="18" stroke="#cc0000" stroke-width="5" stroke-linecap="round"/>
    <line x1="62" y1="28" x2="78" y2="18" stroke="#cc0000" stroke-width="5" stroke-linecap="round"/>
    <line x1="44" y1="50" x2="34" y2="66" stroke="#cc0000" stroke-width="5" stroke-linecap="round"/>
    <line x1="56" y1="50" x2="66" y2="66" stroke="#cc0000" stroke-width="5" stroke-linecap="round"/>
    <ellipse cx="50" cy="35" rx="12" ry="16" fill="none" stroke="#000066" stroke-width="1.5" opacity="0.5"/>
  </g>
  <text x="450" y="85" text-anchor="middle" class="title-text" filter="url(#redglow)">ARSAL ADNAN</text>
  <text x="450" y="115" text-anchor="middle" class="sub-text">AI ENGINEER  ·  FULL-STACK  ·  SYSTEMS ARCHITECT</text>
  <line x1="150" y1="125" x2="370" y2="125" stroke="#cc0000" stroke-width="1" opacity="0.5"/>
  <line x1="530" y1="125" x2="750" y2="125" stroke="#cc0000" stroke-width="1" opacity="0.5"/>
  <circle cx="450" cy="125" r="3" fill="#cc0000" opacity="0.8"/>
</svg>

</div>

---

<div align="center">

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Share+Tech+Mono&size=14&duration=2500&pause=1200&color=CC0000&background=00000000&center=true&vCenter=true&width=700&lines=AI+Engineer+%2F+Full-Stack+Developer+%2F+Systems+Architect;LangGraph+%7C+LangChain+%7C+FastAPI+%7C+MERN+Stack;Building+autonomous+agents+that+think%2C+validate+%26+self-heal;With+great+power+comes+great+responsibility+and+great+code;Currently+%40+Intercraft+Pvt+Ltd+%E2%80%94+Rawalpindi%2C+Pakistan)](https://git.io/typing-svg)

</div>

---

<div align="center">
<svg width="860" height="80" viewBox="0 0 860 80" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      @keyframes crawl { 0%{transform:translateX(-40px)} 100%{transform:translateX(920px)} }
      @keyframes fadeWeb { 0%,100%{opacity:0.15} 50%{opacity:0.5} }
      .crawl-spider { animation: crawl 8s linear infinite; }
      .fade-web { animation: fadeWeb 3s ease-in-out infinite; }
    </style>
  </defs>
  <rect width="860" height="80" fill="#050505"/>
  <g class="fade-web">
    <line x1="430" y1="0" x2="100" y2="80" stroke="#cc0000" stroke-width="0.7" opacity="0.4"/>
    <line x1="430" y1="0" x2="200" y2="80" stroke="#cc0000" stroke-width="0.7" opacity="0.4"/>
    <line x1="430" y1="0" x2="300" y2="80" stroke="#cc0000" stroke-width="0.7" opacity="0.4"/>
    <line x1="430" y1="0" x2="430" y2="80" stroke="#cc0000" stroke-width="0.7" opacity="0.4"/>
    <line x1="430" y1="0" x2="560" y2="80" stroke="#cc0000" stroke-width="0.7" opacity="0.4"/>
    <line x1="430" y1="0" x2="660" y2="80" stroke="#cc0000" stroke-width="0.7" opacity="0.4"/>
    <line x1="430" y1="0" x2="760" y2="80" stroke="#cc0000" stroke-width="0.7" opacity="0.4"/>
    <path d="M 220,0 Q 430,55 640,0" fill="none" stroke="#cc0000" stroke-width="0.6" opacity="0.35"/>
    <path d="M 130,0 Q 430,75 730,0" fill="none" stroke="#cc0000" stroke-width="0.6" opacity="0.25"/>
    <path d="M 310,0 Q 430,35 550,0" fill="none" stroke="#cc0000" stroke-width="0.6" opacity="0.3"/>
  </g>
  <g class="crawl-spider">
    <circle cx="0" cy="40" r="5" fill="#cc0000"/>
    <line x1="-8" y1="37" x2="-16" y2="30" stroke="#cc0000" stroke-width="1.5"/>
    <line x1="-8" y1="40" x2="-16" y2="40" stroke="#cc0000" stroke-width="1.5"/>
    <line x1="-8" y1="43" x2="-16" y2="50" stroke="#cc0000" stroke-width="1.5"/>
    <line x1="8" y1="37" x2="16" y2="30" stroke="#cc0000" stroke-width="1.5"/>
    <line x1="8" y1="40" x2="16" y2="40" stroke="#cc0000" stroke-width="1.5"/>
    <line x1="8" y1="43" x2="16" y2="50" stroke="#cc0000" stroke-width="1.5"/>
    <circle cx="-2" cy="38" r="1.5" fill="white"/>
    <circle cx="2" cy="38" r="1.5" fill="white"/>
  </g>
</svg>
</div>

## `> PERSONNEL FILE`

```yaml
name         : Arsal Adnan
handle       : Lunarfang08
current_role : AI Engineer — Intercraft Pvt Ltd
location     : Rawalpindi, Pakistan
education    : BS Computer Science — Bahria University (2020–2024)
status       : ACTIVE
clearance    : Full-Stack | AI/ML | Autonomous Agents | DevOps
mission      : Building scalable, intelligent systems that operate at the edge of automation
```

---

## `> OPERATIONAL TIMELINE`

```
2026 — PRESENT  [========================================]  AI ENGINEER
                 Intercraft Pvt Ltd, Rawalpindi
                 — Autonomous error-detection & auto-fixing agents via LangGraph + LLM
                 — Multi-phase QA pipelines: PRE-QA  BUILD-QA  RUNTIME-QA
                 — Production REST APIs (FastAPI) with async ops & multi-user sessions
                 — Docker containerization with auto port management & error recovery
                 — LLM integration: OpenAI, Anthropic, Ollama via LangChain
                 — Stack: Python · FastAPI · Docker · LangChain · LangGraph

2024 — 2025     [================================]  SOFTWARE ENGINEER
                 eGeefis Global, Rawalpindi
                 — AI & data-driven application design and deployment
                 — Full-stack web & enterprise application delivery
                 — Stack: Python · JavaScript · TensorFlow · MongoDB

AUG 2024        [================]  RESEARCH ANALYST
                 eGeefis Global — 100+ market data reports — +15% sales growth

SEP 2023        [========]  FRONT-END DEVELOPER
                 Internee.pk, Islamabad — Flutter — +30% app performance

JUL 2023        [====]  JUNIOR DEVELOPER
                 The Worx, Islamabad — React.js — +40% load speed
```

---

## `> SYSTEM CAPABILITIES`

<div align="center">

| Domain | Technologies |
|---|---|
| **Languages** | Python · JavaScript · TypeScript · C++ · C# · SQL · HTML5 · CSS · SCSS |
| **Frontend** | React · Next.js · Tailwind CSS · Flutter · ASP.NET |
| **Backend** | Node.js · Express · FastAPI · Flask · Django · ASP.NET Core |
| **AI / ML** | LangChain · LangGraph · TensorFlow · PyTorch · spaCy · Pandas · RAG · FAISS |
| **Databases** | MongoDB · MongoDB Atlas |
| **DevOps** | Docker · Docker Compose · AWS · Apache · Nginx · Gunicorn · Uvicorn |
| **LLM Backends** | OpenAI GPT · Anthropic Claude · Ollama |
| **Auth / Security** | JWT · bcrypt.js · RBAC · SSL/TLS · Token-based APIs |
| **Tools** | Git · GitHub · VS Code · Jupyter · Figma · Power BI · Pydantic |

</div>

---

## `> DEPLOYED PROJECTS`

```
╔══════════════════════════════════════════════════════════════════════════════╗
║  [ WEB-01 ] :: AI FULLSTACK GENERATOR AGENT                          [2026]  ║
║  ─────────────────────────────────────────────────────────────────────────  ║
║  Autonomous agent — generates production-ready fullstack apps from prompts   ║
║  React/Vue/Angular + Express/Flask/FastAPI auto-detection                    ║
║  > 3-phase QA pipeline with auto error detection & fixing                    ║
║  > Docker Compose automation — hours to seconds                              ║
║  > Anthropic prompt caching — 40% LLM cost reduction                        ║
║  > CloudFlare Tunnel — global HTTPS, zero port forwarding                    ║
║  Stack: FastAPI · LangGraph · Docker · Anthropic/OpenAI · FAISS · asyncio   ║
╚══════════════════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════════════════╗
║  [ WEB-02 ] :: AI-POWERED CHATBOT SYSTEM                             [2026]  ║
║  ─────────────────────────────────────────────────────────────────────────  ║
║  Bookings: hotels, buses, tours. LLM intent + entity extraction.             ║
║  Multi-turn memory. RAG-based FAQ. Guardrails for structured responses.      ║
╚══════════════════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════════════════╗
║  [ WEB-03 ] :: NUMBUDDY — E-LEARNING PLATFORM                        [2024]  ║
║  ─────────────────────────────────────────────────────────────────────────  ║
║  For individuals with dyscalculia. Full MERN stack.                          ║
║  bcrypt.js · JWT · RBAC — full security layer.                               ║
╚══════════════════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════════════════╗
║  [ WEB-04 ] :: EMPLOYEE MANAGEMENT SYSTEM                            [2024]  ║
║  ─────────────────────────────────────────────────────────────────────────  ║
║  Payroll · ledger · payslip generation. 25% HR workload down.                ║
║  20% payroll accuracy up. React · Node.js · MongoDB Atlas · Vercel           ║
╚══════════════════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════════════════╗
║  [ WEB-05 ] :: APPOINTMENT BOOKING SYSTEM                            [2024]  ║
║  ─────────────────────────────────────────────────────────────────────────  ║
║  MERN stack scheduling. $500,000 operational savings via MongoDB + Vercel.   ║
╚══════════════════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════════════════╗
║  [ WEB-06 ] :: CHATREADER API                                        [2025]  ║
║  ─────────────────────────────────────────────────────────────────────────  ║
║  Memory · intent classification · data extraction.                           ║
║  FastAPI · OpenAI GPT-3.5 · MongoDB · asyncio · spaCy · Pydantic            ║
╚══════════════════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════════════════╗
║  [ WEB-07 ] :: TASK MANAGEMENT APP                                   [2025]  ║
║  ─────────────────────────────────────────────────────────────────────────  ║
║  Next.js 14 · TypeScript · Tailwind CSS                                      ║
║  Real-time countdown timers · idle detection · Excel export                  ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

---

## `> KEY ACHIEVEMENTS`

```
[01]  Reduced LLM API token costs by 60% via Anthropic prompt caching
[02]  Cut project deployment time by 35% using ThreadPoolExecutor + asyncio
[03]  REST endpoints handling 50+ concurrent requests with full SSL/TLS
[04]  Website load speed improved by 40% at The Worx
[05]  App performance increased by 30% at Internee.pk via Flutter optimization
[06]  15% sales growth from 100-report market analysis at eGeefis Global
[07]  HR workload reduced by 25%, payroll accuracy improved by 20%
[08]  Appointment system enabled $500,000 in operational cost reductions
[09]  Modular agent architecture enabling independent AI pipeline scaling
[10]  Sub-2-second API response times maintained under concurrent load
```

---

## `> CERTIFICATIONS`

```
[x]  AWS Cloud Architecting
[x]  AWS Cloud Developing
[x]  Google — Introduction to Generative AI
[x]  Meta — Frontend Development
[x]  Introduction to Figma
[x]  Introduction to WordPress
```

---

## `> OPEN CHANNELS`

<div align="center">

[![Portfolio](https://img.shields.io/badge/PORTFOLIO-arsaladnan01.vercel.app-CC0000?style=flat-square&labelColor=0a0a0a&color=CC0000)](https://arsaladnan01.vercel.app/)
&nbsp;
[![LinkedIn](https://img.shields.io/badge/LINKEDIN-in%2Farsaladnan-CC0000?style=flat-square&labelColor=0a0a0a&color=CC0000)](https://www.linkedin.com/in/arsaladnan/)
&nbsp;
[![LeetCode](https://img.shields.io/badge/LEETCODE-arsaladnan-CC0000?style=flat-square&labelColor=0a0a0a&color=CC0000)](https://leetcode.com/u/arsaladnan/)
&nbsp;
[![NumBuddy](https://img.shields.io/badge/NUMBUDDY-LIVE-CC0000?style=flat-square&labelColor=0a0a0a&color=CC0000)](https://numbuddy.vercel.app/)
&nbsp;
[![Email](https://img.shields.io/badge/EMAIL-arsaladnan07%40gmail.com-CC0000?style=flat-square&labelColor=0a0a0a&color=CC0000)](mailto:arsaladnan07@gmail.com)

</div>

---

## `> DIAGNOSTICS`

<div align="center">

![GitHub Stats](https://github-readme-stats.vercel.app/api?username=Lunarfang08&show_icons=true&hide_border=true&bg_color=050505&title_color=CC0000&icon_color=CC0000&text_color=888888&ring_color=CC0000)

&nbsp;

![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=Lunarfang08&layout=compact&hide_border=true&bg_color=050505&title_color=CC0000&text_color=888888)

</div>

<div align="center">

![Streak](https://streak-stats.demolab.com?user=Lunarfang08&hide_border=true&background=050505&ring=CC0000&fire=CC0000&currStreakLabel=CC0000&sideLabels=666666&dates=444444&currStreakNum=CC0000&sideNums=888888)

</div>

---

<div align="center">
<svg width="860" height="120" viewBox="0 0 860 120" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      @keyframes spinWeb { 0%{transform:rotate(0deg)}100%{transform:rotate(360deg)} }
      @keyframes glowPulse { 0%,100%{opacity:0.15}50%{opacity:0.5} }
      @keyframes textFade { 0%,100%{opacity:0.5}50%{opacity:1} }
      .spin-slow { animation: spinWeb 20s linear infinite; transform-origin: 430px 60px; }
      .glow-p { animation: glowPulse 3s ease-in-out infinite; }
      .footer-text { font-family: 'Courier New', monospace; fill: #cc0000; font-size: 11px; letter-spacing: 4px; animation: textFade 4s ease-in-out infinite; }
    </style>
  </defs>
  <rect width="860" height="120" fill="#050505"/>
  <g class="spin-slow glow-p">
    <line x1="430" y1="20" x2="430" y2="100" stroke="#cc0000" stroke-width="0.7"/>
    <line x1="390" y1="30" x2="470" y2="90" stroke="#cc0000" stroke-width="0.7"/>
    <line x1="370" y1="60" x2="490" y2="60" stroke="#cc0000" stroke-width="0.7"/>
    <line x1="390" y1="90" x2="470" y2="30" stroke="#cc0000" stroke-width="0.7"/>
    <ellipse cx="430" cy="60" rx="20" ry="20" fill="none" stroke="#cc0000" stroke-width="0.6"/>
    <ellipse cx="430" cy="60" rx="35" ry="35" fill="none" stroke="#cc0000" stroke-width="0.5"/>
  </g>
  <g class="glow-p" style="animation-delay:1s">
    <line x1="0" y1="0" x2="180" y2="120" stroke="#cc0000" stroke-width="0.6"/>
    <line x1="0" y1="0" x2="120" y2="120" stroke="#cc0000" stroke-width="0.6"/>
    <line x1="0" y1="0" x2="60" y2="120" stroke="#cc0000" stroke-width="0.6"/>
    <line x1="0" y1="0" x2="240" y2="120" stroke="#cc0000" stroke-width="0.6"/>
    <path d="M 0,30 Q 80,50 160,30" fill="none" stroke="#cc0000" stroke-width="0.5"/>
    <path d="M 0,60 Q 100,80 200,60" fill="none" stroke="#cc0000" stroke-width="0.5"/>
    <path d="M 0,90 Q 120,100 240,90" fill="none" stroke="#cc0000" stroke-width="0.5"/>
  </g>
  <g class="glow-p" style="animation-delay:1.5s">
    <line x1="860" y1="0" x2="680" y2="120" stroke="#cc0000" stroke-width="0.6"/>
    <line x1="860" y1="0" x2="740" y2="120" stroke="#cc0000" stroke-width="0.6"/>
    <line x1="860" y1="0" x2="800" y2="120" stroke="#cc0000" stroke-width="0.6"/>
    <line x1="860" y1="0" x2="620" y2="120" stroke="#cc0000" stroke-width="0.6"/>
    <path d="M 860,30 Q 780,50 700,30" fill="none" stroke="#cc0000" stroke-width="0.5"/>
    <path d="M 860,60 Q 760,80 660,60" fill="none" stroke="#cc0000" stroke-width="0.5"/>
    <path d="M 860,90 Q 740,100 620,90" fill="none" stroke="#cc0000" stroke-width="0.5"/>
  </g>
  <text x="430" y="65" text-anchor="middle" class="footer-text">"WITH GREAT POWER COMES GREAT CODE"</text>
  <line x1="180" y1="75" x2="340" y2="75" stroke="#cc0000" stroke-width="0.8" opacity="0.4"/>
  <line x1="520" y1="75" x2="680" y2="75" stroke="#cc0000" stroke-width="0.8" opacity="0.4"/>
</svg>

![Visitor Badge](https://komarev.com/ghpvc/?username=Lunarfang08&style=flat-square&color=CC0000&label=PROFILE+READS)

</div>
