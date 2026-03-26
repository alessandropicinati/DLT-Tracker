# DLT-Tracker
A personal intelligence layer for tracking developments across regulatory, market, and quantitative dimensions of the blockchain &amp; finance space.
# 🏦 Digital Assets & RegTech Intelligence Tracker

## Overview
This repository serves as a centralized, automated knowledge graph tracking the intersection of traditional finance, blockchain technology, and global regulatory frameworks.

As the industry matures (e.g., European MiCA implementation, institutional tokenization), the gap between raw news and actionable strategy must be bridged. This project automates that synthesis.

## How It Works
The repository is powered by a custom **Streamlit Application** hooked into the **Gemini LLM API**. 

1. **Ingestion:** Raw articles, whitepapers, or regulatory updates are fed into the app.
2. **Synthesis:** The AI acts as a strategic analyst, extracting data into three strict pillars:
   - *Regulatory Perspective*
   - *Quantitative/Technical Developments*
   - *Strategic Positioning for Market Players*
3. **Storage:** Insights are downloaded as standardized Markdown files and stored in this repository for easy search and reference.

## Repository Structure
- `/scripts`: Contains the `app.py` Streamlit application code.
- `/summaries`: Contains the synthesized markdown reports of all tracked articles.
