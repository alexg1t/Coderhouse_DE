import requests
from datetime import datetime, timedelta,timezone
import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def conectar_Redshift():
    print("Intentando conexión a Redshift")
    try:
        conn = psycopg2.connect(
            host='**********',
            dbname='**********',
            user='**********',
            password='**********',
            port='**********'
        )
        print("Conectado a Redshift con éxito!")
        
    except Exception as e:
        print("No es posible conectar a Redshift")
        print(e)
    
    with conn.cursor() as cur:
            print("Creando tabla si no existe")
            cur.execute("""
                CREATE TABLE IF NOT EXISTS crypto_aov(
                time timestamp PRIMARY KEY UNIQUE,
                btc_price FLOAT(8),
                eth_price FLOAT(8),
                xrp_price FLOAT(8),
                ltc_price FLOAT(8),
                bch_price FLOAT(8),
                ada_price FLOAT(8),
                dot_price FLOAT(8),
                link_price FLOAT(8),
                xlm_price FLOAT(8),
                bnb_price FLOAT(8)
                );
            """)
            print("tabla creada")
            conn.commit()
            conn.close()
 

def get_crypto_prices_hourly(symbol, start_date=None):
    # Set up the API endpoint for historical hourly data
    url = "https://min-api.cryptocompare.com/data/v2/histohour"


    start_date = datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S')

    # Paramtros API
    params = {
        'fsym': symbol,          # Crypto symbol
        'tsym': 'USD',           # US Dollar
        'limit': 24,             # Numero de datos
        'toTs': int(datetime.timestamp(start_date)),  # Timestamp de la fecha inicial
    }

    try:
        # GET request
        response = requests.get(url, params=params)

        # Check
        if response.status_code == 200:
            data = response.json()
            hourly_prices = data['Data']['Data']
            return hourly_prices
        else:
            print(f"Failed to retrieve data for {symbol}. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    return None

def extract():
    print("Iniciando extracción de datos")
    # Lista de cryptos
    cryptos = ['btc', 'eth', 'xrp', 'ltc', 'bch', 'ada', 'dot', 'link', 'xlm', 'bnb']

    # Dictionario dummy
    crypto_dataframes = {}

    # Definir la fecha inicial - creo que por utc-5 es necesario que esto empieze a las 19:00 para que el df empieze a las 0:00
    current_date = datetime.now(timezone.utc)

    yesterday=current_date-timedelta(days=1)
    yest=yesterday.replace(hour=0, minute=0, second=0, microsecond=0)
    start_date=yest.strftime("%Y-%m-%d %H:%M:%S")
    print(start_date)

    # Consigue data de cada crypto y los guarda en un df
    for symbol in cryptos:
        hourly_prices = get_crypto_prices_hourly(symbol, start_date)
        if hourly_prices is not None:
            df = pd.DataFrame(hourly_prices)
            df.rename(columns={'close': f'{symbol}_price'}, inplace=True)
            crypto_dataframes[symbol] = df

    # Concatenar data en un df
    merged_df = pd.concat([crypto_dataframes[symbol][['time', f'{symbol}_price']] for symbol in cryptos], axis=1)
    merged_df.to_csv('extracted_data.csv',index=False)
    print("Extracción de datos Finalizada")
    
def transform():
#Crear dataframe donde se eliminan columnas repetidas
    print("Transformación de datos iniciada")
    merged_df=pd.read_csv('extracted_data.csv')
    ccdb=merged_df.T.drop_duplicates().T
    #Convertir columna time de unix a tiempo
    ccdb['time'] = pd.to_datetime(ccdb['time'], unit='s',utc=False)
    #Solo agarrar las 24 primeras para empezar en 0:00 y termine en 23:00- para un dia sguiente se hace lo mismo
    cc_db = ccdb.iloc[:24]
    cc_db.to_csv('transformed_data.csv',index=False)
    print(cc_db)
    print("Transformación de datos finalizada")
    
    

def load2rds():
    print("Iniciando carga de datos")
    df=pd.read_csv('transformed_data.csv')
    
    print(df)
    print(df.dtypes)
    print("FLAG1")
    redshift_params = {
    'dbname': '**********',
    'user': '**********',
    'password': '**********',
    'host': '**********',
    'port': '**********'
    }

    engine = create_engine(f"postgresql+psycopg2://{redshift_params['user']}:{redshift_params['password']}@{redshift_params['host']}:{redshift_params['port']}/{redshift_params['dbname']}")
    print(df)
    table='crypto_aov'
    df.to_sql(name=table, con=engine, if_exists='append', index=False,chunksize=24)

    print("Finalizando carga de datos")

def sendmail():
    try:
        #Detalles de servidor
        smtp_server= 'smtp.gmail.com'
        smtp_port=587
        #Detalles de gmail
        myEmail = '**********'
        myEmail2 = '**********'
        #Detalles del mail
        msg = MIMEMultipart()
        msg['Subject']="Datos de cryptomonedas del día"
        msg['From']="Mensaje enviado por Airflow"
        msg['To']=myEmail2
        #Configuracion de alerta
        valormin=30000
        valormax=37000
        #['btc', 'eth', 'xrp', 'ltc', 'bch', 'ada', 'dot', 'link', 'xlm', 'bnb']
        crypto_alerta='btc'
        #Dataframe a enviar
        df=pd.read_csv('transformed_data.csv')
        html_table=df.to_html(index=False)
        msg.attach(MIMEText("Datos de crypto del día", 'plain'))
        msg.attach(MIMEText(html_table,'html'))
        #Revisión de alerta
        s1=df[crypto_alerta+"_price"]>valormax
        s2=df[crypto_alerta+"_price"]<valormin
        if df[s1].shape[0]>0:
            msg.attach(MIMEText(f"El valor de {crypto_alerta} sobrepasó el umbral superior de {valormax} USD en la siguiente fecha:"))
            msg.attach(MIMEText(df[s1].to_html(index=False),'html'))
        else:
            msg.attach(MIMEText(f"El valor de {crypto_alerta} no sobrepasó el umbral superior de {valormax} USD"))

        if df[s2].shape[0]>0:
            msg.attach(MIMEText(f"El valor de {crypto_alerta} bajó el umbral inferior de {valormin} USD en la siguiente fecha:"))
            msg.attach(MIMEText(df[s2].to_html(index=False),'html'))
        else:
            msg.attach(MIMEText(f"El valor de {crypto_alerta} no bajó del umbral inferior de {valormin} USD"))        

        #Envío
        server = smtplib.SMTP(smtp_server,smtp_port)
        server.starttls()
        server.login(myEmail,'**********')
        server.send_message(msg)
        server.quit()
        print('Mensaje enviado')
    except Exception as exception:
        print(exception)
        print('No se logró enviar el mensaje')

  
