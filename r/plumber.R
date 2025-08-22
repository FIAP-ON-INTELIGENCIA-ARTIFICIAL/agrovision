library(plumber)
library(jsonlite)

#* @apiTitle AgroVision R (estatística)

#* @post /predict_producao
function(req, res){
  b <- fromJSON(req$postBody)
  a <- 1.2; k <- 0.8; c <- 0.5
  y <- a*b$area_ha + k*b$insumo_kg + c*b$chuva_mm
  list(predicao=y, unidade="ton")
}
