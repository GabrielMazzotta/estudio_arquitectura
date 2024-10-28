import scrapy
import cloudscraper
import pandas as pd
from estudio_arquitectura.items import EstudioArquitecturaItem



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
      
               
        links = response.css('div.CardContainer-sc-1tt2vbg-5 ::attr(data-to-posting)').getall()
        for link in links[:3]:
            link_url = response.urljoin(link)
            yield response.follow(url=link_url, 
                                  callback=self.parse_article,
                                  meta={
                                      "playwright": True
                                        }                    
                                  )
            
    def parse_article(self, response):
        self.log(f'Got article from {response.url}')
        
        selector_to_wait = '.static-map-container img::attr(style)'
        
        
        
        articles_items = EstudioArquitecturaItem()
        
        articles_items['titulo'] = response.css('.title-property::text').get()
        articles_items['link'] = response.url
        articles_items['direccion_barrio_ciudad'] = response.css('.section-location-property h4::text').get()
        #articles_items['direccion'] = response.css(selector_to_wait).get()
        articles_items['descripcion'] = response.css('.article-section .section-description::text').getall()
        articles_items['link'] = response.url
        
        yield articles_items



