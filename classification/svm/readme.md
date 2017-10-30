The SVM had to be built from scratch to understand the steps. The already existing SVM's serve as a good reference, but it was not as simple as we had hoped to modify them to fit our needs. So our own was built.

The current version being used is **jeff_linear_svm**

The SVM takes data that is stored in the CSV format, organized as follows:

| Classifier (True/False) | Feature 1 | Feature 2 | ... | Feature N |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| 0  | float  | float  | ...  | float  |
| 1  | float  | float  | ...  | float  |
| 1  | float  | float  | ...  | float  |
| 0  | float  | float  | ...  | float  |
| ...  | ...  | ...  | ...  | ...  |

# Non-Linear SVM (scikit-learn)
## 2-D Example for visualization
### Support vector classifier using RBF kernel
![](/classification/data/images/graph-nl1.PNG?raw=true "Non-linear Separator")

# Linear SVM (TensorFlow)
### Linear Separator
![](/classification/data/images/graph1.PNG?raw=true "Linear Separator")
### Train and Test Accuracies
![](/classification/data/images/graph2.PNG?raw=true "Linear Separator")
### Loss
![](/classification/data/images/graph3.PNG?raw=true "Linear Separator")
