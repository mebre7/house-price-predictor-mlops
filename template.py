import os
from pathlib import Path

project_name = "house_price_predictor_mlops"

list_of_files = [
    # root
    f"{project_name}/__init__.py",
    # components
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",  
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_training.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pushing.py",
    # utils
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    # configuration
    f"{project_name}/configuration/__init__.py",
    # constants
    f"{project_name}/constants/__init__.py",
    # exception
    f"{project_name}/exception/__init__.py",
    # logger
    f"{project_name}/logger/__init__.py",
    # logs
    f"{project_name}/logs/__init__.py",
    # entity
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    # monitoring
    f"{project_name}/monitoring/__init__.py",
    f"{project_name}/monitoring/logger.py",
    f"{project_name}/monitoring/drift_detector.py",
    # pipeline
    f"{project_name}/pipline/__init__.py",
    f"{project_name}/pipline/training_pipeline.py",
    f"{project_name}/pipline/prediction_pipeline.py",

    f"tests/__init__.py",
    f"tests/test_data.py",
    f"tests/test_model.py",
    f"tests/test_api.py"

    f"app.py",
    f".dockerignore",
    f"Dockerfile",
    f"demo.py",
    f"setup.py",
    f"config/model.yaml",
    f"config/schema.yaml",
]
for filepath in list_of_files:
    path = Path(filepath)
    filedir, filename = os.path.split(path)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(path)) or (os.path.getsize(path) == 0):
        with open(path, "w") as f:
            pass
    else:
        print(f"{filename} already exists")
