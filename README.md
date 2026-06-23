# Project SAFAR: Strengthening Food Security & Resilience in Turkana County, Kenya

## 📌 Project Overview
Project SAFAR ("Journey" in Swahili) is an 18-month, $3.2 Million USD climate-resilience and food security initiative implemented by Horizon Relief International (HRI) and funded by the **USAID Bureau for Humanitarian Assistance (BHA)**. The project targets 8,500 conflict-displaced and host community households (approx. 51,000 individuals) across Lodwar, Kakuma, and Lokichoggio sub-counties to mitigate acute food insecurity and protect local livelihoods.

This repository serves as an end-to-end portfolio demonstration of a **BHA-Grade Monitoring, Evaluation, Accountability, and Learning (MEAL)** information management architecture, designed and executed completely independently.

---

## 📁 Portfolio Architecture & Navigation
This project is systematically broken down into four distinct operational directories:

1. **Strategic MEAL Design**: BHA logframe alignment and complex indicator math frameworks (Detailed below).
2. **[Field Data Engineering](./data-engineering/)**: Production-ready XLSForms with mobile phone regex verification and data protection constraints.
3. **[Cloud Survey Deployment Proofs](./Kobotoolbox/)**: Live Enketo web form deployments running inside KoboToolbox with functioning dynamic protection alerts and form validators.
4. **[Relational Data Modeling & Analytics](./analytics/)**: Multi-table Star Schema database specifications and advanced production-grade Power BI DAX measures.
5. **[Accountability & Adaptive Management](./accountability/)**: Closed-loop Community Accountability and Response Mechanisms (CARM) matrices and automated threat-detection pivot scenarios.

---

## 📑 1. Strategic MEAL Design

### BHA-Compliant Performance Indicator Matrix
The project logic maps direct field-level activities to high-level strategic outcomes using USAID/BHA standard metrics.

| Level | Performance Indicator (KPI) | Baseline | Target | Data Source & Frequency |
| :--- | :--- | :--- | :--- | :--- |
| **GOAL** | Prevalence of severe food insecurity (%) | 58% | < 15% | Annual Household Endline Survey (Month 18) |
| **OUTCOME 1** | % Households with **Acceptable FCS** (>35) | 22% | > 80% | Monthly Post-Distribution Monitoring (PDM) |
| **OUTCOME 1** | Mean **rCSI** score | 28.4 | < 10.0 | Monthly Post-Distribution Monitoring (PDM) |
| **OUTCOME 2** | Mean **Yield per Hectare** (Short-cycle crops) | 450 kg | 600 kg | Seasonal Post-Harvest Survey (Months 12 & 18) |
| **OUTPUT 1.1** | Cumulative cash transferred via M-PESA (USD) | \$0 | \$1.84M | Automated M-PESA API Transaction Logs (Monthly) |
| **OUTPUT 1.2** | Number of unique households reached with cash | 0 | 8,500 | Registration Database (Monthly) |
| **OUTPUT 2.1** | Number of farmers receiving seed & tool kits | 0 | 2,000 | Real-time Field Distribution Log / ODK App |

### Indicator Mathematical Formulations
To ensure high-level technical precision, field metrics are calculated utilizing standard international formulas:

*   **Food Consumption Score (FCS):** Calculates dietary diversity over a 7-day recall period using weighted nutritional values:
    $$\text{FCS} = (D_{\text{Cereals}} \times 2) + (D_{\text{Pulses}} \times 3) + (D_{\text{Vegetables}} \times 1) + (D_{\text{Fruit}} \times 1) + (D_{\text{Meat/Fish}} \times 4) + (D_{\text{Dairy}} \times 4) + (D_{\text{Sugar}} \times 0.5) + (D_{\text{Oil}} \times 0.5)$$
    *Thresholds: 0-21 (Poor), 21.5-35 (Borderline), >35 (Acceptable).*

*   **Reduced Coping Strategies Index (rCSI):** Tracks the frequency and behavioral severity of negative coping mechanisms:
    $$\text{rCSI} = (D_{\text{Less Preferred Food}} \times 1) + (D_{\text{Borrow Food / Help}} \times 2) + (D_{\text{Limit Portion Sizes}} \times 1) + (D_{\text{Restrict Adult Intake for Kids}} \times 3) + (D_{\text{Reduce Number of Meals}} \times 1)$$

---

## 🛠️ Core System Tools Used
* **Data Collection Platforms:** KoboToolbox / ODK / SurveyCTO (XLSForm Architecture)
* **Data Engineering Pipelines:** Python (Pandas & NumPy for data cleansing and Statistical Disclosure Control masking)
* **Business Intelligence Layer:** Power BI Desktop (Advanced DAX modeling and Star Schema architecture layout)
