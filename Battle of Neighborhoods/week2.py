# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
null.tpl [markdown]
# # Battle of the Neighborhoods week 2
null.tpl [markdown]
# ## Part 1
null.tpl [markdown]
# ## Table of contents
# * [Introduction: Business Problem](#introduction)
# * [Data](#data)
# * [Methodology](#methodology)
# * [Analysis](#analysis)
# * [Results and Discussion](#results)
# * [Conclusion](#conclusion)
null.tpl [markdown]
# ## Introduction: Business Problem <a name="introduction"></a>
# 
null.tpl [markdown]
# The objective of this project is to find the best location to move into the Abingdon-on-Thames area.
# Currently looking to move into the Area of Abingdon-on-Thames and would like to take advantage of this project to use it in my favour to help me identify the best and the worst areas to live.
# First step is to choose the safest borough by analysis police crime data and then after having chosen an area, use data from FourSquare to help us choose the best area for supermarkets, leisure centres, good schools, parks and restaurants, etc.
# 
# Using data science tools, will help us analyse data and focus on the safest borough and explore its neighborhoods and the common venues in each neighborhood.
# 
# The success criteria of the project will be that after having analysed such factors, we would then be able to make the best choice for the family.
null.tpl [markdown]
# ## Data <a name="data"></a>
null.tpl [markdown]
# After having defined our problem, below are the factors that will help us make our decission:
# * finding the safest borough based on crime statistics
# * finding the most common venues
# * choosing the right neighbourhood within the borough
# 
# We will be using the geographical coordinates of Vancouver to plot neighbourhoods in a borough that is safe and in the city's vicinity, and finally cluster our neighborhoods and present our findings.
# 
# Following data sources will be needed to extract/generate the required information:
# 
# - [**Part 1**: Using a real world data set from Kaggle containing the Vancouver Crimes from 2003 to 2019](#part1):  A dataset consisting of the crime statistics of each Neighbourhoof in Vancouver along with type of crime, recorded year, month and hour.
# 
# - [**Part 2**: Gathering additional information of the list of officially categorized boroughs in Vancouver from Wikipedia.](#part2): Borough information will be used to map the existing data where each neighbourhood can be assigned with the right borough.
# 
# - [**Part 3**: Creating a new consolidated dataset of the Neighborhoods, along with their boroughs, crime data and the respective Neighbourhood's co-ordinates.](#part3): This data will be fetched using OpenCage Geocoder to find the safest borough and explore the neighbourhood by plotting it on maps using Folium and perform exploratory data analysis.
# 
# - [**Part 4**: Creating a new consolidated dataset of the Neighborhoods, boroughs, and the most common venues and the respective Neighbourhood along with co-ordinates.](#part4): This data will be fetched using Four Square API to explore the neighbourhood venues and to apply machine learning algorithm to cluster the neighbourhoods and present the findings by plotting it on maps using Folium.
null.tpl [markdown]
# 

# %%



# %%



