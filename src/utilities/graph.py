from lib2to3.pytree import convert
import matplotlib.pyplot as plt
import seaborn as sns

def convert_snake_case(label, capitalize_first=True, capitalize_all=False):
# Code directly taken from breakfast hour lecture: https://git.generalassemb.ly/DSIR-222/breakfast-hour/tree/master/06_week/reusable-graphing-fx
    """Takes an input string assumed to be in snake case and returns it with spaces inserted and capitalized to your liking.

    Keyword Arguments:
    label: a_snake_case_string
    capitalize_first: Bool, capitalize the first word of the string
    capitalize_all: Bool, capitalize all words of the string"""

    if capitalize_all:
        return ' '.join([word.capitalize() for word in label.split('_')])
    elif capitalize_first:
        return ' '.join([word.capitalize() if i == 0 else word for i, word in enumerate(label.split('_'))])
    else:
        return ' '.join([word for word in label.split('_')])

def my_catplot(df, x_col, y_col, size=10, col=None, col_wrap=None, height=5, hue=None, hue_order=None, kind="box"):
    # Set figure size
#    plt.figure(figsize=(size, size))

    # Create plot
    sns.catplot(data=df, x=x_col, y=y_col, col=col, col_wrap=col_wrap, height=height, hue=hue, hue_order=hue_order, kind=kind)

    # Set title
    plt.title(f"{convert_snake_case(x_col, capitalize_all=True)} vs. {convert_snake_case(y_col, capitalize_all=True)}", fontsize=size*2)

    # Set labels and ticks
#    plt.xlabel(convert_snake_case(label=x_col, capitalize_all=True), fontsize = size * 1.75, labelpad = size/2)
#    plt.xticks(fontsize=size*1.25, rotation=45)
#    plt.ylabel(convert_snake_case(label=y_col, capitalize_all=True), fontsize = size * 1.75, labelpad = size/2)
#    plt.yticks(fontsize=size*1.25, rotation=45)

def my_scatterplot(df, x_col, y_col, size):
    # Set figure size
    plt.figure(figsize=(size, size))

    # Create plot
    sns.scatterplot(data=df, x=x_col, y=y_col)

    # Set title
    plt.title(f"Scatterplot: {convert_snake_case(x_col, capitalize_all=True)} vs. {convert_snake_case(y_col, capitalize_all=True)}", fontsize=size*2)

    # Set labels and ticks
    plt.xlabel(convert_snake_case(label=x_col, capitalize_all=True), fontsize = size * 1.75, labelpad = size/2)
    plt.xticks(fontsize=size*1.25, rotation=45)
    plt.ylabel(convert_snake_case(label=y_col, capitalize_all=True), fontsize = size * 1.75, labelpad = size/2)
    plt.yticks(fontsize=size*1.25, rotation=45)

def my_boxplot(df, x_col, y_col, size):
    # Set figure size
    plt.figure(figsize=(size, size))

    # Create order of boxplots by median
    order = list(df.groupby(x_col)[y_col].median().sort_values().index)

    # Create plot
    sns.boxplot(data=df, x=x_col, y=y_col, order=order)

    # Set title
    plt.title(f"Boxplot: {convert_snake_case(x_col, capitalize_all=True)} vs. {convert_snake_case(y_col, capitalize_all=True)}", fontsize=size*2)

    # Set labels and ticks
    plt.xlabel(convert_snake_case(label=x_col, capitalize_all=True), fontsize = size * 1.75, labelpad = size/2)
    plt.xticks(fontsize=size*1.25, rotation=45)
    plt.ylabel(convert_snake_case(label=y_col, capitalize_all=True), fontsize = size * 1.75, labelpad = size/2)
    plt.yticks(fontsize=size*1.25, rotation=45)

def my_histplot(df, x_col, size):
    # Set figure size
    plt.figure(figsize=(size, size))

    # Create plot
    sns.histplot(data=df, x=x_col)

    # Set title
    plt.title(f"Distribution of {convert_snake_case(x_col, capitalize_all=True)}", fontsize=size*2)

    # Set labels and ticks
    plt.xlabel(convert_snake_case(label=x_col, capitalize_all=True), fontsize = size * 1.75, labelpad = size/2)
    plt.xticks(fontsize=size*1.25, rotation=45)

def my_barplot(df, x_col, y_col, title, size):
    # Set figure size
    plt.figure(figsize=(18,6))
    
    # Create plot
    sns.barplot(x=df[x_col], y=df[y_col]);
    
    # Set title
    plt.title(title, fontsize=size)
    
    # Set labels and ticks
    plt.xlabel(convert_snake_case(label=x_col, capitalize_all=True), fontsize = size - 4, labelpad = size/2)
    plt.xticks(fontsize=size/2, rotation=45)
    plt.ylabel(convert_snake_case(label=y_col, capitalize_all=True), fontsize = size - 4, labelpad = size/2)
    plt.yticks(fontsize=size/2);
    