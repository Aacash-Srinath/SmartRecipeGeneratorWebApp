'''
Streamlit Web App to Display Predicted Recipes from the Smart Recipe Generator Function,
Based on the User Given Ingredients List
'''

import streamlit as st   #Streamlit Library to create Web App
from prediction import predictRecipes   #Smart Recipe Generator Prediction Function


st.title('Smart Recipe Generator')   #Web App Title
st.write(' ')
ingredients = st.text_input('Enter Ingredients (comma-separated):')   #User Input Ingredients


if st.button('Predict Recipes'):  #Button to Start Prediction
    st.write(' ')
    inputIngredients = ingredients
    predictedOutput = predictRecipes(inputIngredients)   #Predicted Output from the Prediction Function
    
    recipe1, recipe2, recipe3, recipe4 = st.tabs(predictedOutput['RecipeName'])   #Tabs to Display Predicted Recipes

    #Function to Display Predicted Recipe Details
    def displayRecipe(recipeNum):
        st.header(predictedOutput['RecipeName'][recipeNum])   #Display Recipe Name
        i, middle, j = st.columns(3)
        with middle:
            st.image(predictedOutput['URLs'][recipeNum], width=300)   #Display Recipe Image

        st.subheader("Ingredients")
        recipeIngredients = predictedOutput['Recipes'][recipeNum][1].split(',')   #Display Recipe Ingredients
        s = ''
        for i in recipeIngredients:
            s += "- " + i + "\n"
        st.markdown(s)

        st.subheader("Instructions")
        recipeInstructions = predictedOutput['Recipes'][recipeNum][2]   #Display Recipe Instructions
        st.write(recipeInstructions)


    with recipe1:
        displayRecipe(0) #Display First Predicted Recipe Details

    with recipe2:
        displayRecipe(1) #Display Second Predicted Recipe Details
        
    with recipe3:
        displayRecipe(2) #Display Third Predicted Recipe Details
        
    with recipe4:
        displayRecipe(3) #Display Fourth Predicted Recipe Details


footer="""<style>
.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
height: 25px
}

</style>
<div class="footer">
<p>Developed by Aacash, Nandan, Armaan</p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
        