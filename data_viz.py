import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('Agg')


def boxplot(data, labels, title, x_axis, y_axis, out_file_name):

    """
    Makes a plot of a series of boxplots

    Arguments
    ________
    data: 2D array of ints or floats
        plot each array in this 2D array as a separate boxplot
    labels: 1D array of boxplot labels
        labels for each boxplot
    title: string
        plot title
    x_axis: string
        x-axis title
    y_axis: string
        y-axis title
    out_file_name: string + ".png"
        filename for boxplot to be saved as

    Returns
    _______
    None. However, string + ".png" file saved to working directory.
    """

    fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
    ax.boxplot(data)
    ax.set_xticklabels(labels, rotation='vertical', fontsize=10)
    ax.set_title(title)
    ax.set_xlabel(x_axis)
    ax.set_ylabel(y_axis)
    fig.savefig(out_file_name, bbox_inches='tight')
