import os
import subprocess


def test_training_pipeline():
    """
    Verify model training runs successfully
    and creates artifact files.
    """

    subprocess.run(
        ["python", "ml/train_model.py"],
        check=True
    )

    assert os.path.exists("ml/winner_model.pkl")
    assert os.path.exists("ml/score_model.pkl")
