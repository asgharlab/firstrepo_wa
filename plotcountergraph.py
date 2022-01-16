from tkinter import Y
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme (style = "ticks", color_codes= True)
# import dataset
kashti = sns.load_dataset ("titanic")

# print (kashti)

#make a basic plot with 1 variable
# p1 = sns.countplot (x='sex', data = kashti)
# p1.set_title ("Plot for Counting")
# plt.show()

# # make advanced plot with 2 variable
# p1 = sns.countplot (x='sex', hue="class", data = kashti)
# p1.set_title ("Plot for Counting")
# p1.set_title("Sample Count Plot")
# plt.show()