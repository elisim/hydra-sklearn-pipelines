# Hydra-Sklearn Processing Pipelines

![Sklearn-Hydra](https://user-images.githubusercontent.com/17675462/131835987-63b1d347-5a05-49c8-af36-d1a393d87c22.png)


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
Hydra also supports [Tab completion](https://hydra.cc/docs/tutorials/basic/running_your_app/tab_completion/) to complete config.


# Adding New Pipelines
Adding new pipelines can be easily done using a yaml configuration in `configs/preprocessing_pipeline`.
You might add another configurations: which model to use, which visualizations, etc. - learn more here: [Hydra — A fresh look at configuration for machine learning projects](https://medium.com/pytorch/hydra-a-fresh-look-at-configuration-for-machine-learning-projects-50583186b710)


#### We hope this will help you to better organize your data preprocessing pipelines 🙂
