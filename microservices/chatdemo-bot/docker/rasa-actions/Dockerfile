# RASA-CONTAINER (#178): THIN variant layer for the actions server.
# Same base, "actions" mode (rasa run actions --actions actions --port 5055).
FROM healthidpuaeacr.azurecr.io/rasa-base:v1.0.0
COPY --chown=1001:1001 . /app/bot/
CMD ["actions"]
