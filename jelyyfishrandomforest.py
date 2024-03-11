# -*- coding: utf-8 -*-
"""JelyyfishRf.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10LiBurNytIMYHJJMiZamVsVF-o9HwKdH
"""



import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score

def initialize_population(npop, param_range):
    return np.random.uniform(param_range[0], param_range[1], size=(npop, 2))

def jellyfish_algorithm(npop, max_iter, X_train, y_train):
    population = initialize_population(npop, param_range=[0, 10])

    for t in range(1, max_iter + 1):
        best_jellyfish = find_best_jellyfish(population, X_train, y_train)

        for i in range(npop):
            c_t = abs((1 - t / max_iter) * (2 * np.random.rand() - 1))

            if c_t >= Co:
                trend = best_jellyfish - beta * np.random.rand() * mu
                population[i] = population[i] + np.random.rand() * trend
            else:
                if np.random.rand() > (1 - c_t):
                    population[i] = population[i] + gamma * np.random.rand() * (Ub - Lb)
                else:
                    other_jellyfish = population[np.random.randint(0, npop)]
                    direction = other_jellyfish - population[i] if calculate_fitness(other_jellyfish, X_train, y_train) >= calculate_fitness(population[i], X_train, y_train) else population[i] - other_jellyfish
                    step = np.random.rand() * direction
                    population[i] = population[i] + step

        # Yeni jölebalığı parametrelerini kontrol et
        best_jellyfish = find_best_jellyfish(population, X_train, y_train)

        # Check and handle the condition for 'n_estimators'
        if best_jellyfish[0] <= 0:
            best_jellyfish[0] = 1  # If 'n_estimators' is 0, set it to 1

        # Check and handle the condition for 'max_depth'
        if best_jellyfish[1] <= 0:
            best_jellyfish[1] = 1  # If 'max_depth' is 0, set it to 1

    best_solution = find_best_jellyfish(population, X_train, y_train)
    return best_solution

def find_best_jellyfish(population, X_train, y_train):
    return population[np.argmax([calculate_fitness(j, X_train, y_train) for j in population])]

def calculate_fitness(params, X, y):
    n_estimators = int(params[0])
    max_depth = int(params[1])

    rf_classifier = RandomForestClassifier(n_estimators=max(1, n_estimators), max_depth=max_depth if max_depth > 0 else None, random_state=42)
    rf_classifier.fit(X, y)

    y_pred = rf_classifier.predict(X)
    f_measure = f1_score(y, y_pred)

    return f_measure

# BCD.train.xls ve BCD.test.xls dosyalarını okuyun
train_data = pd.read_excel("/content/BCD_Train.xlsx")
test_data = pd.read_excel("/content/BCD_Test.xlsx")

# Eğitim ve test verilerini özellik matrisi (X) ve hedef değişken (y) olarak ayırın
X_train = train_data.drop("Diagnosis", axis=1)
y_train = train_data["Diagnosis"]

X_test = test_data.drop("Diagnosis", axis=1)
y_test = test_data["Diagnosis"]

# npop ve max_iter değerlerini belirleyin
npop = 5
max_iter = 10

# Diğer jellyfish algoritması parametrelerini belirleyin
Co = 0.5
beta = 0.1
mu = 0.1
gamma = 0.1
Ub = 1.0
Lb = 0.0

# Jellyfish algoritmasını çalıştır
optimized_params = jellyfish_algorithm(npop, max_iter, X_train, y_train)

# Optimize edilmiş parametreleri yazdırın
print("Optimized Parameters:", optimized_params)

# Optimize edilmiş parametrelerle Random Forest sınıflandırıcısını eğitin
optimal_n_estimators, optimal_max_depth = int(optimized_params[0]), int(optimized_params[1])
rf_classifier_optimized = RandomForestClassifier(n_estimators=max(1, optimal_n_estimators), max_depth=optimal_max_depth if optimal_max_depth > 0 else None, random_state=42)
rf_classifier_optimized.fit(X_train, y_train)

# Eğitim veri setinde F-measure hesapla
y_train_pred_optimized = rf_classifier_optimized.predict(X_train)
f_measure_train_optimized = f1_score(y_train, y_train_pred_optimized)
print("Optimized F-measure on Training Data:", f_measure_train_optimized)

# Test veri setinde F-measure hesapla
y_test_pred_optimized = rf_classifier_optimized.predict(X_test)
f_measure_test_optimized = f1_score(y_test, y_test_pred_optimized)
print("Optimized F-measure on Test Data:", f_measure_test_optimized)

# Genel F-measure hesapla
general_f_measure = (f_measure_train_optimized + f_measure_test_optimized) / 2
print("General F-measure:", general_f_measure)
