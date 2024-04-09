import pandas as pd
import joblib

def predictRecipes(inputIngredients):

    classifier = joblib.load('recipe_classifier.pkl')
    vectorizer = joblib.load("recipe_vectorizer.pkl")
    recipeDF = joblib.load("CIFD.pkl")

    inputText = inputIngredients.split(',')
    inputText = " ".join(inputText)
    inputVector = vectorizer.transform([inputText])

    # Find the k nearest neighbors
    _, indices = classifier.kneighbors(inputVector, n_neighbors=4)
    try:
        RecipeName = [recipeDF['RecipeName'].loc[i] for i in indices[0]]
        Cuisines = [recipeDF['Cuisine'].loc[i] for i in indices[0]]
        URLs = [recipeDF['image-url'].loc[i] for i in indices[0]]
        TotalTimeInMins = [str(recipeDF['TotalTimeInMins'].loc[i]) for i in indices[0]]
        Recipes = [recipeDF['Recipe'].loc[i] for i in indices[0]]
        Recipes = [i.split("<recipeend>") for i in Recipes]

        predictions = {"RecipeName":RecipeName, "Cuisines":Cuisines, 
                       "URLs":URLs, "TotalTimeInMins":TotalTimeInMins, "Recipes":Recipes}
        return predictions
    except Exception as e:
        return e
