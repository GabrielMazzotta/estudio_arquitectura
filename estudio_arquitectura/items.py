# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EstudioArquitecturaItem(scrapy.Item):
    # define the fields for your item here like:
    direccion_barrio_ciudad = scrapy.Field()
    ciudad = scrapy.Field()
    barrio = scrapy.Field()
    precio = scrapy.Field()
    link = scrapy.Field()
    titulo = scrapy.Field()
    descripcion = scrapy.Field()
    direccion = scrapy.Field()
    mapa_estatico = scrapy.Field()
    metros_totales = scrapy.Field()
