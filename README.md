# Cross-Chain Protocols Analysis Project

## Overview

This project is a **Python-based analytical tool for collecting, parsing, and analyzing cross-chain protocol data across multiple blockchain networks**.  
It focuses on retrieving raw protocol data from external APIs, normalizing it, and producing structured outputs suitable for further quantitative or comparative analysis.

The repository is designed as a **modular data-collection and processing pipeline**, separating concerns such as API access, configuration, parsing, and execution logic.

---

## Project Objectives

- Retrieve cross-chain and protocol-level data from public APIs
- Analyze protocol activity across different blockchain networks
- Normalize heterogeneous API responses into a consistent format
- Enable scalable, concurrent data collection
- Provide a foundation for further cross-chain research and metrics analysis

---

## Repository Structure

- main.py # Entry point – orchestrates data collection & analysis
- API.py # API request logic and data retrieval functions
- parse.py # Parsing and normalization of API responses
- Configuration.py # Global configuration and constants
- tokens.py # Blockchain and token metadata
- Custom_decorator.py # Utility decorators (e.g., execution timing)
- requierments.txt # Python dependencies


---

## How the System Works

### 1. Configuration Layer
`Configuration.py` defines:
- API endpoints
- Headers and SSL behavior
- Global runtime parameters

This allows easy modification without touching core logic.

---

### 2. Data Retrieval Layer
`API.py` handles:
- HTTP requests to external data providers
- SSL handling and request reliability
- Structured response collection

All API interaction is centralized to keep networking logic isolated.

---

### 3. Parsing & Normalization
`parse.py`:
- Processes raw API responses
- Extracts relevant protocol and chain data
- Converts heterogeneous inputs into structured Python objects or tabular formats

This makes downstream analysis consistent and reliable.

---

### 4. Token & Chain Metadata
`tokens.py`:
- Stores blockchain identifiers
- Maps chain IDs to human-readable names
- Acts as a reference layer for cross-chain comparisons

---

### 5. Execution & Concurrency
`main.py`:
- Coordinates the full pipeline
- Uses concurrent execution to improve performance
- Queues and processes multiple chains/protocols efficiently
- Outputs processed data for analysis

---

### 6. Performance Utilities
`Custom_decorator.py`:
- Provides a timing decorator
- Measures execution time for data retrieval
- Useful for benchmarking and optimization

---

## Installation

### Prerequisites
- Python 3.9+
- Virtual environment recommended

### Setup

```bash
git clone https://github.com/khashayarkeivanfar/Cross-chain-Protocols-Analysis-Project-Khashayar-keivanfar.git
cd Cross-chain-Protocols-Analysis-Project-Khashayar-keivanfar
pip install -r requierments.txt
```
## Usage

Run the main pipeline:

```bash
python main.py
```
## The script will:

- Fetch cross-chain protocol data
- Parse and normalize results
- Output structured analytical data (console/log-based by default)
## Dependencies
### Key libraries include:
- requests – HTTP communication
- pandas, numpy – data handling
- matplotlib – optional visualization
- concurrent.futures – parallel execution
- urllib3 – SSL and connection handling
Full list available in requierments.txt.
## Use Cases
- Cross-chain protocol comparison
- Blockchain ecosystem research
- Academic or exploratory blockchain analytics
- Foundation for DeFi risk or liquidity analysis
- Data ingestion layer for dashboards or ML models
## Limitations & Notes
- This project focuses on data collection and normalization, not trading or execution
- API availability and rate limits depend on external providers
Output formatting can be extended for CSV/JSON export or database ingestion
## Future Improvements
- Persistent storage (PostgreSQL / TimescaleDB)
- Formal output schemas (JSON/CSV)
- Visualization dashboards
- Protocol risk metrics and scoring
- API abstraction layer for multiple providers
## Author
Khashayar Keivanfar
