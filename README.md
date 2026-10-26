<!-- Header -->
<p align="right">
  <b>English</b> · <a href="README.es.md">Español</a>
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/hero-dark.svg" />
    <img src="assets/hero-light.svg" alt="Roberto Gallardo — Software Architect · Full Stack .NET · AI tooling" width="100%" />
  </picture>
</p>

<p align="center">
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=21&duration=3200&pause=1100&color=8B5CF6&center=true&vCenter=true&width=720&lines=Hey%2C+I%27m+Roberto+%F0%9F%91%8B+software+architect+from+Guadalajara;From+.NET+Framework+2.0+to+.NET+10+%26+11;Building+Rekora%3A+memory+for+AI+agents+%F0%9F%A7%A0;Now+shipping+RepoRinse+%F0%9F%A7%BC+in+Rust;Teaching+AI+agents+to+edit+my+videos+%F0%9F%8E%AC;If+it%27s+not+clear%2C+it%27s+not+done+%E2%9C%A8" alt="Typing SVG" />
  </a>
</p>

<p align="center">
  <a href="https://robertogallardo.dev"><img src="https://img.shields.io/badge/Website-robertogallardo.dev-0EA5E9?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Website" /></a>
  <a href="https://linkedin.com/in/robgallardof"><img src="https://img.shields.io/badge/LinkedIn-robgallardof-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  <a href="https://github.com/robgallardof?tab=repositories"><img src="https://img.shields.io/badge/Repos-explore-181717?style=for-the-badge&logo=github&logoColor=white" alt="Repositories" /></a>
</p>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=robgallardof&label=Profile%20views&color=6D28D9&style=flat-square" alt="Profile views" />
  <img src="https://img.shields.io/github/followers/robgallardof?label=Followers&style=flat-square&color=0EA5E9&logo=github" alt="Followers" />
  <img src="https://img.shields.io/badge/%F0%9F%93%8D-Guadalajara%2C%20Jalisco%20%F0%9F%87%B2%F0%9F%87%BD-512BD4?style=flat-square" alt="Location" />
</p>

<p align="center"><b><a href="#about">About</a> · <a href="#building">Building now</a> · <a href="#toolbox">AI toolbox</a> · <a href="#stack">Stack</a> · <a href="#projects">Projects</a> · <a href="#experience">Experience</a> · <a href="#stats">Stats</a></b></p>

<p align="center"><img src="assets/divider.svg" alt="" width="80%" /></p>

<a id="about"></a>
<p align="center"><img src="assets/sections/en-01.svg" alt="01 · About me" width="100%" /></p>

<table>
<tr>
<td width="55%" valign="top">

```csharp
public sealed record Developer
{
    public string Name     => "Roberto Gallardo";
    public string Role     => "Software Architect · Full Stack .NET";
    public string Location => "Guadalajara, Jalisco 🇲🇽";
    public string DotNet   => ".NET Framework 2.0 → .NET 10 / 11";
    public string[] Stack  => ["C#", "VB.NET", "Rust", "Python",
                               "Vue", "React", "Next.js",
                               "MongoDB", "SQL Server"];
    public string[] Loves  => ["Clean Architecture", "SOLID",
                               "CI/CD", "AI agents & MCP"];
    public string Motto    => "Code that works is the minimum. "
                            + "Code that's clear is the goal.";
}
```

</td>
<td width="45%" valign="top">

I read the legacy code before judging it — then leave it better than I found it.

🏗️ **By day:** backend services in **.NET** for a global logistics company.<br/><br/>
🔄 **Every .NET generation:** from **.NET Framework 2.0 / 3.5 / 4.x** through .NET Core and **.NET 5 → 10 and 11** — and the migrations in between.<br/><br/>
🤖 **4 years with AI:** from ChatGPT to Codex, Claude Code and Antigravity — reviewed and guarded, never blind.<br/><br/>
🌙 **By night:** AI agents that do real work — editing my videos, publishing them, even doing my taxes.<br/><br/>
🔨 **Right now:** building [**RepoRinse**](https://github.com/robgallardof/RepoRinse) and [**Rekora**](https://github.com/robgallardof/rekora), Rust tools for AI coding agents.<br/><br/>
💬 **Ask me about:** C#, .NET migrations, software design, MongoDB, Vue/Next.js, DevOps and AI agents.

</td>
</tr>
</table>

<p align="center"><img src="assets/divider.svg" alt="" width="80%" /></p>

<a id="building"></a>
<p align="center"><img src="assets/sections/en-02.svg" alt="02 · What I'm building now" width="100%" /></p>

Tools that let AI coding agents work safely and remember what matters — local, no telemetry, written in Rust.

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>🧼 <a href="https://github.com/robgallardof/RepoRinse">RepoRinse</a></h3>
      <p>Local, deterministic Rust CLI that keeps repos clean: strips AI co-author trailers (keeps the humans), whitespace and invisible Unicode, plus guardrails for Claude Code, Codex, Gemini CLI and Cursor.</p>
      <p><code>Rust</code> <code>Git hooks</code> <code>Agent guardrails</code></p>
      <p>
        <img src="https://img.shields.io/github/languages/top/robgallardof/RepoRinse?style=flat-square&color=6D28D9" alt="Top language" />
        <img src="https://img.shields.io/github/stars/robgallardof/RepoRinse?label=stars&style=flat-square&color=F59E0B&logo=github" alt="Stars" />
        <img src="https://img.shields.io/github/last-commit/robgallardof/RepoRinse?label=last%20commit&style=flat-square&color=0EA5E9" alt="Last commit" />
      </p>
    </td>
    <td width="50%" valign="top">
      <h3>🧠 <a href="https://github.com/robgallardof/rekora">Rekora</a></h3>
      <p>Local-first, verifiable memory for AI coding agents: decisions, constraints and known issues with their sources, flagged as stale when a cited file changes, served through a CLI and an MCP server within a token budget. Early development.</p>
      <p><code>Rust</code> <code>SQLite</code> <code>MCP</code> <code>Early stage</code></p>
      <p>
        <img src="https://img.shields.io/github/languages/top/robgallardof/rekora?style=flat-square&color=6D28D9" alt="Top language" />
        <img src="https://img.shields.io/github/stars/robgallardof/rekora?label=stars&style=flat-square&color=F59E0B&logo=github" alt="Stars" />
        <img src="https://img.shields.io/github/last-commit/robgallardof/rekora?label=last%20commit&style=flat-square&color=0EA5E9" alt="Last commit" />
      </p>
    </td>
  </tr>
</table>

```sh
reporinse install --provider git --all --yes            # clean every commit message
reporinse install --provider claude,codex --all --yes   # guardrails for your agents
```

<p align="center"><img src="assets/divider.svg" alt="" width="80%" /></p>

<a id="toolbox"></a>
<p align="center"><img src="assets/sections/en-03.svg" alt="03 · My AI agent toolbox" width="100%" /></p>

I build **MCP servers, skills and hooks** so agents can do real work on my machine — locally, with me in control.

<table>
  <tr>
    <th width="33%">🔌 MCP servers</th>
    <th width="33%">🎯 Skills &amp; agent roles</th>
    <th width="33%">🧠 Memory &amp; guardrails</th>
  </tr>
  <tr>
    <td valign="top">
      <a href="https://github.com/robgallardof/davinci-resolve-mcp">davinci-resolve-mcp</a> — video editing<br/>
      <a href="https://github.com/robgallardof/social-publisher-mcp">social-publisher-mcp</a> — publishing<br/>
      <a href="https://github.com/robgallardof/declaracion">declaracion</a> — Mexican taxes
    </td>
    <td valign="top">
      Producer, editors, colorist and QA for Resolve<br/>
      Copywriter, strategist and analyst for social<br/>
      Accountant and auditor for tax returns
    </td>
    <td valign="top">
      <a href="https://github.com/robgallardof/rekora">Rekora</a> — verifiable memory for agents<br/>
      <a href="https://github.com/robgallardof/RepoRinse">RepoRinse</a> — Git &amp; agent hooks<br/>
      Command and path guards for agents<br/>
      A clean, human-only commit history
    </td>
  </tr>
</table>

<p align="center">
  <img src="https://img.shields.io/badge/MCP-servers-8A2BE2?style=for-the-badge&logo=anthropic&logoColor=white" alt="MCP" />
  <img src="https://img.shields.io/badge/Claude%20Code-skills%20%26%20plugins-D97757?style=for-the-badge&logo=anthropic&logoColor=white" alt="Claude Code skills and plugins" />
  <img src="https://img.shields.io/badge/Ollama-local%20RAG-000000?style=for-the-badge&logo=ollama&logoColor=white" alt="Ollama" />
</p>

<p align="center"><img src="assets/divider.svg" alt="" width="80%" /></p>

<a id="stack"></a>
<p align="center"><img src="assets/sections/en-04.svg" alt="04 · Tech stack" width="100%" /></p>

<p align="center">
  <b>Backend</b><br/><br/>
  <img src="https://skillicons.dev/icons?i=cs,dotnet,rust,python,kotlin,nodejs&theme=dark" alt="Backend" />
</p>
<p align="center">
  <b>Frontend</b><br/><br/>
  <img src="https://skillicons.dev/icons?i=ts,js,react,nextjs,vue,tailwind,html,css&theme=dark" alt="Frontend" />
</p>
<p align="center">
  <b>Data · Cloud · DevOps</b><br/><br/>
  <img src="https://skillicons.dev/icons?i=mongodb,mysql,azure,docker,kubernetes,nginx,cloudflare,linux&theme=dark" alt="Data, cloud and DevOps" />
</p>
<p align="center">
  <b>Tools</b><br/><br/>
  <img src="https://skillicons.dev/icons?i=git,github,githubactions,vscode,visualstudio,postman,powershell,bash&theme=dark" alt="Tools" />
</p>

<p align="center">
  <b>AI &amp; agents</b><br/><br/>
  <img src="https://img.shields.io/badge/Claude%20Code-D97757?style=for-the-badge&logo=claude&logoColor=white" alt="Claude Code" />
  <img src="https://img.shields.io/badge/ChatGPT-10A37F?style=for-the-badge&logoColor=white" alt="ChatGPT" />
  <img src="https://img.shields.io/badge/Codex-412991?style=for-the-badge&logoColor=white" alt="Codex" />
  <img src="https://img.shields.io/badge/Gemini-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white" alt="Gemini" />
  <img src="https://img.shields.io/badge/Antigravity-4285F4?style=for-the-badge&logo=google&logoColor=white" alt="Antigravity" />
  <img src="https://img.shields.io/badge/Cursor-000000?style=for-the-badge&logo=cursor&logoColor=white" alt="Cursor" />
  <img src="https://img.shields.io/badge/DeepSeek-4D6BFE?style=for-the-badge&logo=deepseek&logoColor=white" alt="DeepSeek" />
  <img src="https://img.shields.io/badge/Ollama-000000?style=for-the-badge&logo=ollama&logoColor=white" alt="Ollama" />
  <img src="https://img.shields.io/badge/MCP-8A2BE2?style=for-the-badge&logo=anthropic&logoColor=white" alt="MCP" />
</p>
<p align="center">
  <b>Content &amp; automation</b><br/><br/>
  <img src="https://img.shields.io/badge/DaVinci%20Resolve-233A51?style=for-the-badge&logo=davinciresolve&logoColor=white" alt="DaVinci Resolve" />
  <img src="https://img.shields.io/badge/TikTok-000000?style=for-the-badge&logo=tiktok&logoColor=white" alt="TikTok" />
  <img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" alt="Instagram" />
  <img src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="YouTube" />
  <img src="https://img.shields.io/badge/Facebook-0866FF?style=for-the-badge&logo=facebook&logoColor=white" alt="Facebook" />
  <img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" />
  <img src="https://img.shields.io/badge/Playwright-2EAD33?style=for-the-badge&logoColor=white" alt="Playwright" />
  <img src="https://img.shields.io/badge/Tampermonkey-00485B?style=for-the-badge&logo=tampermonkey&logoColor=white" alt="Tampermonkey" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/SQL%20Server-CC2927?style=flat-square&logo=microsoftsqlserver&logoColor=white" alt="SQL Server" />
  <img src="https://img.shields.io/badge/EF%20Core-512BD4?style=flat-square&logo=dotnet&logoColor=white" alt="EF Core" />
  <img src="https://img.shields.io/badge/SignalR-512BD4?style=flat-square&logo=dotnet&logoColor=white" alt="SignalR" />
  <img src="https://img.shields.io/badge/xUnit%20%2B%20Moq-5C2D91?style=flat-square&logo=dotnet&logoColor=white" alt="xUnit" />
  <img src="https://img.shields.io/badge/Azure%20DevOps-0078D7?style=flat-square&logo=azuredevops&logoColor=white" alt="Azure DevOps" />
  <img src="https://img.shields.io/badge/shadcn%2Fui-000000?style=flat-square&logo=shadcnui&logoColor=white" alt="shadcn/ui" />
  <img src="https://img.shields.io/badge/DaVinci%20Resolve-233A51?style=flat-square&logo=davinciresolve&logoColor=white" alt="DaVinci Resolve" />
</p>

<p align="center"><img src="assets/divider.svg" alt="" width="80%" /></p>

<a id="projects"></a>
<p align="center"><img src="assets/sections/en-05.svg" alt="05 · Featured projects" width="100%" /></p>

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>🎬 <a href="https://github.com/robgallardof/davinci-resolve-mcp">davinci-resolve-mcp</a></h3>
      <p>Edit in DaVinci Resolve by talking to an AI that works like a producer: vertical & horizontal cuts, motion that keeps faces whole, designed captions, music on the beat and QA before every render.</p>
      <p><code>MCP</code> <code>Python</code> <code>Video</code></p>
      <p>
        <img src="https://img.shields.io/github/languages/top/robgallardof/davinci-resolve-mcp?style=flat-square&color=6D28D9" alt="Top language" />
        <img src="https://img.shields.io/github/stars/robgallardof/davinci-resolve-mcp?label=stars&style=flat-square&color=F59E0B&logo=github" alt="Stars" />
        <img src="https://img.shields.io/github/last-commit/robgallardof/davinci-resolve-mcp?label=last%20commit&style=flat-square&color=0EA5E9" alt="Last commit" />
      </p>
    </td>
    <td width="50%" valign="top">
      <h3>📲 <a href="https://github.com/robgallardof/social-publisher-mcp">social-publisher-mcp</a></h3>
      <p>An AI community manager for short‑form video as an MCP server: watches your videos, writes the copy for every network, schedules at 05:00 and tells you what worked.</p>
      <p><code>MCP</code> <code>Python</code> <code>Social</code></p>
      <p>
        <img src="https://img.shields.io/github/languages/top/robgallardof/social-publisher-mcp?style=flat-square&color=6D28D9" alt="Top language" />
        <img src="https://img.shields.io/github/stars/robgallardof/social-publisher-mcp?label=stars&style=flat-square&color=F59E0B&logo=github" alt="Stars" />
        <img src="https://img.shields.io/github/last-commit/robgallardof/social-publisher-mcp?label=last%20commit&style=flat-square&color=0EA5E9" alt="Last commit" />
      </p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>🧾 <a href="https://github.com/robgallardof/declaracion">declaracion</a></h3>
      <p>A personal tax assistant for Mexico inside your AI agent: reads CFDI, computes ISR and IVA (RESICO) and guides you through filing. Your data stays on your PC.</p>
      <p><code>MCP</code> <code>Python</code> <code>SAT</code></p>
      <p>
        <img src="https://img.shields.io/github/languages/top/robgallardof/declaracion?style=flat-square&color=6D28D9" alt="Top language" />
        <img src="https://img.shields.io/github/stars/robgallardof/declaracion?label=stars&style=flat-square&color=F59E0B&logo=github" alt="Stars" />
        <img src="https://img.shields.io/github/last-commit/robgallardof/declaracion?label=last%20commit&style=flat-square&color=0EA5E9" alt="Last commit" />
      </p>
    </td>
    <td width="50%" valign="top">
      <h3>📚 <a href="https://github.com/robgallardof/wikdoc">wikdoc</a></h3>
      <p>Turn any folder of code into a local, searchable knowledge base you can chat with — embeddings + RAG over Ollama, nothing leaves your machine.</p>
      <p><code>Python</code> <code>Ollama</code> <code>RAG</code></p>
      <p>
        <img src="https://img.shields.io/github/languages/top/robgallardof/wikdoc?style=flat-square&color=6D28D9" alt="Top language" />
        <img src="https://img.shields.io/github/stars/robgallardof/wikdoc?label=stars&style=flat-square&color=F59E0B&logo=github" alt="Stars" />
        <img src="https://img.shields.io/github/last-commit/robgallardof/wikdoc?label=last%20commit&style=flat-square&color=0EA5E9" alt="Last commit" />
      </p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>🤖 <a href="https://github.com/robgallardof/wallybot">wallybot</a></h3>
      <p>Self‑hosted hub for market analysis, portfolio and AI‑assisted trading: explained proposals, your approval and risk controls.</p>
      <p><code>Python</code> <code>Self-hosted</code></p>
      <p>
        <img src="https://img.shields.io/github/languages/top/robgallardof/wallybot?style=flat-square&color=6D28D9" alt="Top language" />
        <img src="https://img.shields.io/github/stars/robgallardof/wallybot?label=stars&style=flat-square&color=F59E0B&logo=github" alt="Stars" />
        <img src="https://img.shields.io/github/last-commit/robgallardof/wallybot?label=last%20commit&style=flat-square&color=0EA5E9" alt="Last commit" />
      </p>
    </td>
    <td width="50%" valign="top">
      <h3>🦊 <a href="https://github.com/robgallardof/multig">multig</a></h3>
      <p>Manage many persistent, isolated browser profiles with Camoufox, a Next.js dashboard and a Python backend.</p>
      <p><code>Next.js</code> <code>Python</code> <code>Camoufox</code></p>
      <p>
        <img src="https://img.shields.io/github/languages/top/robgallardof/multig?style=flat-square&color=6D28D9" alt="Top language" />
        <img src="https://img.shields.io/github/stars/robgallardof/multig?label=stars&style=flat-square&color=F59E0B&logo=github" alt="Stars" />
        <img src="https://img.shields.io/github/last-commit/robgallardof/multig?label=last%20commit&style=flat-square&color=0EA5E9" alt="Last commit" />
      </p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>⚡ <a href="https://github.com/robgallardof/arquest">arquest</a></h3>
      <p>A Postman/Thunder‑like HTTP client on Next.js App Router: dark‑mode‑first UI and installable PWA with offline cache.</p>
      <p><code>Next.js</code> <code>PWA</code></p>
      <p>
        <img src="https://img.shields.io/github/languages/top/robgallardof/arquest?style=flat-square&color=6D28D9" alt="Top language" />
        <img src="https://img.shields.io/github/stars/robgallardof/arquest?label=stars&style=flat-square&color=F59E0B&logo=github" alt="Stars" />
        <img src="https://img.shields.io/github/last-commit/robgallardof/arquest?label=last%20commit&style=flat-square&color=0EA5E9" alt="Last commit" />
      </p>
    </td>
    <td width="50%" valign="top">
      <h3>🎮 <a href="https://github.com/robgallardof/ruxtbot">ruxtbot</a></h3>
      <p>Discord bot for Rust: raid planning with pictures, crafting, live servers, player lookups and BattleMetrics alerts, in English and Spanish.</p>
      <p><code>Discord</code> <code>Bot</code></p>
      <p>
        <img src="https://img.shields.io/github/languages/top/robgallardof/ruxtbot?style=flat-square&color=6D28D9" alt="Top language" />
        <img src="https://img.shields.io/github/stars/robgallardof/ruxtbot?label=stars&style=flat-square&color=F59E0B&logo=github" alt="Stars" />
        <img src="https://img.shields.io/github/last-commit/robgallardof/ruxtbot?label=last%20commit&style=flat-square&color=0EA5E9" alt="Last commit" />
      </p>
    </td>
  </tr>
</table>

<p align="center">
  <a href="https://github.com/robgallardof?tab=repositories"><b>➜ See all repositories</b></a>
</p>

<p align="center"><img src="assets/divider.svg" alt="" width="80%" /></p>

<a id="experience"></a>
<p align="center"><img src="assets/sections/en-06.svg" alt="06 · Experience & education" width="100%" /></p>

| Industry | Role | Period |
|---|---|---|
| 🚚 **Global logistics** | Full Stack .NET Developer — .NET 8, Clean Architecture, CQRS, Docker/K8s, Azure DevOps, Vue, MongoDB | 2023 – present |
| 🏦 **Banking** | .NET Developer — .NET Framework → .NET 5, biometrics, GCM → FCM, Kotlin | 2022 |
| 📡 **Telecom** | Developer — VB.NET / C# / Java, SQL Server, SSRS, Mulesoft | 2019 – 2022 |

### 🎓 Education

| | Degree | School |
|---|---|---|
| 🎓 | **Master's Degree in Software Architecture** | Università degli Studi Guglielmo Marconi · taken at AICAD Business School |
| 🎓 | **Bachelor's in Administrative Computer Systems** | Universidad Veracruzana |

<p align="center"><img src="assets/divider.svg" alt="" width="80%" /></p>

<a id="stats"></a>
<p align="center"><img src="assets/sections/en-07.svg" alt="07 · GitHub stats" width="100%" /></p>

<p align="center">
  <img src="./profile-summary-card-output/tokyonight/0-profile-details.svg" alt="Profile details" width="100%" />
</p>
<p align="center">
  <img src="./profile-summary-card-output/tokyonight/1-repos-per-language.svg" alt="Repos per language" height="180" />
  <img src="./profile-summary-card-output/tokyonight/2-most-commit-language.svg" alt="Most commit language" height="180" />
</p>
<p align="center">
  <img src="./profile-summary-card-output/tokyonight/3-stats.svg" alt="Stats" height="180" />
  <img src="./profile-summary-card-output/tokyonight/4-productive-time.svg" alt="Productive time" height="180" />
</p>
<p align="center">
  <a href="https://git.io/streak-stats"><img src="https://streak-stats.demolab.com?user=robgallardof&theme=tokyonight&hide_border=true&date_format=j%20M%5B%20Y%5D" alt="GitHub streak" /></a>
</p>

### 🐍 Contribution snake

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/robgallardof/robgallardof/output/github-snake-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/robgallardof/robgallardof/output/github-snake.svg" />
    <img alt="Contribution snake" src="https://raw.githubusercontent.com/robgallardof/robgallardof/output/github-snake.svg" />
  </picture>
</p>

<p align="center"><img src="assets/divider.svg" alt="" width="80%" /></p>

<p align="center">
  <i>“Make it work, make it right, make it fast.” — Kent Beck</i>
</p>

<img src="assets/footer-en.svg" alt="Thanks for stopping by" width="100%" />
