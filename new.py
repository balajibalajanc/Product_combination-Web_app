def print_value(val):
    import pandas as pd
    import numpy as np
    from pandas import ExcelFile
    import matplotlib.pyplot as plt
    from sklearn.metrics.pairwise import cosine_similarity
    from scipy import sparse

    # ------------------
    # LOAD THE DATASET
    # ------------------

    data = pd.read_csv('dataset/dataset.csv')

    # Create a new dataframe without the user ids.
    data_items = data.drop('user', 1)
    # ------------------------
    # ITEM-ITEM CALCULATIONS
    # ------------------------

    # As a first step we normalize the user vectors to unit vectors.

    # magnitude = sqrt(x2 + y2 + z2 + ...)
    magnitude = np.sqrt(np.square(data_items).sum(axis=1))

    # unitvector = (x / magnitude, y / magnitude, z / magnitude, ...)
    data_items = data_items.divide(magnitude, axis='index')

    def calculate_similarity(data_items):
        """Calculate the column-wise cosine similarity for a sparse
        matrix. Return a new dataframe matrix with similarities.
        """
        data_sparse = sparse.csr_matrix(data_items)
        similarities = cosine_similarity(data_sparse.transpose())
        sim = pd.DataFrame(data=similarities, index=data_items.columns, columns=data_items.columns)
        return sim

    def simple_bar_chart(name, values):
        colors = ['#008000', '#808000', '#FFFF00', '#000000', '#FF0000', '#00FF00', '#0000FF', '#008080', '#aa22ff',
                  '#aa22ff', '#dd0022', '#ff00cc', '#eeaa22', '#22bbaa', '#C0C0C0']
        nam=name[1:11]
        val=values[1:11]
        y_pos = np.arange(len(nam))
        x_pos = np.array(val)
        plt.barh(y_pos, x_pos, color=colors, align='center', edgecolor='green')
        plt.yticks(y_pos, nam)
        plt.ylabel('Products', fontsize=16)
        plt.xlabel('Pecentage of Buying', fontsize=18)
        plt.title(name[0], fontsize=20)
        plt.show()

    data_matrix = calculate_similarity(data_items)
    str_b = val.strip()
    values_s = (data_matrix.loc[str_b].nlargest(11))
    sd = values_s.to_dict()
    name = sd.keys()
    values = sd.values()
    items = [x * 100 for x in values]
    results = list(map(str, name))
    results2 = list(map(int, items))
    simple_bar_chart(results, results2)
    return sd

