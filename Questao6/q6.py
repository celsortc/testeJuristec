# tentei utilizar a IA para obter alguma solução, porém não consegui, preferi deixar minha tentativa do que entregar em branco.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time

def get_inmet_data(municipio, uf):
    # Caminho para o ChromeDriver
    driver_path = "chromedriver.exe"  # altere se estiver em outro caminho
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # roda sem abrir janela
    driver = webdriver.Chrome(executable_path=driver_path, options=options)

    try:
        # Abre a página de estações automáticas do INMET
        driver.get("https://portal.inmet.gov.br/dadoshistoricos")
        wait = WebDriverWait(driver, 10)

        # Seleciona UF
        uf_select = wait.until(EC.presence_of_element_located((By.ID, "selectUf")))
        for option in uf_select.find_elements(By.TAG_NAME, "option"):
            if option.text.strip().upper() == uf.upper():
                option.click()
                break
        time.sleep(1)

        # Seleciona município
        municipio_select = wait.until(EC.presence_of_element_located((By.ID, "selectMunicipio")))
        for option in municipio_select.find_elements(By.TAG_NAME, "option"):
            if option.text.strip().lower() == municipio.lower():
                option.click()
                break
        time.sleep(1)

        # Clica em "Consultar" ou "Enviar"
        consultar_btn = driver.find_element(By.ID, "btnConsultar")
        consultar_btn.click()

        # Espera a tabela carregar
        tabela = wait.until(EC.presence_of_element_located((By.ID, "tabelaDados")))
        rows = tabela.find_elements(By.TAG_NAME, "tr")

        result = {}
        for row in rows[1:]:  # ignora cabeçalho
            cols = row.find_elements(By.TAG_NAME, "td")
            if len(cols) >= 3:
                hora = cols[0].text.strip()  # coluna hora
                temperatura = cols[1].text.strip().replace(",", ".")
                umidade = cols[2].text.strip().replace(",", ".")
                try:
                    T = float(temperatura)
                    U = float(umidade)
                    result[hora] = (T, U)
                except:
                    continue
        return result

    finally:
        driver.quit()


# Exemplo de uso
if __name__ == "__main__":
    municipio = "Belo Horizonte"
    uf = "MG"
    dados = get_inmet_data(municipio, uf)
    if not dados:
        print("Nenhum dado disponível.")
    else:
        for hora, valores in dados.items():
            print(hora, valores)
    input("Pressione ENTER para sair")