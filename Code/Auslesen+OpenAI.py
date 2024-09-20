import os
import re
from sklearn.metrics import jaccard_score
import random
import pandas as pd
import numpy as np
import tiktoken
from openai import AzureOpenAI
import mediapipe as mp
BaseOptions = mp.tasks.BaseOptions
TextEmbedder = mp.tasks.text.TextEmbedder
TextEmbedderOptions = mp.tasks.text.TextEmbedderOptions
from sentence_transformers import util
import classdiagrams_lists
import plotting


folder = 'Improved line'
#folder = 'Basic line'
client = AzureOpenAI(
  api_key = os.getenv("AZURE_OPENAI_API_KEY"),
  api_version = "2024-02-01",
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
)
modelname = 9

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
    df_bills = pd.DataFrame(data)
    tokenizer = tiktoken.get_encoding("cl100k_base") 
    df_bills["models"] = df_bills["models"].apply(lambda x: normalize_text(x))
    df_bills["encoding"] = df_bills["models"].apply(lambda x: len(tokenizer.encode(x)))
    return df_bills


# s is input text
def normalize_text(s, sep_token = " \n "):
    s = re.sub(r'\s+',  ' ', s).strip()
    s = re.sub(r". ,","",s)
    # remove all instances of multiple spaces
    s = s.replace("..",".")
    s = s.replace(". .",".")
    s = s.replace("\n", "")
    s = s.strip()
    
    return s 

# model should be set to the deployment name you chose when you deployed the text-embedding-ada-002 (Version 2) model
def generate_embeddings(text, model): # model = "deployment_name"
    return client.embeddings.create(input = [text], model=model).data[0].embedding

def get_embedding(df_bills,y):
  #                                                                         text-embedding-ada-002   text-embedding-3-large                              
  df_bills["ada_v2"]  = df_bills["models"].apply(lambda x: generate_embeddings (x, model = "text-embedding-ada-002"))
  ii = 1
  my_list =[]
  print(len(df_bills["ada_v2"][0]))
  while ii < len(df_bills["ada_v2"]):
    input_string = str(util.cos_sim(df_bills["ada_v2"][0], df_bills["ada_v2"][ii]))
    cleaned_string = input_string.replace("tensor([[0.", "0.")
    cleaned_string = cleaned_string.replace("]])", "")
    cleaned_string = cleaned_string.replace("tensor([[1.", "1.0")
    my_list.append(float(cleaned_string))
    ii += 1
  return my_list

#gets just the value for cosine similarity
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

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

def split_string_at_class(input_string):
    keyword = "class"
    index = input_string[6:].find(keyword)
    index += 6
    if index != -1:
        part1 = input_string[:index]
        part2 = input_string[index:]
        return part1, part2
    else:
        return input_string, "class"

def extract_classes(input_string):
    # Regular expression to match class definitions
    class_pattern = re.compile(r'class.*?}', re.DOTALL)
    # Find all matches
    matches = class_pattern.findall(input_string)
    # Process each match to exclude the 'class' keyword from the beginning
    class_definitions = [match[match.index('class'):] for match in matches]
        # Find the last match
    last_match = matches[-1] if matches else ''
    # Get the part of the string after the last match
    if last_match:
        last_match_end = input_string.rfind(last_match) + len(last_match)
        remaining_part = input_string[last_match_end:]
        if remaining_part.strip():  # Check if there is any non-whitespace text
            class_definitions.append(remaining_part.strip())
    j = len(class_definitions)
    i = 0
    while i < j:
        before, after = split_string_at_class(class_definitions[i])
        if after != "class":
            class_definitions[i] = before
            class_definitions.append(after)
        i += 1
    i = 0
    j = len(class_definitions)
    while i < j:
        if class_definitions[i] == "class":
            class_definitions.pop(i)
            i -= 1
            j -= 1
        i += 1
    return class_definitions


def permutation_model(list):
  random.seed(10)
  Model_1 = str("".join(list))
  end_index = len(list) -2
  part_list = list[1:end_index]
  random.shuffle(part_list)
  list[1:end_index] = part_list
  random.shuffle(part_list)
  Model_2 = str("".join(list))
  list[1:end_index] = part_list
  random.shuffle(part_list)
  Model_3 = str("".join(list))
  list[1:end_index] = part_list
  random.shuffle(part_list)
  Model_4 = str("".join(list))
  print(Model_4)
  list[1:end_index] = part_list
  random.shuffle(part_list)
  Model_5 = str("".join(list))
  list[1:end_index] = part_list
  random.shuffle(part_list)
  Model_6 = str("".join(list))
  list[1:end_index] = part_list
  random.shuffle(part_list)
  Model_7 = str("".join(list))
  list[1:end_index] = part_list
  random.shuffle(part_list)
  Model_8 = str("".join(list))
  list[1:end_index] = part_list
  Model_9 = str("".join(list))
  print(type(Model_9))
  data = {
          'models': [
              Model_1,
              Model_2,
              Model_3,
              Model_4,
              Model_5,
              Model_6,
              Model_7,
              Model_8,
              Model_9,
          ]
      }
  return pd.DataFrame(data)

def permutation():
  bb = permutation_model(classdiagrams_lists.getlistclass_BicycleIO_Structure())
  b = get_embedding(bb, modelname)
  bb['dataset'] = 'andere_Struktur_Bicycle'
  
  cc = permutation_model(classdiagrams_lists.getlistclass_BicycleIO_Base())
  c = get_embedding(cc, modelname)
  cc['dataset'] = 'Base_Bicycle'
  dd = permutation_model(classdiagrams_lists.getlistclass_University_Base())
  d = get_embedding(dd, modelname)
  dd['dataset'] = 'Base_Universtiy'
  
  ee = permutation_model(classdiagrams_lists.getlistclass_University_Structure())
  e = get_embedding(ee, modelname)
  ee['dataset'] = 'andere_Struktur_Universtiy'
  plotting.mds([bb,cc,dd,ee])

def basic_models():
  folder = 'Basic line'
  asdsdwad = """
  Class Prime {
    + int age;
    + double duration;
    + boolean keyboard_used;
  }
  """
  aa = dataframe("University")
  a= get_embedding(aa, modelname)
  aa['dataset'] = 'University'
  bb = dataframe("Mycompany")
  b = get_embedding(bb, modelname)
  bb['dataset'] = 'Mycompany'
  cc = dataframe("Pizzeria")
  c = get_embedding(cc, modelname)
  cc['dataset'] = 'Pizzeria'
  ee = dataframe("Bicycle")
  e = get_embedding(ee, modelname)
  ee['dataset'] = 'Bicycle'
  ii = 0
  x = []
  while ii < len(a):
    j = a[ii] + b[ii] +c[ii] +e[ii]
    x.append(j/4)
    ii+=1
  print(order_giver(x))
  print(a,",",b,",",c,",",e,",",x)
  plotting.pcas([aa,bb,cc,ee,])
  #plotting.tsne([aa,bb,cc,ee])
  #plotting.wrong([aa,bb,cc,ee])

def better_models():
  folder = 'Improved line'
  asdsdwad = """
  Class Prime {
    + int age;
    + double duration;
    + boolean keyboard_used;
  }
  """
  aa = dataframe("Universitybetter")
  a= get_embedding(aa, modelname)
  aa['dataset'] = 'Universitybetter'
  bb = dataframe("Mycompanybetter")
  b = get_embedding(bb, modelname)
  bb['dataset'] = 'Mycompanybetter'
  cc = dataframe("Pizzeriabetter")
  c = get_embedding(cc, modelname)
  cc['dataset'] = 'Pizzeriabetter'
  ee = dataframe("Elevatorbetter")
  e = get_embedding(ee, modelname)
  ee['dataset'] = 'Elevatorbetter'
  ff = dataframe("Bicyclebetter")
  f = get_embedding(ff, modelname)
  ff['dataset'] = 'Bicyclebetter'
  gg = dataframe("Trainbetter")
  g = get_embedding(gg, modelname)
  gg['dataset'] = 'Trainbetter'
  hh = dataframe("BicycleSellerbetter")
  h = get_embedding(hh, modelname)
  hh['dataset'] = 'BicycleSellerbetter'
  ii = 0
  x = []
  while ii < len(a):
    j = a[ii] + b[ii] +c[ii] +e[ii] +f[ii] +g[ii] +h[ii]
    x.append(j/7)
    ii+=1
  print(order_giver(x))
  print(a,",",b,",",c,",",e,",",f,",",g,",",h,",",x)
  #plotting.pcas_old([aa,bb,cc,ee,ff,gg,hh])
  #plotting.tsne([aa,bb,cc,ee,ff,gg,hh])
  #plotting.wrong([aa,bb,cc,ee,ff,gg,hh])

#permutation()

#basic_models()
better_models()