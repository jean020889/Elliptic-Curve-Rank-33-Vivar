# Numerical Investigation of Rank 33 Candidates in Elliptic Curves over $\mathbb{Q}$

![Mathematics](https://img.shields.io/badge/Field-Arithmetic%20Geometry-blue)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0004--1739--7945-brightgreen)](https://orcid.org/0009-0004-1739-7945)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 📌 Overview
This repository documents a high-precision numerical investigation into an elliptic curve over the rational field $\mathbb{Q}$ that exhibits strong evidence of a **rank of 33**. This study provides a detailed numerical analysis of 33 candidate generators identified through ultra-high-precision computation, offering a significant dataset for the study of the **Birch and Swinnerton-Dyer (BSD) Conjecture**.

The research focuses on the transition between numerical stability and algebraic verification, conducted by **Jean Carlos Vivar Benítez**.

## 🏆 Numerical Evidence & Findings
- **Candidate Rank:** 33 (Numerical)
- **Curve Equation:** $y^2 = x^3 + 852223x + 1847$
- **Audit Precision:** 2000+ decimal places (using mpmath).
- **Residual Analysis:** Points show a residual error near $10^{-1992}$ or absolute zero under 2000 dps.
- **Current Status:** These points are identified as **high-precision numerical candidates**. Further algebraic reconstruction into exact rational fractions ($p/q$) is required for formal database integration (LMFDB).

## 🧪 Methodology
The **Vivar Precision Audit** utilizes a specialized numerical protocol to isolate points in the arithmetic landscape where the $L$-series exhibits extreme vanishing stability. By bypassing standard search limitations of lower-precision software, this method identifies candidate generators that reside beyond the typical search depth of automated solvers like `ellrank`.

## 📂 Repository Structure
- `/src/`: Python scripts for high-precision numerical auditing (`vivar_precision_audit_r33.py`).
- `/data/`: Full set of 33 candidate generators in JSON format (2000 dps).
- `/docs/`: Technical notes on numerical stability and residual error analysis.

## 📝 Citation & Contribution
If you are a researcher with access to high-performance LLL (Lenstra-Lenstra-Lovász) lattice reduction algorithms or symbolic computation environments (Magma/SageMath) and wish to contribute to the exact rational reconstruction of these points, please contact the author.

**Vivar, J. C. (2026).** *Numerical Investigation of Rank 33 Candidates in Elliptic Curves over Q*. Independent Research. Huaquillas, Ecuador.  
**ORCID:** [https://orcid.org/0009-0004-1739-7945](https://orcid.org/0009-0004-1739-7945)

## 👤 Contact
**Jean Carlos Vivar Benítez** Independent Researcher  
Huaquillas, El Oro, Ecuador  
ORCID: [0009-0004-1739-7945](https://orcid.org/0009-0004-1739-7945)

---
*Disclaimer: This repository presents numerical evidence and high-precision candidates. Algebraic verification of exact rational coordinates is an ongoing part of this open research.*
