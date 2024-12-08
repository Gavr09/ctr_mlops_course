from dataclasses import dataclass, field


@dataclass()
class TrainingParams:
    model_type: str = field(default="RandomForestClassifier")
    random_state: int = field(default=42)

    # RF params
    depth: int = field(default=5)
    n_estimators: int = field(default=50)
    learning_rate: float = field(default=0.05)
    bagging_temperature: float = field(default=0.2)

    # LR params
    # solver: str = field(default="lbfgs")
    # reg_coeff: float = field(default=1.0)
