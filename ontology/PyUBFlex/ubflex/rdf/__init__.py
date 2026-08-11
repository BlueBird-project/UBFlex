from rdflib import URIRef

UBFLEX_MARKET_BASE = "https://ubflex.bluebird.eu/market/"

EURPerMWH = URIRef(value="EURPerMegawattHour", base=UBFLEX_MARKET_BASE)
PLNPerMWH = URIRef(value="PLNPerMegawattHour", base=UBFLEX_MARKET_BASE)


DAYAHEAD_MARKET_TYPE = URIRef(value="DayAheadMarket", base=UBFLEX_MARKET_BASE)
INTRADAY_MARKET_TYPE = URIRef(value="IntradayMarket", base=UBFLEX_MARKET_BASE)
