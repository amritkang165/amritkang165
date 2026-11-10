<div align="center">
  <picture>
    <source media="(prefers-reduced-motion: reduce)" srcset="assets/after-hours/amrit-hero-effects.jpg" />
    <img src="assets/after-hours/amrit-hero-animated.svg" width="100%" alt="Amrit Kang / After Hours. Ideas loud. Code louder. A face portrait beside a rear-view JATT KANG shirt photo, with a charcoal background, orange rim lighting and an animated orange frame. Full-stack development, iOS, AI engineering, and open source." />
  </picture>
</div>

<div align="center">

**Open source, open tabs, and one more PR.**

[portfolio ↗](https://amritkang.vercel.app) &nbsp; / &nbsp; [linkedin ↗](https://www.linkedin.com/in/amritkang28/) &nbsp; / &nbsp; [say hello ↗](mailto:amritkang2805@icloud.com)

[open source](#open-source) · [selected builds](#selected-builds) · [the lab](#the-lab) · [track record](#track-record) · [off the clock](#off-the-clock)

</div>

<br>

i'm **amrit**, a computer science student at **BITS Pilani**, based in Bengaluru. i build native apps, backends, and developer tools—and contribute fixes to the open-source projects behind them.

i like the parts that make software dependable: local data, clear failure messages, and tests that catch the bug before someone else does. outside code, i help bring builders into the same room.

| What I build | What I use |
| :--- | :--- |
| Native apps | Swift · SwiftUI · SwiftData · Vision |
| Backends & tools | Python · FastAPI · Go · SQL |
| Web interfaces | TypeScript · React · Next.js |
| Infrastructure & AI integrations | AWS · Docker · LLM APIs · structured outputs |

<br>

<img src="assets/after-hours/signal.svg" width="100%" alt="" />

<a id="open-source"></a>

## 01 / open source

**fix the problem. test the edge cases. follow through on review.**

Selected merged contributions:

| Project | Contribution | Merged PR |
| :--- | :--- | :--- |
| **Flisk** | Added a JSON Schema for `service.json`, with editor guidance, validation, and contract tests for generated manifests. | [#416 ↗](https://github.com/flisk-sh/flisk/pull/416) |
| **Flisk** | Added `flisk open --print` for scripts and SSH sessions, with regression coverage for URL selection and failure cases. | [#3623 ↗](https://github.com/flisk-sh/flisk/pull/3623) |
| **Neo.mjs** | Cancelled pending buffer, debounce, and throttle calls when an instance is destroyed; covered cleanup and wrapper reuse with regression tests. | [#20723 ↗](https://github.com/neomjs/neo/pull/20723) |
| **Flisk** | Added text-width tests covering Unicode, fallback widths, and rounding in documentation helpers. | [#3535 ↗](https://github.com/flisk-sh/flisk/pull/3535) |

also contributed interactive flowcharts, branching simulations, and saved history to **iffy.ai**: [flowcharts + branching ↗](https://github.com/Muneer320/iffy-ai/commit/03c2909bb2b878792cd894aee1f07b66ed28e5f6) · [history + fixes ↗](https://github.com/Muneer320/iffy-ai/commit/dc9e93cb8da958b7140f45c33523343a1c7d251a).

[![Founding Contributor #6 @amritkang165](https://img.shields.io/static/v1?label=%E2%9A%A1%20FOUNDING%20CONTRIBUTOR&message=%236%20of%20100%20%E2%80%A2%20%40amritkang165&color=06b6d4&labelColor=07080f&style=for-the-badge)](https://discord.gg/qMu5Xn8Kaq)
[![White Belt @amritkang165](https://img.shields.io/static/v1?label=FLISK%20WHITE%20BELT&message=8-7%20kyu%20%E2%80%A2%20%40amritkang165&color=e5e7eb&labelColor=07080f&style=for-the-badge)](https://discord.gg/qMu5Xn8Kaq)

<br>

<img src="assets/after-hours/signal.svg" width="100%" alt="" />

<a id="selected-builds"></a>

## 02 / selected builds

### [Clippit ↗](https://github.com/amritkang165/clippit) · clipboard history that stays on your Mac

a native macOS clipboard manager with searchable history, snippets, configurable shortcuts, and on-device OCR. clipboard data stays local, and automated macOS checks cover the project.

`Swift` `SwiftUI` `Vision` · **MIT-licensed · development preview, build from source**

### [MeraWard ↗](https://github.com/amritkang165/meraward) · from a complaint to a tracking record

a civic-reporting demo that turns voice, photos, or text into reviewed complaints and bilingual letters. includes ward lookup, public tracking, and a demo outbox. drafting uses templates by default; Bedrock is optional.

**my part:** team lead, frontend, and ward data pipeline at First Commit. [team contributions ↗](https://github.com/amritkang165/meraward#team-and-contribution)

`React` `MapLibre` `Python` `AWS Lambda` `DynamoDB` `SQS`

### [Placement Week Scheduler ↗](https://github.com/amritkang165/placement-week-scheduler) · keep the schedule working when plans change

a CP-SAT interview scheduler with a coordinator dashboard. it handles student, room, and panel constraints, then replans around disruptions while keeping valid appointments in place. the repository documents its reference dataset, metrics, and test commands.

`Python` `OR-Tools` `FastAPI` `React`

### [Pocki ↗](https://github.com/amritkang165/Pocki) · a payment screenshot becomes an expense

a native iOS finance tracker that uses on-device OCR to prefill expenses from UPI screenshots. review and correct the amount, merchant, and date before saving. parsing and storage stay on the phone.

`Swift` `SwiftUI` `SwiftData` `Vision` · **MIT-licensed**

### [ReGit ↗](https://github.com/amritkang165/ReGit) · version control for research

a team-built workspace for versioned research artifacts, semantic diffs, merge conflicts, and live collaboration.

**my part:** the research workspace frontend, including artifact ingestion, branch management, commit history, diff and conflict views, and collaboration wiring. [contributors ↗](https://github.com/amritkang165/ReGit/blob/main/CONTRIBUTORS.md)

`React` `TypeScript` `Yjs` · project backend: `Python` `FastAPI`

<details>
<summary><b>more experiments ↗</b></summary>

- **[iffy.ai](https://github.com/amritkang165/iffy-ai)** — explorable consequence graphs for “what if?” questions; i built the frontend. `React` `TypeScript`
- **[TintAudit](https://github.com/amritkang165/TintAudit)** — browser-based palette accessibility analysis. `Swift` `WebAssembly`
- **[Gitty](https://github.com/amritkang165/gitty)** — a mobile GitHub explorer with developer tools. `React Native`
- **[exHacker](https://github.com/amritkang165/exHacker)** — a pipeline from problem statement to project plan. `LangGraph` `FastAPI` `Next.js`
- **[WearWise](https://github.com/amritkang165/wearwise)** — a wardrobe manager with outfit suggestions. `Next.js` `Prisma`
- **[Oratio](https://github.com/amritkang165/Oratio)** — voice-enabled debates with transcription and automated judging. `WebSockets` `LLM APIs`
- **[LaunderLens](https://github.com/amritkang165/Launder-Lens)** — an experiment in graph-based transaction analysis. `Node.js`
- **[Gotermi](https://github.com/amritkang165/Gotermi)** — a terminal pet with persistent stats and interactions. `Go`

</details>

<br>

<a id="the-lab"></a>

## 03 / the lab

**JattChat** is my private exploration of on-device conversations: local responses, conversation state, and persistence using Apple's Foundation Models, SwiftUI, and SwiftData.

<details>
<summary><b>JattChat preview · private build, coming soon ↗</b></summary>

<br>

<!-- Public teaser only: no private repository links or unreleased source. -->
<img src="assets/after-hours/jattchat.svg" width="100%" alt="JattChat — your thoughts, your phone. Native on-device AI. Private build, coming soon." />

the interesting constraint is device readiness: making model availability and local state part of the experience, on compatible iPhones with the system model available.

</details>

<br>

<a id="track-record"></a>

## 04 / track record

- **Grabware / SDE & Forward Deployed Engineer Intern** — May 2026–present. hosting, deployment, and infrastructure for production PHP sites; migrated a subset to MERN and tested the integrations.
- **BITS Pilani / B.Sc. Computer Science** — 2025–2029 · CGPA **9.27**.
- **Gradient Rush / top 6** — ReGit, a research version-control system.
- **ProdX @ NAVERA 26 / top 7 finalist** — frontend for iffy.ai.
- **Hack Club / Bengaluru organizer** — Sunbeam, a global initiative spanning 40 cities.
- **Ignite Room / events lead** — venues, volunteers, speakers, and making the room happen.

<br>

<a id="off-the-clock"></a>

## 05 / off the clock

Apple platform deep dives. system design. *Designing Data-Intensive Applications*. community events that start as a group chat and somehow become a real room.

if you're building something useful, strange, or slightly over-engineered, we'll probably get along.

**[send a hello ↗](mailto:amritkang2805@icloud.com)** · **[read my posts ↗](https://dev.to/amritkang165)** · **[AWS Builder profile ↗](https://builder.aws.com/profile/jattkang)**

<br>

<a href="mailto:amritkang2805@icloud.com">
  <img src="assets/after-hours/footer.svg" width="100%" alt="Have a strange idea? Let's build it. Email Amrit Kang." />
</a>
