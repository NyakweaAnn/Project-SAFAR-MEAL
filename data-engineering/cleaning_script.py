"""
Project SAFAR: Automated ETL & Statistical Disclosure Control (SDC) Pipeline
Author: Nyakwea The Analyst
Context: USAID/BHA Emergency Food Security & Livelihoods Response (Turkana County, Kenya)
"""

import pandas as pd
import numpy as np

def run_safar_pipeline():
    print("=========================================================================")
    print("🚀 INITIALIZING PROJECT SAFAR INGESTION & DATA ENGINEERING PIPELINE")
    print("=========================================================================\n")
    
    # 1. EXTRACT: Simulate raw API data download from KoboToolbox/SurveyCTO endpoints
    raw_field_data = {
        'submission_id': [2001, 2002, 2003, 2004],
        'sub_county': ['lodwar', 'kakuma', 'lokichoggio', 'lodwar'],
        'beneficiary_name': ['Amina Ibrahim', 'John Lokol', 'Ekai Emoni', 'Mary Kasi'],
        'mpesa_num': ['0712345678', '0723456789', '0114567890', '0798765432'],
        'head_age': [34, 15, 42, 61],  # Household 2002 represents an under-18 child-headed case
        'cereals_d': [7, 2, 5, 1],
        'pulses_d': [5, 1, 3, 0],
        'veg_d': [4, 0, 2, 1],
        'fruit_d': [2, 0, 1, 0],
        'meat_fish_d': [3, 0, 1, 0],
        'dairy_d': [5, 0, 0, 0],
        'sugar_d': [6, 2, 3, 1],
        'oil_d': [7, 1, 4, 2]
    }
    
    df = pd.DataFrame(raw_field_data)
    print("✔️ Step 1: Raw data stream successfully ingested from server.")
    
    # 2. TRANSFORM: Compute USAID/BHA Food Consumption Score (FCS)
    # Applying universal category scalar weights
    df['FCS'] = (
        (df['cereals_d'] * 2) + 
        (df['pulses_d'] * 3) + 
        (df['veg_d'] * 1) + 
        (df['fruit_d'] * 1) + 
        (df['meat_fish_d'] * 4) + 
        (df['dairy_d'] * 4) + 
        (df['sugar_d'] * 0.5) + 
        (df['oil_d'] * 0.5)
    )
    
    # Segment food security categories using standardized thresholds
    fcs_bins = [df['FCS'] <= 21, (df['FCS'] > 21) & (df['FCS'] <= 35), df['FCS'] > 35]
    fcs_labels = ['Poor', 'Borderline', 'Acceptable']
    df['FCS_Profile'] = np.select(fcs_bins, fcs_labels, default='Undefined')
    print("✔️ Step 2: Complex mathematical calculations (FCS) completed automatically.")
    
    # 3. TRANSFORM: Protection Mechanism & Operational Alert Generation
    # Dynamically tracking child-headed households via code logic
    df['protection_risk'] = np.where(df['head_age'] < 18, 'HIGH_RISK_CHILD_HEADED', 'Standard')
    print("✔️ Step 3: Vulnerability monitoring alerts programmatically calculated.")
    
    # 4. RESPONSIBLE DATA MANAGEMENT: Statistical Disclosure Control (SDC) Implementation
    # To protect vulnerable conflict-displaced households from target identification leaks,
    # full names are stripped completely and phone routing sequences are structurally masked.
    df['beneficiary_name'] = '[REDACTED_PROTECTION_COMPLIANT]'
    df['mpesa_num'] = df['mpesa_num'].apply(lambda x: f"XXXX-XX-{x[-4:]}")
    print("✔️ Step 4: SDC protocols applied. PII elements masked successfully.")
    
    # 5. LOAD: Structural serialization for Star Schema Database formatting
    analytical_dim = ['submission_id', 'sub_county', 'FCS', 'FCS_Profile', 'protection_risk', 'mpesa_num']
    df_clean = df[analytical_dim]
    print("✔️ Step 5: Cleaned output columns processed into storage array variables.\n")
    
    print("=========================================================================")
    print("📊 FINAL SANITIZED DATA OUTFLOW (Ready for Power BI Modeling)")
    print("=========================================================================")
    print(df_clean.to_string(index=False))
    print("=========================================================================\n")
    
    return df_clean

if __name__ == "__main__":
    run_safar_pipeline()
