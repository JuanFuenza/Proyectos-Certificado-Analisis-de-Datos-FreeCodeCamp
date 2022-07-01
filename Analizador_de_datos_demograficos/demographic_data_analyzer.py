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

    # Cual es el porcentaje de gente con educación avanzada (`Bachelors`, `Masters`, or `Doctorate`) y ganan más de 50K?
    # Cual es el porcentaje de gente sin educación avanzada que gana más de 50K?

    # Con y sin `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df.loc[(df['education']=='Bachelors') | (df['education']=='Masters') | (df['education']=='Doctorate')]
    lower_education =df.loc[(df['education']!='Bachelors') & (df['education']!='Masters') & (df['education']!='Doctorate')]

    # Porcentaje con salario >50K
    higher_education_rich = len(higher_education[higher_education['salary'] == '>50K']) / len(higher_education) * 100
    lower_education_rich = len(lower_education[lower_education['salary'] == '>50K']) / len(lower_education) * 100
    
    # Cual es el minimo de horas que una persona trabaja por semana?
    min_work_hours = df['hours-per-week'].min()

    # Que porcentaje de gente que trabaja el minimo de horas por semana tiene un salario >50K?
    num_min_workers = df.loc[(df['hours-per-week'] == df['hours-per-week'].min())]

    rich_percentage = len(num_min_workers.loc[num_min_workers['salary'] == '>50K']) / len(num_min_workers) * 100

    # print(race_count)
    # print(average_age_men)
    # print(percentage_bachelors)
    # print(higher_education_rich)
    # print(lower_education_rich)
    # print(min_work_hours)
    print(rich_percentage)

calculate_demographic_data()
