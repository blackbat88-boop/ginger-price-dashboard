# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

生姜价格监控中心 (Ginger Price Dashboard) - A static dashboard for tracking fresh ginger prices across major production regions in China.

## Architecture

**Single-file architecture**: All HTML, CSS, and JavaScript reside in `index.html`. No build process or dependencies required.

**Tech stack**:
- Pure HTML + CSS + JavaScript (ES6+)
- Custom SVG charts (no external charting libraries)
- CSS variables for theming (OKX-style dark theme)
- Responsive design with mobile-first breakpoints
- GitHub Pages deployment

**Data flow**:
1. Price data generated client-side via `generatePriceData()` / `generateForecastData()`
2. SVG charts rendered dynamically via `drawChart()` / `drawForecastChart()`
3. User preferences (price alerts) stored in `localStorage`

**Key components**:
- 30-day price trend chart (national average + Yishui region)
- Price forecast charts (7/30/90 day predictions)
- Regional price comparison tabs (Shandong, Hebei, Yunnan, Other)
- Price alert system with localStorage persistence

## Commands

**Development**:
- Open `index.html` directly in browser for local development

**Deployment**:
- Deployed to GitHub Pages at `https://<username>.github.io/ginger-price-dashboard`

## Data Sources

Prices sourced from:
- 我的钢铁网 (Mysteel)
- 中姜网 (China Ginger Network)

Data represents mainstream transaction prices from production regions.
