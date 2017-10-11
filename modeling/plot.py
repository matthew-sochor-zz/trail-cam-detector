import pandas as pd 
import os

from dotenv import load_dotenv, find_dotenv
import matplotlib.pyplot as plt
import seaborn as sns

load_dotenv(find_dotenv())

model_name = os.environ.get("MODEL_NAME")
plot_dir = 'data/plots'
results_dir = 'data/results'

cm_df = pd.read_csv(os.path.join(results_dir, 'confusion_matrix_' + model_name + '.csv'))
sns.heatmap(cm_df, annot=True, fmt='g', cbar=False)
plt.yticks(rotation=0)
plt.xticks(rotation=90)
plt.gcf().subplots_adjust(bottom=0.30, left=0.20)
plt.savefig(os.path.join(plot_dir, model_weights.split('.')[0] + '.png'))