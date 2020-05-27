from requests import get
from bs4 import BeautifulSoup
# from config import get_config
from datetime import datetime
import pandas as pd
from time import time
from time import sleep
from random import randint
import matplotlib.pyplot as plt



def generate_url():
    # base url
    # base_url = get_config("BASE_URL", default="https://www.imovelweb.com.br/apartamentos-venda-q-sao-paulo.html")
    base_url = "https://www.imovelweb.com.br/apartamentos-venda-q-sao-paulo.html"

    # # release date
    # release_date = get_config("RELEASE_DATE", default="release_date="+str(datetime.year))
    
    # # sort attribute
    # sort_attribute = get_config("SORT_ON")
    
    # # count
    # count = get_config("COUNT", default=50)
    
    # # start - in a loop this value should incrementally change
    # start = get_config("START", default=1) + (iter*count)
    
    # # reference
    # ref = get_config("REF_", default="ref_=adv_next")
    
    # # connector 
    # connector = "&"
    
    # # consolidated url
    # url = base_url \
    #     + release_date \
    #         + connector + sort_attribute \
    #             + connector + "count=" + str(count) \
    #                 + connector + "start=" + str(start) \
    #                     + connector + ref
    
    # return url

    return base_url


def extract_data(url):
    # get the response from the url provided
    response = get(url)

    # create a BeautifulSoub object to parse HTML response
    html_soup = BeautifulSoup(response.text, 'html.parser')

    # print(html_soup)
    # with open('out.txt', 'a+') as f:
    #     print(html_soup, file=f)  # Python 3.x

    # # extract just the movie containers from the scraped data
    title_data = html_soup.find_all('a', class_ = 'go-to-posting')
    
    title = []

    for rec in title_data:
        title.append(rec.text.strip())

    print(title)

    # output:
    # ['Apartamento, Jardim Celeste - São Paulo', 'Apartamento Com 3 Dormitórios à Venda, 
    # 120 m² Por R$1.200.000 - Real Parque - São Paulo/sp', 'Montecattini Morumbi São Paulo', 
    # 'Apartamento em Pinheiros - Benedito Pinheiros', 'Super Oportunidade De Investimento no 
    # Ibis Budget São Paulo Jardins', 'Apartamento 2 Dorms, 1 Suíte Próximo à Av Cupecê E 
    # Washington Luís', 'Apartamento Ipiranga Com Varanda Gourmet, 3 Suítes, Lazer Completo 
    # Ótima Localização Perto Do Museu.', 'Apartamento na Lapa - Sp - Quintas Da Lapa', 'Ipiranga. 
    # Próximo à Rua Silva Bueno. Aceita Permuta', 'Apartamento 2 Dormitórios Suite Duas Vagas 
    # Próximo Ao Metrô Saude!', 'Moema na Av Dos Eucaliptos - Lado Passaros', 'Apartamento na Vila 
    # Mariana - Atmosfera Vila Mariana', 'Excelente Apartamento - Próximo Ao Metrô Saúde', 
    # 'Apartamento Próximo Ao Metrô Conceição', 'Próximo Ao Metrô Alto Do Ipiranga.', 
    # 'Apartamento na Vila Madalena - Sp. E Vila Madalena', 'Cambuci, Aclimação, 2 Dormitórios, 
    # 50 m², Garagem Livre', 'Excelente Cobertura Duplex A 850 m Do Metrô São Judas', 
    # 'Apartamento Saúde, Semi Novo, Terraço Gourmet, 3 Dorm, 1 Suíte E 2 Vagas Com Deposito', 
    # 'Apartamento na Bela Vista, Sp - Facto Paulista']

    # # create an empty dataframe to store the extracted data
    # df_movie = pd.DataFrame()

    # # iterate through the containers to extract the required data
    # for container in movie_containers:
    #     # only extract movies with a non-blank Metascore
    #     if container.find('div', class_ = 'ratings-metascore') is not None:
    #         # create an empty dict
    #         movie_info = {}            
    #         movie_info['name'] = container.h3.a.text
    #         movie_info['year'] = container.h3.find('span', class_ = 'lister-item-year text-muted unbold').text
    #         movie_info['imdb'] = container.strong.text
    #         movie_info['metascore'] = container.find('span', class_ = 'metascore').text
    #         movie_info['votes'] = container.find('span', attrs = {'name': 'nv'})['data-value']

    #         # append the extracted record to the dataframe
    #         df_movie = df_movie.append(movie_info, ignore_index=True)

    # return df_movie


# def monitor_and_delay(start_time, requests):
#         # Pause the loop
#         sleep(randint(8,15))

#         # Monitor the requests - need to revisit this 
#         elapsed_time = time() - start_time
#         print('Request:{0}; Frequency: {1:.4f} requests/s'.format(requests, requests/elapsed_time))


# def data_cleaning(data_frame):
#     # assign a header to the dataframe

#     data_frame.columns = ['IMDB', 'Metascore', 'Name', 'Votes', 'Year']
    
#     # convert the IMDB rating column to float
#     data_frame['IMDB'] = data_frame['IMDB'].map(lambda imdb: float(imdb))

#     # convert Metascore to float
#     data_frame['Metascore'] = data_frame['Metascore'].map(lambda metascore: float(metascore.strip()))

#     # format Year to extract the numeric value
#     data_frame['Year'] = data_frame['Year'].map(lambda year: int(year[-5:-1]))

#     return data_frame


# def plot_and_analyze(data_frame):
#     fig, axes = plt.subplots(nrows = 1, ncols = 3, figsize = (16,4))
#     ax1, ax2, ax3 = fig.axes
#     ax1.hist(data_frame['IMDB'], bins = 10, range = (0,10)) # bin range = 1
#     ax1.set_title('IMDB rating')
#     ax2.hist(data_frame['Metascore'], bins = 10, range = (0,100)) # bin range = 10
#     ax2.set_title('Metascore')
#     ax3.hist(data_frame['IMDB'], bins = 10, range = (0,10), histtype = 'step')
#     ax3.hist(data_frame['Metascore'], bins = 10, range = (0,100), histtype = 'step')
#     ax3.legend(loc = 'upper left')
#     ax3.set_title('The Two Normalized Distributions')
#     for ax in fig.axes:
#         ax.spines['top'].set_visible(False)
#         ax.spines['right'].set_visible(False)
#     plt.show()


if __name__ == "__main__":    

    # # extracting top 'n' movie entries only 
    # top_n = get_config("TOP_N", default=1000)
    # count = get_config("COUNT", default=50)
    
    # # get the count of iterations required
    # iteration = int(top_n / count)

    # # create a master dataframe to hold the entire dataset
    # df_master = pd.DataFrame()

    # # initialize monitoring and delay variables
    # start_time = time()

    # # for each iteration generate a new url and scrape data
    # for iter in range(iteration):

    #     # generate the url
    #     url = generate_url(iter)
        
    #     # extract the data for each call and append to the master dataframe
    #     df_master =  df_master.append(extract_data(url), ignore_index=True)

    #     # add monitoring and delibrate delaying steps to adhere to ethics
    #     monitor_and_delay(start_time, iter+1)

    # # data cleaning
    # df_master = data_cleaning(df_master)

    # # extract the master data to a csv file
    # df_master.to_csv("scrapedData.csv")

    # # plotting and analyzing the data
    # plot_and_analyze(df_master)
    
    extract_data(generate_url())
