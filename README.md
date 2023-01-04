# Hydra-Sklearn Preprocessing Pipelines

![Sklearn-Hydra](https://user-images.githubusercontent.com/17675462/131835987-63b1d347-5a05-49c8-af36-d1a393d87c22.png)


This repository accompanying the blog post:

[Creating Configurable Data Pre-Processing Pipelines by Combining Hydra and Sklearn](https://medium.com/beyondminds/creating-configurable-data-pre-processing-pipelines-by-combining-hydra-and-sklearn-812065c9ab64) - by Eli Simhayev & Benjamin Bodner

## Update 4.1.23
When I wrote this blog-post, the stable version of Hydra was 1.1
Now, the stable version is 1.3, so note that this code work with Hydra 1.1 :) 

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
