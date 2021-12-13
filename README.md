# Diamond Price Regression

![Alt](/images/diamond.jpeg)

# :warning: About

Predicting a feature is just the beginning of a new entire world, in this case, We are working with diamond features, where we are going to predict the diamond price using other features as carat, cut, color, clarity, etc. In this research, the idea is to try to find which feature is more relevant to predict the diamond price. 

### Database Description 

The data.csv file contains the necessary data to create your models, and is made up of the following columns:

- price: in US dollars [TARGET]
- carat: weight of the diamond
- cut: quality of the cut (Fair, Good, Very Good, Premium, Ideal)
- color: diamond colour, from J (worst) to D (best)
- clarity: a measurement of how clear the diamond is (I1 (worst), SI2, SI1, VS2, VS1, VVS2, VVS1, IF (best))
- x: length in mm
- y: width in mm
- z: depth in mm
- depth: total depth percentage = z / mean(x, y) = 2 * z / (x + y)
- table: width of top of diamond relative to widest point


#### Tools

You can, and should, test different models, parameters, and data preparation. The sklearn documentation will be your best friend:

- [Pre Processing] (https://scikit-learn.org/stable/modules/classes.html#module-sklearn.preprocessing)
- [Supervised Learning] (https://scikit-learn.org/stable/supervised_learning.html)
- [Model Selection] (https://scikit-learn.org/stable/modules/classes.html#module-sklearn.model_selection)

note: The metric used in that competition will be the RMSE.



## :books: Resources 

- [IGS - Measurements](https://www.gemsociety.org/article/diamond-measurements/)
- [The Diamond Pro - Clarity](https://www.diamonds.pro/education/clarity/)
- [The Diamond Pro - Proportions](https://www.diamonds.pro/guides/diamond-proportion/)
- [Loose Diamond - Cuts](https://www.loosediamondsreviews.com/diamondcut.html)
- [Beyond - Colors](https://beyond4cs.com/color/)


## :envelope: Contact

peresrjavier@gmail.com