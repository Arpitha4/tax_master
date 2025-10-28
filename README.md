# Tax Master
Python project to calculate and manage sales tax based on item rate and country.

### Project Structure
  - sales.json → Stores all sales transactions
  - tax_structures.json → Stores tax rule definitions
  - tax_rules_manager.py → Defines and manages tax rules
  - tax_master.py → Main file

### Features
  - Store data in JSON format
  - Simple menu-based console application
  - Apply tax automatically based on rules
  - Manage and update tax structures
  - Add and view sales transactions

### Tax Rules
  - Items above ₹2000 → 10% tax (India only)
  - Items ₹2000 or below → Exempt
  - Customers outside India → Tax exempt

### How to Run
  - Clone the repository
  - Run the project using:
      python tax_master.py
  - Choose options from the on-screen menu
