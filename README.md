# Hydra-Sklearn Processing Pipelines

This repository accompanying the blog post:

[Creating Configurable Data Pre-Processing Pipelines by Combining Hydra and Sklearn]() - by Eli Simhayev & Benjamin Bodner

# Running Different Pipelines
Run:

```commandline
python main.py preprocessing_pipeline=decision_tree
```

to execute the `decision_tree` preprocessing pipeline. You might also run other pipelines (from `configs/preprocessing_pipeline`)
by just changing:

```commandline
python main.py preprocessing_pipeline=<your-pipeline>
```

Adding new pipelines can be easily done using a yaml configuration.

You might add another configurations: which model to use, which visualizations, etc. Learn more here: [Hydra — A fresh look at configuration for machine learning projects](https://medium.com/pytorch/hydra-a-fresh-look-at-configuration-for-machine-learning-projects-50583186b710)


#### We hope this will help you to better organize your data preprocessing pipelines 🙂