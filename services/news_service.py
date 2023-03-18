from datetime import timedelta, datetime
import requests
from app.models import News


class NewsService:
    def __init__(self):
        self.crypto_keywords = {
            'bitcoin': ['bitcoin', 'btc'],
            'ethereum': ['ethereum', 'eth'],
            # Adicione outras criptomoedas e suas palavras-chave aqui
        }

    def populate_database_if_empty(self, db):
        session = db.Session()
        news_count = session.query(News).count()
        if news_count == 0:
            news_data = self.fetch_news_from_last_hours(90)
            self.insert_news_into_database(news_data, db)

    def fetch_news_from_last_hours(self,hours):
        query = "cryptocurrency"
        to_date = datetime.utcnow()
        from_date = to_date - timedelta(hours=hours)
        from_date_str = from_date.strftime("%Y-%m-%dT%H:%M:%SZ")
        to_date_str = to_date.strftime("%Y-%m-%dT%H:%M:%SZ")

        url = f"https://newsapi.org/v2/everything?q={query}&from={from_date_str}&to={to_date_str}&sortBy=popularity&apiKey={app.config.GOOGLE_NEWS_API_KEY}"
        response = requests.get(url)
        response_json = response.json()

        if response.status_code != 200:
            raise Exception(f"Google News API request failed with status code {response.status_code}")

        return response_json["articles"]

    def insert_news_into_database(self, news_data, db):
        session = db.Session()

        for article in news_data:
            title = article["title"]
            description = article["description"]
            published_at = article["publishedAt"]
            url = article["url"]
                    cryptocurrency = self
            if not article.analyzed:
                sentiment_score = self.analyze_sentiment(f"{article.title}. {article.description}")
                trend = self.calculate_trend(cryptocurrency, sentiment_score)

                # Insere os dados na tabela Trends
                trends = Trends(timestamp=article.published_at, trend=trend, sentiment_score=sentiment_score)
                db.session.add(trends)

                # Obtem o preço da criptomoeda no horário da consulta
                price = self.price_service.fetch_crypto_price(cryptocurrency, article.published_at)

                # Insere os dados na tabela HistoricalPrices
                historical_prices = HistoricalPrices(cryptocurrency=cryptocurrency, date=article.published_at, open=price,
                                                     high=price, low=price, close=price, volume=0)
                db.session.add(historical_prices)

                # Marca a notícia como analisada
                article.analyzed = True
