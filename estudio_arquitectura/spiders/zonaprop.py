import scrapy

class ZonapropSpider(scrapy.Spider):
    name = "zonaprop"

    def start_requests(self):
        yield scrapy.Request(url="https://www.zonaprop.com.ar/casas-ph-terrenos-venta-capital-federal-mas-400-m2-menos-300000-dolar.html", 
                             callback=self.parse,
                             meta={"playwright": True}                    
                             )

    def parse(self, response):
        pass
