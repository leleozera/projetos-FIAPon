
#LeonardoNunesUrbano_565518_fase2_cap7
#ErickSouzaPereira_564996_fase2_cap7



hectares <- c(274.27, 401.06, 355.21, 406.42, 297.24, 89.92, 264.56, 193.59, 134.46, 357.75, 486.04, 255.23, 138.26, 323.34, 68.35, 23.33, 297.03, 452.37, 126.47, 121.26, 94.15, 392.32, 300.08, 491.57, 203.68, 31.53, 127.73, 344.72, 205.82, 210.95)
tratores <- c(3, 5, 9, 10, 6, 11, 9, 3, 2, 11, 1, 7, 13, 5, 0, 8, 14, 6, 15, 7, 15, 5, 12, 8, 9, 0, 13, 6, 14, 3)
# Calculando a Média:
media_hectares <- mean(hectares)

# Calculando a Mediana:
mediana_hectares <- median(hectares)

# Calculando a Moda: 
moda_hectares <- as.numeric(names(sort(table(hectares), decreasing = TRUE)[1]))

# Máximo:
máximo_hectares <- max(hectares)

#Mínimo:
mínimo_hectares <- min(hectares)

# Calculando a Amplitude:
amplitude_hectares <- diff(range(hectares)) 
                  
# Calculando a Variância:
variancia_hectares <- var(hectares)
                         
# Calculando o Desvio Padrão:
desvio_padrao_hectares <- sd(hectares)
                         
# Calculando o Coeficiente de Variação:
cv_hectares <- (sd(hectares)/mean(hectares))*100 
                         
# Calculando os Quartis:
quartis_hectares <- quantile(hectares, probs=c(0.25, 0.50, 0.75))
                         
# Calculando os Decis:
decis_hectares <- quantile(hectares, probs = seq(0.1, 0.9, by = 0.1))
                         
# Calculando os Centis:
centis_hectares <- quantile(hectares, probs = seq(0.01, 0.99, by = 0.01))

# Criar o gráfico da variável quantitativa:
plot(tratores, type = "l", col = "blue", lwd = 2,
     ylim = range(c(tratores, hectares)), 
     ylab = "Hectares", xlab = "Tratores", 
     main = "Gráfico de Linhas: Tratores vs Hectares")

#Adicionar a segunda linha (hectares):
lines(hectares, type = "l", col = "green", lwd = 2)




# Criar o gráfico da variável qualitativa:
cultura <- c("Café", "Soja", "Algodão", "Café", "Soja", "Milho", "Algodão", "Algodão", 
             "Soja", "Milho", "Soja", "Soja", "Algodão", "Soja", "Café", "Milho", "Algodão", 
             "Feijão", "Feijão", "Soja", "Café", "Arroz", "Arroz", "Arroz", "Soja", 
             "Soja", "Café", "Algodão", "Milho", "Milho")


barplot(table(cultura), main = "Distribuição da variável qualitativa nominal", 
        xlab = "Produtos", ylab = "Frequência", col = "lightgreen", border = "darkgreen")
