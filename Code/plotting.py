import seaborn as sns
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from scipy.spatial.distance import hamming
from scipy.spatial import distance
import pandas as pd
from sklearn.manifold import MDS
import matplotlib.pyplot as plt
import numpy as np

def plot_with_labels(df_combined):
  # Create a color palette
  palette = sns.color_palette("hsv", len(df_combined['dataset'].unique()))
  color_map = dict(zip(df_combined['dataset'].unique(), palette))
  # Extract Vectors, Cities, and Datasets
  vector0 = df_combined['Vec1'].tolist()
  vector1 = df_combined['Vec2'].tolist()
  cities = df_combined['city'].tolist()
  datasets = df_combined['dataset'].tolist()
  # Plot the Vectors
  plt.figure(figsize=(10, 8))
  for vector0, vector1, city, dataset in zip(vector0, vector1, cities, datasets):
      plt.scatter(vector0, vector1, color=color_map[dataset], label=dataset)
      plt.text(vector0, vector1, city, fontsize=12, ha='right')
  # Create legend for datasets
  handles, labels = plt.gca().get_legend_handles_labels()
  by_label = dict(zip(labels, handles))
  plt.legend(by_label.values(), by_label.keys())
  plt.title('2D Vectors with City Labels and Dataset Colors')
  plt.xlabel('X-coordinate')
  plt.ylabel('Y-coordinate')
  plt.grid(True)
  plt.show()

def plot_with_labels2(df_combined):
    # Create a color palette
    palette = sns.color_palette("hsv", len(df_combined['dataset'].unique()))
    color_map = dict(zip(df_combined['dataset'].unique(), palette))
    
    # Define marker styles for each unique city
    unique_cities = df_combined['city'].unique()
    markers = ['o', 's', 'D', 'v', '^', '<', '>', 'p', '*', 'h']  # Add more markers if needed
    marker_map = dict(zip(unique_cities, markers))
    
    # Extract Vectors, Cities, and Datasets
    vector0 = df_combined['Vec1'].tolist()
    vector1 = df_combined['Vec2'].tolist()
    cities = df_combined['city'].tolist()
    datasets = df_combined['dataset'].tolist()
    
    # Plot the Vectors with appropriate colors and markers
    plt.figure(figsize=(10, 8))
    for vector0, vector1, city, dataset in zip(vector0, vector1, cities, datasets):
        plt.scatter(vector0, vector1, color=color_map[dataset], marker=marker_map[city], s=100)
    
    # Create legend for datasets (colors)
    dataset_handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color_map[ds], markersize=10) 
                       for ds in df_combined['dataset'].unique()]
    dataset_labels = df_combined['dataset'].unique()
    plt.legend(dataset_handles, dataset_labels, title='Datasets', loc='upper right')
    # Create legend for cities (markers)
    city_handles = [plt.Line2D([0], [0], marker=marker_map[city], color='w', markerfacecolor='k', markersize=10) 
                    for city in unique_cities]
    city_labels = unique_cities
    plt.legend(city_handles, city_labels, title='Modifications', loc='lower right')
    plt.xlabel('X-coordinate')
    plt.ylabel('Y-coordinate')
    plt.grid(True)
    plt.show()


def plot_without_labels(df_combined):
  # Create a color palette
  palette = sns.color_palette("hsv", len(df_combined['dataset'].unique()))
  color_map = dict(zip(df_combined['dataset'].unique(), palette))
  # Extract Vectors, Cities, and Datasets
  vector0 = df_combined['Vec1'].tolist()
  vector1 = df_combined['Vec2'].tolist()
  datasets = df_combined['dataset'].tolist()
  # Plot the Vectors
  plt.figure(figsize=(10, 8))
  for vector0, vector1, dataset in zip(vector0, vector1, datasets):
      plt.scatter(vector0, vector1, color=color_map[dataset], label=dataset)
  # Create legend for datasets
  handles, labels = plt.gca().get_legend_handles_labels()
  by_label = dict(zip(labels, handles))
  plt.legend(by_label.values(), by_label.keys())
  plt.title('2D Vectors with Dataset Colors')
  plt.xlabel('X-coordinate')
  plt.ylabel('Y-coordinate')
  plt.grid(True)
  plt.show()

def plot_with_labels_wrong(df_combined):
  # Create a color palette
  palette = sns.color_palette("hsv", len(df_combined['dataset'].unique()))
  color_map = dict(zip(df_combined['dataset'].unique(), palette))
  # Extract Vectors, Cities, and Datasets
  vectors = df_combined['ada_v2'].tolist()
  cities = df_combined['city'].tolist()
  datasets = df_combined['dataset'].tolist()
  # Plot the Vectors
  plt.figure(figsize=(10, 8))
  for vector, city, dataset in zip(vectors, cities, datasets):
      plt.scatter(vector[0], vector[1], color=color_map[dataset], label=dataset)
      plt.text(vector[0], vector[1], city, fontsize=12, ha='right')
  # Create legend for datasets
  handles, labels = plt.gca().get_legend_handles_labels()
  by_label = dict(zip(labels, handles))
  plt.legend(by_label.values(), by_label.keys())
  plt.title('2D Vectors with City Labels and Dataset Colors')
  plt.xlabel('X-coordinate')
  plt.ylabel('Y-coordinate')
  plt.grid(True)
  plt.show()

def plot_without_labels_wrong(df_combined):
  # Create a color palette
  palette = sns.color_palette("hsv", len(df_combined['dataset'].unique()))
  color_map = dict(zip(df_combined['dataset'].unique(), palette))
  # Extract Vectors, Cities, and Datasets
  vectors = df_combined['ada_v2'].tolist()
  datasets = df_combined['dataset'].tolist()
  # Plot the Vectors
  plt.figure(figsize=(10, 8))
  for vector, dataset in zip(vectors, datasets):
      plt.scatter(vector[0], vector[1], color=color_map[dataset], label=dataset)
  # Create legend for datasets
  handles, labels = plt.gca().get_legend_handles_labels()
  by_label = dict(zip(labels, handles))
  plt.legend(by_label.values(), by_label.keys())
  plt.title('2D Vectors with Dataset Colors')
  plt.xlabel('X-coordinate')
  plt.ylabel('Y-coordinate')
  plt.grid(True)
  plt.show()

def mds(ls):
  pca = MDS(n_components=2)
  city = ['Ground truth', 'change1', 'change2', 'change3', 'change4', 'change5', 'change6', 'change7', 'change8']
  for x in ls:
    df = pd.DataFrame(pca.fit_transform(np.array(x["ada_v2"].tolist())), columns = ['Vec1', 'Vec2']) 
    x["Vec1"] = df["Vec1"] 
    x["Vec2"] = df["Vec2"]
    x["city"] = city
  df_combined = pd.concat(ls)
  plot_with_labels(df_combined)

def pcas(ls):
  pca = PCA(n_components=2)
  help_df = pd.DataFrame()
  city = ['Model_Base', 'Names changed', 'other arrangements', '2 associations removed', 'all associations removed', 'other structure', 'small class removed', 'large class removed', 'classdiagram{}']
  help_df['ada_v2'] = pd.concat([df['ada_v2'] for df in ls], ignore_index=True)
  df = pd.DataFrame(pca.fit_transform(np.array(help_df["ada_v2"].tolist())), columns = ['Vec1', 'Vec2']) 
  current_index = 0
  for x in ls:
    df["Vec1"][current_index:(current_index+len(x))]
    x["Vec1"] = df["Vec1"].tolist()[current_index:(current_index+len(x))]
    x["Vec2"] = df["Vec2"].tolist()[current_index:(current_index+len(x))]
    x["city"] = city
    current_index += len(x)
  df_combined = pd.concat(ls)
  plot_without_labels(df_combined)
  plot_with_labels2(df_combined)


def tsne(ls):
  pca = TSNE(n_components=2, perplexity=30)
  help_df = pd.DataFrame()
  city =  ['Model_Base', 'Names changed', 'other arrangements', '2 associations removed', 'all associations removed', 'other structure', 'small class removed', 'large class removed', 'classdiagram{}']
  help_df['ada_v2'] = pd.concat([df['ada_v2'] for df in ls], ignore_index=True)
  df = pd.DataFrame(pca.fit_transform(np.array(help_df["ada_v2"].tolist())), columns = ['Vec1', 'Vec2']) 
  current_index = 0
  for x in ls:
    df["Vec1"][current_index:(current_index+len(x))]
    x["Vec1"] = df["Vec1"].tolist()[current_index:(current_index+len(x))]
    x["Vec2"] = df["Vec2"].tolist()[current_index:(current_index+len(x))]
    x["city"] = city
    current_index += len(x)
  df_combined = pd.concat(ls)
  plot_without_labels(df_combined)
  plot_with_labels2(df_combined)

def wrong(ls):
  city =  ['Model_Base', 'Names changed', 'other arrangements', '2 associations removed', 'all associations removed', 'other structure', 'small class removed', 'large class removed', 'classdiagram{}']
  for x in ls:
    x["city"] = city
  df_combined = pd.concat(ls)
  plot_without_labels_wrong(df_combined)
  print(len(df_combined['ada_v2'].tolist()[0]))

def pcas_old(ls):
  pca = PCA(n_components=2)
  city =  ['Model_Base', 'Names changed', 'other arrangements', '2 associations removed', 'all associations removed', 'other structure', 'small class removed', 'large class removed', 'classdiagram{}']
  for x in ls:
    df = pd.DataFrame(pca.fit_transform(np.array(x["ada_v2"].tolist())), columns = ['Vec1', 'Vec2'])
    x["Vec1"] = df["Vec1"]
    x["Vec2"] = df["Vec2"]
    x["city"] = city
  df_combined = pd.concat(ls)
  plot_without_labels(df_combined)
  plot_with_labels2(df_combined)

def tcne_old(ls):
  pca = TSNE(n_components=2, perplexity=6)
  city =  ['Model_Base', 'Names changed', 'other arrangements', '2 associations removed', 'all associations removed', 'other structure', 'small class removed', 'large class removed', 'classdiagram{}']
  for x in ls:
    df = pd.DataFrame(pca.fit_transform(np.array(x["ada_v2"].tolist())), columns = ['Vec1', 'Vec2'])
    x["Vec1"] = df["Vec1"]
    x["Vec2"] = df["Vec2"]
    x["city"] = city
  df_combined = pd.concat(ls)
  plot_without_labels(df_combined)
  plot_with_labels2(df_combined)