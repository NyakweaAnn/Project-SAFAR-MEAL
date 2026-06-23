# Phase 3: Relational Data Modeling & Advanced Power BI Analytics

To support real-time, evidence-based decision-making for Project SAFAR, I engineered a relational database using a Star Schema framework. This design completely moves away from flat-file architectures, decoupling core baseline data from transactional programmatic activities while maintaining absolute referential integrity.

## 1. Star Schema Data Architecture
The database model separates tracking into specific dimension tables (descriptive attributes) and fact tables (measurable data points).

                     [Dim_Locations]                 [Dim_Calendar]
                            │                               │
                            └───┐                       ┌───┘
                                ▼                       ▼
                         [Fact_Household_Registration] (Core Fact)
                                ▲                       ▲
                            ┌───┘                       └───┐
                            │                               │
                     [Fact_Cash_Transfers]         [Fact_Nutrition_PDM]
                     (M-PESA API Logs)             (Recurring Monitoring)

### Table Schemas & Key Mapping
* **`Dim_Calendar` (Dimension):** Continuous dates, reporting months, and operational quarters.
    * *Primary Key:* `Date_Key`
* **`Dim_Locations` (Dimension):** Maps geographical boundaries specific to Turkana County.
    * *Primary Key:* `Location_Key` (Attributes: Sub_County, Village_Name, IDP_Camp_Status).
* **`Fact_Household_Registration` (Core Fact Table):** Ingests initial baseline indicators.
    * *Primary Key:* `Household_ID`
    * *Foreign Keys:* `Location_Key`, `Date_Key`
    * *Attributes:* Head_Age, Head_Gender, Household_Size, Baseline_FCS, Baseline_rCSI.
* **`Fact_Cash_Transfers` (Transactional Fact Table):** Logs individual financial remittances.
    * *Primary Key:* `Transaction_ID`
    * *Foreign Keys:* `Household_ID`, `Date_Key`
    * *Attributes:* Amount_USD, Transfer_Status (Success/Failed), Disbursement_Round.
* **`Fact_Nutrition_PDM` (Operational Fact Table):** Captures recurring performance tracking data.
    * *Primary Key:* `Log_ID`
    * *Foreign Keys:* `Household_ID`, `Date_Key`
    * *Attributes:* MUAC_Status (Red/Yellow/Green), PDM_FCS_Score, PDM_rCSI_Score, CARM_Feedback_ID.

---

## 🧠 2. Production-Grade DAX Measure Repository
Rather than counting on default card metrics, the Power BI layer evaluates program success against targets using custom Data Analysis Expressions (DAX).

### A. Cumulative Beneficiary Cash Reach (Output 1.2 Target)
Evaluates unique household reach performance dynamically against the 8,500 target boundary.
```dax
HH_Reach_Achievement_Pct = 
DIVIDE(
    DISTINCTCOUNT(Fact_Household_Registration[Household_ID]),
    8500,
    0
)
Acceptable_FCS_Prevalence = 
DIVIDE(
    CALCULATE(
        DISTINCTCOUNT(Fact_Nutrition_PDM[Household_ID]),
        Fact_Nutrition_PDM[PDM_FCS_Score] > 35
    ),
    DISTINCTCOUNT(Fact_Nutrition_PDM[Household_ID]),
    0
)
Operational_Risk_Flag = 
VAR MeanrCSI = AVERAGE(Fact_Nutrition_PDM[PDM_rCSI_Score])
VAR FailureRate = DIVIDE(
    CALCULATE(COUNT(Fact_Cash_Transfers[Transaction_ID]), Fact_Cash_Transfers[Transfer_Status] = "Failed"),
    COUNT(Fact_Cash_Transfers[Transaction_ID]),
    0
)
RETURN
IF(
    MeanrCSI > 20 || FailureRate > 0.05,
    "⚠️ CRITICAL ACTION REQUIRED: High Coping Spikes or Payment Failures Detected",
    "✅ Operational Performance Stable"
)
