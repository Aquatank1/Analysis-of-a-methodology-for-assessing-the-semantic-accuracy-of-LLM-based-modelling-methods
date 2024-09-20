#Mediapipe/Google Version
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import text
BaseOptions = mp.tasks.BaseOptions
TextEmbedder = mp.tasks.text.TextEmbedder
TextEmbedderOptions = mp.tasks.text.TextEmbedderOptions
import re
from sentence_transformers import SentenceTransformer
from sentence_transformers import SentenceTransformer, util
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import re
from scipy.optimize import linear_sum_assignment
from scipy.spatial import distance
import pandas as pd
import os
import re
import seaborn as sns
from sklearn.metrics import jaccard_score
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from scipy.spatial.distance import hamming
import plotting

#current_mdodels = "BicycleIObetter"
#current_mdodels = "Elevatorbetter"
#current_mdodels = "Pizzeriabetter"
#current_mdodels = "MyCompanybetter"
#current_mdodels = "Universitybetter"


def dataframe(current_mdodels, add_before = False, sentencess = "not", testing = False):
  #"C:\\Users\\fredg\\Documents\\Semester 6\\Bachelor\\Code\\content\\"BicycleIO_2_Assoziationen_entfernt.txt
  p = "C:\\Users\\fredg\\Documents\\Semester 6\\Bachelor\\Code\\content\\" + current_mdodels + '_Model_Base.txt'
  with open(p, 'r',encoding='cp1252') as file:
      # Read the entire content of the file into a string
      file_content = file.read()
  Model_Base = file_content

  p = "C:\\Users\\fredg\\Documents\\Semester 6\\Bachelor\\Code\\content\\" + current_mdodels + '_Namen_geändert.txt'
  with open(p, 'r',encoding='cp1252') as file:
      # Read the entire content of the file into a string
      file_content = file.read()
  Model_1 = file_content

  p = "C:\\Users\\fredg\\Documents\\Semester 6\\Bachelor\\Code\\content\\" + current_mdodels + '_andere_Anordnung.txt'
  with open(p, 'r',encoding='cp1252') as file:
      # Read the entire content of the file into a string
      file_content = file.read()
  Model_2 = file_content

  p = "C:\\Users\\fredg\\Documents\\Semester 6\\Bachelor\\Code\\content\\" + current_mdodels + '_2_Assoziationen_entfernt.txt'
  with open(p, 'r',encoding='cp1252') as file:
      # Read the entire content of the file into a string
      file_content = file.read()
  Model_3 = file_content

  p = "C:\\Users\\fredg\\Documents\\Semester 6\\Bachelor\\Code\\content\\" + current_mdodels + '_alle_Assoziationen_entfernt.txt'
  with open(p, 'r',encoding='cp1252') as file:
      # Read the entire content of the file into a string
      file_content = file.read()
  Model_4 = file_content

  p = "C:\\Users\\fredg\\Documents\\Semester 6\\Bachelor\\Code\\content\\" + current_mdodels + '_andere_Struktur.txt'
  with open(p, 'r',encoding='cp1252') as file:
      # Read the entire content of the file into a string
      file_content = file.read()
  Model_5 = file_content

  p = "C:\\Users\\fredg\\Documents\\Semester 6\\Bachelor\\Code\\content\\" + current_mdodels + '_kleine_Klasse_weg.txt'
  with open(p, 'r',encoding='cp1252') as file:
      # Read the entire content of the file into a string
      file_content = file.read()
  Model_6 = file_content

  p = "C:\\Users\\fredg\\Documents\\Semester 6\\Bachelor\\Code\\content\\" + current_mdodels + '_große_Klasse_weg.txt'
  with open(p, 'r',encoding='cp1252') as file:
      # Read the entire content of the file into a string
      file_content = file.read()
  Model_7 = file_content
  if testing:
    p = "C:\\Users\\fredg\\Documents\\Semester 6\\Bachelor\\Code\\content\\" + current_mdodels + '_all_in_one.txt'
    with open(p, 'r',encoding='cp1252') as file:
        # Read the entire content of the file into a string
        file_content = file.read()
    Model_8 = file_content
    if add_before:
      data = {
          'models': [
              (sentencess + Model_Base),
              (sentencess + Model_1),
              (sentencess + Model_2),
              (sentencess + Model_3),
              (sentencess + Model_4),
              (sentencess + Model_5),
              (sentencess + Model_6),
              (sentencess + Model_7),
              (sentencess + Model_8),
              """classdiagram{}"""

          ]
      }
      return pd.DataFrame(data)
    else:
      data = {
        'models': [
            Model_Base,
            Model_1,
            Model_2,
            Model_3,
            Model_4,
            Model_5,
            Model_6,
            Model_7,
            Model_8,
            """classdiagram{}"""
        ]
      }
      return pd.DataFrame(data)
  else:
    data = {
        'models': [
            Model_Base,
            Model_1,
            Model_2,
            Model_3,
            Model_4,
            Model_5,
            Model_6,
            Model_7,
            """classdiagram{}"""
        ]
    }
    return pd.DataFrame(data)

def order_giver(values):
  if len(values) == 9:
    # List of names in the desired order of importance
    names = [
        "Names changed",
        "other arrangements",
        "2 associations removed",
        "all associations removed",
        "other structure",
        "small class",
        "large class",
        "testing",
        "classdiagram{}"
    ]
    # Pair each name with its value
    name_value_pairs = list(zip(names, values))

    # Sort the pairs by the values in descending order (highest value first)
    sorted_pairs = sorted(name_value_pairs, key=lambda pair: pair[1], reverse=True)

    # Extract the names from the sorted pairs
    sorted_names = [name for name, value in sorted_pairs]

    # Print the names in the sorted order
    for name in sorted_names:
        print(name)
  else:
    # List of names in the desired order of importance
    names = [
        "Names changed",
        "other arrangements",
        "2 associations removed",
        "all associations removed",
        "other structure",
        "small class",
        "large class",
        "classdiagram{}"
    ]
    # Pair each name with its value
    name_value_pairs = list(zip(names, values))

    # Sort the pairs by the values in descending order (highest value first)
    sorted_pairs = sorted(name_value_pairs, key=lambda pair: pair[1], reverse=True)

    # Extract the names from the sorted pairs
    sorted_names = [name for name, value in sorted_pairs]

    # Print the names in the sorted order
    for name in sorted_names:
        print(name)

"""Sentence Transformer"""
def get_embedding(inputdataframe, model):
  inputdataframe["ada_v2"]  = inputdataframe["models"].apply(lambda x: model.encode(x))

  # Berechne die Cosinus-Ähnlichkeit
  #Alle Modelle mit dem 1. Vergleichen
  ii = 1
  my_list =[]
  while ii < len(inputdataframe["ada_v2"]):
    input_string = str(util.cos_sim(inputdataframe["ada_v2"][0], inputdataframe["ada_v2"][ii]))
    cleaned_string = input_string.replace("tensor([[", "")
    cleaned_string = cleaned_string.replace("]])", "")
    cleaned_string = cleaned_string.replace("tensor([[1.", "1.0")
    cleaned_string = cleaned_string.replace("tensor([[-1.", "-1.0")
    my_list.append(float(cleaned_string))
    ii += 1
  return my_list

#dataframe(current_mdodels, add_before = False, sentencess = "not")
modelname ="not here"
def better_models():
  asdsdwad = """
  Class Prime {
    + int age;
    + double duration;
    + boolean keyboard_used;
  }
  """
  aa = dataframe("Universitybetter")
  a= get_embedding(aa, modelname)
  aa['dataset'] = 'University'
  bb = dataframe("Mycompanybetter")
  b = get_embedding(bb, modelname)
  bb['dataset'] = 'Mycompanybetter'
  cc = dataframe("Pizzeriabetter")
  c = get_embedding(cc, modelname)
  cc['dataset'] = 'Pizzeriabetter'
  dd = dataframe("Elevatorbetter")
  d = get_embedding(dd, modelname)
  dd['dataset'] = 'Elevatorbetter'
  ee = dataframe("Bicyclebetter")
  e = get_embedding(ee, modelname)
  ee['dataset'] = 'Bicyclebetter'
  ff = dataframe("Trainbetter")
  f = get_embedding(ff, modelname)
  ff['dataset'] = 'Trainbetter'
  gg = dataframe("BicycleSellerbetter")
  g = get_embedding(gg, modelname)
  gg['dataset'] = 'BicycleSellerbetter'
  ii = 0
  x = []
  while ii < len(a):
    j = a[ii] + b[ii] +c[ii] +d[ii] +e[ii] +f[ii] +g[ii]
    x.append(j/7)
    ii+=1
  print(order_giver(x))
  print(a,",",b,",",c,",",d,",",e,",",f,",",g,",",x)
  plotting.pcas([aa,bb,cc,dd,ee,ff,gg])
  #plotting.tcne_old([aa,bb,cc,ee])
  #plotting.wrong([aa,bb,cc,dd,ee,ff,gg])

def basic_models():
  asdsdwad = """
  Class Prime {
    + int age;
    + double duration;
    + boolean keyboard_used;
  }
  """
  aa = dataframe("University")
  a = get_embedding(aa, modelname)
  aa['dataset'] = 'University'
  bb = dataframe("MyCompany")
  b = get_embedding(bb, modelname)
  bb['dataset'] = 'MyCompany'
  cc = dataframe("Pizzeria")
  c = get_embedding(cc, modelname)
  cc['dataset'] = 'Pizzeria'
  ee = dataframe("Bicycle")
  e = get_embedding(ee, modelname)
  ee['dataset'] = 'Bicycle'
  ii = 0
  x = []
  while ii < len(a):
    j = a[ii] + b[ii] +c[ii]  +e[ii]
    x.append(j/4)
    ii+=1
  #print(order_giver(x))
  #print(a,",",b,",",c,",",e,",",x)
  plotting.pcas([aa,bb,cc,ee])
  #plotting.pcas_old([aa,bb,cc,ee])
  #plotting.tsne([aa,bb,cc,ee])
  #plotting.tcne_old([aa,bb,cc,ee])
  #plotting.wrong([aa,bb,cc,ee])

#modelname = SentenceTransformer(
#    "jinaai/jina-embeddings-v2-base-code",
#    trust_remote_code=True
#)
modelname = SentenceTransformer("microsoft/codeexecutor")
better_models()
#better_models()