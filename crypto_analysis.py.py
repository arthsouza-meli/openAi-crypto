from typing import List
from datetime import datetime, timedelta
from collections import defaultdict
from database import Crypto, News, Trend, HistoryPrice, db_session
from services import CryptoNewsService, PriceService, SentimentAnalysisService


def remove_duplicates(items: List) -> List:
    return list(set(items))


def update_trends(crypto: Crypto, news: List[News]):
    for n in news:
        for tag in n.tags:
            trend = Trend.query.filter_by(crypto_id=crypto.id, tag=tag).first()
            if not trend:
                trend = Trend(crypto_id=crypto.id, tag=tag, count=0)
            trend.count += 1
            db_session.add(trend)


def analyze_sentiment(news: News) -> str:
    sentiment = SentimentAnalysisService.analyze(news.title)
    return 'UP' if sentiment > 0 else 'DOWN'


def update_crypto(crypto: Crypto, news: List[News]):
    sentiment_counts = defaultdict(int)
    for n in news:
        sentiment = analyze_sentiment(n)
        sentiment_counts[sentiment] += 1
        n.analyzed = True
        n.sentiment = sentiment
        db_session.add(n)
    crypto.sentiment = max(sentiment_counts, key=sentiment_counts.get)
    db_session.add(crypto)


def update_historical_price(crypto: Crypto):
    historical_prices = PriceService.get_historical_prices(crypto.symbol, 30)
    for price in historical_prices:
        history_price = HistoryPrice(crypto_id=crypto.id, date=price['date'], price=price['price'])
        db_session.add(history_price)


def main():
    cryptos = Crypto.query.all()
    for crypto in cryptos:
        crypto_news_service = CryptoNewsService(crypto.symbol)
        news = crypto_news_service.get_unanalyzed_news()
        if news:
            update_crypto(crypto, news)
            update_trends(crypto, news)
            update_historical_price(crypto)
    db_session.commit()


if __name__ == '__main__':
    main()
