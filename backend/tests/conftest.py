import os


# Set before application modules import Settings. Tests must not depend on a
# developer's .env file or initialise real provider credentials.
os.environ.update(
    {
        "APP_NAME": "LeadPilot Test",
        "ENVIRONMENT": "test",
        "API_V1_PREFIX": "/api/v1",
        "DEBUG": "false",
        "HOST": "127.0.0.1",
        "PORT": "8000",
        "FIRECRAWL_API_KEY": "test-firecrawl-key",
        "GEMINI_API_KEY": "test-gemini-key",
        "DATABASE_URL": "postgresql+psycopg://test:test@localhost:5432/test",
        "SUPABASE_URL": "https://example.supabase.co",
        "SUPABASE_ANON_KEY": "test-supabase-key",
    }
)
