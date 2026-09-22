# Real Estate Price Prediction & Production MLOps Pipeline

An end-to-end, production-grade machine learning system designed to predict residential property values using the **Ames Housing Dataset**. This repository avoids notebook-centric design by implementing a modular, production-ready MLOps framework.

## 🏗️ System Architecture

*   **Orchestration:** ZenML manages individual steps from raw ingest to final scoring.
*   **Experiment Tracking:** MLflow tracks models, hyperparameters (`learning_rate`, `max_depth`), and evaluation metrics.
*   **Model Core:** Gradient-boosted ensembles (**XGBoost**, **LightGBM**, **CatBoost**) evaluated via RMSE and R².
*   **Serving Engine:** FastAPI wraps the best-performing model behind a validated REST API endpoint.
*   **CI/CD:** GitHub Actions triggers lint checks and automated unit tests (`pytest`) on every commit.
*   **Observability:** Evidently AI generates automatic data and target drift reports to alert for model decay.

---

> I will be working on this project for coming few days.
