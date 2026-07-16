from tavily import TavilyClient
import os

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

response = client.search(
    query="OpenAI CEO",
    search_depth="advanced",
    max_results=5,
)

print(response)