# 1. Load the dataset
from preswald import connect, get_df, query, table, text, plotly
import plotly.express as px

connect()
df = get_df("bird_migration_data") 

# 2. Query or manipulate the data
sql = """
SELECT * FROM bird_migration_data
WHERE "Migration_Success" = 'Successful'
AND "Wind_Speed_kmph" IS NOT NULL
AND "Max_Altitude_m" IS NOT NULL
"""
filtered_df = query(sql, "bird_migration_data")

# 3. Build an interactive UI
text("🦅 Bird Migration Explorer")
table(filtered_df, title="Successful Bird Migrations")

# 4. Create a visualization
fig = px.scatter(
    filtered_df,
    x="Wind_Speed_kmph",
    y="Max_Altitude_m",
    color="Temperature_C",
    hover_data=["Species", "Flight_Distance_km"],
    title="Wind Speed vs Max Altitude in Successful Bird Migrations"
)
plotly(fig)
