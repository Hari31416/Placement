# PyStock

## Objects

### Stock

An object to represent a stock. Should have the following attributes:

- ticker
- data
- start_date
- end_date
- frequency
- columns
- loaded
- Returns9
- alpha (Only in Portfolio object)
- beta (Only in Portfolio object)

### Portfolio

An object to represent a collection of stocks with a benchmark. Should have the following attributes:

- stocks
- benchmark

### CAPM

An object to represent the Capital Asset Pricing Model. Should have the following attributes:

- portfolio (Portfolio object)
- weights
