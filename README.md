Jellyfish Search(JS) optimizer is metaheuristic algorithm that is motivated by search behaivor of jellyfish involves their following the ocean current, their motions inside a jellyfish swarm(active motions and passive motions).In this project we use Jellyfish search optimizer algorithm to optimize Random Forest parameter that observe F-measure Score.We also compare the output of the F-measure with Jellyfish optimizer and without Jellyfish optimizer.

# Jellyfish Pseudo Code:

In general Rule:

1-	Jellyfısh eıther follow the ocean current or move ınsıde the swarm, and a "time control mechanism" governs the switching between these types of movement.

2-	Jellyfish move in the ocean in search of food. They are more attracted to locations where the available quantity of food is greater.

3-	The amount of food found is determined by the location and the objective function associated with it.

![image](https://github.com/zuleyhairmakk/Jellyfish-Search-Optimizer-with-Random-Forest/assets/87870858/75d7abb5-a4e5-4ca3-9977-2b8d0c51d2b0)

# COUNCLISION:

Within the scope of this study, modeling was performed using two different approaches: a Random Forest model adapted with the Jellyfish Optimizer algorithm and a Random Forest model only. To test the two methods, both models were evaluated on the same test data set. The results obtained using the Jellyfish Optimizer algorithm showed that the F-measure value on the test dataset was 0.94. On the other hand, it was observed that this value was 0.98 when only the Random Forest model was used.
These results indicate that the performance of the Jellyfish Optimizer algorithm is lower than using the Random Forest model in this particular scenario. Comparing the performance of different optimization algorithms and models can provide important insights into model selection and hyperparameter tuning. In conclusion, this study highlights the need to carefully evaluate various methods to achieve the best performance in the context of the data set and problem. It is recommended to obtain more comprehensive results by testing different optimization algorithms and model combinations in future studies.


