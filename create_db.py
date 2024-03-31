import lancedb # embedded in your app, no servers to manage!
import pandas as pd
import pyarrow as pa

uri = "data/sample-lancedb"
db = lancedb.connect(uri)

# LanceDb offers both a synchronous and an asynchronous client.  There are still a
# few operations that are only supported by the synchronous client (e.g. embedding
# functions, full text search) but both APIs should soon be equivalent

# In this guide we will give examples of both clients.  In other guides we will
# typically only provide examples with one client or the other.
# uri = "data/sample-lancedb"
# async_db = await lancedb.connect_async(uri)

# Persist your embeddings, metadata, text, images, video, audio & more
db = lancedb.connect("./data/my_db")
table = db.open_table("my_table")

# Production-ready, scalable vector search with optional SQL filters
query = table.search([0.1, 0.3, 0.2])\
            .where("item != 'item foo'")\
            .limit(2)\
            .to_df()
