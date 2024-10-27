import scrapy
import cloudscraper
import pandas as pd

class ZonapropSpider(scrapy.Spider):
    name = "zonaprop_free"



    def start_requests(self):
             
        yield scrapy.Request(url="https://www.zonaprop.com.ar/casas-ph-terrenos-venta-capital-federal-mas-400-m2-menos-300000-dolar.html", 
                             callback=self.parse,
                             meta={
                                "playwright": True,
}                    
                             )
        
        

    def parse(self, response):
        self.log(f'Got response from {response.url}')
        data = {
                'Dirección' : response.css('.postingAddress::text').getall(),
                'Precio' : response.css('.Price-sc-12dh9kl-3::text').getall(),
                
                }
        
        df = pd.DataFrame(data)

        # Save to CSV
        df.to_csv(r'..\Exports\zonaprop_data.csv', index=False, encoding='utf-8')

        self.log('Data saved to zonaprop_data.csv')



