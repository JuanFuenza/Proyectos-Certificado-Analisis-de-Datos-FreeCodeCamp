import pandas as pd

pd.set_option('display.max_columns', 15)
pd.set_option('display.width', 1000)

def calculate_demographic_data(print_data=True):
    # Leer data de un archivo
    # df = pd.read_csv('#Path-to-file')
    print(df.head(5))

    # Cuantas razas estan representadas en el dataset? Esto deberia ser una serie de Pandas con los nombres de las razas como indices.
    race_count = df['race'].value_counts()

    # La media de la edad de los hombres
    filter_men = df['sex'] == 'Male'
    average_age_men = float('{0:.1f}'.format(df.loc[filter_men, 'age'].mean()))

    # ¿Cual es el porcentaje de gente con un grado de Bachillerato?
    percentage_bachelors = float('{0:.1f}'.format((df['education'].value_counts()['Bachelors'] / df['education'].value_counts().sum()) * 100))

    # Cual es el porcentaje de gente con educación avanzada (`Bachelors`, `Masters`, or `Doctorate`) y ganan más de 50K?
    # Cual es el porcentaje de gente sin educación avanzada que gana más de 50K?

    # Con y sin `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df.loc[(df['education']=='Bachelors') | (df['education']=='Masters') | (df['education']=='Doctorate')]
    lower_education =df.loc[(df['education']!='Bachelors') & (df['education']!='Masters') & (df['education']!='Doctorate')]

    # Porcentaje con salario >50K
    higher_education_rich = float('{0:.1f}'.format(len(higher_education[higher_education['salary'] == '>50K']) / len(higher_education) * 100))
    lower_education_rich = float('{0:.1f}'.format(len(lower_education[lower_education['salary'] == '>50K']) / len(lower_education) * 100))
    
    # Cual es el minimo de horas que una persona trabaja por semana?
    min_work_hours = df['hours-per-week'].min()

    # Que porcentaje de gente que trabaja el minimo de horas por semana tiene un salario >50K?
    num_min_workers = df.loc[(df['hours-per-week'] == df['hours-per-week'].min())]

    rich_percentage = int(len(num_min_workers.loc[num_min_workers['salary'] == '>50K']) / len(num_min_workers) * 100)

    # Cual es el pais con el mayor porcentaje de gente que gana >50K?
    indexing = df.groupby('native-country')['salary'].value_counts() # Separación de paises con sus respectivos valores `>50K` y `<=50K`
    calc_percentage = indexing.div(indexing.groupby(level=[0]).transform('sum') / 100) # Calculo porcentaje de los valores `>50K` y `<=50K`
    set_name = calc_percentage.reset_index(name='count') # Convirtiendo el multiindex a index
    highest_earning_country = set_name['native-country'][set_name[(set_name['salary'] == '>50K')]['count'].idxmax()]
    highest_earning_country_percentage = float('{0:.1f}'.format(set_name[(set_name['salary'] == '>50K')]['count'].max()))

    # Identificar la ocupación más popular para aquellos que ganan >50K en India.
    index_t_in_o = df.groupby(['native-country', 'occupation'])['salary'].value_counts()
    search_india = index_t_in_o['India']
    filter_salary = search_india[search_india.index.get_level_values('salary').isin(['>50K'])]
    top_IN_occupation = filter_salary.idxmax()[0]

    print(race_count)
    print(average_age_men)
    print(percentage_bachelors)
    print(higher_education_rich)
    print(lower_education_rich)
    print(min_work_hours)
    print(rich_percentage)
    print(highest_earning_country)
    print(highest_earning_country_percentage)
    print(top_IN_occupation)

calculate_demographic_data()
