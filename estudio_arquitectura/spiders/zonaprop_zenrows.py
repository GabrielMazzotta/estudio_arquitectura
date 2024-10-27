import scrapy
from urllib.parse import urlencode

# function to generate the ZenRows API URL with the required parameters
def get_zenrows_api_url(url, api_key):
    params = {
        "url": url,            
        "js_render": "true",      
        "premium_proxy": "true"   
    }

    api_url = f"https://api.zenrows.com/v1/?apikey={api_key}&{urlencode(params)}"
    return api_url

class ZonapropSpider(scrapy.Spider):
    name = "zonaprop_zenrows"

    def start_requests(self):
        urls = ["https://www.zonaprop.com.ar/casas-ph-terrenos-venta-capital-federal-mas-400-m2-menos-300000-dolar.html"]
        api_key = "e8201d4fead35ca9e3e1aa58a8f9917ca4df4ab2" 
        for url in urls:
            # make a request using the ZenRows API
            api_url = get_zenrows_api_url(url, api_key)
            yield scrapy.Request(api_url, callback=self.parse)
        
        
        """
        yield scrapy.Request(url="https://www.zonaprop.com.ar/casas-ph-terrenos-venta-capital-federal-mas-400-m2-menos-300000-dolar.html", 
                             callback=self.parse,
                             meta={"playwright": True}                    
                             )
        """
        

    def parse(self, response):
        self.log(f'Got response from {response.url}')
            
