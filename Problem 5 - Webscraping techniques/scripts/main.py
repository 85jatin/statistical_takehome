import scraping_core_data_extraction_logic_company_specif_2c0b45e6 as scraper
import output_formatting_and_storage_script_1ca38083 as formatter

# Main function to orchestrate the web scraping process
def main():
    # Step 1: Extract firmographic information from selected companies
    firmographic_data = scraper.extract_firmographic_data()
    
    # Step 2: Format and store the extracted data
    formatter.format_and_store_data(firmographic_data)

if __name__ == "__main__":
    main()