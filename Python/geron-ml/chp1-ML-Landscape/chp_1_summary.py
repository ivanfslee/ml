"""
Machine Learning is about making machines to get 
    better at some task by learning from data,
    instead of having to explicitly code rules.

There are many types of ML systems:
    supervised or not
    batch or online
    instance-based or model-based
    etc.

In an ML project you:
    Gather data in a training set.
    Feed the training set to a learning algorithm.

    If algo is model-based, it tunes some parameters
        to fit the model to the training set.
    
    That is, make good prediction on the training set itself.

    Hopefully, it will be able to make good predictions
        on new cases also.

    If algo is instance-based, it just learns the examples 
        by heart and uses a similarity measure to generalize
        to new instances.

The system will not perform well if your training set
    is too small or if the data is not representative,
    noisy, or polluted with irrelevant features.

    Our model needs to be neither to simple (results in an underfit)
    nor too complex (results in an overfit).

Once you trained a model, you don't want to hope
    it generalizes to new cases. 

    You want to evaluate it and fine-tune it if necessary.

"""