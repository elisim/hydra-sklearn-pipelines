import logging

import hydra
import numpy as np
from omegaconf import DictConfig

import utils

log = logging.getLogger(__name__)


@hydra.main(config_path="configs/", config_name="config.yaml")
def main(config: DictConfig):
    # Pretty print config using Rich library
    if config.get("print_config"):
        utils.print_config(config, resolve=True)

    log.info("Instantiating preprocessing pipeline")
    preprocessing_pipeline = hydra.utils.instantiate(
        config.preprocessing_pipeline, _recursive_=False
    )
    print(type(preprocessing_pipeline))

    preprocessing_pipeline.fit(np.random.random((10, 100)))


if __name__ == "__main__":
    main()
