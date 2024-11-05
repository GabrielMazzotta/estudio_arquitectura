

<p><img alt="image" src="img.jpg">

# Web Scraping for Real State Business

This repository performs web scraping on real state investment opportunities from the renowned property site ZonaProp, including CloudFlare detection handling.

### Website

https://www.zonaprop.com.ar/casas-ph-terrenos-venta-capital-federal-mas-400-m2-menos-300000-dolar.html

The following filters have been applied as an example, which can be easily modified:

- City: Capital Federal
- Price: Up to 300,000
- Property type: House, Land, Horizontal Property
- Total square meters: from 400

 

The extracted data is saved in a .JSON file and then processed for the final version in Excel format.

### Performance

452 sites were scraped in 283 seconds.


### Execution

To run the spider, execute in the console: 

*scrapy crawl zonaprop -O zonaprop_data_total.json*

