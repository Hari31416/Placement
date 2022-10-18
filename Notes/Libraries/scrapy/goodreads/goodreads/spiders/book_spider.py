import scrapy


class QuotesSpider(scrapy.Spider):
    name = "book"
    start_urls = [
        "https://www.goodreads.com/book/show/60177373-fairy-tale"
    ]

    def parse(self, response):
        details = response.css("#details")
        for detail in details:
            yield {
                "bookFormat": detail.css("span[itemprop='bookFormat']::text").get(),
                "numberOfPages": detail.css("span[itemprop='numberOfPages']::text").get(),
                # "published": detail.css("div.row::text").get(),
            }
        # for quote in response.css("div.quote"):
        #     yield {
        #         "text": quote.css("span.text::text").get(),
        #         "author": quote.css("small.author::text").get(),
        #         "tags": quote.css("div.tags a.tag::text").getall(),
        #     }

        # next_page = response.css("li.next a::attr(href)").get()
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)
