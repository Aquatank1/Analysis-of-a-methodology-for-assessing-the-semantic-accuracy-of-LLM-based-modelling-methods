from openai import AzureOpenAI
import os
def beschreibung(input):
    input.replace("<->", "< - >")
    input.replace("<-", "< -")
    input.replace("->", "- >")
    api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
    api_key= os.getenv("AZURE_OPENAI_API_KEY")
    deployment_name = 'gpt-4'
    api_version = '2023-12-01-preview' # this might change in the future

    client = AzureOpenAI(
        api_key=api_key,  
        api_version=api_version,
        base_url=f"{api_base}/openai/deployments/{deployment_name}"
    )
    inputs = "Describe this classdiagram as accuretly as possible go into the amount of classes and associations it has and then go over every class and association and describe what its attributes are." + input
    response = client.chat.completions.create(
        model=deployment_name,
        messages=[
            { "role": "system", "content": "You are a helpful assistant." },
            { "role": "user", "content": [  
                { 
                    "type": "text", 
                    "text": inputs
                },
            ] } 
        ],
        max_tokens=2000 
    )
    return response


def help(current_mdodels):
    ls = ['_Model_Base',"_Namen_geändert","_andere_Anordnung", "_2_Assoziationen_entfernt", "_alle_Assoziationen_entfernt", "_andere_Struktur", "_kleine_Klasse_weg", "_große_Klasse_weg"]
    for jj in ls:
        j = jj + ".txt"
        p = 'C:\\Users\\fredg\\Documents\\Semester 6\\Bachelor\\Klassendiagramme\\Oldstuff\\' + current_mdodels + j
        with open(p, 'r') as file:
            # Read the entire content of the file into a string
            file_content = file.read()
        Model_Base = file_content
        response = beschreibung(Model_Base)
        file_path = 'C:\\Users\\fredg\\Documents\\Semester 6\\Bachelor\\Klassendiagramme\\GPT4 Beschreibungen\\' + current_mdodels + j
        with open(file_path, 'w') as file:
            # Write the text to the file
            file.write(str(response))
        print(1)
        print(response)


help("BicycleIO")
help("MyCompany")
help("Pizzeria")
help("Elevator")