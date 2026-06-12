# RASA-CONTAINER (#178): THIN variant layer — all deps live in rasa-base.
# Build context = this service directory. The RUN bakes the trained model at
# build time; the entrypoint's content-hash cache makes it a no-op at boot.
FROM healthidpuaeacr.azurecr.io/rasa-base:v1.0.0
COPY --chown=1001:1001 . /app/bot/
RUN train-if-needed.sh
