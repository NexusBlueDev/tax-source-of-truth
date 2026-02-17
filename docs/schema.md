# Database Schema Design

## Table: source_registry

Purpose:
Stores authoritative public sources for tax and accounting law.
This table defines WHAT sources are trusted, not the content itself.

One row = one authoritative source endpoint.

### Columns

id
- Type: UUID
- Notes: Primary key

jurisdiction_level
- Type: text
- Allowed values: federal, state, city
- Example: state

jurisdiction_name
- Type: text
- Example: Ohio, Florida, Columbus OH

authority_type
- Type: text
- Description: What kind of authority this source represents
- Examples:
  - statute
  - regulation
  - tax_agency_guidance
  - administrative_bulletin
  - municipal_ordinance
  - rate_table

source_name
- Type: text
- Description: Human-readable name
- Example: Ohio Department of Taxation

source_url
- Type: text
- Description: Canonical public URL

official_status
- Type: text
- Allowed values: primary, secondary, convenience
- Description:
  primary = official publisher
  secondary = official agency summary
  convenience = hosted code library or aggregator

coverage_notes
- Type: text
- Description: What this source covers

update_method
- Type: text
- Examples: rss, manual, page_monitor, api, email

active
- Type: boolean
- Description: Whether this source is currently monitored

created_at
- Type: timestamp
- Notes: Set by database

updated_at
- Type: timestamp
- Notes: Set by database

### Deferred (Not in v1)
- Source content ingestion
- Versioned documents
- Effective date tracking
- Change detection
