<!-- Header -->
<p align="right">
  <b>English</b> · <a href="README.es.md">Español</a>
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:512BD4,50:6D28D9,100:0EA5E9&height=230&section=header&text=Roberto%20Gallardo&fontSize=60&fontColor=ffffff&fontAlignY=36&desc=Full%20Stack%20.NET%20Developer%20%C2%B7%20Software%20Architecture%20%C2%B7%20AI%20tooling&descSize=17&descAlignY=58&animation=fadeIn" alt="Roberto Gallardo" width="100%" />
</p>

<p align="center">
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=21&duration=3200&pause=1100&color=8B5CF6&center=true&vCenter=true&width=720&lines=Hey%2C+I%27m+Roberto+%F0%9F%91%8B+a+dev+from+Guadalajara+%F0%9F%8C%AE;I+turn+legacy+code+into+clean+.NET+8;Now+shipping+RepoRinse+%F0%9F%A7%BC+in+Rust;Teaching+AI+agents+to+edit+my+videos+%F0%9F%8E%AC;If+it%27s+not+clear%2C+it%27s+not+done+%E2%9C%A8" alt="Typing SVG" />
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

---

## 👋 About me

<table>
<tr>
<td width="55%" valign="top">

```csharp
public sealed record Developer
{
    public string Name     => "Roberto Gallardo";
    public string Role     => "Full Stack .NET Developer";
    public string HomeTown => "Guadalajara 🇲🇽 — tortas ahogadas certified";
    public string[] Stack  => [".NET 8", "C#", "Rust", "Vue",
                               "React", "Next.js", "MongoDB"];
    public string[] Loves  => ["Clean Architecture", "SOLID",
                               "CI/CD", "AI agents & MCP"];
    public string Motto    => "Code that works is the minimum. "
                            + "Code that's clear is the goal.";
}
```

</td>
<td width="45%" valign="top">

I read the legacy code before judging it — then leave it better than I found it.

🏗️ **By day:** backend services in **.NET 8** for a global logistics company.<br/><br/>
🌙 **By night:** AI agents that do real work — editing my videos, publishing them, even doing my taxes. 😅<br/><br/>
🧼 **Right now:** shipping [**RepoRinse**](https://github.com/robgallardof/RepoRinse), a Rust CLI that keeps repos clean.<br/><br/>
💬 **Ask me about:** C#, software design, MongoDB, Vue/Next.js, DevOps — or the best taquería in GDL.

</td>
</tr>
</table>

---

## 🧼 Spotlight: RepoRinse

<p align="center">
  <a href="https://github.com/robgallardof/RepoRinse">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://socialify.git.ci/robgallardof/RepoRinse/image?theme=Dark&font=Inter&language=1&description=1&name=1&owner=1&pattern=Circuit%20Board" />
      <img src="https://socialify.git.ci/robgallardof/RepoRinse/image?theme=Light&font=Inter&language=1&description=1&name=1&owner=1&pattern=Circuit%20Board" alt="RepoRinse" width="80%" />
    </picture>
  </a>
</p>

<p align="center"><b>Keep the code. Rinse the noise.</b></p>

<p align="center">
  <img src="https://img.shields.io/badge/Rust-000000?style=flat-square&logo=rust&logoColor=white" alt="Rust" />
  <img src="https://img.shields.io/badge/Git%20hooks-F05032?style=flat-square&logo=git&logoColor=white" alt="Git hooks" />
  <img src="https://img.shields.io/badge/Claude%20Code-D97757?style=flat-square&logo=anthropic&logoColor=white" alt="Claude Code" />
  <img src="https://img.shields.io/badge/Codex-412991?style=flat-square&logo=openai&logoColor=white" alt="Codex" />
  <img src="https://img.shields.io/badge/Gemini%20CLI-8E75B2?style=flat-square&logo=googlegemini&logoColor=white" alt="Gemini CLI" />
  <img src="https://img.shields.io/badge/Cursor-000000?style=flat-square&logo=cursor&logoColor=white" alt="Cursor" />
  <img src="https://img.shields.io/badge/offline-no%20telemetry-2ea44f?style=flat-square" alt="Offline" />
  <img src="https://img.shields.io/github/last-commit/robgallardof/RepoRinse?style=flat-square&color=6D28D9" alt="Last commit" />
</p>

A local, deterministic CLI that strips AI co-author trailers (and keeps the humans), cleans whitespace and invisible
Unicode, and plugs guardrails into the native hooks of **Claude Code, Codex, Gemini CLI and Cursor**. It installs
next to your existing hooks and uninstalls byte-for-byte. It is the successor of my little
[`no-ai-coauthor`](https://github.com/robgallardof/no-ai-couathor) hook.

```sh
reporinse install --provider git --all --yes           # clean every commit message
reporinse install --provider claude,codex --all --yes  # guardrails for your agents
```

---

## 🧩 My AI agent toolbox

I build **MCP servers, skills and hooks** so agents can do real work on my machine — locally, with me in control.

<table>
  <tr>
    <th width="33%">🔌 MCP servers</th>
    <th width="33%">🎯 Skills &amp; agent roles</th>
    <th width="33%">🪝 Hooks &amp; guardrails</th>
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

---

## 🛠️ Tech stack

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

---

## 🚀 Featured projects

<table>
  <tr>
    <td width="50%" valign="top">
      <a href="https://github.com/robgallardof/davinci-resolve-mcp"><img src="https://socialify.git.ci/robgallardof/davinci-resolve-mcp/image?theme=Dark&font=Inter&language=1&name=1&owner=1&pattern=Plus&stargazers=1" alt="davinci-resolve-mcp" width="100%" /></a>
      <p>🎬 Edit in DaVinci Resolve by talking to an AI that works like a producer: vertical &amp; horizontal cuts, motion that keeps faces whole, designed captions, music on the beat and QA before every render.</p>
    </td>
    <td width="50%" valign="top">
      <a href="https://github.com/robgallardof/social-publisher-mcp"><img src="https://socialify.git.ci/robgallardof/social-publisher-mcp/image?theme=Dark&font=Inter&language=1&name=1&owner=1&pattern=Plus" alt="social-publisher-mcp" width="100%" /></a>
      <p>📲 An AI community manager for short‑form video as an MCP server: watches your videos, writes the copy for every network, schedules at 05:00 and tells you what worked.</p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <a href="https://github.com/robgallardof/declaracion"><img src="https://socialify.git.ci/robgallardof/declaracion/image?theme=Dark&font=Inter&language=1&name=1&owner=1&pattern=Plus" alt="declaracion" width="100%" /></a>
      <p>🧾 A personal tax assistant for Mexico inside your AI agent: reads CFDI, computes ISR and IVA (RESICO) and guides you through filing. Your data stays on your PC.</p>
    </td>
    <td width="50%" valign="top">
      <a href="https://github.com/robgallardof/wallybot"><img src="https://socialify.git.ci/robgallardof/wallybot/image?theme=Dark&font=Inter&language=1&name=1&owner=1&pattern=Plus" alt="wallybot" width="100%" /></a>
      <p>🤖 Self‑hosted hub for market analysis, portfolio and AI‑assisted trading: explained proposals, your approval and risk controls.</p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <a href="https://github.com/robgallardof/wikdoc"><img src="https://socialify.git.ci/robgallardof/wikdoc/image?theme=Dark&font=Inter&language=1&name=1&owner=1&pattern=Plus" alt="wikdoc" width="100%" /></a>
      <p>📚 Turn any folder of code into a local, searchable knowledge base you can chat with — embeddings + RAG over Ollama, nothing leaves your machine.</p>
    </td>
    <td width="50%" valign="top">
      <a href="https://github.com/robgallardof/arquest"><img src="https://socialify.git.ci/robgallardof/arquest/image?theme=Dark&font=Inter&language=1&name=1&owner=1&pattern=Plus" alt="arquest" width="100%" /></a>
      <p>⚡ A Postman/Thunder‑like HTTP client on Next.js App Router: dark‑mode‑first UI and installable PWA with offline cache.</p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <a href="https://github.com/robgallardof/ruxtbot"><img src="https://socialify.git.ci/robgallardof/ruxtbot/image?theme=Dark&font=Inter&language=1&name=1&owner=1&pattern=Plus" alt="ruxtbot" width="100%" /></a>
      <p>🎮 Discord bot for Rust: raid planning with pictures, crafting, live servers, player lookups and BattleMetrics alerts, in English and Spanish.</p>
    </td>
    <td width="50%" valign="top">
      <a href="https://github.com/robgallardof/portfolio-roberto-gallardo"><img src="https://socialify.git.ci/robgallardof/portfolio-roberto-gallardo/image?theme=Dark&font=Inter&language=1&name=1&owner=1&pattern=Plus" alt="portfolio" width="100%" /></a>
      <p>🌐 My personal portfolio: Next.js, Tailwind and shadcn/ui, bilingual and dark‑mode ready.</p>
    </td>
  </tr>
</table>

<p align="center">
  <a href="https://github.com/robgallardof?tab=repositories"><b>➜ See all repositories</b></a>
</p>

---

## 💼 Experience

| Industry | Role | Period |
|---|---|---|
| 🚚 **Global logistics** | Full Stack .NET Developer — .NET 8, Clean Architecture, CQRS, Docker/K8s, Azure DevOps, Vue, MongoDB | 2023 – present |
| 🏦 **Banking** | .NET Developer — .NET Framework → .NET 5, biometrics, GCM → FCM, Kotlin | 2022 |
| 📡 **Telecom** | Developer — VB.NET / C# / Java, SQL Server, SSRS, Mulesoft | 2019 – 2022 |

## 🎓 Education

| | Degree | School |
|---|---|---|
| 🎓 | **Master's Degree in Software Architecture** | AICAD Business School |
| 🎓 | **Bachelor's in Administrative Computer Systems** | Universidad Veracruzana |

---

## 📊 GitHub stats

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

## 🐍 Contribution snake

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/robgallardof/robgallardof/output/github-snake-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/robgallardof/robgallardof/output/github-snake.svg" />
    <img alt="Contribution snake" src="https://raw.githubusercontent.com/robgallardof/robgallardof/output/github-snake.svg" />
  </picture>
</p>

---

<p align="center">
  <i>“Make it work, make it right, make it fast.” — Kent Beck</i>
</p>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0EA5E9,50:6D28D9,100:512BD4&height=110&section=footer" width="100%" alt="footer" />
