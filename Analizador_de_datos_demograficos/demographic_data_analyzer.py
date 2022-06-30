import pandas as pd

pd.set_option('display.max_columns', 15)
pd.set_option('display.width', 1000)

def calculate_demographic_data(print_data=True):
    # Leer data de un archivo
    df = pd.read_csv('F:\Python\Proyecto-Certificado-AdDFCC\Proyectos-Certificado-Analisis-de-Datos-FreeCodeCamp\Analizador_de_datos_demograficos\\adult_data.csv')
    print(df.head(5))

    # Cuantas razas estan representadas en el dataset? Esto deberia ser una serie de Pandas con los nombres de las razas como indices.
    race_count = df['race'].value_counts()

    # La media de la edad de los hombres
    filter_men = df['sex'] == 'Male'
    average_age_men = df.loc[filter_men, 'age'].mean()

    # ¿Cual es el porcentaje de gente con un grado de Bachillerato?
    percentage_bachelors = (df['education'].value_counts()['Bachelors'] / df['education'].value_counts().sum()) * 100
    
    print(race_count)
    print(average_age_men)
    print(percentage_bachelors)

calculate_demographic_data()
