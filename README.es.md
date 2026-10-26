<!-- Encabezado -->
<p align="right">
  <a href="README.md">English</a> · <b>Español</b>
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/hero-dark.svg" />
    <img src="assets/hero-light.svg" alt="Roberto Gallardo — Arquitecto de Software · Full Stack .NET · Herramientas de IA" width="100%" />
  </picture>
</p>

<p align="center">
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=21&duration=3200&pause=1100&color=8B5CF6&center=true&vCenter=true&width=720&lines=Hola%2C+soy+Roberto+%F0%9F%91%8B+arquitecto+de+software+en+Guadalajara;De+.NET+Framework+2.0+a+.NET+10+y+11;Construyendo+Rekora%3A+memoria+para+agentes+de+IA+%F0%9F%A7%A0;Ahora+lanzando+RepoRinse+%F0%9F%A7%BC+en+Rust;Ense%C3%B1ando+a+agentes+de+IA+a+editar+mis+videos+%F0%9F%8E%AC;Si+no+se+entiende%2C+no+est%C3%A1+terminado+%E2%9C%A8" alt="Typing SVG" />
  </a>
</p>

<p align="center">
  <a href="https://robertogallardo.dev"><img src="https://img.shields.io/badge/Sitio-robertogallardo.dev-0EA5E9?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Sitio web" /></a>
  <a href="https://linkedin.com/in/robgallardof"><img src="https://img.shields.io/badge/LinkedIn-robgallardof-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  <a href="https://github.com/robgallardof?tab=repositories"><img src="https://img.shields.io/badge/Repos-explorar-181717?style=for-the-badge&logo=github&logoColor=white" alt="Repositorios" /></a>
</p>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=robgallardof&label=Visitas&color=6D28D9&style=flat-square" alt="Visitas" />
  <img src="https://img.shields.io/github/followers/robgallardof?label=Seguidores&style=flat-square&color=0EA5E9&logo=github" alt="Seguidores" />
  <img src="https://img.shields.io/badge/%F0%9F%93%8D-Guadalajara%2C%20Jalisco%20%F0%9F%87%B2%F0%9F%87%BD-512BD4?style=flat-square" alt="Ubicación" />
</p>

<p align="center"><b><a href="#sobre-mi">Sobre mí</a> · <a href="#construyendo">Construyendo</a> · <a href="#herramientas">Herramientas IA</a> · <a href="#tecnologias">Stack</a> · <a href="#proyectos">Proyectos</a> · <a href="#experiencia">Experiencia</a> · <a href="#estadisticas">Estadísticas</a></b></p>

<p align="center"><img src="assets/divider.svg" alt="" width="80%" /></p>

<a id="sobre-mi"></a>
<p align="center"><img src="assets/sections/es-01.svg" alt="01 · Sobre mí" width="100%" /></p>

<table>
<tr>
<td width="55%" valign="top">

```csharp
public sealed record Developer
{
    public string Name     => "Roberto Gallardo";
    public string Role     => "Arquitecto de Software · Full Stack .NET";
    public string Location => "Guadalajara, Jalisco 🇲🇽";
    public string DotNet   => ".NET Framework 2.0 → .NET 10 / 11";
    public string[] Stack  => ["C#", "VB.NET", "Rust", "Python",
                               "Vue", "React", "Next.js",
                               "MongoDB", "SQL Server"];
    public string[] Loves  => ["Clean Architecture", "SOLID",
                               "CI/CD", "Agentes de IA y MCP"];
    public string Motto    => "Que funcione es lo mínimo. "
                            + "Que se entienda es la meta.";
}
```

</td>
<td width="45%" valign="top">

Leo el código legacy antes de juzgarlo, y luego lo dejo mejor de como lo encontré.

🏗️ **De día:** servicios backend en **.NET** para una empresa global de logística.<br/><br/>
🔄 **Todas las generaciones de .NET:** desde **.NET Framework 2.0 / 3.5 / 4.x**, pasando por .NET Core, hasta **.NET 5 → 10 y 11** — y las migraciones entre ellas.<br/><br/>
🤖 **4 años con IA:** de ChatGPT a Codex, Claude Code y Antigravity — con revisión y límites, no a ciegas.<br/><br/>
🌙 **De noche:** agentes de IA que hacen trabajo real — editan mis videos, los publican y hasta hacen mi declaración.<br/><br/>
🔨 **Ahora mismo:** construyendo [**RepoRinse**](https://github.com/robgallardof/RepoRinse) y [**Rekora**](https://github.com/robgallardof/rekora), herramientas en Rust para agentes de IA.<br/><br/>
💬 **Platícame de:** C#, migraciones de .NET, diseño de software, MongoDB, Vue/Next.js, DevOps y agentes de IA.

</td>
</tr>
</table>

<p align="center"><img src="assets/divider.svg" alt="" width="80%" /></p>

<a id="construyendo"></a>
<p align="center"><img src="assets/sections/es-02.svg" alt="02 · Lo que estoy construyendo" width="100%" /></p>

Herramientas para que los agentes de IA trabajen de forma segura y con memoria — locales, sin telemetría y en Rust.

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>🧼 <a href="https://github.com/robgallardof/RepoRinse">RepoRinse</a></h3>
      <p>CLI local y determinista en Rust que mantiene limpios los repos: quita trailers de coautoría de IA (respeta a las personas), espacios e Unicode invisible, y añade límites para Claude Code, Codex, Gemini CLI y Cursor.</p>
      <p><code>Rust</code> <code>Git hooks</code> <code>Límites para agentes</code></p>
      <p>
        <img src="https://img.shields.io/github/languages/top/robgallardof/RepoRinse?style=flat-square&color=6D28D9" alt="Top language" />
        <img src="https://img.shields.io/github/stars/robgallardof/RepoRinse?label=estrellas&style=flat-square&color=F59E0B&logo=github" alt="Stars" />
        <img src="https://img.shields.io/github/last-commit/robgallardof/RepoRinse?label=%C3%BAltimo%20commit&style=flat-square&color=0EA5E9" alt="Last commit" />
      </p>
    </td>
    <td width="50%" valign="top">
      <h3>🧠 <a href="https://github.com/robgallardof/rekora">Rekora</a></h3>
      <p>Memoria local y verificable para agentes de IA de código: decisiones, restricciones y problemas conocidos con sus fuentes, marcados como desactualizados si cambia un archivo citado, servidos por CLI y servidor MCP dentro de un presupuesto de tokens. En desarrollo temprano.</p>
      <p><code>Rust</code> <code>SQLite</code> <code>MCP</code> <code>Etapa temprana</code></p>
      <p>
        <img src="https://img.shields.io/github/languages/top/robgallardof/rekora?style=flat-square&color=6D28D9" alt="Top language" />
        <img src="https://img.shields.io/github/stars/robgallardof/rekora?label=estrellas&style=flat-square&color=F59E0B&logo=github" alt="Stars" />
        <img src="https://img.shields.io/github/last-commit/robgallardof/rekora?label=%C3%BAltimo%20commit&style=flat-square&color=0EA5E9" alt="Last commit" />
      </p>
    </td>
  </tr>
</table>

```sh
reporinse install --provider git --all --yes            # limpia cada mensaje de commit
reporinse install --provider claude,codex --all --yes   # límites para tus agentes
```

<p align="center"><img src="assets/divider.svg" alt="" width="80%" /></p>

<a id="herramientas"></a>
<p align="center"><img src="assets/sections/es-03.svg" alt="03 · Mi caja de herramientas de IA" width="100%" /></p>

Construyo **servidores MCP, skills y hooks** para que los agentes hagan trabajo real en mi equipo — en local y
conmigo al mando.

<table>
  <tr>
    <th width="33%">🔌 Servidores MCP</th>
    <th width="33%">🎯 Skills y roles de agentes</th>
    <th width="33%">🧠 Memoria y límites</th>
  </tr>
  <tr>
    <td valign="top">
      <a href="https://github.com/robgallardof/davinci-resolve-mcp">davinci-resolve-mcp</a> — edición de video<br/>
      <a href="https://github.com/robgallardof/social-publisher-mcp">social-publisher-mcp</a> — publicación<br/>
      <a href="https://github.com/robgallardof/declaracion">declaracion</a> — impuestos en México
    </td>
    <td valign="top">
      Productor, editores, colorista y QA para Resolve<br/>
      Copywriter, estratega y analista para redes<br/>
      Contador y auditor para declaraciones
    </td>
    <td valign="top">
      <a href="https://github.com/robgallardof/rekora">Rekora</a> — memoria verificable para agentes<br/>
      <a href="https://github.com/robgallardof/RepoRinse">RepoRinse</a> — hooks de Git y agentes<br/>
      Guardas de comandos y rutas para agentes<br/>
      Un historial de commits solo con personas
    </td>
  </tr>
</table>

<p align="center">
  <img src="https://img.shields.io/badge/MCP-servidores-8A2BE2?style=for-the-badge&logo=anthropic&logoColor=white" alt="MCP" />
  <img src="https://img.shields.io/badge/Claude%20Code-skills%20y%20plugins-D97757?style=for-the-badge&logo=anthropic&logoColor=white" alt="Skills y plugins de Claude Code" />
  <img src="https://img.shields.io/badge/Ollama-RAG%20local-000000?style=for-the-badge&logo=ollama&logoColor=white" alt="Ollama" />
</p>

<p align="center"><img src="assets/divider.svg" alt="" width="80%" /></p>

<a id="tecnologias"></a>
<p align="center"><img src="assets/sections/es-04.svg" alt="04 · Tecnologías" width="100%" /></p>

<p align="center">
  <b>Backend</b><br/><br/>
  <img src="https://skillicons.dev/icons?i=cs,dotnet,rust,python,kotlin,nodejs&theme=dark" alt="Backend" />
</p>
<p align="center">
  <b>Frontend</b><br/><br/>
  <img src="https://skillicons.dev/icons?i=ts,js,react,nextjs,vue,tailwind,html,css&theme=dark" alt="Frontend" />
</p>
<p align="center">
  <b>Datos · Nube · DevOps</b><br/><br/>
  <img src="https://skillicons.dev/icons?i=mongodb,mysql,azure,docker,kubernetes,nginx,cloudflare,linux&theme=dark" alt="Datos, nube y DevOps" />
</p>
<p align="center">
  <b>Herramientas</b><br/><br/>
  <img src="https://skillicons.dev/icons?i=git,github,githubactions,vscode,visualstudio,postman,powershell,bash&theme=dark" alt="Herramientas" />
</p>

<p align="center">
  <b>IA y agentes</b><br/><br/>
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
  <b>Contenido y automatización</b><br/><br/>
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

<a id="proyectos"></a>
<p align="center"><img src="assets/sections/es-05.svg" alt="05 · Proyectos destacados" width="100%" /></p>

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>🎬 <a href="https://github.com/robgallardof/davinci-resolve-mcp">davinci-resolve-mcp</a></h3>
      <p>Edita en DaVinci Resolve hablando con una IA que trabaja como productor: cortes verticales y horizontales, movimiento que no corta caras, subtítulos con diseño, música a tiempo y revisión antes de cada render.</p>
      <p><code>MCP</code> <code>Python</code> <code>Video</code></p>
      <p>
        <img src="https://img.shields.io/github/languages/top/robgallardof/davinci-resolve-mcp?style=flat-square&color=6D28D9" alt="Top language" />
        <img src="https://img.shields.io/github/stars/robgallardof/davinci-resolve-mcp?label=estrellas&style=flat-square&color=F59E0B&logo=github" alt="Stars" />
        <img src="https://img.shields.io/github/last-commit/robgallardof/davinci-resolve-mcp?label=%C3%BAltimo%20commit&style=flat-square&color=0EA5E9" alt="Last commit" />
      </p>
    </td>
    <td width="50%" valign="top">
      <h3>📲 <a href="https://github.com/robgallardof/social-publisher-mcp">social-publisher-mcp</a></h3>
      <p>Un community manager con IA para video corto, como servidor MCP: ve tus videos, escribe el copy de cada red, programa a las 05:00 y te dice qué funcionó.</p>
      <p><code>MCP</code> <code>Python</code> <code>Redes</code></p>
      <p>
        <img src="https://img.shields.io/github/languages/top/robgallardof/social-publisher-mcp?style=flat-square&color=6D28D9" alt="Top language" />
        <img src="https://img.shields.io/github/stars/robgallardof/social-publisher-mcp?label=estrellas&style=flat-square&color=F59E0B&logo=github" alt="Stars" />
        <img src="https://img.shields.io/github/last-commit/robgallardof/social-publisher-mcp?label=%C3%BAltimo%20commit&style=flat-square&color=0EA5E9" alt="Last commit" />
      </p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>🧾 <a href="https://github.com/robgallardof/declaracion">declaracion</a></h3>
      <p>Tu asistente de impuestos personales en México dentro de tu agente de IA: lee CFDI, calcula ISR e IVA (RESICO) y te guía al declarar. Tus datos se quedan en tu PC.</p>
      <p><code>MCP</code> <code>Python</code> <code>SAT</code></p>
      <p>
        <img src="https://img.shields.io/github/languages/top/robgallardof/declaracion?style=flat-square&color=6D28D9" alt="Top language" />
        <img src="https://img.shields.io/github/stars/robgallardof/declaracion?label=estrellas&style=flat-square&color=F59E0B&logo=github" alt="Stars" />
        <img src="https://img.shields.io/github/last-commit/robgallardof/declaracion?label=%C3%BAltimo%20commit&style=flat-square&color=0EA5E9" alt="Last commit" />
      </p>
    </td>
    <td width="50%" valign="top">
      <h3>📚 <a href="https://github.com/robgallardof/wikdoc">wikdoc</a></h3>
      <p>Convierte cualquier carpeta de código en una base de conocimiento local con la que puedes chatear — embeddings + RAG con Ollama, nada sale de tu equipo.</p>
      <p><code>Python</code> <code>Ollama</code> <code>RAG</code></p>
      <p>
        <img src="https://img.shields.io/github/languages/top/robgallardof/wikdoc?style=flat-square&color=6D28D9" alt="Top language" />
        <img src="https://img.shields.io/github/stars/robgallardof/wikdoc?label=estrellas&style=flat-square&color=F59E0B&logo=github" alt="Stars" />
        <img src="https://img.shields.io/github/last-commit/robgallardof/wikdoc?label=%C3%BAltimo%20commit&style=flat-square&color=0EA5E9" alt="Last commit" />
      </p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>🤖 <a href="https://github.com/robgallardof/wallybot">wallybot</a></h3>
      <p>Centro autoalojado de análisis de mercado, cartera y trading asistido por IA: propuestas explicadas, tu aprobación y controles de riesgo.</p>
      <p><code>Python</code> <code>Autoalojado</code></p>
      <p>
        <img src="https://img.shields.io/github/languages/top/robgallardof/wallybot?style=flat-square&color=6D28D9" alt="Top language" />
        <img src="https://img.shields.io/github/stars/robgallardof/wallybot?label=estrellas&style=flat-square&color=F59E0B&logo=github" alt="Stars" />
        <img src="https://img.shields.io/github/last-commit/robgallardof/wallybot?label=%C3%BAltimo%20commit&style=flat-square&color=0EA5E9" alt="Last commit" />
      </p>
    </td>
    <td width="50%" valign="top">
      <h3>🦊 <a href="https://github.com/robgallardof/multig">multig</a></h3>
      <p>Administra muchos perfiles de navegador persistentes y aislados con Camoufox, un panel en Next.js y un backend en Python.</p>
      <p><code>Next.js</code> <code>Python</code> <code>Camoufox</code></p>
      <p>
        <img src="https://img.shields.io/github/languages/top/robgallardof/multig?style=flat-square&color=6D28D9" alt="Top language" />
        <img src="https://img.shields.io/github/stars/robgallardof/multig?label=estrellas&style=flat-square&color=F59E0B&logo=github" alt="Stars" />
        <img src="https://img.shields.io/github/last-commit/robgallardof/multig?label=%C3%BAltimo%20commit&style=flat-square&color=0EA5E9" alt="Last commit" />
      </p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>⚡ <a href="https://github.com/robgallardof/arquest">arquest</a></h3>
      <p>Cliente HTTP estilo Postman/Thunder con Next.js App Router: interfaz pensada en modo oscuro y PWA instalable con caché offline.</p>
      <p><code>Next.js</code> <code>PWA</code></p>
      <p>
        <img src="https://img.shields.io/github/languages/top/robgallardof/arquest?style=flat-square&color=6D28D9" alt="Top language" />
        <img src="https://img.shields.io/github/stars/robgallardof/arquest?label=estrellas&style=flat-square&color=F59E0B&logo=github" alt="Stars" />
        <img src="https://img.shields.io/github/last-commit/robgallardof/arquest?label=%C3%BAltimo%20commit&style=flat-square&color=0EA5E9" alt="Last commit" />
      </p>
    </td>
    <td width="50%" valign="top">
      <h3>🎮 <a href="https://github.com/robgallardof/ruxtbot">ruxtbot</a></h3>
      <p>Bot de Discord para Rust: planeación de raids con imágenes, crafteo, servidores en vivo, búsqueda de jugadores y alertas de BattleMetrics, en inglés y español.</p>
      <p><code>Discord</code> <code>Bot</code></p>
      <p>
        <img src="https://img.shields.io/github/languages/top/robgallardof/ruxtbot?style=flat-square&color=6D28D9" alt="Top language" />
        <img src="https://img.shields.io/github/stars/robgallardof/ruxtbot?label=estrellas&style=flat-square&color=F59E0B&logo=github" alt="Stars" />
        <img src="https://img.shields.io/github/last-commit/robgallardof/ruxtbot?label=%C3%BAltimo%20commit&style=flat-square&color=0EA5E9" alt="Last commit" />
      </p>
    </td>
  </tr>
</table>

<p align="center">
  <a href="https://github.com/robgallardof?tab=repositories"><b>➜ Ver todos los repositorios</b></a>
</p>

<p align="center"><img src="assets/divider.svg" alt="" width="80%" /></p>

<a id="experiencia"></a>
<p align="center"><img src="assets/sections/es-06.svg" alt="06 · Experiencia y formación" width="100%" /></p>

| Sector | Puesto | Periodo |
|---|---|---|
| 🚚 **Logística global** | Desarrollador Full Stack .NET — .NET 8, Clean Architecture, CQRS, Docker/K8s, Azure DevOps, Vue, MongoDB | 2023 – actual |
| 🏦 **Banca** | Desarrollador .NET — .NET Framework → .NET 5, biometría, GCM → FCM, Kotlin | 2022 |
| 📡 **Telecomunicaciones** | Desarrollador — VB.NET / C# / Java, SQL Server, SSRS, Mulesoft | 2019 – 2022 |

### 🎓 Formación

| | Grado | Institución |
|---|---|---|
| 🎓 | **Maestría en Arquitectura de Software** | Università degli Studi Guglielmo Marconi · cursada en AICAD Business School |
| 🎓 | **Licenciatura en Sistemas Computacionales Administrativos** | Universidad Veracruzana |

<p align="center"><img src="assets/divider.svg" alt="" width="80%" /></p>

<a id="estadisticas"></a>
<p align="center"><img src="assets/sections/es-07.svg" alt="07 · Estadísticas de GitHub" width="100%" /></p>

<p align="center">
  <img src="./profile-summary-card-output/tokyonight/0-profile-details.svg" alt="Detalles del perfil" width="100%" />
</p>
<p align="center">
  <img src="./profile-summary-card-output/tokyonight/1-repos-per-language.svg" alt="Repos por lenguaje" height="180" />
  <img src="./profile-summary-card-output/tokyonight/2-most-commit-language.svg" alt="Lenguaje con más commits" height="180" />
</p>
<p align="center">
  <img src="./profile-summary-card-output/tokyonight/3-stats.svg" alt="Estadísticas" height="180" />
  <img src="./profile-summary-card-output/tokyonight/4-productive-time.svg" alt="Horario productivo" height="180" />
</p>
<p align="center">
  <a href="https://git.io/streak-stats"><img src="https://streak-stats.demolab.com?user=robgallardof&theme=tokyonight&hide_border=true&date_format=j%20M%5B%20Y%5D&locale=es" alt="Racha en GitHub" /></a>
</p>

### 🐍 Serpiente de contribuciones

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/robgallardof/robgallardof/output/github-snake-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/robgallardof/robgallardof/output/github-snake.svg" />
    <img alt="Serpiente de contribuciones" src="https://raw.githubusercontent.com/robgallardof/robgallardof/output/github-snake.svg" />
  </picture>
</p>

<p align="center"><img src="assets/divider.svg" alt="" width="80%" /></p>

<p align="center">
  <i>“Primero que funcione, luego que esté bien, luego que sea rápido.” — Kent Beck</i>
</p>

<img src="assets/footer-es.svg" alt="Gracias por pasar" width="100%" />
