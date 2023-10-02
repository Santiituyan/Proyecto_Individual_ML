from fastapi import FastAPI
from fastapi.responses import JSONResponse,HTMLResponse
import pandas as pd
import ast



app = FastAPI(title= 'Games-Steam-API')

#http://127.0.0.1:8000

@app.get("/PlayTimeGenre/{genero}",tags=['Funcion generos'])


def PlayTimeGenre(genero: str):
    # Carga el archivo CSV en un DataFrame
    df = pd.read_csv('funcionuno.csv', dtype={'genres': str})  # Reemplaza 'tu_archivo.csv' y 'nombre_columna' con los valores correctos

    # Convierte la columna a tipo int, ignorando errores
    df['playtime_forever'] = pd.to_numeric(df['playtime_forever'], errors='coerce')

    # Filtra las filas del DataFrame por genero y asegurate de que el género esté en minúsculas
    genero_df = df[df['genres'].str.lower() == genero.lower()]

    if genero_df.empty:
        return {f"Anio con más horas jugadas para {genero}": "No se encontraron datos para este genero"}

    anio_con_mas_horas = genero_df.loc[genero_df['playtime_forever'].idxmax()]['year']
    
    anio_con_mas_horas = anio_con_mas_horas.item()
    
    return {f"Año con más horas jugadas para {genero}": anio_con_mas_horas}


@app.get("/UserForGenre/{genero}",tags=['Funcion generos'])

def UserForGenre(genero: str):
    
    genre_max_playtime_df = pd.read_csv('funciondos.csv')
    playtime_by_user_df = pd.read_csv('funciondos1.csv')
    
    # Filtra el DataFrame de géneros por el género deseado
    genre_filtered = genre_max_playtime_df[genre_max_playtime_df['genres'].str.lower() == genero.lower()]

    if genre_filtered.empty:
        return {f"Usuario con más horas jugadas para el genero {genero}": "No se encontraron usuarios para este género", "Acumulación de horas jugadas por año": {}}

    # Obtiene al usuario con el mayor playtime para el género dado
    max_playtime_user = genre_filtered.iloc[0]['user_id']

    # Filtra el DataFrame de tiempo de juego por el usuario seleccionado
    user_playtime_filtered = playtime_by_user_df[playtime_by_user_df['user_id'] == max_playtime_user]

    # Agrupa el tiempo de juego por año y suma las horas jugadas
    playtime_by_year = user_playtime_filtered.groupby('year')['playtime_forever'].sum().reset_index()

    # Convierte el resultado a un diccionario para la respuesta
    playtime_by_year_dict = playtime_by_year.set_index('year').to_dict()['playtime_forever']

    return {f"Usuario con más horas jugadas para el genero {genero}": max_playtime_user, "Acumulación de horas jugadas por año": playtime_by_year_dict}



@app.get("/game_recommendations/{game_id}",tags=['Funcion de recomendacion de juego'])
def game_recommendations( game_id : int ):
     # carga de archivos
    df = pd.read_csv("modelo.csv")

    if game_id not in df['id'].values:
        return JSONResponse(status_code=404,content={'error':f"Game Id '{game_id}' not found"})

    # Obtiene la lista de recomendaciones
    result = df[df['id'] == game_id]['recommends'].iloc[0]

    # Conversion a lista
    try:
        result = ast.literal_eval(result)
    except (SyntaxError, ValueError):
        # retorno error
        return JSONResponse(status_code=404,content={'error':f"Game Id '{game_id}' not found "})

    response =[]
    item_buscado = df[df['id'] == game_id].iloc[0]

    for item_id in result:
        # Obtiene la información del juego recomendado
        item_info = df[df['id'] == item_id].iloc[0]  
        #append a la lista de salida
        response.append({'game_id': int(item_info['id']), 
                         'title': item_info['title']})
    dict_respuesta = {'titulo_buscado': item_buscado['title'], 'results':response}  
    return JSONResponse(status_code=200,content=dict_respuesta)