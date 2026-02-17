# Seed Plan: source_registry (v1)

Purpose:
Define the initial authoritative sources to be inserted into the
source_registry table. No inserts occur until this plan is reviewed
and committed.

## Principles
- Public, authoritative URLs only
- Prefer primary sources
- One row per authoritative endpoint
- No convenience duplicates in v1 unless required

## Federal (United States)

1. Internal Revenue Bulletin
- jurisdiction_level: federal
- jurisdiction_name: United States
- authority_type: administrative_bulletin
- source_name: Internal Revenue Bulletin
- source_url: https://www.irs.gov/internal-revenue-bulletins
- official_status: primary
- coverage_notes: Authoritative IRS vehicle for rulings, procedures, and Treasury Decisions
- update_method: manual

2. Code of Federal Regulations (Title 26)
- jurisdiction_level: federal
- jurisdiction_name: United States
- authority_type: regulation
- source_name: Code of Federal Regulations - Title 26
- source_url: https://www.ecfr.gov/current/title-26
- official_status: primary
- coverage_notes: Treasury regulations governing federal tax law
- update_method: manual

## Ohio (State)

3. Ohio Revised Code
- jurisdiction_level: state
- jurisdiction_name: Ohio
- authority_type: statute
- source_name: Ohio Revised Code
- source_url: https://codes.ohio.gov/ohio-revised-code
- official_status: primary
- coverage_notes: Statutory law for the State of Ohio
- update_method: manual

4. Ohio Administrative Code
- jurisdiction_level: state
- jurisdiction_name: Ohio
- authority_type: regulation
- source_name: Ohio Administrative Code
- source_url: https://codes.ohio.gov/ohio-administrative-code
- official_status: primary
- coverage_notes: Administrative rules for Ohio agencies
- update_method: manual

5. Ohio Department of Taxation
- jurisdiction_level: state
- jurisdiction_name: Ohio
- authority_type: tax_agency_guidance
- source_name: Ohio Department of Taxation
- source_url: https://tax.ohio.gov/home
- official_status: primary
- coverage_notes: Official guidance, forms, notices, and tax administration for Ohio
- update_method: manual

## Florida (State)

6. Florida Statutes
- jurisdiction_level: state
- jurisdiction_name: Florida
- authority_type: statute
- source_name: Florida Statutes
- source_url: https://www.leg.state.fl.us/STATUTES/
- official_status: primary
- coverage_notes: Statutory law for the State of Florida
- update_method: manual

7. Florida Administrative Code
- jurisdiction_level: state
- jurisdiction_name: Florida
- authority_type: regulation
- source_name: Florida Administrative Code
- source_url: https://www.flrules.org/
- official_status: primary
- coverage_notes: Administrative rules and register for Florida agencies
- update_method: manual

8. Florida Department of Revenue
- jurisdiction_level: state
- jurisdiction_name: Florida
- authority_type: tax_agency_guidance
- source_name: Florida Department of Revenue
- source_url: https://floridarevenue.com/
- official_status: primary
- coverage_notes: Official guidance, forms, notices, and tax administration for Florida
- update_method: manual

## Ohio (City)

9. Columbus Income Tax Division
- jurisdiction_level: city
- jurisdiction_name: Columbus OH
- authority_type: tax_agency_guidance
- source_name: City of Columbus Income Tax Division
- source_url: https://www.columbus.gov/Government/City-Auditor/Income-Tax-Division
- official_status: primary
- coverage_notes: Official municipal income tax administration, forms, rules, and guidance for Columbus, Ohio
- update_method: manual

10. Dayton Income Tax Division
- jurisdiction_level: city
- jurisdiction_name: Dayton OH
- authority_type: tax_agency_guidance
- source_name: City of Dayton Income Tax Division
- source_url: https://www.daytonohio.gov/262/Tax-Information-Forms
- official_status: primary
- coverage_notes: Official municipal income tax administration, forms, rules, and guidance for Dayton, Ohio
- update_method: manual

11. Cincinnati Income Tax Division
- jurisdiction_level: city
- jurisdiction_name: Cincinnati OH
- authority_type: tax_agency_guidance
- source_name: City of Cincinnati Income Tax Division
- source_url: https://www.cincinnati-oh.gov/finance/income-taxes/
- official_status: primary
- coverage_notes: Official municipal income tax administration, forms, rules, and guidance for Cincinnati, Ohio
- update_method: manual

12. Regional Income Tax Agency (RITA)
- jurisdiction_level: state
- jurisdiction_name: Ohio
- authority_type: tax_agency_guidance
- source_name: Regional Income Tax Agency (RITA)
- source_url: https://www.ritaohio.com/
- official_status: primary
- coverage_notes: Official municipal income tax administrator for participating Ohio municipalities, including filing, payments, ordinances, and guidance
- update_method: manual

