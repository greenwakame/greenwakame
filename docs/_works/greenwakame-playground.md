---
title: Greenwakame Playground
slug: greenwakame-playground
description: A collection of playable browser games and interactive experiments, starting with Midnight Inspection.
description_ja: ブラウザーで遊べる小さなゲームと実験の作品集。第1作「Midnight Inspection」の技術プロトタイプを公開しています。
date: 2026-10-11
category: Game / Interactive
kind: website
tags:
  - Browser Game
  - TypeScript
  - Three.js
  - Rapier
  - Web Audio
thumbnail: /assets/works/greenwakame-playground/poster.webp
thumbnail_alt: Greenwakame PlaygroundのPS1風作品ジャケットを使用した紹介ポスター。ゲーム実画面ではありません。
media:
  type: image
  src: /assets/works/greenwakame-playground/poster.webp
  alt: PS1風のMidnight Inspectionジャケット全体とPhase 1技術プロトタイプの文字を配置した紹介ポスター
listed: true
featured: false
status: Active
site_url: https://greenwakame.github.io/greenwakame-playground/
github: https://github.com/greenwakame/greenwakame-playground
related_links:
  - label: Playgroundを開く
    url: https://greenwakame.github.io/greenwakame-playground/
  - label: Midnight Inspectionをプレイ
    url: https://greenwakame.github.io/greenwakame-playground/works/midnight-inspection/v0.1.0-phase1/
  - label: GitHubリポジトリ
    url: https://github.com/greenwakame/greenwakame-playground
---

## 概要

GREENWAKAME PLAYGROUNDは、ブラウザーで遊べるゲームやインタラクティブな実験をまとめる独立サイトです。作品紹介から公開ゲームへ進み、操作方法や開発履歴も確認できます。

## 最初の作品：PW / 001 — Midnight Inspection

「Midnight Inspection（深夜巡回）」は、3Dの廊下を中心に探索と音響を検証する**Phase 1の技術プロトタイプ**です。深夜の東棟で3室を巡回し、扉の向こうの返答や異変を確かめて記録します。入口の報告ポストへ戻ると、記録に応じて2種類のエンディングに分かれます。

実装済みの要素：

- 一人称視点の移動、衝突判定、しゃがみ
- ドアの開閉とノック
- 空間音響、遮音、聞き耳
- 異変の発生と調査
- 3室の巡回記録・報告
- 2種類のエンディングと再巡回

昭和の日本家屋を舞台にしたホラーへの発展は将来構想です。**その舞台は現在のPhase 1には実装していません。** 掲載ポスターのPS1風ジャケットは、採用済みの生成AIコンセプトアートを使用しています。ゲーム実画面のスクリーンショットではありません。

## 技術

ゲームはTypeScriptとThree.jsによる3D描画、Rapierによる物理・衝突判定、Web Audio APIによる音声合成と空間音響を組み合わせ、Viteでビルドしています。Playgroundの案内サイトは、作品メタデータとテンプレートからPythonで生成する静的サイトです。

公開ゲームの動作確認対象はmacOS版Google Chromeです。キーボードとマウスを使用し、ヘッドホンを推奨します。WebGL 2とWebAssemblyが利用できる環境が必要です。

## 公開先

[GREENWAKAME PLAYGROUNDを開く](https://greenwakame.github.io/greenwakame-playground/)と、作品一覧・紹介・操作方法を確認できます。

[Midnight Inspection Phase 1をプレイ](https://greenwakame.github.io/greenwakame-playground/works/midnight-inspection/v0.1.0-phase1/)するか、[GitHubリポジトリ](https://github.com/greenwakame/greenwakame-playground)でサイトの構成と公開資料をご覧ください。
