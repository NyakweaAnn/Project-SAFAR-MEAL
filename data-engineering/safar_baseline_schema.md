# SAFAR Baseline & Registration Form Schema (XLSForm Architecture)

This document contains the production-ready XLSForm architecture designed for Project SAFAR's mobile data collection workflow in Turkana County. It is fully compatible with KoboToolbox, ODK, and SurveyCTO.

## 1. Survey Sheet Logic
This sheet defines the prompt variables, strict ranges, data types, and live field validation checks enforced directly on the data collector's mobile device.

| type | name | label | hint / constraint rules | relevant (Skip Logic) |
| :--- | :--- | :--- | :--- | :--- |
| **start** | start | | Automated metadata capture | |
| **today** | today | | Automated date capture | |
| **deviceid** | device_id | | Captures mobile hardware ID | |
| **select_one sub_counties** | sub_county | Select the Sub-County: | Mandatory field select list | |
| **text** | location | Specific Village/IDP Camp Name: | Text input | |
| **integer** | hh_size | Total number of household members: | Constraint: `. > 0 and . < 25`<br>Message: *Error: Realistic family size must be between 1 and 24.* | |
| **integer** | head_age | Age of the Head of Household: | Constraint: `. >= 12 and . <= 100`<br>Message: *Error: Age parameter must be between 12 and 100.* | |
| **select_one gender** | head_gender | Gender of Head of Household: | Select list options | |
| **text** | mpesa_num | Registered M-PESA Phone Number: | Constraint: `regex(., '^0(7\|1)\d{8}$')`<br>Message: *Error: Invalid format. Must be a valid 10-digit Safaricom mobile money number.* | |
| **note** | child_head_alert | **⚠️ CRITICAL PROTECTION ALERT** | Display message: *This household is flagged as child-headed (<18 years). Prioritize immediately for direct protection and nutritional assessment tracking.* | `${head_age} < 18` |

## 2. Choices Sheet Logic
This sheet maps the internal alphanumeric database codes to clean, human-readable choices on the enumerator interface.

| list_name | name | label |
| :--- | :--- | :--- |
| **sub_counties** | lodwar | Lodwar |
| **sub_counties** | kakuma | Kakuma |
| **sub_counties** | lokichoggio | Lokichoggio |
| **gender** | female | Female |
| **gender** | male | Male |
| **gender** | non_binary | Prefer not to say |

## 3. Engineering Implementation Notes
* **Mobile Money Verification Vector:** The constraint `regex(., '^0(7|1)\d{8}$')` acts as a syntax gatekeeper. It blocks incomplete or mis-typed phone numbers at the point of registration, reducing transactional remittance bounces over the automated M-PESA API pipeline by preventing bad data ingestion.
* **Dynamic Vulnerability Trigger:** The protection note utilizes conditional dependency logic (`${head_age} < 18`). By checking the age value in real-time, it flashes an unskippable protection alert on-screen to ensure field team compliance without requiring supervisor intervention.
