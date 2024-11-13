# Project Plan

## Title
<!-- Give your project a short title. -->
Assessing the Impact of Flash Floods on Local Economy and Housing Prices

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
1. How do frequent flash floods affect local housing prices and business revenues?

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
The main aim of the project is to analyze the impact flash floods might have on housing prices. The aim is to compare the housing prices before and after the flash floods with the prices during the period when the flash floods occured. This could be further extended to compare the revenue of local businesses and analyze the effects that the flash floods might have on them. We will thus be able to see the varying impact that flash floods have on different businesses

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: CyberFlood1104
* Metadata URL: https://zenodo.org/records/7545697
* Data URL: https://zenodo.org/records/7545697/files/cyberFlood_1104.csv?download=1
* Data Type: CSV

Web-based crowdsourced flood database, developed at the University of Oklahoma (Wan et al., 2014). 203 flood events from 1998 to 2008 are retrieved with the latest version.

Data attributes: ID, Year, Month, Day, Duration, fatality, Severity, Cause, Lat, Long, Country Code, Continent Code

### Datasource2: HPIData
* Metadata URL: https://www.fhfa.gov/sites/default/files/2023-09/HPI_specifications.xls
* Data URL: https://www.fhfa.gov/hpi/download/monthly/hpi_master.csv
* Data Type: CSV

The FHFA House Price Index (HPI) is a broad measure of the movement of single-family house prices.  The HPI is a weighted, repeat-sales index, meaning that it measures average price changes in repeat sales or refinancings on the same properties. This information is obtained by reviewing repeat mortgage transactions on single-family properties whose mortgages have been purchased or securitized by Fannie Mae or Freddie Mac since January 1975. The data covers dates from 1991 till the present date

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Preprocessing the dataset [#2][i1]

[i1]: https://github.com/harshvardhan10/made-ws-25/issues/2
