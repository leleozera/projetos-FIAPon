library(httr)
library(jsonlite)
library(dplyr)
library(glue)


api_key <- "e213356ed7f255883294bcd1d8e34f2d"  
cidade <- "Cotia"
pais <- "BR"
unidades <- "metric"  
lingua <- "pt"       


codificar_url <- function(texto) {
  URLencode(texto, reserved = TRUE)
}


url_base <- "https://api.openweathermap.org/data/2.5/weather"
url_completa <- glue("{url_base}?q={codificar_url(cidade)},{pais}&units={unidades}&lang={lingua}&appid={api_key}")


obter_dados_meteorologicos <- function() {
  resposta <- GET(url_completa)
  
  if (status_code(resposta) == 200) {
    conteudo <- content(resposta, "text", encoding = "UTF-8")
    dados <- fromJSON(conteudo)
    return(dados)
  } else {
    stop("Erro ao acessar a API: ", status_code(resposta))
  }
}


exibir_dados <- function(dados) {
  
  cidade <- dados$name
  temperatura <- dados$main$temp
  sensacao <- dados$main$feels_like
  temp_min <- dados$main$temp_min
  temp_max <- dados$main$temp_max
  umidade <- dados$main$humidity

  
 
  cat("\n")
  cat(glue("Condições Meteorológicas em {cidade}\n"))
  cat(glue("---------------------------------\n"))
  cat(glue("Temperatura atual: {temperatura}°C (Sensação: {sensacao}°C)\n"))
  cat(glue("Mínima/Máxima: {temp_min}°C / {temp_max}°C\n"))
  cat(glue("Umidade: {umidade}%\n"))
  cat("\n")
}


tryCatch({
  dados <- obter_dados_meteorologicos()
  exibir_dados(dados)
}, error = function(e) {
  cat(glue("Erro: {e$message}\n"))
})

