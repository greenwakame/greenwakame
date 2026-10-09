---
title: Wan Animate 2 — Apple Silicon Lab
slug: wan-animate2-apple-silicon-lab
description: A field report on local Wan Animate 2 experiments with Apple M5, ComfyUI, and MPS.
description_ja: 32GBのMacBook Airでローカル動画生成を検証。動画を書き出せたことと、キャラクターの一貫性に残る課題を記録しました。
date: 2026-10-10
category: Local AI / Research
kind: website
tags:
  - Wan Animate 2
  - Apple Silicon
  - ComfyUI
  - MPS
thumbnail: /assets/works/wan-animate2-apple-silicon-lab/poster.webp
thumbnail_alt: Dark field-report poster reading Wan Animate 2 on Apple Silicon and Technical PASS ≠ Visual SUCCESS, with an abstract execution diagram.
media:
  type: image
  src: /assets/works/wan-animate2-apple-silicon-lab/poster.webp
  alt: Editorial poster for the field report, with green and cyan typography and a schematic of the completed load, sample, decode, and save path.
listed: true
featured: false
status: Published
site_url: https://greenwakame.github.io/wan-animate2-apple-silicon-lab/
github: https://github.com/greenwakame/wan-animate2-apple-silicon-lab
related_links:
  - label: Read the full field report
    url: https://greenwakame.github.io/wan-animate2-apple-silicon-lab/
---

## Overview

A local AI video field report that keeps execution success and visual quality separate. The specialist site holds the experiment records, limitations, and public workflow templates.

<p lang="ja">動画を書き出せたことと、使える品質であることを分けて記録した実験です。</p>

## Tested environment

Apple M5 MacBook Air with **32 GiB unified memory**, running **ComfyUI / MPS**. The test envelope was **512 × 512, 17 frames, 8 fps** on this single machine.

## Technical outcome

**V2 and V3 completed loading, sampling, VAE decoding, and video saving: Technical PASS.** Approximate observed runtimes were **02:55:37** for V2 and **02:23:41** for V3. Each is an individual run, not an average or a performance benchmark.

## Visual limitations

**Technical PASS ≠ Visual SUCCESS.** V2 retained identity relatively well through F11, then collapsed from F12 onward, with severe breakdown at F17. V3 reduced subject oversizing but **worsened identity**, with face/hood collapse from F1 and reduced motion readability.

V4 passed historical workflow static/UI validation but remains **UNRUN**. The public template received static checks only; there is no V4 generated result or evidence of improvement.

## Key observations

- Post-run swap was **17.76 GiB (V2)** and **17.69 GiB (V3)**. These are system observations after execution, **not peak memory** or exclusive model usage.
- Six identified model files total **31.758971 GiB of storage**; this is not a runtime RAM requirement.
- Two short completed runs do not establish production readiness, stable identity, or broad Apple Silicon performance.

## Read the full field report

[Explore the field report](https://greenwakame.github.io/wan-animate2-apple-silicon-lab/) for the evidence, caveats, and experiment lineage. [Browse the GitHub source](https://github.com/greenwakame/wan-animate2-apple-silicon-lab) for the public records and templates.

<p lang="ja">詳しい検証記録は専門サイトでご覧ください。非公開のキャラクター画像・動画は使用していません。</p>
